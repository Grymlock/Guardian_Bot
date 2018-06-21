import discord
from discord.ext import commands
from discord.utils import find
import constants as c
Bot=commands.Bot(description="A WIP discord bot I'll fix in 5 weeks",command_prefix="--")


@Bot.event
async def on_ready():
    for cog in c.cogs:

        try:
            Bot.load_extension(f"{cog}")
            print(f"Cog {cog} successfully loaded.")
            
        except Exception as e:
            print(f"CRITICAL: Cog {cog} failed to load.")
            print(e)

    print(f'Logged in as\n{Bot.user .name}\n{Bot.user.id}\nGuardian v{c.version} Online')

    botusers = 0    
    for user in Bot.users:  
        if user.bot is True:
            continue
        else:
            botusers = botusers + 1

    botguilds = 0
    for guild in Bot.guilds:
        botguilds = botguilds + 1

    botchannels = 0
    for guild in Bot.guilds:
        for channel in guild.channels:
            botchannels = botchannels + 1

    presence = discord.Game(f"--help | v{c.version}")
    await Bot.change_presence(status=discord.Status.online, activity=presence)

@Bot.event
async def on_guild_join(guild):
    try:
        general=find(lambda m:"general" in m.name, guild.text_channels)
        await general.send("Hello everybody. I am a WIP discord bot a bored junior made. I'm fairly basic, but new features will be added soon")
    except:
        pass

Bot.run(c.token)