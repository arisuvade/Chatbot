import discord
import responses


async def send_message(
    msg: discord.Message, user_msg: str, is_private: bool
) -> str | None:
    try:
        response = responses.responses_handler(user_msg)
        if is_private:
            await msg.author.send(response)
        else:
            await msg.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot() -> None:
    TOKEN: str = "MTAyNTk3Nzg0NDc1NDU1NDkyMA.GiNOUB\
.TtVTj8HMwqZOU5POc6tw4V3rs0DOLZ1sKVF9so"

    intents: discord.Intents = discord.Intents.default()
    intents.message_content = True
    client: discord.Client = discord.Client(intents=intents)

    @client.event
    async def on_ready() -> str | None:
        print(f"{client.user} is now running!")

    @client.event
    async def on_message(msg: discord.Message) -> str | None:
        if msg.author == client.user:
            return

        usernameid: discord.abc.User = msg.author
        user_msg: str = msg.content
        channel: discord.abc.Messageable = msg.channel
        print(f"Channel: {channel} | {usernameid}: {user_msg}")

        if user_msg.startswith("?"):
            user_msg = user_msg[1:]
            await send_message(msg, user_msg, is_private=True)
        else:
            await send_message(msg, user_msg, is_private=False)

    client.run(TOKEN)
