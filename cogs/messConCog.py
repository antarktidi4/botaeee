from discord.ext import commands
import discord, jellyfish


class messageControlCog(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_raw_message_delete(self, payload: discord.RawReactionActionEvent):
		if payload.cached_message.author.bot is False:

			cachedMessText = payload.cached_message.content
			author = payload.cached_message.author

			try:
				embed=discord.Embed(title='Deleted Message:', description = cachedMessText, color=0xff00f6)
				embed.set_author(name = author, icon_url = author.avatar_url)
				if payload.cached_message.attachments != []:
					embed.set_image(url = payload.cached_message.attachments[0].proxy_url)
				await payload.cached_message.channel.send(embed = embed)
			except:
				await payload.cached_message.channel.send(f'{author.mention} delete: ' + cachedMessText)


	@commands.Cog.listener()
	async def on_raw_message_edit(self, payload: discord.RawReactionActionEvent):
		if payload.cached_message.author.bot is False:

			cached_message = payload.cached_message.content
			data = payload.data['content']
			author = payload.cached_message.author
			text = "edit '{0}' to '{1}'".format(cached_message, data)
			k = jellyfish.jaro_similarity(cached_message, data)
			dataL = len(data)
			cachL = len(cached_message)

			if k <= 0.45 or dataL*5 <= cachL:
				try:
					embed=discord.Embed(title='Edit message:', description = text, color=0xff00f6)
					embed.set_author(name = author, icon_url = author.avatar_url)
					if payload.cached_message.attachments != []:
						embed.set_image(url = payload.cached_message.attachments[0].proxy_url)
					await payload.cached_message.channel.send(embed = embed)
				except:
					await payload.cached_message.channel.send(f'{author.mention} edit: ' + text)



def setup(client):
	client.add_cog(messageControlCog(client))
