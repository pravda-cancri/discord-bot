import os
from keep_alive import keep_alive
from discord.ext import commands
import discord
import random
import PIL




hex_vals="123456789ABCDEF"
def randhex():
    hex=''.join(random.choice(list(hex_vals)) for _ in range(int(6)))
    hex="0x"+hex
    hex = int(hex, 16)
    return hex 


bot = commands.Bot(
	command_prefix="~",  # Change to desired prefix. 
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 852192736231948308  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier
    
@bot.command()
async def picture(ctx,*arg1):
    x=[""]
    try:
        x[0]=arg1[1]
    except:
        pass
    try:
        if arg1[0]==('astolfo')and x[0]=="":
            await ctx.send("sending pic")
            f=open("images.txt","r")
            f=f.read().splitlines()
            num=int(random.randint(0,len(f)-1))
            image = (f[num])
            embed = discord.Embed(colour=randhex())
            embed.set_image(url=image)
            await ctx.send(embed=embed)
            # importing google_images_download module
        if arg1[0]==('astolfo')and arg1[1]==("add"):
            a=open("images.txt","r")
            a=a.read().splitlines()
            f=open("images.txt","a")
            if "png" in arg1[2]:
                await ctx.send("pngs dont work")
                await ctx.send("link wasnt added")
            elif str(arg1[2]) in a:
                await ctx.send("duplicate link")
                await ctx.send("link wasnt added")
            else:
                f.write(arg1[2]+"\n")
                f.close()
    except:pass
        
   
    
        
extensions = [
	'cogs.cg1',
    'cogs.music'
]

if __name__ == '__main__': 
	for extension in extensions:
		bot.load_extension(extension) 

keep_alive() 

my_secret = os.environ['maijn']
bot.run(my_secret)  



