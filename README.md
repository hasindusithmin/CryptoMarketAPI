# CryptoMarketAPI

![cryptomarketapi](https://i.ibb.co/QmQPyRJ/cryptomarketapi.jpg)

Welcome to the CryptoMarketAPI documentation!

With this API, users can access a variety of data related to cryptocurrency trading on various exchanges. The data provided by this API is intended for use in algorithmic trading.

## Endpoints

`GET /symbols`

Returns a list of all available cryptocurrency symbols on the specified exchange.


`GET /recent-trades`

Returns a list of recent trades in CSV format for the specified symbol.

`GET /aggregate-trades`

Returns a list of aggregate trades in CSV format for the specified symbol.

`GET /candlestick-data`

Returns candlestick data in CSV format for the specified symbol and time frame.

`GET /uiklines-data`

Returns UIKlines data in CSV format for the specified symbol and time frame.

`GET /ticker-price-change-24hr`

Returns 24-hour ticker price change statistics in CSV format for the specified symbol.

`GET /order-book-ticker`

Returns symbol order book ticker data in CSV format for the specified symbol.

### Usage

To use the API, send a `GET` request to the appropriate endpoint with the required parameters. The API will return the requested data in CSV format.

```
https://cryptomarketapi.deta.dev/symbols
```

This request will return a list of all available cryptocurrency symbols on the Binance exchange.

### Note

This API is provided as is, and the API developers are not responsible for any losses or damages resulting from its use. Use of this API is at the user's own risk.







[CryptoMarketAPI](https://cryptomarketapi.deta.dev/)