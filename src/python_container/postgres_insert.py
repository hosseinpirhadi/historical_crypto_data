from database import session, Candlestick
from datetime import datetime

class PostgresInsert:
    def insert_data(self, session, data):
        for symbol in data:
            for item in data[symbol]:
                candlestick = Candlestick(
                    time=datetime.fromtimestamp(item[0] / 1000),
                    open_price=float(item[1]),
                    high_price=float(item[2]),
                    low_price=float(item[3]),
                    close_price=float(item[4]),
                    volume=float(item[5]),
                    symbol=symbol
                )
                session.add(candlestick)
        session.commit()
