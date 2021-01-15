from discord import Activity, ActivityType
from discord.ext import commands
import discord, os



intents = discord.Intents.all()
client = commands.Bot(command_prefix = '$', intents = intents)
client.remove_command('help')


@client.command()
async def load(ctx, extension):
	role = discord.utils.get(ctx.author.guild.roles, name="Власть")
	if role in ctx.message.author.roles or ctx.message.author.id == 305715782732480512:
		client.load_extension(f"cogs.{extension}")
		await ctx.send(f'{extension} is loaded :white_check_mark:')

@client.command()
async def unload(ctx, extension):
	role = discord.utils.get(ctx.author.guild.roles, name="Власть")
	if role in ctx.message.author.roles or ctx.message.author.id == 305715782732480512:
		client.unload_extension(f"cogs.{extension}")
		await ctx.send(f'{extension} is unloaded :white_check_mark:')

@client.command()
async def reload(ctx, extension):
	role = discord.utils.get(ctx.author.guild.roles, name="Власть")
	if role in ctx.message.author.roles or ctx.message.author.id == 305715782732480512:
		client.unload_extension(f"cogs.{extension}")
		client.load_extension(f"cogs.{extension}")
		await ctx.send(f'{extension} is reloaded :arrows_counterclockwise:')


for files in os.listdir('./cogs'):
	if files.endswith('.py'):
		client.load_extension(f'cogs.{files[:-3]}')


@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=Activity(name='за всеми', type=ActivityType.watching))
token = os.environ.get('token')
client.run(token)
