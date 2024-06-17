from binance.client import Client
from datetime import datetime, timedelta

class BinanceClient:
    def __init__(self):
        self.client = Client()

    def get_usdt_symbols(self):
        exchange_info = self.client.get_exchange_info()
        symbols = [i['symbol'] for i in exchange_info['symbols'] if i['symbol'].endswith('USDT')]
        return [i.lower() + '@kline_1m' for i in symbols]

    def get_historical(self, pair):
        historical_data = self.client.get_historical_klines(
                                              pair, 
                                              Client.KLINE_INTERVAL_1MINUTE, 
                                              start_str=str(datetime.today() - timedelta(days=7)),
                                              end_str=str(datetime.today())
                                        )
        return {pair: historical_data}
