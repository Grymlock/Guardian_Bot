import discord
from discord.ext import commands
import constants as c
import sys
import os
class Owner:

    def __init__(self,bot):
        self.bot=bot
    
    @commands.group(hidden=True,invoke_without_command=True)
    async def owner(self,ctx,argument=None):
        if ctx.author.id != c.owner_id:
            pass
    

    @owner.command(name="shutdown")
    async def owner_shutdown(self,ctx):
        if ctx.author.id == c.owner_id:
            await ctx.send("Bot shutting down")
            await sys.exit()
        else:
            ctx.send(f"I'm sorry {ctx.author.name},I can't let you do that...")
        
    @owner.command(name="restart")
    async def owner_restart(self,ctx):
        if ctx.author.id==c.owner_id:
            await ctx.send("Bot restarting")
            await sys.exit
            await os.execl(sys.executable,sys.executable,*sys.argv)
        else:
            ctx.send(f"I'm sorry {ctx.author.name},I can't let you do that...")
    
    @owner.command(name="presence")
    async def admin_presence(self, ctx, *, presence=None):
        '''Sets the bot's "Playing" status.'''
        if ctx.author.id ==c.owner_id:
            if presence is None or "default"==presence:
                presence = discord.Game(f"--help | version{c.version}")
                await self.bot.change_presence(status=discord.Status.online, activity=presence)
                await ctx.send('Presence reset to default.')    
            else:
                presence = discord.Game(presence)
                await self.bot.change_presence(status=discord.Status.online, activity=presence)
                await ctx.send(f'Presence set to `{presence}`.')
        else:
            pass
    
    @owner.command(name="nick")
    async def admin_nick(self, ctx, *, reqnick=None):
        "Sets the bot's nickname for the server."
        if ctx.author.id ==c.owner_id:
            bb=ctx.guild.get_member(459390955691442177)
            if reqnick is None:
                await bb.edit(nick="Guardian")
                await ctx.send('Nickname reset')
            else:
                try:
                    await bb.edit(nick=reqnick)
                    await ctx.send(f'Nickname set to `{reqnick}`.')
                except:
                    await ctx.send('Nickname is too long!')
        else:
            pass
    
    @owner.command(name="say")
    async def admin_say(self, ctx, *, reqsaying=None):
        if ctx.author.id ==c.owner_id:
            if reqsaying is None:
                await ctx.send("You didn't tell me what you wanted me to say!")
            else:
                await ctx.send(reqsaying)
        else:
            pass
    
    @owner.command(name="leave")
    @commands.has_permissions(manage_guild=True)
    async def owner_leave(self,ctx):
        "Makes the bot leave the server"
        try:
            await ctx.send("Leaving the server see ya")
            await ctx.guild.leave()
        except:
            print(f"could not leave{ctx.guild.name}")
    
   
    
    @commands.bot_has_permissions(ban_members=True)
    @owner.command(name="ban")
    async def owner_ban(self,ctx,member:discord.Member=None,reason=None):
        if ctx.author.id != c.owner_id:
            pass
        else:
            try:
                await ctx.guild.ban(member,reason=reason)
                print(f"{member} was succesfully banned")
            except Exception as e:
                print(e)
    
    @commands.bot_has_permissions(kick_members=True)
    @owner.command(name="kick")
    async def owner_kick(self,ctx,member:discord.Member):
        if ctx.author.id != c.owner_id:
            pass
        else:
            try:
                await ctx.guild.kick(member,reason="gottem")
                print(f"{member} was kicked")
            except Exception as e:
                print(e)

def setup(bot):
    bot.add_cog(Owner(bot))

