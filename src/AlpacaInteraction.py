import alpaca_trade_api as api
from dotenv import load_dotenv
import yfinance as yf
import os
load_dotenv()

class AlpacaInteraction:
    def __init__(self) :
        self.alpaca = api.REST(
            os.getenv("APCA_API_KEY_ID"), os.getenv("APCA_API_SECRET_KEY"),
            os.getenv("APCA_API_BASE_URL"), 'v2')
        self.tsla = yf.Ticker('TSLA')
    
    def getHistoricData(self) :
        quotes = self.tsla.history(period='60d', interval='15m', actions=False)
        with open("marketData.csv", "w", newline='') as fp:
            quotes.to_csv(fp)
        
    