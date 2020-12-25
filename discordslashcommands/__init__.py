r"""
Discordslashcommand is an extension library to discord.py
It allows you to easily manipulate discord slash (/) commands.
You can create commands that will follow a particular patern and that will be easy to use on the discord application.
"""

__version__ = '1.0.0'
__all__ = [
    'Manager'
    'Command'
    'Option'
    'Interaction'
]

__author__ = 'Macéo Tuloup'

from .manager import Manager
from .commands import Command
from .options import Option
from .interactions import Interaction


STRING  = 3
INTEGER = 4
BOOLEAN = 5