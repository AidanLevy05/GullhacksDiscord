# GullhacksDiscord

A Discord bot for the Gullhacks hackathon that answers frequently asked questions about parking, food, schedule, and more!

## Features

- **Q&A System**: Answer common hackathon questions using keywords
- **Easy to Customize**: Edit `responses.json` to add/modify Q&A pairs
- **Embed Responses**: Clean, formatted responses using Discord embeds
- **Welcome Messages**: Greet new members automatically

## Setup Instructions

### 1. Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" tab and click "Add Bot"
4. Under "Privileged Gateway Intents", enable:
   - **Message Content Intent** (required for reading messages)
5. Click "Reset Token" and copy your bot token (keep it secret!)

### 2. Install the Bot

```bash
# Clone the repository (if you haven't already)
git clone <repository-url>
cd GullhacksDiscord

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure the Bot

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your bot token
# DISCORD_TOKEN=your_actual_token_here
```

### 4. Invite the Bot to Your Server

1. Go to the Discord Developer Portal
2. Select your application > OAuth2 > URL Generator
3. Select scopes: `bot`
4. Select bot permissions:
   - Send Messages
   - Embed Links
   - Read Message History
5. Copy the generated URL and open it in your browser
6. Select your server and authorize the bot

### 5. Run the Bot

```bash
python bot.py
```

## Usage

### Commands

| Command | Description |
|---------|-------------|
| `!ask <question>` | Ask a question about the hackathon |
| `!info` | Display available help topics |
| `!ping` | Check if the bot is online |

### Examples

```
!ask where can I park?
!ask what's for dinner?
!ask wifi password
!ask schedule
```

## Customizing Responses

Edit `responses.json` to add or modify Q&A pairs:

```json
{
  "keywords": ["your", "keywords", "here"],
  "answer": "Your answer here!"
}
```

### Tips for Keywords

- Use lowercase keywords (matching is case-insensitive)
- Add multiple variations (e.g., "park", "parking", "car")
- More specific keywords should come first in the list

## File Structure

```
GullhacksDiscord/
├── bot.py              # Main bot code
├── responses.json      # Q&A pairs (edit this!)
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment file
├── .env                # Your actual environment file (don't commit!)
└── README.md           # This file
```

## Troubleshooting

**Bot not responding?**
- Make sure Message Content Intent is enabled in the Developer Portal
- Check that the bot has permission to read/send messages in the channel

**"DISCORD_TOKEN not found" error?**
- Make sure you created a `.env` file (not just `.env.example`)
- Check that the token is correct and not expired

## License

MIT
