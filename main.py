import os
from keep_alive import keep_alive
from discord.ext import commands
import os
import os.path

bot = commands.Bot(
	command_prefix="~",  # Change to desired prefix. 
	case_insensitive=True  # Commands aren't case-sensitive
)

my_secret1 = os.environ['id']
bot.author_id = my_secret1  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

extensions = [
	'cogs.cg1',
    'cogs.fun',
    'cogs.music'
]

if __name__ == '__main__': 
	for extension in extensions:
		bot.load_extension(extension) 

keep_alive() 

my_secret = os.environ['maijn']
bot.run(my_secret)  