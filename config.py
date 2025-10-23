import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

# Bot settings
PREFIX = "!"
COLOR_WELCOME = 0x00FFAA
COLOR_DM = 0x5865F2
COLOR_ANNOUNCEMENT = 0xFEE75C
