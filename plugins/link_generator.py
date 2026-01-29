# (©) @ALONEKINGSTAR77

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from bot import Bot
from helper_func import encode, get_message_id, admin

@Bot.on_message(filters.private & admin & filters.command('batch') & unbanned)
async def batch(client: Client, message: Message):
    if not await is_user_verified(message.from_user.id):
        return await message.reply_text("Please verify first.")
    while True:
        try:
            first_message = await client.ask(
                text="<b>⛩️ ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ꜰɪʀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ꜰʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ (ᴡɪᴛʜ ǫᴜᴏᴛᴇꜱ)..\n\nᴏʀ ꜱᴇɴᴅ ᴛʜᴇ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴘᴏꜱᴛ ʟɪɴᴋ</b>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60
            )
        except:
            return

        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("<b>❌ ᴇʀʀᴏʀ: ᴛʜɪꜱ ᴘᴏꜱᴛ ɪꜱ ɴᴏᴛ ꜰʀᴏᴍ ᴍʏ ᴅʙ ᴄʜᴀɴɴᴇʟ!</b>", quote=True)
            continue

    while True:
        try:
            second_message = await client.ask(
                text="<b>⛩️ ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ꜰʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ (ᴡɪᴛʜ ǫᴜᴏᴛᴇꜱ)..\n\nᴏʀ ꜱᴇɴᴅ ᴛʜᴇ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴘᴏꜱᴛ ʟɪɴᴋ</b>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60
            )
        except:
            return

        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("<b>❌ ᴇʀʀᴏʀ: ᴛʜɪꜱ ᴘᴏꜱᴛ ɪꜱ ɴᴏᴛ ꜰʀᴏᴍ ᴍʏ ᴅʙ ᴄʜᴀɴɴᴇʟ!</b>", quote=True)
            continue

    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    buttons = [[
        InlineKeyboardButton("🔁 sʜᴀʀᴇ ᴜʀʟ", url=f'https://telegram.me/share/url?url={link}')
    ]]

    await second_message.reply_text(
        f"<b>🌸 ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ʙᴀᴛᴄʜ ʟɪɴᴋ:</b>\n\n<code>{link}</code>",
        quote=True,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Bot.on_message(filters.private & admin & filters.command('genlink') & unbanned)
async def link_generator(client: Client, message: Message):
    if not await is_user_verified(message.from_user.id):
        return await message.reply_text("Please verify first.")
    while True:
        try:
            channel_message = await client.ask(
                text="<b>⛩️ ꜰᴏʀᴡᴀʀᴅ ᴍᴇꜱꜱᴀɢᴇ ꜰʀᴏᴍ ᴛʜᴇ ᴅʙ ᴄʜᴀɴɴᴇʟ (ᴡɪᴛʜ ǫᴜᴏᴛᴇꜱ)..\n\nᴏʀ ꜱᴇɴᴅ ᴛʜᴇ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴘᴏꜱᴛ ʟɪɴᴋ</b>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60
            )
        except:
            return

        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("<b>❌ ᴇʀʀᴏʀ: ᴛʜɪꜱ ᴘᴏꜱᴛ ɪꜱ ɴᴏᴛ ꜰʀᴏᴍ ᴍʏ ᴅʙ ᴄʜᴀɴɴᴇʟ!</b>", quote=True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"

    buttons = [[
        InlineKeyboardButton("🔁 sʜᴀʀᴇ ᴜʀʟ", url=f'https://telegram.me/share/url?url={link}')
    ]]

    await channel_message.reply_text(
        f"<b>🌸 ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ꜰɪʟᴇ ʟɪɴᴋ:</b>\n\n<code>{link}</code>",
        quote=True,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Bot.on_message(filters.private & admin & filters.command("custom_batch") & unbanned)
async def custom_batch(client: Client, message: Message):
    if not await is_user_verified(message.from_user.id):
        return await message.reply_text("Please verify first.")
    collected = []
    STOP_KEYBOARD = ReplyKeyboardMarkup([["STOP"]], resize_keyboard=True)

    await message.reply(
        "<b>⛩️ ꜱᴇɴᴅ ᴀʟʟ ᴍᴇꜱꜱᴀɢᴇꜱ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɪɴᴄʟᴜᴅᴇ ɪɴ ʙᴀᴛᴄʜ.\n\nᴘʀᴇꜱꜱ STOP ᴡʜᴇɴ ʏᴏᴜ'ʀᴇ ᴅᴏɴᴇ.</b>",
        reply_markup=STOP_KEYBOARD
    )

    while True:
        try:
            user_msg = await client.ask(
                chat_id=message.chat.id,
                text="<b>Waiting for files/messages... (Press STOP to finish)</b>",
                timeout=300
            )
        except asyncio.TimeoutError:
            break

        if user_msg.text and user_msg.text.strip().upper() == "STOP":
            break

        try:
            sent = await user_msg.copy(client.db_channel.id, disable_notification=True)
            collected.append(sent.id)
        except Exception as e:
            await message.reply(f"<b>❌ ꜰᴀɪʟᴇᴅ ᴛᴏ ꜱᴛᴏʀᴇ ᴍᴇꜱꜱᴀɢᴇ:\n<code>{e}</code></b>")
            continue

    await message.reply("<b>✅ ʙᴀᴛᴄʜ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ᴄᴏᴍᴘʟᴇᴛᴇ.</b>", reply_markup=ReplyKeyboardRemove())

    if not collected:
        await message.reply("<b>❌ ɴᴏ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡᴇʀᴇ ᴀᴅᴅᴇᴅ ᴛᴏ ʙᴀᴛᴄʜ.</b>")
        return

    start_id = collected[0] * abs(client.db_channel.id)
    end_id = collected[-1] * abs(client.db_channel.id)
    string = f"get-{start_id}-{end_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    buttons = [[
        InlineKeyboardButton("🔁 sʜᴀʀᴇ ᴜʀʟ", url=f'https://telegram.me/share/url?url={link}')
    ]]

    await message.reply(
        f"<b>🌸 ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ʙᴀᴛᴄʜ ʟɪɴᴋ:</b>\n\n<code>{link}</code>",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
