from random import randint, choice
import cogs.ext.dbExt as dataBase
from discord.ext import commands
import discord


class UserLvl(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_member_join(self, member):
		try:
			if member.guild.id == 778169282655551498:
				guild = self.client.get_guild(member.guild.id)
				await member.add_roles(discord.utils.get(guild.roles, name="Рабочий класс"))
				dataBase.updateData(member)
		except AttributeError:
			pass

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.content.lower().startswith('когда'):
			list = ['сейчас', 'вчера', 'завтра', 'через неделю', f'через {randint(5,16)} дней']
			await message.channel.send(f'{message.author.mention} {choice(list)}')
		try:
			if message.author.bot is False and message.channel.guild.id == 778169282655551498:
				dataBase.updateData(message.author)
				uExp = dataBase.UI(message.author)[1]
				dataBase.addExp(uExp, 5, message.author)
				updated = dataBase.updateLvl(message.author, message.channel)
				if updated is not None:
					await message.channel.send(updated)
		except AttributeError:
			pass


def setup(client):
	client.add_cog(UserLvl(client))
