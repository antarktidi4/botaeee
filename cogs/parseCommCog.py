from discord.ext import commands
import discord, requests
from bs4 import BeautifulSoup as BS
from random import randint
from pybooru import Danbooru


class parseCommands(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command('anec')
	async def anec(self, ctx):
		r = requests.get('https://4tob.ru/anekdots/tag/short/page' + str(randint(1, 27)))
		html = BS(r.content, 'html.parser')
		text = html.select('.text')
		await ctx.send(text[randint(0, 29)].text)

	@commands.command('meme')
	async def meme(self, ctx):
		r = requests.get('https://meme-api.herokuapp.com/gimme').json()
		embed = discord.Embed(title="Random Meme!", description=f"link: {r['postLink']}\ntitle: {r['title']}", color=0xff00f6)
		embed.set_image(url = r['url'])
		await ctx.send(embed = embed)

	@commands.command('rhentai')
	async def rhentai(self, ctx):
		r = requests.get('https://meme-api.herokuapp.com/gimme/hentai').json()
		embed = discord.Embed(title="Random hentai!", description=f"link: {r['postLink']}\ntitle: {r['title']}", color=0xff00f6)
		embed.set_image(url = r['url'])
		await ctx.send(embed = embed)

	@commands.command('dhentai')
	async def dhentai(self, ctx, tags):
		dClient = Danbooru('danbooru')
		s = dClient.post_list(limit=1, tags=tags, random = True)
		embed = discord.Embed(title="Danbooru hentai!", description=f"link: [source]({s[0]['source']})", color=0xff00f6)
		embed.set_image(url = s[0]['file_url'])
		embed.set_footer(text = s[0]['tag_string'])
		await ctx.send(embed = embed)


def setup(client):
	client.add_cog(parseCommands(client))
