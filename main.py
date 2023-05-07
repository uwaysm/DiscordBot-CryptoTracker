import discord
import requests
import aiohttp
import asyncio
from pycoingecko import CoinGeckoAPI
from dotenv import load_dotenv
import os

client = discord.Client(intents=discord.Intents.default())
cg = CoinGeckoAPI()
load_dotenv()

# BOT_TOKEN = os.getenv("BOT_TOKEN")
## when storing bot_token locally in .env

BOT_TOKEN = os.environ['BOT_TOKEN']
## when storing bot token in heroku
print(BOT_TOKEN)
def fetch_crypto_price(crypto_id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        crypto_price = data[crypto_id]['usd']
        return crypto_price
    else:
        print(f"Error: {response.status_code}")
        return None

async def fetch_crypto_image_url(crypto_id):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                image_url = data['image']['large']
                return image_url
            else:
                print(f"Error: {response.status}")
                return None

async def update_bot_avatar(crypto_id):
    image_url = await fetch_crypto_image_url(crypto_id)
    if image_url:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                if response.status == 200:
                    image_data = await response.read()
                    await client.user.edit(avatar=image_data)
                else:
                    print(f"Error: {response.status}")

async def update_bot_nickname(crypto_id):
    while True:
        crypto_price = fetch_crypto_price(crypto_id)
        if crypto_price:
            nickname = f"${crypto_price}"
            for guild in client.guilds:
                await guild.me.edit(nick=nickname)
        await asyncio.sleep(1 * 60)  # Wait for 1 minute

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    crypto_id = 'alpharushai'  # Change 'cosmos' to any other crypto ID to fetch its price and image
    await update_bot_avatar(crypto_id)  # Update bot avatar only when the script is run
    await update_bot_nickname(crypto_id)

client.run(BOT_TOKEN)

