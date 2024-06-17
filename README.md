# AI-Enhanced Discord ChatBot

This is a feature-rich Discord bot that provides various functionalities, including weather information, stock prices, news updates, translation capabilities, and an integration with the ChatGPT API for intelligent conversation.

## Features

- **Weather Information**: Get real-time weather updates for any location using the `!weather` command followed by the city name.
- **Stock Prices**: Retrieve the current stock price of a company by using the `!stock` command followed by the stock symbol.
- **News Updates**: Stay updated with the latest news headlines related to a specific topic by using the `!news` command followed by the topic keyword.
- **Translation**: Translate text to different languages using the `!translate` command followed by the target language code and the text to translate.
- **ChatGPT Integration**: Engage in intelligent conversations with the bot by mentioning it in your message. The bot will use the ChatGPT API to generate relevant and contextual responses.

## Prerequisites

Before running the bot, make sure you have the following:

1. A Discord account and a server where you have permission to add bots.
2. API keys for the following services:
  - OpenWeatherMap (for weather information)
  - Alpha Vantage (for stock prices)
  - News API (for news updates)
  - RapidAPI (for ChatGPT integration)
  - Google Translate API (optional, for translation functionality)

## Usage

Once the bot is running, you can use the following commands in your Discord server:

- `!weather <city_name>`: Get the current weather information for the specified city.
- `!stock <stock_symbol>`: Retrieve the current stock price for the specified company.
- `!news <topic>`: Get the latest news headlines related to the specified topic.
- `!translate <target_language_code> <text>`: Translate the given text to the specified target language.
- `@mention_the_bot <your_message>`: Engage in a conversation with the bot, and it will respond using the ChatGPT API.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
