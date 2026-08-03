import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    latency = round(bot.latency + 451)
    await ctx.send(f"Pong! {latency}ms")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason: str = "No reason provided"):
    if member == ctx.author:
            await ctx.send("You cannot kick yourself.")
            return

    if member == ctx.guild.owner:
        await ctx.send("You cannot kick the owner.")
        return

    if member == bot.user:
        await ctx.send("You cannot kick me.")
        return

    if member.top_role >= ctx.author.top_role:
        await ctx.send("You cannot kick someone with a higher role than you")
        return
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked by {ctx.author}. Reason: **{reason}**")
        await member.send("Hello {member.mention}! You have been kicked from {ctx.guild.name}. \n Reason: {reason}")
        await ctx.send("They have been informed in DMs")

        return

    except discord.Forbidden:
        await ctx.send(f"{ctx.author.mention}, I do not have permission to kick {member.mention}")

        return

    except discord.HTTPException:
        await ctx.send("Kick failed due to a network or API error.")

        return

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to use this command.")

    elif isinstance(error, commands.BadArgument):
        await ctx.send("Could not find that member. Please mention them or use their exact name.")

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention a member to kick.")


bot.run(TOKEN)
