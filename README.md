# discord_slash_command

Discordslashcommand is an extension library to discord.py
It allows you to easily manipulate discord slash (/) commands.
You can create commands that will follow a particular patern and that will be easy to use on the discord application.

## installation

This package is on pypi.
You can install it via pip

In a command prompt, run this command:
```
pip3 install discordslashcommands
```
If it doesn't work, try all this commands, maybe one can work.
```
pip install discordslashcommands
py -m pip install discordslashcommands
python3 -m pip install discordslashcommands
py -m pip3 install discordslashcommands
python3 -m install discordslashcommands
py3 -m pip install discordslashcommands
py3 -m pip3 install discordslashcommands
python -m pip install discordslashcommands
python3 -m pip install discordslashcommands
python-pip install discordslashcommands
python3-pip install discordslashcommands
python-pip3 install discordslashcommands
python3-pip3 install discordslashcommands
```

## Documentation

The main class of this libary is the Manager class,
you have to call it at the bot's start.
You can call it again after if you need it.

The minimal code is like that
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client) # this is the code of discordslashcommands libary


client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```


### Create a global slash command

To create a slash command, we need to create this command in a local object and put it on discord.
The local object is call Command()

a simple command without arguments looks like this
```py
command = dsc.Command(name="help", description="display help")
```
To put in on discord, we have to use the manager
```py
manager = dsc.Manager(client)
command = dsc.Command(name="help", description="display help")
manager.add_global_command(command)
```

Here is the full code
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client) # create the manager
    command = dsc.Command(name="help", description="display help") # create the command
    manager.add_global_command(command) # put it on discord

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```


### Create a guild slash command

To create the command localy, it's the same way that for global commands.
The change is only with the manager.
The name of the put function is different and it takes one more argument, the id of the guild.

```py
manager = dsc.Manager(client)
command = dsc.Command(name="help", description="display help")
manager.add_guild_command(REPLACE_WITH_THE_ID_OF_YOUR_GUILD, command)
```

documentation is coming
