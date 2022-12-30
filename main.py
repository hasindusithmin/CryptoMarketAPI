import io
import pandas as pd
from datetime import datetime
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse
from crypto_market_wrapper import crypto

app = FastAPI(
    title="CryptoMarketAPI"
)

@app.get("/")
def redirect_to_docs():
    return

# Recent Trades List
@app.get("/recent-trades")
async def Recent_Trades_List(symbol:str="btcusdt"):
    """
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
            "Content-Disposition": f"attachment; filename=recent_trades_list_{int(UNIX)}.csv"
        }
    )