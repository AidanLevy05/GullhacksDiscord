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
HELP_CHANNEL_NAME = 'help'  # The channel where the bot answers questions

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


def is_help_channel(channel) -> bool:
    """Check if the channel is the designated help channel."""
    return channel.name == HELP_CHANNEL_NAME


async def redirect_to_help(ctx) -> bool:
    """
    Check if user is in help channel. If not, redirect them.
    Returns True if redirected (command should stop), False if in correct channel.
    """
    if not is_help_channel(ctx.channel):
        help_channel = discord.utils.get(ctx.guild.channels, name=HELP_CHANNEL_NAME)
        if help_channel:
            await ctx.send(f"Please head over to {help_channel.mention} for help!")
        else:
            await ctx.send(f"Please go to the #{HELP_CHANNEL_NAME} channel for help!")
        return True
    return False


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
    # Redirect to help channel if not already there
    if await redirect_to_help(ctx):
        return

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
    # Redirect to help channel if not already there
    if await redirect_to_help(ctx):
        return

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
