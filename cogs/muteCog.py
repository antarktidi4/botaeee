from discord.ext import commands
import discord


class muteCog(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command()
	async def mute(self, ctx, member: discord.Member):
		Vrole = discord.utils.get(member.guild.roles, name = "Власть")
		Prole = discord.utils.get(member.guild.roles, name = "парламентъ")
		if Vrole in ctx.message.author.roles or Prole in ctx.message.author.roles:
			role = discord.utils.get(member.guild.roles, name = "muted")
			if role not in member.roles:
				await member.add_roles(discord.utils.get(member.guild.roles, name="muted"))
				embed = discord.Embed(title="User Muted!", description=f"**{member}** was muted by **{ctx.message.author}**!", color=0xff00f6)
			else:
				embed = discord.Embed(title="User Is Ulready Muted!", description="You can't mute this member, he's already muted.", color=0xff00f6)
		await ctx.send(embed = embed)

	@commands.command()
	async def unmute(self, ctx, member: discord.Member):
		Vrole = discord.utils.get(member.guild.roles, name = "Власть")
		Prole = discord.utils.get(member.guild.roles, name = "парламентъ")
		if Vrole in ctx.message.author.roles or Prole in ctx.message.author.roles:
			role = discord.utils.get(member.guild.roles, name = "muted")
			if role not in member.roles:
				await member.remove_roles(discord.utils.get(member.guild.roles, name="muted"))
				embed = discord.Embed(title="User Unmuted!", description = f"**{member}** was unmuted by **{ctx.message.author}**!", color=0xff00f6)
			else:
				embed = discord.Embed(title = "User Not Muted!", description = "You can't unmute this member, he's not muted.", color=0xff00f6)
		await ctx.send(embed = embed)


def setup(client):
	client.add_cog(muteCog(client))
