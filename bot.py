import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot configuration
TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = '!'

# Initialize bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)


def load_responses():
    """Load Q&A responses from JSON file."""
    with open('responses.json', 'r') as f:
        return json.load(f)


def find_answer(question: str) -> str:
    """Find the best matching answer for a question."""
    responses = load_responses()
    question_lower = question.lower()

    # Check each Q&A pair for keyword matches
    for qa in responses['questions']:
        for keyword in qa['keywords']:
            if keyword.lower() in question_lower:
                return qa['answer']

    # Return default response if no match found
    return responses['default_response']


@bot.event
async def on_ready():
    """Called when the bot is ready and connected."""
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} server(s)')

    # Set bot status
    await bot.change_presence(activity=discord.Game(name="!ask for help"))


@bot.event
async def on_member_join(member):
    """Welcome new members."""
    responses = load_responses()
    welcome_channel = discord.utils.get(member.guild.channels, name='welcome')

    if welcome_channel:
        await welcome_channel.send(f"Welcome {member.mention}! {responses['welcome_message']}")


@bot.command(name='ask')
async def ask(ctx, *, question: str = None):
    """
    Ask the bot a question about the hackathon.
    Usage: !ask where can I park?
    """
    if question is None:
        await ctx.send("Please provide a question! Example: `!ask where can I park?`")
        return

    answer = find_answer(question)

    # Create an embed for a nicer response
    embed = discord.Embed(
        title="Gullhacks Helper",
        description=answer,
        color=discord.Color.blue()
    )
    embed.set_footer(text=f"Asked by {ctx.author.display_name}")

    await ctx.send(embed=embed)


@bot.command(name='info')
async def info(ctx):
    """Display general hackathon information."""
    embed = discord.Embed(
        title="Welcome to Gullhacks!",
        description="Here's what I can help you with:",
        color=discord.Color.green()
    )
    embed.add_field(name="Parking", value="`!ask parking`", inline=True)
    embed.add_field(name="Food", value="`!ask food`", inline=True)
    embed.add_field(name="WiFi", value="`!ask wifi`", inline=True)
    embed.add_field(name="Schedule", value="`!ask schedule`", inline=True)
    embed.add_field(name="Submissions", value="`!ask submit`", inline=True)
    embed.add_field(name="Help", value="`!ask help`", inline=True)
    embed.set_footer(text="Type !ask followed by your question!")

    await ctx.send(embed=embed)


@bot.command(name='ping')
async def ping(ctx):
    """Check if the bot is responsive."""
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')


# Run the bot
if __name__ == '__main__':
    if TOKEN is None:
        print("Error: DISCORD_TOKEN not found!")
        print("Please create a .env file with your bot token.")
        print("See .env.example for reference.")
    else:
        bot.run(TOKEN)
