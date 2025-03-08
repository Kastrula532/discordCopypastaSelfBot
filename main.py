import discord
from discord.ext import commands
from functions import *

import random
import json
import asyncio
import os
import sys

os.system('cls')

words_path = 'words.txt'

with open('config.json', 'r') as file:
    config = json.load(file)

prefix = config['prefix']
token = config['token']
if not token:
    print("[!] Token is empty")
    sys.exit(1)


bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print('-' * 55)
    print('[+] Bot started!')
    print(f'[+] Username: {bot.user.name}')
    print(f'[+] UserID: {bot.user.id}')
    print('[+] Bot is online!')
    print('-' * 55)

# if you send this command from bot account(in any chat), then all possible messages from all
# servers where the bot is a member will be collected and saved to words.txt. there is a possibility
# that it might not work properly as expected in some cases
@bot.command(name='collect_messages')
async def collect_messages(ctx):
    await ctx.message.delete()

    existing_words = read_words_from_file(words_path)
    words = existing_words.copy()

    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel and channel.permissions_for(channel.guild.me).read_messages:
                async for message in channel.history(limit=2999):
                    if not message.author.bot and message.type == discord.MessageType.default:
                        words.extend(message.content.split())

    write_words_to_file("words.txt", words)
    print("[+] Messages collected")

# this function listens for messages in any text channel the bot has access to
# when a message is detected, the bot replies with a weird generated copypasta 
# based on words stored in words.txt
@bot.event
async def on_message(message):

    await bot.process_commands(message)

    if message.author.id == bot.user.id:
        return
    
    print(f"[+] Message detected in {message.guild.name} from {message.author.name}")

    async with message.channel.typing():
        words = read_words_from_file(words_path)

        new_words = message.content.split()
        words.extend(new_words)
        write_words_to_file(words_path, words)
        
        random_length = random.randint(10, 200)
        random_stateSize = random.randint(1, 3)
        random_delay = random.randint(5, 30)

        markov_chain = build_markov_chain(words, random_stateSize)
        generated_text = generate_text(markov_chain, random_stateSize, random_length)

        await asyncio.sleep(random_delay)

    await message.reply(generated_text)
    words_cleanup(words_path)
    print(f"[+] Message was sent to {message.author.name}")

bot.run(token)