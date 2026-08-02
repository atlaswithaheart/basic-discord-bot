# Discord Bot

A simple Discord bot built with Python using `discord.py`.

This is my first Discord bot project. It includes basic commands and demonstrates how to create a bot, handle commands, and safely store secrets using environment variables.

![Bot Commands Screenshot](commands.png)

## Features

* `!ping` - Shows the bot's latency
* `!hello` - Greets the user and mentions them
* Secure token handling using `.env` files

## Commands

| Command  | Description                            |
| -------- | -------------------------------------- |
| `!ping`  | Displays the bot's response time       |
| `!hello` | Sends a greeting and mentions the user |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create your environment file

Create a file named `.env`:

```env
DISCORD_TOKEN=your_bot_token_here
```

Replace `your_bot_token_here` with your Discord bot token.

## Running the Bot

Run:

```bash
python bot.py
```

If everything is set up correctly, the bot will appear online in your Discord server.

## Security

The bot token is stored in a `.env` file and is **not uploaded to GitHub**.

The `.gitignore` file prevents sensitive files from being committed:

```
.env
```

## Built With

* Python
* discord.py
* python-dotenv

## License

This project is for learning and demonstration purposes.
