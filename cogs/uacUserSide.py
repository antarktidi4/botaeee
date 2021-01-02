from random import choice
from discord.ext import commands
from cogs.dbCog import UI, updateAlias
from cogs.uacAdmSide import uacAdmSide
import discord


class uAliasCog(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command(name = 'ua')
	async def ua(self, ctx, member: discord.Member = None):
		p = ['попущенец', 'педофилыч', 'хуйс', 'король', 'пиздоблядка', 'хохол', 'вор', 'чиркаш', 'депутат', 'шнырь', 'водолаз', 'колпак', 'пидорас', 'вахчун', 'шпак', 'Гудабзай', 'симп', 'инцел']
		if member is None:
			user = ctx.message.author.mention
			uInfo = await UI(ctx.message.author.id)
			if uInfo[3] is not None:
				await ctx.send(f'{user} имеет заслуженное звание "{uInfo[3]}"\n*(для смены напишите $uaChange и после рассмотрения модерации будет доступна смена.)*')
			else:
				alias = choice(p)
				await updateAlias(ctx.message.author.id, alias)
				await ctx.send(f'{user} получает заслуженное звание "{alias}"\n*(для смены напишите $uaChange и после рассмотрения модерации будет доступна смена.)*')
		elif member is not None and member.bot is False:
			user = member.mention
			uInfo = await UI(member.id)
			if uInfo[3] is not None:
				await ctx.send(f'{user} имеет заслуженное звание "{uInfo[3]}"')
			else:
				await ctx.send(f'у {user} отстутствует звание')
		else:
			await ctx.send(f'{user} имеет заслуженное звание "None"')

	@commands.command(name = 'uaChange')
	async def uaChange(self, ctx):
		user = ctx.message.author
		uInfo = await UI(user.id)
		if uInfo[3] is not None:
			await uacAdmSide.requestMessage(self, user)
			await ctx.send(f'{user.mention} заявка на смену отправлена, ожидайте ответа модерации.')
		else:
			await ctx.send(f'{user.mention} для смены нужно иметь погоняло. Пропишите $ua')


def setup(client):
	client.add_cog(uAliasCog(client))
