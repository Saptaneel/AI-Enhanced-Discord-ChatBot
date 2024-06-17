## Project Name:  AI-Enhanced-Discord-ChatBot

### Description
This Discord bot integrates with the ChatGPT API via RapidAPI to provide responses when mentioned in a Discord server. It listens for messages, appends them to a chat history, and replies using AI-generated responses from ChatGPT.

### Setup Instructions
1. **Environment Setup**
   - Clone the repository.
   - Install necessary Python packages (`discord`, `requests`, `dotenv`).

2. **Configuration**
   - Create a `.env` file in the project root.
   - Add your Discord bot token (`DISCORD_TOKEN`) and RapidAPI key (`RAPIDAPI_KEY`) to the `.env` file.
  
 3. **Running the Bot**
- Run the Python script (`bot.py` or your chosen filename) to start the bot.
- Ensure your bot is invited to your Discord server with appropriate permissions.

### Usage
- Once the bot is running and connected to your Discord server, it will listen for messages.
- Mention the bot (@botname) in any channel where it has access to trigger a response from ChatGPT.
- The bot will reply with AI-generated text based on the messages it receives.

### Example
- User: `@botname How are you?`
- Bot: `I'm doing well, thank you!`

### Dependencies
- `discord.py`: Python library for Discord bot development.
- `requests`: HTTP library for making API requests.
- `dotenv`: Python library for loading environment variables from a `.env` file.

### Notes
- This bot uses the ChatGPT API via RapidAPI. Ensure your RapidAPI key (`RAPIDAPI_KEY`) is kept confidential and not shared publicly.


  
