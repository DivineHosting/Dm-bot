import discord
from discord.ext import commands
import asyncio
from config import BOT_TOKEN, PREFIX, COLOR_WELCOME, COLOR_DM, COLOR_ANNOUNCEMENT
from database import log_dm

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# -----------------------------------------
# READY EVENT
# -----------------------------------------
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game("Welcoming new members 👋"))

# -----------------------------------------
# AUTO WELCOME DM
# -----------------------------------------
@bot.event
async def on_member_join(member):
    try:
        embed = discord.Embed(
            title="🎉 Welcome!",
            description=f"Hey {member.mention}, welcome to **{member.guild.name}**!\nWe’re happy to have you here 💫",
            color=COLOR_WELCOME
        )
        embed.set_footer(text="Enjoy your stay!")
        await member.send(embed=embed)
        await log_dm(member, "Auto welcome message", True)
    except Exception as e:
        print(f"❌ Couldn’t DM {member}: {e}")
        await log_dm(member, "Auto welcome message", False)

# -----------------------------------------
# COMMANDS
# -----------------------------------------

@bot.command()
@commands.has_permissions(administrator=True)
async def dm(ctx, member: discord.Member, *, message: str):
    """DM a specific user in the server"""
    message = message.replace("{user}", member.name)
    embed = discord.Embed(
        title="📩 Message from Admin",
        description=message,
        color=COLOR_DM
    )
    try:
        await member.send(embed=embed)
        await ctx.send(f"✅ DM sent to {member.mention}")
        await log_dm(member, message, True, ctx.author)
    except Exception as e:
        await ctx.send(f"❌ Couldn’t DM {member.mention}: {e}")
        await log_dm(member, message, False, ctx.author)

@bot.command()
@commands.has_permissions(administrator=True)
async def dmuser(ctx, user_id: int, *, message: str):
    """DM a user by ID (not just server members)"""
    try:
        user = await bot.fetch_user(user_id)
        msg = message.replace("{user}", user.name)
        embed = discord.Embed(
            title="📨 Message",
            description=msg,
            color=COLOR_DM
        )
        await user.send(embed=embed)
        await ctx.send(f"✅ DM sent to {user}")
        await log_dm(user, msg, True, ctx.author)
    except discord.NotFound:
        await ctx.send("❌ User not found.")
    except discord.Forbidden:
        await ctx.send("❌ Cannot DM this user (DMs closed).")
    except Exception as e:
        await ctx.send(f"⚠️ Error: {e}")
        await log_dm(user_id, message, False, ctx.author)

@bot.command()
@commands.has_permissions(administrator=True)
async def dmall(ctx, *, message: str):
    """DM all server members (except bots)"""
    await ctx.send("📨 Sending DMs to all members...")
    success = 0
    fail = 0

    for member in ctx.guild.members:
        if not member.bot:
            try:
                msg = message.replace("{user}", member.name)
                embed = discord.Embed(
                    title="📢 Announcement",
                    description=msg,
                    color=COLOR_ANNOUNCEMENT
                )
                await member.send(embed=embed)
                await log_dm(member, msg, True, ctx.author)
                success += 1
                await asyncio.sleep(2)
            except:
                fail += 1

    await ctx.send(f"✅ Sent: {success}, ❌ Failed: {fail}")

# -----------------------------------------
bot.run(BOT_TOKEN)
