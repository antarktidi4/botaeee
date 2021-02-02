import discord, datetime
from discord.ext import commands


class messageControlCog(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_raw_message_delete(self, payload: discord.RawReactionActionEvent):
		global exceptList
		if payload.cached_message.author.bot is False:

			cached_message = payload.cached_message.content
			author = payload.cached_message.author

			try:
				embed=discord.Embed(title='Deleted message:', description = cached_message, color=0xff00f6)
				embed.set_author(name = author, icon_url = author.avatar_url)

				if payload.cached_message.attachments != []:
					embed.set_image(url = cached_message.attachments[0].url)

				await payload.cached_message.channel.send(embed = embed)
			except:
				await payload.cached_message.channel.send(f'{author.mention} delete "{cached_message}"')
			
			except KeyError:
				questTime = datetime.date(2021, 1, 28)
				now = datetime.datetime.today().date()
				await payload.cached_message.channel.send(f'{author.mention} delete pic (waiting for a answer from support in days: {now-questTime})')



	@commands.Cog.listener()
	async def on_raw_message_edit(self, payload: discord.RawReactionActionEvent):
		global exceptList
		if payload.cached_message.author.bot is False:

			cached_message = payload.cached_message.content
			data = payload.data['content']
			author = payload.cached_message.author

			dataL = len(data)
			cachL = len(cached_message)

			if dataL*5 <= cachL:
				text = "edit '{0}' to '{1}'".format(cached_message, data)
				try:
					embed=discord.Embed(title='Edit message:', description = text, color=0xff00f6)
					embed.set_author(name = author, icon_url = author.avatar_url)
					await payload.cached_message.channel.send(embed = embed)
				except:
					await payload.cached_message.channel.send(f'{author.mention} ' + text)




def setup(client):
	client.add_cog(messageControlCog(client))
