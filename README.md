# Discord Welcome DM Bot

A safe, multi-message Discord DM bot with:

- Welcome messages
- Multi-DMs per user (`!dmuser`, `!dm`, `!dmall`)
- MongoDB logging
- Delays to prevent rate-limiting

---

## Commands

| Command | Description |
|---------|-------------|
| `!dmuser @user 50 Hello {user}` | DM a single user 50 times |
| `!dm @user 50 Hello {user}` | DM a server member multiple times |
| `!dmall 50 Hello {user}` | DM all server members multiple times |

---

## Setup

1. Create a bot in Discord Developer Portal
2. Enable intents: SERVER MEMBERS + MESSAGE CONTENT
3. Create `.env` file with:
BOT_TOKEN=your_token
MONGO_URI=your_mongo_uri
4. Install dependencies:
   pip install -r requirements.txt
5. Run the bot:
   python bot.py
> ⚠️ Only DM users in your server. Bots cannot DM users outside servers.
> 
