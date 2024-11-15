import ujson
import os
import aiofiles

DB_FILE = 'data/user_data.json'

if not os.path.exists(DB_FILE):
    with open(DB_FILE, 'w') as f:
        ujson.dump({}, f)

async def load_data():
    async with aiofiles.open(DB_FILE, 'r') as f:
        content = await f.read()
        return ujson.loads(content)

async def save_data(data):
    async with aiofiles.open(DB_FILE, 'w') as f:
        await f.write(ujson.dumps(data, indent=4))

async def add_user(user_id: int, status: str):
    data = await load_data()
    data[str(user_id)] = {'status': status}
    await save_data(data)

async def get_user_status(user_id: int):
    data = await load_data()
    return data.get(str(user_id), {}).get('status')

async def user_exists(user_id: int) -> bool:
    data = await load_data()
    return str(user_id) in data

