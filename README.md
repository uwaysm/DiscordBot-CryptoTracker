# Crypto Price Tracker Bot

This bot will automatically track the price of any cryptocurrency on coingecko through the discord bot's nickname. The nickname will update every 1 minute and reflect the price of the cryptocurrency being tracked.

### What are the prerequisites for this guide?

You must have an account for Discord [[Link](https://discordapp.com/developers/applications/)], GitHub [[Link](https://github.com/join)]

### How do I create a bot and get a bot token?

- Create an application in the developer portal by clicking [here](https://discordapp.com/developers/applications/)
- Open up your new application and click 'Add Bot' under the Bot settings to create your bot.
- After creating the bot, click the 'Copy' button under the title Token. Take note of your token as you will need it later.

### How to choose the token to track?

- Simply change the 'crypto_id' to the crypto id of the token you want to track.
- Make sure to input your discord bot token on line 61: "YOUR_BOT_TOKEN"

## Deployment

1. Clone this repository to your local machine:

```
git clone https://github.com/uwaysm/DiscordBot-CryptoTracker.git
```

Replace `yourusername` and `your-repo-name` with the appropriate information for your project.

2. Change to the project directory:

```
cd discordbot-cryptotracker
```

3. Log in to Heroku and create a new app:

4. Set the `BOT_TOKEN` config var on Heroku:

```
Replace `BOT_TOKEN` with your actual Discord bot token
```

5. Deploy your bot to Heroku:

```
git push heroku main
```

6. Scale the worker dyno to start running your bot:

```
heroku ps:scale worker=1 -a your-app-name
```

7. Your bot should now be running on Heroku and appear online in your Discord server.

## Customization

To change the cryptocurrency that the bot tracks, update the `crypto_id` variable in the `on_ready()` event in the bot script. You can find the appropriate ID on the [CoinGecko API](https://www.coingecko.com/api/documentation/v3) website.

## Support

If you encounter any issues, please check the Heroku logs for errors and ensure that your bot token and permissions are set correctly. For further assistance, you can reach out through the GitHub Issues section of this repository.
