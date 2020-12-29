from .options import Option
from . import manager as root


class Command:
    """
    This class represents a command who can be send to discord
    if id is not None, it means that this class represents a command who is on discord
    """
    def __init__(self, name, description, client=None, id=None, guild_id=None):
        self.name = name
        self._client = client
        self.description = description
        self.id = id
        self.guild_id = guild_id
        self.options = []


    def add_option(self, option):
        """
        option: Option object
        extend the command with a new option
        """
        self.options += [option]


    def to_dict(self):
        """
        used by the libary, this function transform the class to a dict
        """
        dico = {
            "name": self.name,
            "description": self.description,
            "options": []
        }
        for option in self.options:
            if option._returned:
                optn = {
                    "name": option.name,
                    "description": None,
                    "type": 3,
                    "required": False
                }
            else:
                optn = {
                    "name": option.name,
                    "description": option.description,
                    "type": option.type,
                    "required": option.required,
                    "choices": option.choices
                }
            dico["options"] += [optn]

        return dico


    def delete(self):
        """
        remove the command from discord
        do nothing if the command has no id
        """
        if self.id is not None:
            manager = root.Manager(self._client)
            if self.guild_id is None:
                manager.delete_global_command(self.id)
            else:
                manager.delete_guild_command(self.guild_id, self.id)


    def __str__(self):
        option_str = ""
        for option in self.options:
            option_str += str(option) + ", "
        return '<Command id='+str(self.id)+', name="'+self.name+'", description=\"'+self.description+'", options=['+option_str[:-2]+"]>"



class ReturnedCommand:
    """
    this class is a simplified version of command, used when on_interaction event is call
    """
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.options = []


    def add_option(self, option):
        self.options += [option]


    def __str__(self):
        str_optn = ""
        for optn in self.options:
            str_optn += str(optn) + " "
        return (self.name + " " + str_optn).strip()


def _load_command(dico, client, guild_id=None):
    command = Command(name=dico["name"], description=dico["description"], client=client, id=int(dico["id"]), guild_id=guild_id)
    if "options" in dico:
        for optn in dico["options"]:
            if "required" not in optn:
                optn["required"] = False
            option = Option(name=optn["name"], description=optn["description"], type=optn["type"], required=optn["required"])
            if "choices" in optn:
                for choice in optn["choices"]:
                    option.add_choice(name=choice["name"], value=choice["value"])
            command.add_option(option)
    return command
