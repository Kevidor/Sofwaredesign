import os
import json
import random
import requests
import discord
from discord.ext import commands
from discord import app_commands

# Set up bot intents
intents = discord.Intents.default()
intents.message_content = True  # Required for message-based interactions

# Create the bot instance with an App Command Tree
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=intents)  # No command prefix needed for slash commands
        self.synced = False  # Ensure commands sync only once

    async def on_ready(self):
        if not self.synced:
            try:
                await self.tree.sync()
                self.synced = True
                print(f"✅ Synced {len(self.tree.get_commands())} command(s)")
            except Exception as e:
                print(f"❌ Error syncing commands: {e}")

        print(f"✅ Bot is online as {self.user}!")

with open("Gui_test/compliments.json", "r", encoding="utf-8") as file:
    compliments_data = json.load(file)["compliments"]

def get_random_compliment(name: str) -> str:
    """Returns a random compliment with the user's name inserted."""
    compliment = random.choice(compliments_data)
    return compliment.replace("{name}", name)

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
    except requests.exceptions.JSONDecodeError as e:
        await interaction.response.send_message("❌ Failed to load meme.", ephemeral=True)
        print(f"Error decoding JSON: {e}")

# 😈 INSULT COMMAND (DE)
@app_commands.command(name="insult_de", description="Beleidigt einen erwähnten Nutzer auf Deutsch")
@app_commands.describe(member="Wen möchtest du beleidigen?")
async def insult_de(interaction: discord.Interaction, member: discord.Member):
    insult = requests.get("https://evilinsult.com/generate_insult.php?lang=de&type=json")
    try:
        json_insult_data = insult.json()
        insult_str = json_insult_data.get("insult")
        await interaction.response.send_message(f"😡 Hey {member.mention}, du {insult_str}!")
    except Exception as e:
        await interaction.response.send_message("❌ Fehler beim Abrufen der Beleidigung.", ephemeral=True)
        print(f"Error insult not found: {e}")

# 😈 INSULT COMMAND (EN)
@app_commands.command(name="insult_en", description="Insult a mentioned user in English")
@app_commands.describe(member="Who do you want to insult?")
async def insult_en(interaction: discord.Interaction, member: discord.Member):
    insult = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    try:
        json_insult_data = insult.json()
        insult_str = json_insult_data.get("insult")
        await interaction.response.send_message(f"😡 Hey {member.mention}, {insult_str}")
    except Exception as e:
        await interaction.response.send_message("❌ Failed to retrieve insult.", ephemeral=True)
        print(f"Error insult not found: {e}")

# 😊 COMPLIMENT COMMAND (EN)
@app_commands.command(name="compliment_en", description="Give a compliment to a mentioned user in English")
@app_commands.describe(member="Who do you want to compliment?")
async def compliment_en(interaction: discord.Interaction, member: discord.Member):
    compliment = get_random_compliment(member.mention)
    await interaction.response.send_message(f"😊 {compliment}")

# 🔥 Füge die Befehle zum Bot hinzu
bot.tree.add_command(ping)
bot.tree.add_command(meme)
bot.tree.add_command(insult_de)
bot.tree.add_command(insult_en)
bot.tree.add_command(compliment_en)

# 🔑 RUN THE BOT
bot_token = os.getenv("DISCORD_BOT_TOKEN")
bot.run(str(bot_token))