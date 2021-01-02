from discord.ext import commands
import json, discord
from cogs.dbCog import addExp, UI, removeLvl
from random import randint


class rr(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name = 's')
	async def s(self, ctx):
		role = discord.utils.get(ctx.message.author.guild.roles, name="Власть")
		if role in ctx.message.author.roles:
			soloMess = await ctx.fetch_message(790285591102619690)
			duoMess = await ctx.fetch_message(790285669817778176)
			await soloMess.edit(content='{"user": "sosat!", "bullets": 0}')
			await duoMess.edit(content='{"firstUser": "first sosat!", "secondUser": "second sosat!", "state": 1, "bullets": 0}')
			await ctx.send('дело сделано')


	@commands.command(name = 'grs')
	async def grs(self, ctx):
		soloMess = await ctx.fetch_message(790285591102619690)
		duoMess = await ctx.fetch_message(790285669817778176)
		await ctx.send(f'solo: {soloMess.content}\nduo: {duoMess.content}')

	@commands.command(name = 'rEx')
	async def rEx(self, ctx):
		channel = await self.client.fetch_channel(778308167650115594)
		mess = await channel.fetch_message(790285591102619690)
		data = json.loads(str(mess.content))
		if data['user'] == ctx.message.author.mention:
			exp = 200*(6-data['bullets'])
			uID, uExp, Ulvl, uAlias = await UI(ctx.message.author.id)
			await addExp(uExp, exp, uID)
			data['bullets'] = 0
			data['user'] = 'sosat'
			d = json.dumps(data)
			await mess.edit(content=d)
			await ctx.send(f'{ctx.message.author.mention} Зассал и выкинул револьвер.\n  Полученно exp: {exp}')


	@commands.command(name = 'roulette')
	async def roulette(self, ctx, member: discord.Member = None):
		if member is not None:
			await ctx.send(f'{ctx.message.author.mention} скоро будет сделано')
		else:
			channel = await self.client.fetch_channel(778308167650115594)
			mess = await channel.fetch_message(790285591102619690)
			data = json.loads(str(mess.content))
			if data['bullets'] == 0:
				await ctx.send(f'{ctx.message.author.mention} готов рискнуть жизнью в русской рулетке.\n  Заряжает револьвер.')
				data['bullets'] = 6
				data['user'] = ctx.message.author.mention
				dumped = json.dumps(data)
				await mess.edit(content=dumped)

			elif data['user'] == ctx.message.author.mention:
				state = randint(1, data['bullets'])
				uID, uExp, Ulvl, uAlias = await UI(ctx.message.author.id)

				if state == 1:
					exp = 100+200*(6-data['bullets'])
					await addExp(uExp, -exp, uID)
					lvl = int(uExp ** (1/4))
					data['bullets'] = 0
					data['user'] = 'sosat'
					await ctx.send(f'{ctx.message.author.mention} Сделал выстрел и умер.\n  Потеряно exp: {exp}')
					if Ulvl < lvl:
						await removeLvl(uID, lvl)
						await ctx.send(f'{ctx.message.author.mention} reduced level to {lvl}')

				elif data['bullets'] > 1:
					data['bullets'] -= 1
					await addExp(uExp, 200, uID)
					await ctx.send(f'{ctx.message.author.mention} Сделал выстрел и выжил.\n  Добавлено 200 exp(осталось выстрелов {data["bullets"]-1})')

				elif data['bullets'] == 1:
					data['bullets'] = 0
					await addExp(uExp, 200, uID)
					await ctx.send(f'{ctx.message.author.mention} Сделал последний выстрел и выиграл 1к экспы, поздравьте счастливчика!')

				d = json.dumps(data)
				await mess.edit(content=d)



def setup(client):
	client.add_cog(rr(client))
