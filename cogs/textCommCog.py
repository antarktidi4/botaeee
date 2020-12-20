from discord.ext import commands
from random import randint
import discord


class textCommands(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

	@commands.command()
	async def help(self, ctx):
		embed=discord.Embed(title="Help command")
		embed.add_field(name="text command", value="gaytest - тест на гея\ndickometr - размер твоего гиганта\noppr @nick - унижение чела\nct {text} - клоунский текст", inline=True)
		embed.add_field(name="parse command", value="anec - анекдот\nmeme - рандомный мем\nrhentai - рандом пик хентая\ndhentai {tag} - пик хентая по тегу", inline=True)
		embed.add_field(name="games", value="ttt @nick - крестики нолики\nrHelp - помощь по русской рулетке", inline=True)
		await ctx.send(embed=embed)


	@commands.command(name = 'rHelp')
	async def rHelp(self, ctx):
		await ctx.send(f'{ctx.message.author.mention} соло: стреляешь 5 раз. Стрельнул и не умер? - выиграл 200xp, а если же умер - -100xp и все заработанные выше:)\nдуо: *скоро будет...*\nУдачи!')

	@commands.command(name = 'ct')
	async def ct(self, ctx):
		x = 0
		final = ""
		text = ctx.message.content[4:]
		for Chr in text:
			x += 1
			if x % 2 == 0:
				final += Chr.upper()
			else:
				final += Chr.lower()
		try:
			msg = await ctx.message.channel.fetch_message(ctx.message.id)
			await msg.delete()
		except:
			pass
		await ctx.send(final)


	@commands.command(name = 'gaytest')
	async def gaytest(self, ctx):
		await ctx.send(f'{ctx.message.author.mention} гей на {randint(0,100)}%')

	@commands.command(name = 'dickometr')
	async def test(self, ctx):
		await ctx.send(f'{ctx.message.author.mention} размер твоего члена: {randint(3,35)}см')

	@commands.command(name = 'бодишейминг')
	async def bodyshaming(self, ctx, member: discord.Member):
		msg = await ctx.message.channel.fetch_message(ctx.message.id)
		await msg.delete()
		await ctx.send(f'{ctx.message.author.mention} забодишеймил {member.mention}')

	@commands.command(name = 'oppr')
	async def oppression(self, ctx, member: discord.Member):
		msg = await ctx.message.channel.fetch_message(ctx.message.id)
		chance = randint(1, 4)
		text = f'{ctx.message.author.mention} унизил {member.mention}' if chance != 4 else f'{ctx.message.author.mention} попытался унизить {member.mention}, но обосрался и ушёл с позором'
		await ctx.send(text)
		await msg.delete()


		
def setup(client):
	client.add_cog(textCommands(client))
