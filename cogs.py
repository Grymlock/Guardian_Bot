import discord 
from discord.ext import commands
import constants as c



class CogManager:

    def __init__(self,bot):
        self.bot=bot
    
    @commands.group(invoke_without_command=True,hidden=True)
    async def cm(self,ctx):
        if ctx.author.id != c.owner_id:
            await ctx.send("Not the bot owner buddy")
        else:
            await ctx.send("No cog specified")
    
    @cm.command(name='load')
    async def cm_load(self,ctx,*,rcog):
        if ctx.author.id != c.owner_id:
            await ctx.send("Not the bot owner buddy")
        else:
            try:
                if rcog in c.cogs:
                    self.bot.load_extension(rcog)
                    await ctx.send(f"Cog `{rcog}` loaded successfully.")
            
                else:
                    await ctx.send("That cog does not exist")
            except Exception as e:
                await ctx.send(f"```Python\n{e}```")
                await ctx.send("Error cog failed to load.")

    @cm.command(name='unload')
    async def cm_unload(self,ctx,*,rcog):
        if ctx.author.id != c.owner_id:
            await ctx.send('Not the bot owner buddy')
        else:
            try:
                if rcog in c.cogs:
                    self.bot.unload_extension(rcog)
                    await ctx.send(f"Cog `{rcog}` unloaded succesfully")
                else:
                    await ctx.send("That cog does not exist")
            except Exception as e:
                await ctx.send(f"```Python\n{e}```")
            
    
    @cm.command(name="reload")
    async def cm_reload(self,ctx,*,rcog):
        if ctx.author.id != c.owner_id:
            await ctx.send("Not the bot owner buddy")
        else:
            try:
                if rcog in c.cogs:
                    self.bot.unload_extension(rcog)
                    self.bot.load_extension(rcog)
                    await ctx.send(f"Cog `{rcog}` reloaded succesfully")
                else:
                     await ctx.send("That cog does not exist")
            except Exception as e:
                await ctx.send(f"```Python\n{e}```")
                await ctx.send("Error cog failed to load.")
    
    @cm.command(name="list")
    async def cm_list(self,ctx):
        if ctx.author.id != c.owner_id:
            await ctx.send("Not the bot owner buddy")
        else:
            cogList=discord.Embed(color=discord.Color.green())
            for cog in c.cogs:
                cogList.add_field(name="Cog",value=(f"{cog}"))
            await ctx.send(embed=cogList)

def setup(bot):
    bot.add_cog(CogManager(bot))

                


