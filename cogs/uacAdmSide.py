import cogs.ext.dbExt as dataBase
from discord.ext import commands
import asyncio


class uacAdmSide(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot is False and message.channel.id == 791457394710151199:
			id = message.content[2:]
			adm = await self.client.fetch_user('305715782732480512')
			member = await self.client.fetch_user(id)
			if message.content[:1] == 'y':
				class User(id):				#еее
					id = id				#баа
				user = User(id)				#ть
				dataBase.updateAlias(user, None)	#ну и костыль))
				await adm.send('дело сделано')
				await member.send('администрация одобрило смену погоняла')
			elif message.content[:1] == 'n':
				await adm.send('дело сделано')
				await member.send('вам отказано в смене погоняла')

	async def requestMessage(self, member):
		guild = self.client.get_guild(member.guild.id)
		user = await guild.fetch_member(member.id)
		alias = dataBase.UI(member)[3]
		messBody = f'''
		\n**userID**: {user.id}
		**userName**: {user.name}#{user.discriminator}
		**userNick**: {user.nick}(on {guild.name})
		**userAlias**: {alias}
		'''
		adm = await self.client.fetch_user('305715782732480512')
		await adm.send(messBody)


def setup(client):
	client.add_cog(uacAdmSide(client))
