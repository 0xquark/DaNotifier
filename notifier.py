
import discord

client = discord.Client()

notify_command = "!notify"

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")

@client.event
async def on_message(message):
    
    words = message.content.split(" ")

    
    if words[0] == notify_command and message.author.permissions_in(message.channel).manage_messages:
        # Get the word to notify on and the user to notify
        notify_word = words[1]
        notify_user = message.mentions[0]

        
        @client.event
        async def on_message(message):
            if notify_word in message.content:
                await notify_user.send(f"The word '{notify_word}' was said in {message.channel.name}")


client.run("your-bot-token-here")
