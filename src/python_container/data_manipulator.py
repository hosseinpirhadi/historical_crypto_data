import pandas as pd

class DataManipulator:
    @staticmethod
    def manipulate(data):
        value_d = data['data']['k']
        open, high, low, close, volum, sym = value_d['o'], value_d['c'], value_d['h'], value_d['l'], value_d['v'], value_d['s']
        evt_time = pd.to_datetime([data['data']['E']], unit='ms')
        df = pd.DataFrame([[open, close, high, low, volum, sym]], index=evt_time, columns=['open', 'close', 'high', 'low', 'volum', 'symbol'])
        return df
