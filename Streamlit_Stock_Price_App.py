import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

# Define the ticker symbol
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-05-31', end='2020-05-31')

# Display the closing price line chart
st.line_chart(tickerDf['Close'])

# Display the volume line chart
st.line_chart(tickerDf['Volume'])
