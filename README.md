# Streamlit_Stock_Price_App
A Simple Stock Price Stream lit App
# Simple Stock Price App

This is a simple stock price app built with Python and Streamlit. It retrieves and displays the historical closing price and volume of a specified stock using the Yahoo Finance API.

## Installation

1. Make sure you have Python installed on your machine. You can download it from the official Python website: https://www.python.org/downloads/

2. Clone or download the repository to your local machine.

3. Open a terminal or command prompt and navigate to the project directory.

4. Install the required dependencies by running the following command:

pip install yfinance streamlit

## Usage

1. In the main code file (`stock_price_app.py`), specify the ticker symbol of the stock you want to retrieve data for. For example, to get data for Google, set `tickerSymbol = 'GOOGL'`.

2. Optionally, you can adjust the date range for the historical data by modifying the `start` and `end` parameters in the `tickerData.history()` function.

3. Run the app by executing the following command in the terminal or command prompt:

streamlit run stock_price_app.py

