#imported needed libraries
import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

#### Shown are the stock price ***closing price*** and ***volume*** of Google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol#define the ticker symbol

tickerSymbol = 'GOOGL'  # GOOGL -> Ticker Symbol of Google
                        # What Is a Stock Symbol (Ticker)?
                        # A stock symbol is a unique series of letters assigned to a     security for trading purposes. 
                        # Stocks listed on the New York Stock Exchange (NYSE) can have four or fewer letters. 
                        # Nasdaq-listed securities can have up to five characters. Symbols are just a shorthand way 
                        # of describing a company's stock, so there is no significant difference between those that have 
                        # three letters and those that have four or five. Stock symbols are also known as ticker symbols.
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol) # The Ticker module of yfinance library , which allows you to access ticker data in 
                                     # a more Pythonic way

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d',start='2010-5-31',end='2022-5-31')
# Open   High   Low   Close   Volume   Dividends   Stock   Splits
# ticker dataframe columns above line indicates 

st.write("""
## Closing Price  
         """) # added heading 

st.line_chart(tickerDf.Close)

st.write("""
## Volume Price  
         """) # added heading

st.line_chart(tickerDf.Volume)