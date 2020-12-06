from discord.ext import commands
import discord



class PolitReaction(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
		if payload.message_id == 778357469344694332:
			guild = self.client.get_guild(payload.member.guild.id)
			if payload.emoji.name == 'left':
				role = discord.utils.get(payload.member.guild.roles, name="правые")
				if role not in payload.member.roles:
					await payload.member.add_roles(discord.utils.get(guild.roles, name="левые"))
			elif payload.emoji.name == 'right':
				role = discord.utils.get(payload.member.guild.roles, name="левые")
				if role not in payload.member.roles:
					await payload.member.add_roles(discord.utils.get(guild.roles, name="правые"))


	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
		if payload.message_id == 778357469344694332:
			guild = self.client.get_guild(payload.guild_id)
			member = await guild.fetch_member(payload.user_id)
			if payload.emoji.name == 'left':
				await member.remove_roles(discord.utils.get(guild.roles, name="левые"))
			elif payload.emoji.name == 'right':
				role = discord.utils.get(member.guild.roles, name="правые")
				if role in member.roles:
					await member.remove_roles(discord.utils.get(guild.roles, name="правые"))



def setup(client):
	client.add_cog(PolitReaction(client))
