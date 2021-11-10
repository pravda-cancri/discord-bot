import discord
from discord.ext import commands
import random
from exts.hexs import randhex

import json
usagecount = {}

def _save():
    with open('jsons/usagecount.json', 'w') as f:
        json.dump(usagecount, f)

def timesused(x):
    command = x
    if command in usagecount:
        usagecount[command] = usagecount[command] + 1
        _save()
    elif command not in usagecount:
        usagecount[command] = 1
        _save()

def send(ctx,char):
    f=open("url_list/"+char+".txt","r")
    f=f.read().splitlines()
    num=int(random.randint(0,len(f)-1))
    image = (f[num])
    embed = discord.Embed(title=char, url=image, colour=randhex())
    embed.set_footer(text=f'This command has been used {usagecount[char]} times.')
    embed.set_image(url=image)
    return embed
    
def add_link(ctx,char,link):
    f=open("url_list/"+char+".txt","r")
    f=f.read().splitlines()
    if link not in f:
        f=open("url_list/"+char+".txt","a")
        f.write("\n"+link)
        f.close()
            
class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # says when bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        global usagecount
        try:
            with open('jsons/usagecount.json') as f:
                usagecount = json.load(f)
                print('is loaded\n')
        except FileNotFoundError:
            print("Could not load usagecount.json")
            usagecount = {}

    @commands.command( aliases=['p'])
    async def picture(self,ctx, *arg):
        x=["",""]
        try:
            x[0]=arg[1]
            x[1]=arg[2]
        except:
            pass
        f=open("url_list/characters.txt","r")
        f=f.read().splitlines()
        y=arg[0]
        if y in f and x[0]=="":
            timesused(y)
            await ctx.send(embed=send(ctx,arg[0].lower()))

        if arg[0]==("add"):
            f=open("url_list/characters.txt","r")
            f=f.read().splitlines()
            char= arg[1]
            if char not in f:
                f=open("url_list/characters.txt","a")
                f.write(arg[1].lower()+"\n")
                f.close()
            f=open("url_list/"+arg[1].lower()+".txt","w")
            f.write("")
            f.close()
            add_link(ctx,arg[1].lower(),arg[2])

        if arg[0]=="list":
            f=open("url_list/characters.txt","r")
            f=f.read().splitlines()
            await ctx.send("the availiable photos are")
            v=''.join(_+"\n" for _ in f)
            await ctx.send(v)

def setup(bot):
    bot.add_cog(Fun(bot))
