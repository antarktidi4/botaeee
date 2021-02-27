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

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id == 778169282655551498:
			embed=discord.Embed(title='Caspar message:', description = message.content, color=0xff00f6)
			embed.set_author(name = message.author.name, icon_url = message.author.avatar_url)
			if message.attachments != []:
				attachName = message.attachments[0].filename.split('.')
				if message.attachments[0].filename.split('.')[len(attachName)-1] in 'png,jpg,jpeg'.split(','):
					embed.set_image(url = message.attachments[0].proxy_url)
				else:
					embed.add_field(name = 'File: ', value = f'url: {message.attachments[0].url}')
					embed.add_field(name = 'File: ', value = f'proxy url: {message.attachments[0].proxy_url}')
			await message.channel.send(embed = embed)



def setup(client):
	client.add_cog(UserLvl(client))
