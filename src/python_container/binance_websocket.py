import websocket
import json
from data_manipulator import DataManipulator
from database import session, Candlestick

class BinanceWebSocket:
    def __init__(self, stream_url):
        self.stream_url = stream_url

    def run(self):
        ws = websocket.WebSocketApp(self.stream_url, on_message=self.on_message)
        ws.run_forever()

    def on_message(self, ws, message):
        json_message = json.loads(message)
        df = DataManipulator.manipulate(json_message)
        self.insert_data(df)

    def insert_data(self, df):
        for index, row in df.iterrows():
            candlestick = Candlestick(
                time=index,
                open_price=float(row['open']),
                close_price=float(row['close']),
                high_price=float(row['high']),
                low_price=float(row['low']),
                volume=float(row['volum']),
                symbol=row['symbol']
            )
            session.add(candlestick)
        session.commit()
