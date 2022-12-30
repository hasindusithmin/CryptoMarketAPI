import io
import pandas as pd
from datetime import datetime
from typing import List
from fastapi import FastAPI, HTTPException, status, Query
from fastapi.responses import StreamingResponse, RedirectResponse
from crypto_market_wrapper import crypto


description = """
The Cryptocrypto API is designed to provide users with the information they need to track and analyze cryptocurrency markets. The API will allow users to access a range of data on cryptocurrencies, including recent and aggregate trades data, candlestick data, and UIKlines data.

With this API, users can access:

- Recent Trades List Csv
- Aggregate Trades List Csv
- Candlestick Data Csv
- UIKlines Data Csv
- 24hr Ticker Price Change Statistics Csv
- Symbol Order Book Ticker Csv


"""

app = FastAPI(
    title="CryptoMarketAPI",
    description=description
)

@app.get("/")
def redirect_to_docs():
    return RedirectResponse('/docs')

# Recent Trades List
@app.get("/recent-trades")
async def Recent_Trades_List(symbol:str="btcusdt"):
    """
    A recent trades list is a record of the most recent trades that have been made in a particular security or financial instrument. It typically includes information such as the time the trade was executed, the price at which the trade was made, and the quantity of the security or instrument that was traded. The recent trades list can be useful for investors and traders who are interested in following the activity in a particular security or instrument, as it provides a real-time record of the most recent trades that have been made. It can also provide insight into current market conditions and trends.

    Query:
    
        symbol (str, optional):Defaults to "btcusdt".

    Raises:
    
        HTTPException: symbol is not valid

    Returns:
    
        Csv: Recent Trades List
    """
    # Recent Trades List DataFrame
    df = crypto.GET_RECENT_TRADES_LIST(SYMBOL=symbol)
    if type(df) != pd.DataFrame:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="It has been determined that the symbol provided is invalid."
        )
    BYTE_IO = io.BytesIO()
    df.to_csv(BYTE_IO)
    BYTE_IO.seek(0)
    UNIX = datetime.now().timestamp()
    return StreamingResponse(
        content=BYTE_IO,
        media_type='text/csv',
        headers={
            "Content-Disposition": f"attachment; filename=recent_trades_list_{int(UNIX)}.csv"
        }
    )

# Recent Trades List
@app.get("/aggregate-trades")
async def Aggregate_Trades_List(symbol:str="btcusdt"):
    """
    An aggregate trades list is a record of all the trades that have been made in a particular security or financial instrument over a specified period of time. It provides information about the trading activity in a particular security or instrument, and can be useful for analyzing trends and patterns in the market. The aggregate trades list is typically compiled from the data contained in a recent trades list, which is a record of the most recent trades that have been made in a particular security or instrument. It is typically updated on a regular basis, such as daily or weekly.
    
    Query:
    
        symbol (str, optional):Defaults to "btcusdt".

    Raises:
    
        HTTPException: symbol is not valid

    Returns:
    
        Csv: Aggregate Trades List
    """
    # Recent Trades List DataFrame
    df = crypto.GET_AGGREGATE_TRADES_LIST(SYMBOL=symbol)
    if type(df) != pd.DataFrame:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="It has been determined that the symbol provided is invalid."
        )
    BYTE_IO = io.BytesIO()
    df.to_csv(BYTE_IO)
    BYTE_IO.seek(0)
    UNIX = datetime.now().timestamp()
    return StreamingResponse(
        content=BYTE_IO,
        media_type='text/csv',
        headers={
            "Content-Disposition": f"attachment; filename=aggregate_trades_list_{int(UNIX)}.csv"
        }
    )
    
