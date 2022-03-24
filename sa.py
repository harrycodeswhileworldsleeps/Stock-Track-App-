import yfinance as yf
import streamlit as sl
import pandas as pd
sl.write("""

#Stock Track 1.0.0 by Harsh Sharma

Presenting the closing price and volume of google

""")

tickerSymbol='GOOGL'
tickerData=yf.Ticker(tickerSymbol)
tickerF=tickerData.history(period='2d',start='2010-5-31',end='2022-3-24')

sl.line_chart(tickerF.Close)
sl.line_chart(tickerF.Volume)
