# 🤖 Discord Welcome DM Bot

A safe, full-featured Discord bot that:
- DMs new members automatically
- Allows admins to send DMs
- Logs all sent messages to MongoDB

### ⚙️ Setup
1. Clone the repo
2. Add `.env` with:
BOT_TOKEN=your_token
MONGO_URI=your_mongo_uri
3. pip install -r requirements.txt
      python bot.py
### 🚀 Commands
| Command | Description |
|----------|-------------|
| `!dm @user message` | Send a DM to a server user |
| `!dmuser ID message` | Send a DM by Discord ID |
| `!dmall message` | DM all non-bot members |
