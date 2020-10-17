from urllib.request import urlopen
import logging

class Invit_member:
    def __init__(self, guild_id, member_id):
        """
        guild_id: int or str
        member_id: int or str
        a class who represent invitations informations about an user
        """
        code = str(urlopen("https://eagle-bot.ml/eagleapi/get_invites.php?guild_id="+str(guild_id)+"&member_id="+str(member_id)).read())[2:-1]

        self.nb_invites = None
        self.invited_by = None

        if code == "none":
            logging.warning(" guild or member_id does not exist in eagle files\nif Eagle bot is not in your guild, please invit him with this link https://discord.com/oauth2/authorize?client_id=747855823769829508&permissions=8&scope=bot")
        elif code == "unregistered":
            logging.warning(" your guild is not registered to use invit api service.\nIf you have buy invit api service on https://eagle-bot.ml/eagleapi/, please turn it on for this guild")
        else:
            code = code.split(',')
            self.nb_invites = code[0]
            self.invited_by = code[1]

    def get_nb_invites(self):
        """
        returns the number of invites an user have
        """
        return self.nb_invites

    def get_inviter_id(self):
        """
        returns the id of the user who invite the member
        """
        return self.invited_by