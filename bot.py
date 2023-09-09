import datetime
import os
from dotenv import load_dotenv
import discord

load_dotenv()

TOKEN = os.getenv('TOKEN')
USER_ID = int(os.getenv('USER_ID'))
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

def get_formatted_time():
    time = datetime.datetime.now()
    return time.strftime('%H:%M %m-%d-%Y')

class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_voice_state_update(self, member, before, after):
        if member.id is not USER_ID: return

        message = None
        time_formatted = get_formatted_time()

        # Check if action needed (user left/joined voice chat)
        if before.channel is None and after.channel is not None:
            message = f"joined {time_formatted}"
        elif before.channel is not None and after.channel is None:
            message = f"left {time_formatted}"

        # no status change
        if message is None: return

        # Send status message
        await self.get_channel(CHANNEL_ID).send(message)

intents = discord.Intents.default()

client = BotClient(intents=intents)
client.run(TOKEN)