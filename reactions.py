import discord
import emoji
from discord.ext import commands
import reactions
class Reactions:
    "Lets the bot react to messages"
    def __init__(self,bot):
        self.bot=bot

    async def on_message(self,message):
        if message.author.bot:#prevents the bot from reacting to itself
            pass
        else:
            if "gay" in message.content.lower():
                await message.add_reaction('🏳️‍🌈')
            if "y/n" in message.content.lower():
                await message.add_reaction('👍')
                await message.add_reaction('👎')
            if "think" in message.content.lower():
                await message.add_reaction('🤔')
            if "balloon" in message.content.lower():
                await message.add_reaction('🎈')
            if "epic" in message.content.lower():
                await message.add_reaction('😎')
            if "nut" in message.content.lower():
                await message.add_reaction('😩')
            if "dick" in message.content.lower():
                await message.add_reaction('🍆')
            if "no sex" in message.content.lower():
                await message.add_reaction('🇭')
    
    @commands.command()
    async def reactions(self,ctx):
        "What messages the bot will react to"
        reactionem=discord.Embed(titles="List of reactions",color=discord.Color.red())
        reactionem.add_field(name="gay", value='🏳️‍🌈',inline=True)
        reactionem.add_field(name="y/n", value="👍👎",inline=True)
        reactionem.add_field(name="think",value="🤔",inline=True)
        reactionem.add_field(name="balloon",value='🎈',inline=True)
        reactionem.add_field(name="epic",value='😎',inline=True)
        reactionem.add_field(name="nut",value='😩',inline=True)
        reactionem.add_field(name="dick",value='🍆',inline=True)
        reactionem.add_field(name="no sex",value='🇭',inline=False)
        await ctx.send(embed=reactionem)

def setup(bot):
    bot.add_cog(Reactions(bot))