# discordslashcommands

Discordslashcommand is an extension library to discord.py\
It allows you to easily manipulate discord slash (/) commands.\
You can create commands that will follow a particular patern and that will be easy to use on the discord application.

## installation

This package is on pypi.\
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



### Informations about slash commands

slash commands are restricted by discord.\
There are many things you need to know to be able to use them.

You must have access to your developer portal.\
(here: https://discord.com/developers/applications/)

When prompted on a server, your bot must have permission to use slash commands.\
When you create the invitation link in the Oauth2 tab, you must check the "applications.commands" box and the "applications.commands.update" box in addition to the "bot" box.

#### Limitations

Copy and past of the full documentation of discord api.

An app can have up to 50 top-level global commands (50 commands with unique names)\
An app can have up to an additional 50 guild commands per guild\
An app can have up to 10 subcommand groups on a top-level command\
An app can have up to 10 subcommands within a subcommand group\
choices can have up to 10 values per option\
commands can have up to 10 options per command\



### Manager

The main class of this library is the Manager class,\
you have to call it at the bot's start.\
You can call it again after if you need it.

The minimal code is like that:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client) # this is the code of discordslashcommands library


client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```


#### Create a global slash command

To create a slash command, we need to create this command in a local object and put it on discord.\
The local object is call Command()

a simple command without arguments looks like this:
```py
command = dsc.Command(name="help", description="display help")
```
To put in on discord, we have to use the manager
```py
manager = dsc.Manager(client)
command = dsc.Command(name="help", description="display help")
manager.add_global_command(command)
```

Here is the full code:
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


#### Create a guild slash command

To create the command localy, it's the same way that for global commands.\
The change is only with the manager.\
The name of the put function is different and it takes one more argument, the id of the guild.\

```py
manager = dsc.Manager(client)
command = dsc.Command(name="help", description="display help")
manager.add_guild_command(REPLACE_WITH_THE_ID_OF_YOUR_GUILD, command)
```

The full code:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client) # create the manager
    command = dsc.Command(name="help", description="display help") # create the command
    manager.add_guild_command(REPLACE_WITH_THE_ID_OF_YOUR_GUILD, command) # put it on discord

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```


#### Command object

For all next steps, we need to know better the Command class.\
We have seen a simple command like that:
```py
command = dsc.Command(name="help", description="display help")
```
But we can imagine that the help command can takes arguments, to print parts of help for example.\
We will add an argument, name category, it represents the part of the help that we want print.\
This argument has several predefined values.\
3 for example, an help for premium, moderation and music

We need to add an argument (an option), with a name, a description and predefined values

To do that, we need a new object, call Option.

The type, which is an integer, can take several values between 1 and 8.\
To help you, discordslashcommands has listed these types in constants:
```py
dsc.SUB_COMMAND
dsc.SUB_COMMAND_GROUP
dsc.STRING
dsc.INTEGER
ds
```
```py
command = dsc.Command(name="help", description="display help") # create the main object

option = Option(name="category", description="the part of the help you want to display", type=dsc.STRING, required=False)

option.add_choice(name="premium part", value="premium")
option.add_choice(name="moderation part", value="moderation") # if you don't understand the difference between name and value, put the same string into
option.add_choice(name="music part", value="music")

command.add_option(option) # add the new option created in the command
```

To use this version of the help command, this is the full code:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client) # create the manager
    
    command = dsc.Command(name="help", description="display help") # create the commandcommand = dsc.Command(name="help", description="display help") # create the main object
    option = Option(name="category", description="the part of the help you want to display", type=dsc.STRING, required=False)
    option.add_choice(name="premium part", value="premium")
    option.add_choice(name="moderation part", value="moderation") # if you don't understand the difference between name and value, put the same string into
    option.add_choice(name="music part", value="music")
    command.add_option(option) # add the new option created in the command
    
    manager.add_guild_command(REPLACE_WITH_THE_ID_OF_YOUR_GUILD, command) # put it on discord

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```


#### Get all global slash commands

Maybe, you need having a full list of the commands of your application.\
To get it, you can use the manager with the `get_all_global_commands()` function.\
This function takes no arguments and returns a list of Command objects.

```py
commands = manager.get_all_global_commands()
```

They Command objects returned are like this:
```
Command
    .name: name of the command
    .description: description of the command
    .id: id of the command, to make actions on it
    .options: a list of Option objects
        list
            .name: name of the option
            .description: description of the option
            .type: type of the option (dsc.STRING, dsc.INTEGER, etc...)
            .required: boolean represents if the option is required
            .choices: a list of choices
                list
                    dictionnary
                        key "name": name of the choice
                        key "value": value of the choice

    .add_option(Option): function detailed above

    .delete(): delete the Command directly from discord, without manager object

