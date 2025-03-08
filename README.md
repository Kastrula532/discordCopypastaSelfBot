# What is it?
This is a selfbot, using [discord.py-self](https://github.com/dolfies/discord.py-self), created for fun. Selfbot doesn't work in private messages. I decided not to use markovify because i had some problems with it. Maybe, in a future update i'll add markovify. Anyway, the selfbot works as expected.

**Note**: Automating user accounts is against Discord's Terms of Service. This project is created for educational and entertainment purposes only. I do not encourage or endorse the use of this bot. Use it at your own risk.
# How it works?
Selfbot replies to every member with a copypasta in every server, as long as they send a message. It generates random copypastas based on words collected from server messages and stored in the `words.txt` file. When someone sends a message in any text channel where the selfbot has access, selfbot replies with a weird, randomly generated copypasta
# How to use?
**Python 3.8 or higher is required.**

First of all you need to install discord.py-self
```
**Linux/macOS**
python3 -m pip install -U discord.py-self

**Windows**
py -3 -m pip install -U discord.py-self
```
and clone this project
```
git clone https://github.com/Kastrula532/discordCopypastaSelfBot.git
```

Then you need to get user authorization token(it must be the token of selfbot account), google “how to get discord authorization token”
Paste your selfbot token in `config.json` file.

open cmd, and run main.py
```
python main.py
```

**Now, you need to collect messages for the bot to start working** 
1. Add the bot to a server where both you and the bot are present (the bot does not work in private messages). Then, simply send a lot of messages to the bot and wait for it to start replying.
2. Alternatively, add the bot to any server and send the `!collect_messages` command from the bot's account. This will make the bot collect all available messages and add them to `words.txt`

Once messages are collected, send any message to the server where the bot is, and have fun!