@app.get('/candlestick-data')
async def Candlestick_Data(symbol:str="btcusdt",interval:str="1h",limit:int=500):
    """
    Candlestick data is a type of chart that is used to display the price action of a financial instrument, such as a stock, bond, or currency pair, over a specified period of time. Each candlestick on the chart represents a certain period of time, such as one day or one hour, and is comprised of four components: the open, high, low, and close prices.

    Query:
    
        symbol (str, optional): Defaults to "btcusdt".
        
        interval (str, optional): Defaults to "1h". ['1s','1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M']

        limit (int, optional): Defaults to 500. [500 - 1000]

    Raises:
    
        HTTPException: symbol or interval is not valid.

    Returns:
    
        Csv: Candlestick Data
    """
    df = crypto.GET_CANDLESTICK_DATA(SYMBOL=symbol,INTERVAL=interval,limit=limit)
    if type(df) != pd.DataFrame:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=df
        )
    BYTE_IO = io.BytesIO()
    df.to_csv(BYTE_IO)
    BYTE_IO.seek(0)
    UNIX = datetime.now().timestamp()
    return StreamingResponse(
        content=BYTE_IO,
        media_type='text/csv',
        headers={
            "Content-Disposition": f"attachment; filename=candlestick_data_{int(UNIX)}.csv"
        }
    )

@app.get('/uiklines-data')
async def UIKlines_Data(symbol:str="btcusdt",interval:str="1h",limit:int=500):
    """
    Query:
    
        symbol (str, optional): Defaults to "btcusdt".
        
        interval (str, optional): Defaults to "1h". ['1s','1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M']

        limit (int, optional): Defaults to 500. [500 - 1000]

    Raises:
    
        HTTPException: symbol or interval is not valid.

    Returns:
    
        Csv: Candlestick Data
    """
    df = crypto.GET_UIKLINES(SYMBOL=symbol,INTERVAL=interval,limit=limit)
    if type(df) != pd.DataFrame:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=df
        )
    BYTE_IO = io.BytesIO()
    df.to_csv(BYTE_IO)
    BYTE_IO.seek(0)
    UNIX = datetime.now().timestamp()
    return StreamingResponse(
        content=BYTE_IO,
        media_type='text/csv',
        headers={
            "Content-Disposition": f"attachment; filename=uiklines_data_{int(UNIX)}.csv"
        }
    ) 
    
@app.get("/ticker-price-change-24hr")
async def Ticker_Price_Change(symbols: List[str] = Query(None)):
    """
    24-hour ticker price change statistics refer to the change in the price of a particular financial instrument, such as a stock, bond, or cryptocurrency, over a 24-hour period. These statistics can be displayed in the form of a percentage, indicating the percentage change in the price over the 24-hour period, or as an absolute value, indicating the dollar or currency amount by which the price has changed.

    Query:

        symbols (List[str], optional): Defaults to Query(None).

    Raises:order book ticker

        HTTPException: symbols is not valid.

    Returns:

        Csv: Ticker Price Change
    """
    df = crypto.GET_TICKER_PRICE_CHANGE_24H(SYMBOLS=symbols)
    if type(df) != pd.DataFrame:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="It has been determined that the symbol provided is invalid."
        )
    BYTE_IO = io.BytesIO()
    df.to_csv(BYTE_IO)
    BYTE_IO.seek(0)
    UNIX = datetime.now().timestamp()
    return StreamingResponse(
        content=BYTE_IO,
        media_type='text/csv',
        headers={
            "Content-Disposition": f"attachment; filename=ticker_price_change_24hr_{int(UNIX)}.csv"
        }
    ) 
    
@app.get("/order-book-ticker")
async def Order_Book_Ticker(symbols: List[str] = Query(None)):
    """
    An order book ticker is a financial instrument that displays real-time data about the orders that have been placed for a particular security or financial instrument, such as a stock, bond, or cryptocurrency. The order book ticker typically includes information about the current bid and ask prices for the security or instrument, as well as the quantity of the security or instrument that has been bid or asked for at those prices.

    Query:
    
        symbols (List[str], optional): Defaults to Query(None).

    Raises:
    
        HTTPException: symbols is not valid.

    Returns:
    
        Csv: Order Book Ticker
    """
    df = crypto.GET_SYMBOL_ORDER_BOOK_TICKER(SYMBOLS=symbols)
    if type(df) != pd.DataFrame:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="It has been determined that the symbol provided is invalid."
        )
    BYTE_IO = io.BytesIO()
    df.to_csv(BYTE_IO)
    BYTE_IO.seek(0)
    UNIX = datetime.now().timestamp()
    return StreamingResponse(
        content=BYTE_IO,
        media_type='text/csv',
        headers={
            "Content-Disposition": f"attachment; filename=order_book_ticker_{int(UNIX)}.csv"
        }
    ) 