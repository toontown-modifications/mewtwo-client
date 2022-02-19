from pypresence import Presence
from direct.directnotify.DirectNotifyGlobal import directNotify
import time

class ToontownDiscordPresence:
    notify = directNotify.newCategory('ToontownDiscordPresence')
    notify.setInfo(True)

    def __init__(self):
        self.clientId = config.GetString('discord-client-id')

        self.rpcClient = None

        try:
            self.initialize()
            base.haveDiscordOpen = True
        except:
            # Discord is not running.
            self.notify.warning('Discord is not running.')
            base.haveDiscordOpen = False

    def initialize(self):
        self.rpcClient = Presence(self.clientId)
        self.rpcClient.connect()

        # Send our initial data.
        initialData = {
            'start': time.time(),
            'large_image': 'sunrise_games'
        }

        self.updatePresence(initialData)

    def updatePresence(self, data):
        buttons = [
            {
                'label': 'Website', 'url': 'https://sunrise.games'
            },
            {
                'label': 'Discord', 'url': 'https://discord.gg/8tx4RzRMcm'
            }
        ]

        # Send the update to the RPC client.
        self.notify.debug(f'Updating RPC with data: {data}')
        self.rpcClient.update(**data, buttons = buttons)