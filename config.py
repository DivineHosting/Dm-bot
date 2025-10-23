import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

PREFIX = "!"  # Bot command prefix
COLOR_WELCOME = 0x00FFAA  # Welcome message color
COLOR_DM = 0x5865F2       # DM message color
COLOR_ANNOUNCEMENT = 0xFEE75C  # Mass DM embed color
DELAY = 2  # Seconds delay per DM to avoid rate limits
