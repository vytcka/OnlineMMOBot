import discord
import sys
from Handlers.FileHandler import FileHandler
from Constants.FilePaths import FilePaths

def get_response(message: str):
    user_message = message.lower()

    if user_message == 'help':
        return "!continue - Continues bot from pause\n!action - Shows current bot action and start time"

    if user_message == 'continue':
        FileHandler.write_into_file(
            file_path=FilePaths.BOT_STATUS.value, 
            data="continue"
        )
        return "Script was unpaused! Make sure to have verified AFK check"

    if user_message == 'action':
        current_action_message = FileHandler.read_from_file_lines(FilePaths.CURRENT_BOT_ACTION.value)
        return current_action_message

    return "There's no such command"


async def send_message(message, user_message):
    try:
        response = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


def get_client():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    return client

def run_discord_bot(token):
    client = get_client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        user_message = str(message.content)
        if user_message[0] == "!":
            await send_message(message, user_message[1:])

    client.run(token)

if __name__ == "__main__":
    token = sys.argv[1]
    run_discord_bot(token)