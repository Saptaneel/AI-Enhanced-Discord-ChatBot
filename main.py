import discord
import os
import requests
from dotenv import load_dotenv
from googletrans import Translator
from googletrans import LANGUAGES

translator = Translator()


# Print all supported languages
print("Supported languages:")
for lang_code, lang_name in LANGUAGES.items():
    print(f"{lang_code}: {lang_name}")



# Load environment variables
load_dotenv()

rapidapi_key = os.getenv("RAPIDAPI_KEY")
discord_token = os.getenv("DISCORD_TOKEN")
weather_api_key = os.getenv("WEATHER_API_KEY") # Provided weather API key
stock_api_key = os.getenv("STOCK_API_KEY" ) # Provided stock API key
news_api_key = os.getenv("NEWS_API_KEY")  # Provided News API key
translation_api_key = os.getenv("TRANSLATION_API_KEY")

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

            if message.author == self.user:
                return

            if message.content.startswith("!weather"):
                await self.handle_weather_command(message)
            elif message.content.startswith("!stock"):
                await self.handle_stock_command(message)
            elif message.content.startswith("!news"):
                await self.handle_news_command(message)
            elif message.content.startswith("!translate"):
                await self.handle_translation_command(message)
            elif self.user in message.mentions:
                await self.handle_chatgpt_command(message)

        except Exception as e:
            print(e)
            chat = ""

    async def handle_weather_command(self, message):
        try:
            location = message.content.split(" ", 1)[1]
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']
                city_name = data['name']
                country = data['sys']['country']
                response_text = f"The weather in {city_name}, {country} is currently {weather_description} with a temperature of {temperature}°C."
            else:
                response_text = "Sorry, I couldn't fetch the weather information. Please check the city name and try again."
            await message.channel.send(response_text)
        except Exception as e:
            print(e)
            await message.channel.send("There was an error processing the weather command.")

    async def handle_stock_command(self, message):
        try:
            symbol = message.content.split(" ", 1)[1].upper()
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={stock_api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if "Time Series (1min)" in data:
                    latest_time = list(data["Time Series (1min)"].keys())[0]
                    latest_data = data["Time Series (1min)"][latest_time]
                    stock_price = latest_data["1. open"]
                    response_text = f"The current stock price of {symbol} is ${stock_price}."
                else:
                    response_text = "Sorry, I couldn't fetch the stock information. Please check the stock symbol and try again."
            else:
                response_text = "Sorry, I couldn't fetch the stock information."
            await message.channel.send(response_text)
        except Exception as e:
            print(e)
            await message.channel.send("There was an error processing the stock command.")

    async def handle_news_command(self, message):
        try:
            topic = message.content.split(" ", 1)[1]
            url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={news_api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                articles = data["articles"][:5]  # Get top 5 articles
                response_text = "Top news headlines:\n"
                for article in articles:
                    response_text += f"- {article['title']} ({article['source']['name']})\n"
                if not articles:
                    response_text = "No news articles found for the topic."
            else:
                response_text = "Sorry, I couldn't fetch the news information."
            await message.channel.send(response_text)
        except Exception as e:
            print(e)
            await message.channel.send("There was an error processing the news command.")

    async def handle_translation_command(self, message):
      try:
        # Split message content into parts
        parts = message.content.split(" ")
        
        # Validate command format
        if len(parts) < 3 or parts[0] != "!translate":
            await message.channel.send("Invalid command format. Use '!translate <target_language> <text>'")
            return
        
        # Extract target language and text to translate
        target_lang = parts[1]
        text_to_translate = " ".join(parts[2:])
        
        # Validate target language
        if target_lang.lower() not in LANGUAGES:
            await message.channel.send(f"Unsupported language '{target_lang}'. Please use a valid ISO 639-1 language code.")
            return
        
        # Perform translation
        translator = Translator()
        translation = translator.translate(text_to_translate, dest=target_lang)
        
        response_text = f"Translation ({target_lang}): {translation.text}"
        await message.channel.send(response_text)
        
      except Exception as e:
        print(e)
        await message.channel.send("There was an error processing the translation command.")




    async def handle_chatgpt_command(self, message):
        try:
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
            
            headers = {
                "x-rapidapi-key": rapidapi_key,
                "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
                "Content-Type": "application/json"
            }
            
            url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"

            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                response_data = response.json()
                response_text = response_data.get("result", "Sorry, I couldn't understand that.")
                await message.channel.send(response_text)
            else:
                await message.channel.send("Failed to fetch response from ChatGPT API.")
        except Exception as e:
            print(e)
            await message.channel.send("There was an error processing the ChatGPT command.")
   
        
    
# Set Discord intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize bot client
client = MyClient(intents=intents)
client.run(discord_token)
