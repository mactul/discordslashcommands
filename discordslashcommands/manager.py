import requests
import logging
import discord
import json
from .interactions import Interaction
from .commands import _load_command


class Manager:
    """
    This class need a discord.Client object to work

    It starts the interaction listener
    It allows creation, edition, deletion and fetching of slash commands
    """
    def __init__(self, client):
        self._client = client
        self.token = client.http.token
        self.client_id = str(client.user.id)

        self.headers = {"Authorization": "Bot "+self.token}

        self.url = "https://discord.com/api/v8/applications/"+self.client_id+"/commands"

        client._connection.parsers["INTERACTION_CREATE"] = self._function_runner  # create a new event

    def get_all_global_commands(self):
        """
        return all global slash commands of your application
        """
        r = requests.get(self.url, headers=self.headers)
        cmd_list = json.loads(r.text)
        output = []
        for dico in cmd_list:
            output += [_load_command(dico, self._client)]
        return output


    def get_global_command(self, id: int):
        """
        return a specific global slash command of your application, identified by id
        you can also use discord.utils.get to idenfiate by name
        """
        return discord.utils.get(self.get_all_global_commands(), id=id)


    def delete_global_command(self, id):
        """
        id: int or str
        delete a specific global slash command of your application, identified by id
        """
        requests.delete(self.url+"/"+str(id), headers=self.headers)


    def edit_global_command(self, id, cmd):
        """
        id: int or string
        cmd: Command object
        put a new global command on your application
        need 1h to be efficient
        """
        dico = cmd.to_dict()
        requests.patch(self.url+"/"+str(id), headers=self.headers, json=dico)


    def add_global_command(self, cmd):
        """
        cmd: Command object
        put a new global command on your application
        need 1h to be efficient
        """
        dico = cmd.to_dict()
        requests.post(self.url, headers=self.headers, json=dico)


    def get_all_guild_commands(self, guild_id):
        """
        guild_id: int or string
        return all slash commands of a specific guild, identified by id
        """
        url = "https://discord.com/api/v8/applications/"+self.client_id+"/guilds/"+str(guild_id)+"/commands"

        r = requests.get(url, headers=self.headers)
        cmd_list = json.loads(r.text)
        output = []
        for dico in cmd_list:
            output += [_load_command(dico, self._client, guild_id)]
        return output


    def get_guild_command(self, guild_id, id: int):
        """
        guild_id: int or string
        return a specific slash command of a specific guild
        """
        return discord.utils.get(self.get_guild_commands(guild_id), id=id)


    def delete_guild_command(self, guild_id, id):
        """
        guild_id: int or string
        id: int or string
        delete a specific slash command of a specific guild
        """
        url = "https://discord.com/api/v8/applications/"+self.client_id+"/guilds/"+str(guild_id)+"/commands"

        requests.delete(url+"/"+str(id), headers=self.headers)


    def edit_guild_command(self, guild_id, id, cmd):
        """
        guild_id: int or string
        id: int or string
        cmd: Command object
        put a new command on guild
        """
        url = "https://discord.com/api/v8/applications/"+self.client_id+"/guilds/"+str(guild_id)+"/commands/"+str(id)

        dico = cmd.to_dict()
        requests.patch(url, headers=self.headers, json=dico)


    def add_guild_command(self, guild_id, cmd):
        """
        guild_id: int or string
        cmd: Command object
        put a new command on guild
        """
        url = "https://discord.com/api/v8/applications/"+self.client_id+"/guilds/"+str(guild_id)+"/commands"

        dico = cmd.to_dict()
        requests.post(url, headers=self.headers, json=dico)


    def _function_runner(self, data):
        guild = self._client.get_guild(int(data["guild_id"]))
        member = discord.Member(guild=guild, data=data["member"], state=guild._state)
        interaction = Interaction(client=self._client, version=data["version"], type=data["type"], token=data["token"], id=data["id"], guild=guild, channel_id=data["channel_id"], data=data["data"], member_data=data["member"])
        try:
            self._client.loop.create_task(self._client.on_interaction(member, interaction))
        except:
            pass
