from discord import Activity, ActivityType
from discord.ext import commands
import discord, os



intents = discord.Intents.all()
client = commands.Bot(command_prefix = '$', intents = intents)



@client.command()
async def load(ctx, extension):
	role = discord.utils.get(ctx.author.guild.roles, name="Власть")
	if role in ctx.message.author.roles:
		client.load_extension(f"cogs.{extension}")
		await ctx.send(f'{extension} is loaded :white_check_mark:')

@client.command()
async def unload(ctx, extension):
	role = discord.utils.get(ctx.author.guild.roles, name="Власть")
	if role in ctx.message.author.roles:
		client.unload_extension(f"cogs.{extension}")
		await ctx.send(f'{extension} is unloaded :white_check_mark:')

@client.command()
async def reload(ctx, extension):
	role = discord.utils.get(ctx.author.guild.roles, name="Власть")
	if role in ctx.message.author.roles:
		client.unload_extension(f"cogs.{extension}")
		client.load_extension(f"cogs.{extension}")
		await ctx.send(f'{extension} is reloaded :arrows_counterclockwise:')

cogsList = 'bot is ready!\n'
for files in os.listdir('./cogs'):
	if files.endswith('.py'):
		try:
			client.load_extension(f'cogs.{files[:-3]}')
			cogsList += f'  - *{files[:-3]}* has loaded :white_check_mark:\n'
		except:
			cogsList += f'  - *{files[:-3]}* has no loaded :negative_squared_cross_mark:\n'

@client.event
async def on_ready():
	guild = client.get_guild(778169282655551498)
	channel = discord.utils.get(guild.channels, name='test')
	await channel.send(cogsList)
	await client.change_presence(status=discord.Status.idle, activity=Activity(name='за всеми', type=ActivityType.watching))
token = os.environ.get('token')
client.run(token)