```

A complete example:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client)

    commands = manager.get_all_global_commands()

    for command in commands: # loop on all commands
        print(command.name) # print the name of the current command

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```


#### Get all guild slash commands

Maybe, you need having a full list of the commands of your application in a sepcific guild.\
To get it, you can use the manager with the `get_all_guild_commands(guild_id)` function.\
This function takes the guild id in arguments and returns a list of Command objects.

```py
commands = manager.get_all_guild_commands(REPLACE_WITH_THE_ID_OF_YOUR_GUILD)
```

They Command objects returned are like this:
```
Command
    .name: name of the command
    .description: description of the command
    .id: id of the command, to make actions on it
    .guild_id: id of the guild requested
    .options: a list of Option objects
        list
            .name: name of the option
            .description: description of the option
            .type: type of the option (dsc.STRING, dsc.INTEGER, etc...)
            .required: boolean represents if the option is required
            .choices: a list of choices
                list
                    dictionnary
                        key "name": name of the choice
                        key "value": value of the choice

    .add_option(Option): function detailed above

    .delete(): delete the Command directly from discord, without manager object

```

A complete example:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client)

    commands = manager.get_all_guild_commands(REPLACE_WITH_THE_ID_OF_YOUR_GUILD)

    for command in commands: # loop on all commands
        print(command.name) # print the name of the current command

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```


#### Get a specific global slash commands

If you know the id of your command, you can get it directly with the `get_global_command(id)` function.\
You can also get all global commands and use `discord.utils.get` function to get a specific command by name, id or other.

```py
commands = manager.get_global_command(REPLACE_WITH_THE_ID_OF_YOUR_COMMAND)
```

The Command objects returned are the same as in list of commands in `get_all_global_commands()` function

A complete example:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client)

    command = manager.get_global_command(REPLACE_WITH_THE_ID_OF_YOUR_COMMAND)

    print(command.name) # print the name of the command

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```


#### Get a specific guild slash commands

If you know the id of your command, you can get it directly with the `get_guild_command(guild_id, id)` function.\
You can also get all guild commands and use `discord.utils.get` function to get a specific command by name, id or other.

```py
commands = manager.get_guild_command(REPLACE_WITH_THE_ID_OF_YOUR_GUILD, REPLACE_WITH_THE_ID_OF_YOUR_COMMAND)
```

The Command objects returned are the same as in list of commands in `get_all_guild_commands(guild_id)` function

A complete example:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client)

    command = manager.get_guild_command(REPLACE_WITH_THE_ID_OF_YOUR_GUILD, REPLACE_WITH_THE_ID_OF_YOUR_COMMAND)

    print(command.name) # print the name of the command

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```


#### Delete a global slash command

If you have get your command from the manager, you can delete your command easly like this:
```py
command.delete()
```

A complet example:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client)

    command = manager.get_global_command(REPLACE_WITH_THE_ID_OF_YOUR_COMMAND)

    command.delete()

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```

if you have just the id of your command, it is not necessary to get the whole command.\
You can delete a global command by id, like this:
```py
manager.delete_global_command(REPLACE_WITH_THE_ID_OF_YOUR_COMMAND)
```

A complet example:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client)

    manager.delete_global_command(REPLACE_WITH_THE_ID_OF_YOUR_COMMAND)

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```


#### Delete a guild slash command

If you have get your command from the manager, you can delete your command easly like this:
```py
command.delete()
```

A complet example:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client)

    command = manager.get_guild_command(REPLACE_WITH_THE_ID_OF_YOUR_GUILD, REPLACE_WITH_THE_ID_OF_YOUR_COMMAND)

    command.delete()

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```

if you have just the id of your command, it is not necessary to get the whole command.\
You can delete a guild command by id, like this:
```py
manager.delete_guild_command(REPLACE_WITH_THE_ID_OF_YOUR_GUILD, REPLACE_WITH_THE_ID_OF_YOUR_COMMAND)
```

A complet example:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client)

    manager.delete_guild_command(REPLACE_WITH_THE_ID_OF_YOUR_GUILD, REPLACE_WITH_THE_ID_OF_YOUR_COMMAND)

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```


#### Edit a global slash command

To edit a command, you need is id and a command object, exactly the same as for adding a command.\
This is the edit function:
```py
manager.edit_global_command(REPLACE_WITH_THE_ID_OF_YOUR_COMMAND, command)
```

A complet example:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client)
    command = dsc.Command(name="help", description="display help") # create the command
    manager.edit_global_command(REPLACE_WITH_THE_ID_OF_YOUR_COMMAND, command) # replace existent command by new command

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```

