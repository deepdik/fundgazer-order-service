from datetime import datetime, date
from http.client import HTTPException

from api.utils.api_client.third_party.fyers.login_automatic import get_fyers_obj


async def get_fyers_stocks_client(symbol, range_from: date, range_to: date, resolution: str = "D",
                                  date_format: str = "1", cont_flag: str = "1"):
    """
        data = {
            "symbol": "NSE:SBIN-EQ",
            "resolution": "D",
            "date_format": "1",  -> yyyy-mm-dd
            "range_from": "2022-01-08",
            "range_to": "2023-01-07",
            "cont_flag": "1",
        }
        # https://public.fyers.in/sym_details/NSE_CM.csv
        https://myapi.fyers.in/docs/#tag/Data-Api/paths/~1DataApi/post
        """
    data = {
        "symbol": symbol,
        "range_from": str(range_from),
        "range_to": str(range_to),
        "resolution": resolution,
        "date_format": date_format,
        "cont_flag": cont_flag
    }
    fyers = await get_fyers_obj()
    candles = fyers.history(data=data)
    if candles.get("s") == "ok" or candles.get("code") == 200:
        return candles["candles"], True
    else:
        print(candles.get("message"))
        return [], False


async def get_fyers_latest_price_client(symbols:list):
    """
    data = {"symbols": "NSE:NIFTYBANK-INDEX"}
    """
    payload = {"symbols": ",".join(symbols)}
    print(f"Getting data for ==>{payload}")
    fyers = await get_fyers_obj()
    resp_data = fyers.quotes(data=payload)
    print(f"Response got {resp_data}")
    if resp_data.get("s") == "ok" or resp_data.get("code") == 200:
        data = []
        for ticker in resp_data['d']:
            data.append({"symbol": ticker["n"], "price": ticker['v']['lp']})
        return data, True
    else:
        return resp_data, False




