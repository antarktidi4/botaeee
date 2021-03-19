from discord.ext import commands
import discord, jellyfish


class messageControlCog(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id == 794630173743906836:
			embed = await self.createEmbed(message, 'Send')
			embed.set_footer(text = 'пасасывай~')
			await message.channel.send(embed = embed)

	@commands.Cog.listener()
	async def on_raw_message_delete(self, payload: discord.RawReactionActionEvent):
		if payload.cached_message.author.bot is False and payload.cached_message.author.id != 794630173743906836:
			embed = await self.createEmbed(payload.cached_message, 'Delete')
			await payload.cached_message.channel.send(embed = embed)

	@commands.Cog.listener()
	async def on_raw_message_edit(self, payload: discord.RawReactionActionEvent):
		if payload.cached_message.author.bot is False and payload.cached_message.author.id != 794630173743906836:
			cached_message = payload.cached_message.content
			data = payload.data['content']
			text = "edit '{0}' to '{1}'".format(cached_message, data)
			k = jellyfish.jaro_similarity(cached_message, data)
			dataL = len(data)
			cachL = len(cached_message)
			if k <= 0.45 or dataL*5 <= cachL:
				embed = await self.createEmbed(payload.cached_message, 'Edit')
				embed.description = text
				await payload.cached_message.channel.send(embed = embed)

	async def createEmbed(self, message, name):
		embed=discord.Embed(title=f'{name} message:', description = message.content, color=0xff00f6)
		embed.set_author(name = message.author, icon_url = message.author.avatar_url)
		if message.attachments != []:
			filename = message.attachments[0].filename
			if filename.lower().endswith(('.jpeg', '.jpg', '.png', 'gif')):
				embed.set_image(url = message.attachments[0].proxy_url)
			else:
				embed.add_field(name = 'file:', value = f'link: {message.attachments[0].proxy_url}')
		return embed

	@commands.command(name = 'del')
	async def messageDelete(self, ctx, id):
		if ctx.message.author.id == 305715782732480512:
			mess = await ctx.fetch_message(id)
			await mess.delete()


def setup(client):
	client.add_cog(messageControlCog(client))
