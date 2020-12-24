from discord.ext import commands
from cogs.dbCog import UI, removeAlias



class uacAdmSide(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot is False and message.channel.id == 791457394710151199:
			id = message.content[2:]
			if message.content[:1] == 'y':
				removeAlias(id)
				member = await self.client.fetch_user('305715782732480512')
				await member.send('дело сделано')
				member = await self.client.fetch_user(id)
				await member.send('администрация одобрило смену погоняла')
			elif message.content[:1] == 'n':
				member = await self.client.fetch_user(id)
				await member.send('вам отказано в смене погоняла')


	async def requestMessage(self, member):
		guild = self.client.get_guild(member.guild.id)
		user = await guild.fetch_member(member.id)
		alias = UI(user.id)[3]

		messBody = f'''
		**userID**: {user.id}
		**userName**: {user.name}#{user.discriminator}
		**userNick**: {user.nick}(on {guild.name})
		**userAlias**: {alias}
		'''

		member = await self.client.fetch_user('305715782732480512')
		await member.send(messBody)





def setup(client):
	client.add_cog(uacAdmSide(client))
