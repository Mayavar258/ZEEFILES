#(©)CodeXBotz
# (©) Jigarvarma2005

import pymongo
from config import DB_URI, DB_NAME, FORCE_SUB_CHANNELS, TG_BOT_TOKEN


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

files_cache = database[TG_BOT_TOKEN.split(":")[0]]
user_data = database['users']
fsubs = {x[0]: database[str(x[0])] for x in FORCE_SUB_CHANNELS}

async def add_fsub(channel_id: int, user_id: int):
    try:
        fsubs[channel_id].insert_one({'_id': user_id})
    except:
        pass

async def get_fsub(channel_id: int, user_id: int):
    found = fsubs[channel_id].find_one({'_id': user_id})
    return bool(found)

async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return


async def add_cache(file_id: str, caption: str, tg_file_id: str):
    files_cache.insert_one({'_id': file_id, 'caption': caption, "file_id": tg_file_id})
    return

async def get_cache(file_id: str):
    file = files_cache.find_one({'_id': file_id})
    return file
