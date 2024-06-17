import discord
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

rapidapi_key = os.getenv("RAPIDAPI_KEY")
discord_token = os.getenv("DISCORD_TOKEN")

# Initialize global chat variable
chat = ""

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        try:
            # Append message to chat history
            chat += f"{message.author}: {message.content}\n"
            print(f'Message from {message.author}: {message.content}')

            # Check if bot is mentioned and respond
            if self.user != message.author and self.user in message.mentions:
                # Prepare payload for ChatGPT API request
                payload = {
                    "messages": [
                        {"role": "user", "content": message.content}
                    ],
                    "system_prompt": "",
                    "temperature": 0.9,
                    "top_k": 5,
                    "top_p": 0.9,
                    "max_tokens": 256,
                    "web_access": False
                }
                
                # Headers for RapidAPI request
                headers = {
                    "x-rapidapi-key": rapidapi_key,
                    "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
                    "Content-Type": "application/json"
                }
                
                # RapidAPI endpoint URL
                url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"

                # Make POST request to RapidAPI
                response = requests.post(url, json=payload, headers=headers)

                if response.status_code == 200:
                    response_data = response.json()
                    response_text = response_data.get("result", "Sorry, I couldn't understand that.")
                    channel = message.channel
                    await channel.send(response_text)
                else:
                    await message.channel.send("Failed to fetch response from ChatGPT API.")
        except Exception as e:
            print(e)
            chat = ""

# Set Discord intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize bot client
client = MyClient(intents=intents)
client.run(discord_token)