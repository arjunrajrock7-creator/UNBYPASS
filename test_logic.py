
import asyncio
import time
from unittest.mock import MagicMock, AsyncMock

# Mocking parts of the system
class MockDB:
    def __init__(self):
        self.users = {}
        self.banned_users = set()
        self.verify_status = {
            'is_verified': False,
            'verified_time': 0,
            'verify_token': "",
            'link': "",
            'verify_start_time': 0
        }

    async def ban_user_exist(self, user_id):
        return user_id in self.banned_users

    async def add_ban_user(self, user_id):
        self.banned_users.add(user_id)

    async def get_verify_status(self, user_id):
        return self.users.get(user_id, self.verify_status.copy())

    async def update_verify_status(self, user_id, is_verified=False, verified_time=0):
        if user_id not in self.users:
            self.users[user_id] = self.verify_status.copy()
        self.users[user_id]['is_verified'] = is_verified
        self.users[user_id]['verified_time'] = verified_time

    async def update_verify_start_time(self, user_id, start_time):
        if user_id not in self.users:
            self.users[user_id] = self.verify_status.copy()
        self.users[user_id]['verify_start_time'] = start_time

async def test_bypass_detection():
    db = MockDB()
    user_id = 123

    # 1. User starts verification
    start_time = time.time()
    await db.update_verify_start_time(user_id, start_time)

    # 2. User returns too fast (e.g., after 10 seconds)
    return_time = start_time + 10
    time_taken = return_time - start_time

    if time_taken < 60:
        await db.add_ban_user(user_id)
        print(f"Test 1: User {user_id} banned successfully for bypass ({time_taken:.2f}s)")

    assert await db.ban_user_exist(user_id) is True

async def test_successful_verification():
    db = MockDB()
    user_id = 456

    # 1. User starts verification
    start_time = time.time()
    await db.update_verify_start_time(user_id, start_time)

    # 2. User returns after 65 seconds
    return_time = start_time + 65
    time_taken = return_time - start_time

    if time_taken < 60:
        await db.add_ban_user(user_id)
    else:
        await db.update_verify_status(user_id, is_verified=True, verified_time=return_time)
        print(f"Test 2: User {user_id} verified successfully after {time_taken:.2f}s")

    status = await db.get_verify_status(user_id)
    assert status['is_verified'] is True
    assert await db.ban_user_exist(user_id) is False

async def main():
    await test_bypass_detection()
    await test_successful_verification()
    print("All tests passed!")

if __name__ == "__main__":
    asyncio.run(main())
