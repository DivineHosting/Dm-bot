from pymongo import MongoClient
from datetime import datetime
from config import MONGO_URI

mongo_client = MongoClient(MONGO_URI)
db = mongo_client["discord_dm_bot"]
dm_history = db["dm_history"]

async def log_dm(member, message, success, sender="System"):
    """Log each DM to MongoDB"""
    data = {
        "member_id": getattr(member, "id", member),
        "member_name": getattr(member, "name", str(member)),
        "message": message,
        "success": success,
        "sender": getattr(sender, "name", sender),
        "timestamp": datetime.utcnow()
    }
    dm_history.insert_one(data)
