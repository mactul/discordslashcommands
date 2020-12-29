r"""
Discordslashcommand is an extension library to discord.py
It allows you to easily manipulate discord slash (/) commands.
You can create commands that will follow a particular patern and that will be easy to use on the discord application.
"""

from .manager import Manager
from .commands import Command
from .options import Option
from .interactions import Interaction

__version__ = '1.0.0'
__all__ = [
    'Manager'
    'Command'
    'Option'
    'Interaction'
]

__author__ = 'Macéo Tuloup'


# Options types
SUB_COMMAND       = 1
SUB_COMMAND_GROUP = 2
STRING            = 3
INTEGER           = 4
BOOLEAN           = 5
USER              = 6
CHANNEL           = 7
ROLE              = 8
