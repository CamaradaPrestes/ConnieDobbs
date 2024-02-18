import voltage
import asyncio

client = voltage.Client()  # Initialize the client.


@client.listen("ready")  # Listen to an event.
async def on_ready():
    print(f"Logged in as {client.user}")


@client.listen("message")
async def on_message(message):
    # Change it to your account ID
    my_id = ""

    # Verifica se a mensagem começa com o comando '!say' e se é do seu ID
    if message.content.startswith("!say") and message.author.id == my_id:
        # Pega o conteúdo após o comando '!say'
        content_to_repeat = message.content[len("!say"):].strip()

        # Apaga a mensagem original
        await message.delete()

        # Espera um curto período para garantir que a mensagem seja excluída antes de enviar uma nova
        await asyncio.sleep(0.5)

        # Repete a mensagem
        await message.channel.send(content_to_repeat)


client.run("")  # Replace with your token.
