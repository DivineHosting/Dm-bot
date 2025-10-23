import discord
from discord.ext import commands
import asyncio
from config import BOT_TOKEN, PREFIX, COLOR_WELCOME, COLOR_DM, COLOR_ANNOUNCEMENT, DELAY
from database import log_dm

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# ----------------------------
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# ----------------------------
@bot.event
async def on_member_join(member):
    """Auto-send welcome message when someone joins"""
    embed = discord.Embed(
        title="🎉 Welcome!",
        description=f"Hey {member.mention}, welcome to **{member.guild.name}**! Enjoy your stay 🎉",
        color=COLOR_WELCOME
    )
    embed.set_footer(text="Welcome!")
    try:
        await member.send(embed=embed)
        await log_dm(member, "Auto welcome message", True)
    except:
        await log_dm(member, "Auto welcome message", False)

# ----------------------------
@bot.command()
@commands.has_permissions(administrator=True)
async def dmuser(ctx, member: discord.Member, amount: int, *, message: str):
    """DM a single user multiple times"""
    success, fail = 0, 0
    for i in range(amount):
        try:
            msg = message.replace("{user}", member.name)
            embed = discord.Embed(
                title=f"📩 Message {i+1}/{amount}",
                description=msg,
                color=COLOR_DM
            )
            await member.send(embed=embed)
            await log_dm(member, msg, True, ctx.author)
            success += 1
            await asyncio.sleep(DELAY)
        except discord.Forbidden:
            fail += 1
            await ctx.send(f"❌ Cannot DM {member}. DMs closed or privacy settings block it.")
            break
        except Exception as e:
            fail += 1
            await ctx.send(f"⚠️ Error sending DM: {e}")
            break
    await ctx.send(f"✅ DMs sent: {success}, ❌ Failed: {fail}")

# ----------------------------
@bot.command()
@commands.has_permissions(administrator=True)
async def dm(ctx, member: discord.Member, amount: int, *, message: str):
    """DM a server member multiple times"""
    success, fail = 0, 0
    for i in range(amount):
        try:
            msg = message.replace("{user}", member.name)
            embed = discord.Embed(
                title=f"📩 Message {i+1}/{amount}",
                description=msg,
                color=COLOR_DM
            )
            await member.send(embed=embed)
            await log_dm(member, msg, True, ctx.author)
            success += 1
            await asyncio.sleep(DELAY)
        except discord.Forbidden:
            fail += 1
            await ctx.send(f"❌ Cannot DM {member}.")
            break
        except Exception as e:
            fail += 1
            await ctx.send(f"⚠️ Error: {e}")
            break
    await ctx.send(f"✅ DMs sent: {success}, ❌ Failed: {fail}")

# ----------------------------
@bot.command()
@commands.has_permissions(administrator=True)
async def dmall(ctx, amount: int, *, message: str):
    """DM all server members (non-bots) multiple times"""
    await ctx.send("📨 Sending DMs to all members...")

    members = [m for m in ctx.guild.members if not m.bot]
    success, fail = 0, 0

    for member in members:
        for i in range(amount):
            try:
                msg = message.replace("{user}", member.name)
                embed = discord.Embed(
                    title=f"📢 Announcement {i+1}/{amount}",
                    description=msg,
                    color=COLOR_ANNOUNCEMENT
                )
                await member.send(embed=embed)
                await log_dm(member, msg, True, ctx.author)
                success += 1
                await asyncio.sleep(DELAY)
            except discord.Forbidden:
                fail += 1
                await ctx.send(f"❌ Cannot DM {member}.")
                break
            except Exception as e:
                fail += 1
                await ctx.send(f"⚠️ Error: {e}")
                break

    await ctx.send(f"✅ Total DMs sent: {success}, ❌ Failed: {fail}")

# ----------------------------
bot.run(BOT_TOKEN)
