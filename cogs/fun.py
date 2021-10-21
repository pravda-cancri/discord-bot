import discord
from discord.ext import commands
import random
from ext.hexs import randhex

def send(ctx,char):
    f=open(char+".txt","r")
    f=f.read().splitlines()
    num=int(random.randint(0,len(f)-1))
    image = (f[num])
    embed = discord.Embed(colour=randhex())
    embed.set_image(url=image)
    return embed
    
def add_link(ctx,char,link):
    f=open(char+".txt","a")
    for x in link:
        f.write(x+"\n")
        f.close()

class Funcommands(commands.Cog, name='fun'):
	def __init__(self, bot):
		self.bot = bot

@commands.command()
async def picture(ctx, *arg):
    x=[""]
    try:
        x[0]=arg[1]
    except:
        pass
    f=open("characters.txt","r")
    f=f.read().splitlines()
    if arg[0].lower() in f and x[0] !="":
        await ctx.send(embed=send(ctx,arg[0]))
    elif x[0] !="":
        try:
            f=open("characters.txt","a")
            f.write(arg.lower()+"\n")
            f.close()
        except:
            pass
    if arg[1]==("add"):
        _=[]
        for i in range (len(arg-3)):
            _.append(arg[i+3])
        add_link(ctx,arg[0].lower(),_)

def setup(bot):
	bot.add_cog(Funcommands(bot))