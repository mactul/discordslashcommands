import discord
import discordslashcommands as cmd


YOUR_GUILD = 687640485984206871


client = discord.Client()


# This is a new event, called by discordslashcommands
# member is a classic discord.Member object
# interaction is an object who represent the interaction
# interaction.command is the most important
@client.event
async def on_interaction(member, interaction):
    if interaction.command.name == "clear": # if the command sended is "clear"
        manager = cmd.Manager(client) # create a manager objet to get commands informations
                                      # this object need a discord.Client object to work
                                      
        if interaction.command.options[0].value == "guild": # if the first option is "guild"
            cmds = manager.get_all_guild_commands(YOUR_GUILD) # get the list of commands objects of your application in your guild
        else: # the first option is "global"
            cmds = manager.get_all_global_commands() # get the list of your global commands
        for command in cmds: # loop on commands
            command.delete() # delete the current command
    
    interaction.call_on_message(prefix="+") # transform the interaction object to a fake discord.Message object and call the on_message function with him
                                            # this feature allows compatibility with old discord bots


@client.event
async def on_message(message):
    print(message.content) # print the content of the fake message generated
    print(message.author.roles) # print roles of the member (just to see that it's normal)
    
    
    # a simple bot discord, like before slash commands
    
    
    PREFIX = "+"
    
    cmd = message.content.lower()
    
    if cmd == PREFIX + "help premium":
        await message.channel.send("here is the premium help")
        
    elif cmd == PREFIX + "help moderation":
        await message.channel.send("here is the help of moderation")
    
    
    elif cmd == PREFIX + "help":
        await message.channel.send("here is the normal help")


@client.event
async def on_ready():
    manager = cmd.Manager(client) # create a manager after the bot's start
                                  # /!\ this line is very important because it start the interaction listener /!\

    command = cmd.Command(name="help", description="display help") #create a simple command
    
    option = cmd.Option(name="category", description="different parts of the help", type=cmd.STRING, required=False) # create an option for this command
    option.add_choice(name="premium", value="premium")       # add two differents values from this option
    option.add_choice(name="moderation", value="moderation") #
    
    command.add_option(option) # add the option to the command

    manager.add_guild_command(YOUR_GUILD, command) # put the new command in your guild
    
    
    
    # make another command, but a global command this time
    command = cmd.Command(name="clear", description="delete all slash commands")
    
    option = cmd.Option(name="zone", description="delete guilds commands or global commands", type=cmd.STRING, required=True)
    option.add_choice(name="guild", value="guild")
    option.add_choice(name="global", value="global")
    
    command.add_option(option)

    manager.add_global_command(command) # with this line, a little bit different, the command is a global command for the application
                                        # global commands need 1h to appear
                                        # /!\ if you run this script 3 times for example, 3 new global commands will appear



client.run("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
