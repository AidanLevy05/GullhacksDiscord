import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot configuration
TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = '!'
HELP_CHANNEL_NAME = 'help'  # The channel where the bot answers questions

# Initialize bot with intents (disable default help command to use custom one)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents, help_command=None)


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
    await bot.change_presence(activity=discord.Game(name="!commands for help"))


# =============================================================================
# HACKATHON COMMANDS - Edit the responses below!
# =============================================================================

@bot.command(name='date')
async def date(ctx):
    """Show the hackathon date."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Hackathon Date",
        description="**November 7th - 8th, 2026**\n\nMark your calendars!",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command(name='parking')
async def parking(ctx):
    """Show parking information."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Parking Information",
        description="TODO: Add parking information here",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command(name='food')
async def food(ctx):
    """Show food and meal information."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Food & Meals",
        description="TODO: Add food/meal information here",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command(name='location')
async def location(ctx):
    """Show venue location."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Venue Location",
        description="TODO: Add venue location and address here",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command(name='schedule')
async def schedule(ctx):
    """Show the event schedule."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Event Schedule",
        description="TODO: Add schedule here",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command(name='workshops')
async def workshops(ctx):
    """Show workshop information."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Workshops",
        description="TODO: Add workshop information here",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command(name='categories')
async def categories(ctx):
    """Show hackathon categories/tracks."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Hackathon Categories",
        description="TODO: Add hackathon categories/tracks here",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command(name='submission')
async def submission(ctx):
    """Show submission instructions."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Project Submission",
        description="TODO: Add submission instructions and Devpost link here",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command(name='faq')
async def faq(ctx):
    """Show frequently asked questions."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Frequently Asked Questions",
        description="TODO: Add FAQ items here",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command(name='sponsors')
async def sponsors(ctx):
    """Show sponsor information."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Our Sponsors",
        description="TODO: Add sponsor information here",
        color=discord.Color.gold()
    )
    await ctx.send(embed=embed)


@bot.command(name='checkin')
async def checkin(ctx):
    """Show check-in instructions."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Check-in Information",
        description="TODO: Add check-in location and instructions here",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)


@bot.command(name='troll')
async def troll(ctx):
    """A fun troll response."""
    if await redirect_to_help(ctx):
        return
    await ctx.send("Nice try! Now get back to hacking! :)")


@bot.command(name='info')
async def info(ctx):
    """Show general hackathon information."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Welcome to Gullhacks 2026!",
        description="**November 7th - 8th, 2026**\n\nTODO: Add general info here",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)


@bot.command(name='help')
async def help_command(ctx):
    """Show help and available commands."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Gullhacks Bot Help",
        description="Here are the available commands:",
        color=discord.Color.purple()
    )
    embed.add_field(name="!commands", value="List all commands", inline=True)
    embed.add_field(name="!info", value="General hackathon info", inline=True)
    embed.add_field(name="!faq", value="Frequently asked questions", inline=True)
    await ctx.send(embed=embed)


@bot.command(name='commands')
async def commands_list(ctx):
    """List all available commands."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="All Commands",
        description="Here's everything I can help you with:",
        color=discord.Color.purple()
    )
    embed.add_field(name="!date", value="Hackathon date", inline=True)
    embed.add_field(name="!location", value="Venue location", inline=True)
    embed.add_field(name="!parking", value="Parking info", inline=True)
    embed.add_field(name="!checkin", value="Check-in info", inline=True)
    embed.add_field(name="!schedule", value="Event schedule", inline=True)
    embed.add_field(name="!food", value="Food & meals", inline=True)
    embed.add_field(name="!workshops", value="Workshop info", inline=True)
    embed.add_field(name="!categories", value="Hackathon tracks", inline=True)
    embed.add_field(name="!submission", value="How to submit", inline=True)
    embed.add_field(name="!sponsors", value="Our sponsors", inline=True)
    embed.add_field(name="!faq", value="FAQ", inline=True)
    embed.add_field(name="!info", value="General info", inline=True)
    embed.add_field(name="!help", value="Get help", inline=True)
    embed.add_field(name="!troll", value="???", inline=True)
    embed.set_footer(text="Use these commands in #help")
    await ctx.send(embed=embed)


@bot.command(name='ping')
async def ping(ctx):
    """Check if the bot is responsive."""
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')


# =============================================================================
# RUN THE BOT
# =============================================================================

if __name__ == '__main__':
    if TOKEN is None:
        print("Error: DISCORD_TOKEN not found!")
        print("Please create a .env file with your bot token.")
        print("See .env.example for reference.")
    else:
        bot.run(TOKEN)
