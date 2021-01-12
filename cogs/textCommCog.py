from random import randint
from discord.ext import commands
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
		embed.add_field(name="text command", value="card @nick(опц.) - *карточка юзера*\ngaytest - *тест на гея*\ndickometr - *размер твоего гиганта*\noppr @nick - *унижение чела*\nct {text} - *клоунский текст*\nua @nick(опц.) - *погоняло*", inline=True)
		embed.add_field(name="parse command", value="anec - *анекдот*\nmeme - *рандомный мем*\nrhentai - *рандом пик хентая*\ndhentai {tag} - *пик хентая по тегу*\navatar @nick(опц.) - аватарка юзера\ntoken - *токен бота*\nimg arg(опц.) - *рандом пик по arg*", inline=True)
		embed.add_field(name="games", value="ttt @nick - *крестики нолики*\nrHelp - *помощь по русской рулетке*", inline=True)
		await ctx.send(embed=embed)

	@commands.command(name = 'rHelp')
	async def rHelp(self, ctx):
		embed=discord.Embed(title="roulette Help")
		embed.add_field(name="solo:", value="roulette - стреляешь 5 раз. Стрельнул и не умер? - выиграл 200xp, а если же умер - -100xp и все накопленные выше", inline=True)
		embed.add_field(name="duo", value="*скоро будет...*", inline=True)
		embed.add_field(name="**важно!**", value="в любой момент можно прописать $rEx и выйти из рулетки", inline=False)
		embed.set_footer(text="Удачи!")
		await ctx.send(embed=embed)


	@commands.command(name = 'ct')
	async def ct(self, ctx):
		x = 0
		final = ""
		text = ctx.message.content[4:]
		for Chr in text:
			x += 1
			final += Chr.upper() if x % 2 == 0 else Chr.lower()
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
		text = f'{ctx.message.author.mention} унизил {member.mention}' if randint(1, 4) != 4 else f'{ctx.message.author.mention} попытался унизить {member.mention}, но обосрался и ушёл с позором'
		await ctx.send(text)



	@commands.command(name = 'tn')
	async def tn(self, ctx):
		text = f'токсичность Николая на сегодня превышает 70%, возможны всплески агрессии, куча негатива; советуем сегодня не злить Коляна'
		await ctx.send(text)

		await ctx.send(text)		
		
		

def setup(client):
	client.add_cog(textCommands(client))