#### Edit a guild slash command

To edit a command, you need is id and a command object, exactly the same as for adding a command.\
This is the edit function:
```py
manager.edit_guild_command(REPLACE_WITH_THE_ID_OF_YOUR_GUILD, REPLACE_WITH_THE_ID_OF_YOUR_COMMAND, command)
```

A complet example:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()

@client.event
async def on_ready():
    manager = dsc.Manager(client)
    command = dsc.Command(name="help", description="display help") # create the command
    manager.edit_guild_command(REPLACE_WITH_THE_ID_OF_YOUR_GUILD, REPLACE_WITH_THE_ID_OF_YOUR_COMMAND, command) # replace existent command by new command

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```


### Interactions

Interactions are a very important part of discordslashcommands.\
this is what makes it possible to know when someone is using a command.

When an user click on a command and if you have create a Manager class at the start of the bot, a new event is call.\
This event is the event `on_interaction(member, interaction)`.

this is an example:
```py
import discord
import discordslashcommands as dsc

client = discord.Client()


@client.event
async def on_interaction(member, interaction):  # this event is not in discord.py, it is add by discordslashcommands library
    await interaction.channel.send("an user just click on a command")  # reply just in the same channel as where the command was launched.  


@client.event
async def on_ready():
    manager = dsc.Manager(client)  # just to set up the library with the client

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```

member is a classic discord.Member object.\
Refer to the discord.py documentation https://discordpy.readthedocs.io/en/latest/api.html#member

interaction is a new object

#### Interaction object

Interaction object is a powerfull object who contain many informations about the interaction between the user and the command.

It's looks like:
```
Interaction
    .version: always 1, this is for the future of slash commands
    .type: type of the interaction, can be 1 or 2, 1 is a ping/pong command and 2 is a normal command
    .token: to reply to interaction with webhooks (not implemented in discordslashcommands library)
    .id: the id of the command
    .guild: the guild where the command comes from
    .channel: the channel where the command comes from
    .command: a Command object like Command object can be get
              /!\ warning /!\ this Command object as many property to None, like description
              /!\ warning /!\ options list is not a list of Option objects but a list of ReturnedOption objects
              ReturnedOption
                  .name: the name of the option
                  .value: the value of the option

    .call_on_message(prefix): a function detailed after
```


### Transform an interaction to a message and call on_message function

If you have an old bot discord that works with on_message function, you can adapt it easly to slash commands.\
You have to use the `Interaction.call_on_message(prefix)` function.\
This function will generate a fake discord.Message object, with a fake id, a fake content, etc...

The function takes the name of the command, values of options, and create a string prefixed by the prefix string argument.

for example, if I have created this command (the same as my second creation command example)
```py
command = dsc.Command(name="help", description="display help") # create the main object

option = Option(name="category", description="the part of the help you want to display", type=dsc.STRING, required=False)

option.add_choice(name="premium part", value="premium")
option.add_choice(name="moderation part", value="moderation") # if you don't understand the difference between name and value, put the same string into
option.add_choice(name="music part", value="music")

command.add_option(option) # add the new option created in the command
```

if an user click on this command and choose "premium part" option, if I have this code
```py
@client.event
async def on_interaction(member, interaction):
    interaction.call_on_message("+")
```

The string generated looks like
```
+help premium
```


A full example, with this help command
(I don't put here the creation of the command, because it only has to be done once.)
```py
import discord
import discordslashcommands as dsc

client = discord.Client()


@client.event
async def on_interaction(member, interaction):
    interaction.call_on_message("+")  # we do anything here, but we translate to a classic message


@client.event
async def on_message(message):  # this is the classic discord.py function
    msg_content = message.content.lower()

    if msg_content == "+help premium":
        await message.channel.send(message.author.mention+" here is the premium help.......")

    elif msg_content == "+help moderation":
        await message.channel.send(message.author.mention+" here is the moderation help.......")

    elif msg_content == "+help music":
        await message.channel.send(message.author.mention+" here is the music help.......")

    elif msg_content == "+help":
        await message.channel.send(message.author.mention+" here is the full help.......")





@client.event
async def on_ready():
    manager = dsc.Manager(client)  # DON'T FORGET THAT

client.run("XXXXXXXXXXXXXXXXXXXXXXXXXX")
```




