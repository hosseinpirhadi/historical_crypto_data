from tqdm import tqdm
from binance_client import BinanceClient
from postgres_insert import PostgresInsert
from database import session
# from binance_websocket import BinanceWebSocket

def main():
    binance_client = BinanceClient()
    crypto_pairs = [
        "BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "XRPUSDT",
        "ADAUSDT",
        "SOLUSDT",
        "DOTUSDT",
        "LTCUSDT",
        "DOGEUSDT",
        "AVAXUSDT"
    ]
    
    insertion = PostgresInsert()
    
    for pair in tqdm(crypto_pairs):
        historical_data = binance_client.get_historical(pair)
        insertion.insert_data(session, historical_data)
        
    # symbols = binance_client.get_usdt_symbols()
    # relevant_streams = '/'.join(symbols)
    # stream_url = f'wss://stream.binance.com:9443/stream?streams={relevant_streams}'
    
    # ws_client = BinanceWebSocket(stream_url)
    # ws_client.run()

if __name__ == "__main__":
    main()
