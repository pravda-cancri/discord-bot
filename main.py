import os
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(
	command_prefix="~",  # Change to desired prefix. 
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 852192736231948308  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier
    
extensions = [
	'cogs.cg1',
    'cogs.music',
    'cogs.fun'
]

if __name__ == '__main__': 
	for extension in extensions:
		bot.load_extension(extension) 

keep_alive() 

my_secret = os.environ['maijn']
bot.run(my_secret)  



