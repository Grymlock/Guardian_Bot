import discord
import constants as c
from discord.ext import commands
import random as r
urls=['https://cdn.discordapp.com/attachments/433007901800398858/433047585121501194/maxresdefault.jpg','https://cdn.discordapp.com/attachments/442868510776098818/442879211296915466/9bt3n9w40bp01.jpg','https://cdn.discordapp.com/attachments/442323518860951589/443142715761360915/Dap.PNG',"https://cdn.discordapp.com/attachments/442323518860951589/443250907501821964/IMG_20180222_192827.jpg"]
badWords=["gamer","frick","fudge","heck","bubby"]
class Fun:

    def __init__(self,bot):
        self.bot=bot
    
    @commands.command()
    async def dab(self,ctx, *, member: discord.Member):
        "everybody pause at 1:18"
        try:
            if member.id==426560497781833748 or member.id==c.owner_id:
                await ctx.send("haha no")
            else:
                em=discord.Embed(title="",description='')
                rand=r.randint(0,3)
                em.set_image(url=str(urls[rand]))
                await ctx.send(embed=em)
                await ctx.send(str(member.mention))
        except:
            await ctx.send("Invalid user")
    
    
    @commands.command()
    async def bruhcat(self,ctx):
        "bruh"
        catembed=discord.Embed()
        catembed.set_image(url="https://cdn.discordapp.com/attachments/444325494264037377/445300639631671296/bruh.gif")
        await ctx.send(embed=catembed)
    
    @commands.command()
    async def blicky(self,ctx):
        em=discord.Embed()
        em.set_image(url="https://cdn.discordapp.com/attachments/444325494264037377/445407209359409163/27c3yf.png")
        await ctx.send(embed=em)

    async def on_message(self,message):
        if message.author.bot:#prevents the bot from reacting to itself
            pass
        else:
            for word in badWords:
                if message.content==(word):
                    await message.channel.send(f"Please do not use the word '{word}' or I will report you and block you")
            ran=r.randint(1,2000)
            if ran==1:
                await message.channel.send("^Are you listening to this retard lmao")
            if message.content==("gm") or message.content==("good morning"):
                await message.channel.send("Another day closer to death" + str(message.author.mention))
            if message.content==("gn") or message.content==("good night"):
                await message.channel.send("sleep tight boyo")
            if message.content==("good bye"):
                await message.channel.send("bye loser")
            if message.content==("what do we want"):
                await message.channel.send("Equality for women")
            if message.content==("when do we want it"):
                await message.channel.send("Now")
    

    async def on_member_ban(self,guild,member):
        if member==c.owner_id:
            await guild.owner.send("Can y'all stop banning my master")

def setup(bot):
    bot.add_cog(Fun(bot))