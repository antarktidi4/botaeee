from bs4 import BeautifulSoup as BS
from discord.ext import commands
import discord, requests, json
from pybooru import Danbooru
from random import choice


class parseCommands(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command('anec')
	async def anec(self, ctx):
		rawcontent = requests.get('http://rzhunemogu.ru/RandJSON.aspx?CType=1').text
		await ctx.send(json.loads(rawcontent, strict=False)['content'])

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
		embed = discord.Embed(title="Danbooru hentai!", color=0xff00f6)
		try:
			embed.set_image(url = s[0]['file_url'])
			embed.set_footer(text = s[0]['tag_string'])
			await ctx.send(embed = embed)
		except:
			await ctx.send('попробуй ещё раз')

	@commands.command(name = 'avatar')
	async def avatar(self, ctx, member: discord.Member = None):
		user = ctx.author if member is None else member
		embed = discord.Embed(title = user.name, color=0xff00f6)
		embed.set_image(url = user.avatar_url)
		await ctx.send(embed = embed)

	@commands.command(pass_context = True, aliases = [ 'et', 'eTranslator'])
	async def eblanTranslator(self, ctx):
		eng = list("qwertyuiop[]asdfghjkl;'zxcvbnm,.")
		ru = list("йцукенгшщзхъфывапролджэячсмитьбю")
		engToRu = dict(zip(eng, ru))
		ruToEng = dict(zip(ru, eng))
		message = await ctx.message.channel.fetch_message(ctx.message.reference.message_id)

		for chr in message.content.lower():
			if chr in engToRu:
				language = engToRu
				break
			elif chr in ruToEng:
				language = ruToEng
				break

		lanName = [k for k, v in locals().items() if v is language][0] # чё тут вообще за пиздец, лол
		output = ''

		for chr in message.content.lower():
			try:
				output += eval(f'{language}[chr]') if chr in eng or chr in ru else chr
			except BaseException as e:
				await ctx.send(f'error: {e}')
				return 0

		embed = discord.Embed(title = f'{lanName} message:', description = output, color=0xff00f6)
		embed.set_author(name = message.author, icon_url = message.author.avatar_url)
		await ctx.send(embed = embed)

	@commands.command(name = 'token')
	async def token(self, ctx):
		token = requests.get('https://some-random-api.ml/bottoken').json()['token']
		embed = discord.Embed(title = 'bot token!', description=f"{token}", color=0xff00f6)
		await ctx.send(embed = embed)

	@commands.command(name = 'img')
	async def img(self, ctx, arg = None):
		search = arg if arg is not None else 'cursed image'
		link = f'https://results.dogpile.com/serp?qc=images&q={search}'.replace(' ', '+')
		r = requests.get(link, headers={'User-agent': 'Mozilla/4.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4103.97 Safari/537.36', 'Accept': 'text/html'}).text
		embed = discord.Embed(title = f'img: {search}', color=0xff00f6)
		try:
			embed.set_image(url = choice(BS(r, 'lxml').find_all('img'))['src'])
			await ctx.send(embed = embed)
		except:
			await ctx.send('попробуй ещё раз')


def setup(client):
	client.add_cog(parseCommands(client))
