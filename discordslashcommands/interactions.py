from .commands import Command
from .options import ReturnedOption
import discord
from datetime import datetime, tzinfo, timedelta


class simple_utc(tzinfo):
    """
    a class used by the libary
    """
    def tzname(self, **kwargs):
        return "UTC"

    def utcoffset(self, dt):
        return timedelta(0)


class Interaction:
    """
    An abstact object represents the action of the user on discord
    Interaction.command is the main part, because it represents the command sended by the user
    """
    def __init__(self, client, version, type, token, id, guild, channel_id, data, member_data):
        self._client = client
        self._member_data = member_data
        self.version = 1
        self.type = type
        self.token = token
        self.id = int(id)
        self.guild = guild
        self.channel = client.get_channel(int(channel_id))
        self.command = Command(name=data["name"], description=None, client=client, id=int(data["id"]), guild_id=guild.id)
        if "options" in data:
            for option in data["options"]:
                self.command.add_option(ReturnedOption(name=option["name"], value=option["value"]))


    def __str__(self):
        return str(self.command)


    def call_on_message(self, prefix):
        """
        generate a fake discord.Message object and call the on_message function with him
        with this function, you can adapt your old bot who work with messages
        """
        message = {
            "reactions": [],
            "attachments": [],
            "tts": False,
            "embeds": [],
            "timestamp": str(datetime.utcnow().replace(tzinfo=simple_utc()).isoformat()),
            "mention_everyone": False,
            "id": str(self.id),
            "pinned": False,
            "edited_timestamp": None,
            "author": self._member_data["user"],
            "member": self._member_data,
            "mention_roles": [],
            "content": prefix + str(self.command),
            "channel_id": str(self.channel.id),
            "mentions": [],
            "type": 0
        }

        message = discord.Message(state=self.channel._state, channel=self.channel, data=message)
        self._client.loop.create_task(self._client.on_message(message))
