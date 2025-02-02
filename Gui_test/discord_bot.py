import discord
from discord.ext import commands
from discord import app_commands
import json
import requests

# Set up bot intents
intents = discord.Intents.default()
intents.message_content = True  # Required for message-based interactions

# Create the bot instance with an App Command Tree
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="", intents=intents)  # No command prefix needed for slash commands
        self.synced = False  # Ensure commands sync only once

    async def setup_hook(self):
        # Add commands to the bot tree
        self.tree.add_command(ping)
        self.tree.add_command(meme)
        self.tree.add_command(insult_de)
        self.tree.add_command(insult_en)

    async def on_ready(self):
        if not self.synced:
            try:
                await self.tree.sync()
                self.synced = True
                print(f"✅ Synced {len(self.tree.get_commands())} command(s)")
            except Exception as e:
                print(f"❌ Error syncing commands: {e}")

        print(f"✅ Bot is online as {self.user}!")

bot = MyBot()

# 🏓 PING COMMAND
@app_commands.command(name="ping", description="Check if the bot is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!", ephemeral=True)

# 🖼 MEME COMMAND
@app_commands.command(name="meme", description="Get a random meme from Reddit")
async def meme(interaction: discord.Interaction):
    response = requests.get("https://meme-api.com/gimme")
    try:
        json_data = response.json()
        await interaction.response.send_message(json_data.get("url"))
    except json.JSONDecodeError as e:
        await interaction.response.send_message("❌ Failed to load meme.", ephemeral=True)
        print(f"Error decoding JSON: {e}")

# 😈 INSULT COMMAND (DE) - with Autocomplete
@app_commands.command(name="insult_de", description="Beleidigt einen erwähnten Nutzer auf Deutsch")
@app_commands.describe(member="Wen möchtest du beleidigen?")
async def insult_de(interaction: discord.Interaction, member: discord.Member):
    insult = requests.get("https://evilinsult.com/generate_insult.php?lang=de&type=json")
    try:
        json_insult_data = insult.json()
        insult_str = json_insult_data.get("insult")
        await interaction.response.send_message(f"😈 Hey {member.mention}, du {insult_str}!")
    except Exception as e:
        await interaction.response.send_message("❌ Fehler beim Abrufen der Beleidigung.", ephemeral=True)
        print(f"Error insult not found: {e}")

# 😈 INSULT COMMAND (EN) - with Autocomplete
@app_commands.command(name="insult_en", description="Insult a mentioned user in English")
@app_commands.describe(member="Who do you want to insult?")
async def insult_en(interaction: discord.Interaction, member: discord.Member):
    insult = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    try:
        json_insult_data = insult.json()
        insult_str = json_insult_data.get("insult")
        await interaction.response.send_message(f"😈 Hey {member.mention}, {insult_str}")
    except Exception as e:
        await interaction.response.send_message("❌ Failed to retrieve insult.", ephemeral=True)
        print(f"Error insult not found: {e}")

# 🔑 RUN THE BOT
bot.run("")