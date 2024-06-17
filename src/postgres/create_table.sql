\c crypto;

DO $$
BEGIN

CREATE TABLE candlestick_data (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP NOT NULL,
    open_price NUMERIC(20, 10) NOT NULL,
    close_price NUMERIC(20, 10) NOT NULL,
    high_price NUMERIC(20, 10) NOT NULL,
    low_price NUMERIC(20, 10) NOT NULL,
    volume NUMERIC(20, 10) NOT NULL,
    symbol VARCHAR(10) NOT NULL
);

END $$;
