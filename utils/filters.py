import time
import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from database.database import db
from database.db_premium import is_premium_user
from config import OWNER_ID, FORCE_SUB_CHANNELS

async def is_user_verified(user_id):
    if user_id == OWNER_ID:
        return True
    if await db.admin_exist(user_id):
        return True
    if await is_premium_user(user_id):
        return True

    status = await db.get_verify_status(user_id)
    if status.get('is_verified'):
        verified_time = status.get('verified_time', 0)
        if time.time() - verified_time < 86400:  # 24 hours
            return True
    return False

async def is_sub(client, user_id, channel_id):
    try:
        member = await client.get_chat_member(channel_id, user_id)
        status = member.status
        return status in {
            ChatMemberStatus.OWNER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.MEMBER
        }
    except UserNotParticipant:
        mode = await db.get_channel_mode(channel_id)
        if mode == "on":
            exists = await db.req_user_exist(channel_id, user_id)
            return exists
        return False
    except Exception as e:
        print(f"[!] Error in is_sub(): {e}")
        return False

async def is_subscribed(client, user_id):
    channel_ids = await db.show_channels()
    for cfg_cid in FORCE_SUB_CHANNELS:
        if cfg_cid not in channel_ids:
            channel_ids.append(cfg_cid)
    if not channel_ids:
        return True
    if user_id == OWNER_ID:
        return True
    for cid in channel_ids:
        if not await is_sub(client, user_id, cid):
            mode = await db.get_channel_mode(cid)
            if mode == "on":
                await asyncio.sleep(2)
                if await is_sub(client, user_id, cid):
                    continue
            return False
    return True

async def check_admin(filter, client, update):
    try:
        if not update.from_user:
            return False
        user_id = update.from_user.id
        return any([user_id == OWNER_ID, await db.admin_exist(user_id)])
    except Exception as e:
        print(f"! Exception in check_admin: {e}")
        return False

async def is_verified_filter(filter, client, update):
    if not update.from_user:
        return False
    user_id = update.from_user.id
    if await db.ban_user_exist(user_id):
        return False
    return await is_user_verified(user_id)

async def ban_filter(filter, client, update):
    if not update.from_user:
        return False
    user_id = update.from_user.id
    return not await db.ban_user_exist(user_id)

admin = filters.create(check_admin)
unbanned = filters.create(ban_filter)
verified = filters.create(is_verified_filter)
