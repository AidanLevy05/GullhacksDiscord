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

# Cooldown configuration
COOLDOWN_SECONDS = 3


def cooldown_for_non_admins(ctx):
    """Return cooldown for non-admin users, None for admins (no cooldown)."""
    if ctx.author.guild_permissions.administrator:
        return None  # No cooldown for admins
    return commands.Cooldown(1, COOLDOWN_SECONDS)  # 1 use per 3 seconds


def is_help_channel(channel) -> bool:
    """Check if the channel is the designated help channel."""
    return channel.name in HELP_CHANNEL_NAME


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


@bot.event
async def on_command_error(ctx, error):
    """Handle command errors."""
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Slow down! Try again in {error.retry_after:.1f} seconds.")


# =============================================================================
# HACKATHON COMMANDS - Edit the responses below!
# =============================================================================

@bot.command(name='date')
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
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
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
async def parking(ctx):
    """Show parking information."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Parking Information",
        description="Parking is available in the Guerreri Academic Commons parking lot.",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command(name='food')
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
async def food(ctx):
    """Show food and meal information."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Food & Meals",
        description="We've got you covered all weekend!",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Saturday, November 7th",
        value=(
            "1:00 PM – Lunch\n"
            "7:00 PM – Dinner\n"
            "11:30 PM – Midnight snack"
        ),
        inline=False
    )
    embed.add_field(
        name="Sunday, November 8th",
        value=(
            "9:30 AM – Breakfast\n"
            "12:00 PM – Lunch"
        ),
        inline=False
    )
    await ctx.send(embed=embed)


@bot.command(name='location')
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
async def location(ctx):
    """Show venue location."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Venue Location",
        description="1101 Camden Ave, Salisbury, MD, 21801",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command(name='schedule')
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
async def schedule(ctx):
    """Show the event schedule."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Event Schedule",
        description="**Gullhacks 2026**",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Saturday, November 7th",
        value=(
            "11:00 AM – Arrival & informal gathering\n"
            "12:00 PM – Hacking begins\n"
            "1:00 PM – Lunch\n"
            "1:00 PM – 4:00 PM – Official check-in\n"
            "4:00 PM – Opening ceremony\n"
            "7:00 PM – Dinner\n"
            "11:30 PM – Midnight snack"
        ),
        inline=False
    )
    embed.add_field(
        name="Sunday, November 8th",
        value=(
            "9:30 AM – Breakfast\n"
            "10:00 AM – Mandatory check-in\n"
            "12:00 PM – Lunch & project submission deadline\n"
            "12:30 PM – 2:30 PM – Judging period\n"
            "3:00 PM – Closing ceremony"
        ),
        inline=False
    )
    await ctx.send(embed=embed)


@bot.command(name='workshops')
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
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
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
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
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
async def submission(ctx):
    """Show submission instructions."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Project Submission",
        description=(
            "**Deadline: Sunday, November 8th at 12:00 PM**\n\n"
            "TODO: Add submission instructions and Devpost link here"
        ),
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command(name='faq')
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
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
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
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
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
async def checkin(ctx):
    """Show check-in instructions."""
    if await redirect_to_help(ctx):
        return
    embed = discord.Embed(
        title="Check-in Information",
        description="There are two check-in times:",
        color=discord.Color.green()
    )
    embed.add_field(
        name="Saturday, November 7th",
        value="1:00 PM – 4:00 PM – Official check-in",
        inline=False
    )
    embed.add_field(
        name="Sunday, November 8th",
        value="10:00 AM – **Mandatory check-in**",
        inline=False
    )
    await ctx.send(embed=embed)


@bot.command(name='troll')
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
async def troll(ctx):
    """A fun troll response."""
    if await redirect_to_help(ctx):
        return
    await ctx.send("Nice try! Now get back to hacking! :)")


@bot.command(name='info')
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
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
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
async def help_command(ctx):
    """Show help and available commands."""
    embed = discord.Embed(
        title="Gullhacks Bot Help",
        description="Here are the available commands:",
        color=discord.Color.purple()
    )
    embed.add_field(name="!commands", value="List all commands", inline=True)
    embed.add_field(name="!info", value="General hackathon info", inline=True)
    embed.add_field(name="!faq", value="Frequently asked questions", inline=True)
    embed.add_field(name="!date", value="Hackathon date", inline=True)
    embed.add_field(name="!schedule", value="Event schedule", inline=True)
    embed.add_field(name="!food", value="Food & meals", inline=True)
    await ctx.send(embed=embed)

    # If not in help channel, tell them to go there for full access
    if not is_help_channel(ctx.channel):
        help_channel = discord.utils.get(ctx.guild.channels, name=HELP_CHANNEL_NAME)
        if help_channel:
            await ctx.send(f"Head over to {help_channel.mention} to use all the help commands!")
        else:
            await ctx.send(f"Head over to #{HELP_CHANNEL_NAME} to use all the help commands!")


@bot.command(name='commands')
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
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
@commands.dynamic_cooldown(cooldown_for_non_admins, commands.BucketType.user)
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
