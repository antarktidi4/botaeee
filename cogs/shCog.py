import discord, random, requests, os, shutil
from PIL import Image, ImageEnhance
from discord.ext import commands


class shakalCog(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name = 'sh')
	async def shakal(self, ctx, speed = None):
		l = 100 if speed is None else speed
		img = []
		try:
			async for x in discord.abc.Messageable.history(ctx.message.channel, limit = l):
				if x.attachments != [] and x.attachments[0].filename.endswith(('png', 'jpg', 'jpeg')) is True:
					img.append(x.attachments)
		except:
			await ctx.send('error')
			return
		if img != []:
			img = random.choice(img)
			r = requests.get(img[0].url, stream = True)


			if r.status_code == 200:
				r.raw.decode_content = True
			with open(img[0].filename, 'wb') as f:
				shutil.copyfileobj(r.raw, f)


			imgPIL = Image.open(img[0].filename)

			Con = ImageEnhance.Contrast(imgPIL)
			ConL = Con.enhance(2)
			Sha = ImageEnhance.Sharpness(ConL)
			ShaL = Sha.enhance(200)

			ShaL.save(img[0].filename, quality=1)


			file = discord.File(img[0].filename, filename = img[0].filename)
			embed = discord.Embed(title='шакал', color=0xff00f6)
			embed.set_image(url = f'attachment://{img[0].filename}')
			await ctx.send(embed = embed, file = file)

			os.remove(img[0].filename)
		else:
			await ctx.send('в 100 сообщениях не найдено изображение, пропишите $sh %int%')


def setup(client):
	client.add_cog(shakalCog(client))
