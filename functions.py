from yahooquery import Ticker
import requests

#--------------------------------------------------------------------------------------
# https://github.com/rreichel3/US-Stock-Symbols
#--------------------------------------------------------------------------------------
def download_nasdaq_symbols(path):
    """
    Download nasdaq symbols.

    Parameters:
        path(string): path of file to write list of downloaded symbols

    Returns:
        None
    """

    url = 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nasdaq/nasdaq_tickers.txt'
    response = requests.get(url)

    with open(path, 'wb') as f:
        f.write(response.content)

#--------------------------------------------------------------------------------------
def is_symbol_equity(symbol_name, ticker_data):
#--------------------------------------------------------------------------------------    
    """
    Is the symbol name an equity (versus ETF, etc)?

    Parameters:
        symbol(string): The symbol name, e.g. AAPL
        width (Ticker): Ticker object with data for the above symbol

    Returns:
        boolean: True if symbol is an equity, otherwise false
    """

    if (ticker_data.price[symbol_name]['quoteType'] == "EQUITY"):
        return True
    else:
        return False

#--------------------------------------------------------------------------------------
def is_last_close_greater_than_min(symbol_name, ticker_data, min_val):
#--------------------------------------------------------------------------------------
    """
    Is the close of the symbol > minimum value?

    Parameters:
        symbol(string): The symbol name, e.g. AAPL
        width (Ticker): Ticker object with data for the above symbol
        min_val(int): Minimum value to compare

    Returns:
        boolean: True if close is > minimum value, otherwise false
    """

    if (ticker_data.price[symbol_name]['regularMarketDayLow'] > min_val):
        return True
    else:
        return False

#--------------------------------------------------------------------------------------
def is_price_volume_greater_than_min(symbol_name, ticker_data, min_val):
#--------------------------------------------------------------------------------------
    """
    Is price * volume > minimum?

    Parameters:
        symbol(string): The symbol name, e.g. AAPL
        width (Ticker): Ticker object with data for the above symbol
        min_val(int): Minimum value to compare

    Returns:
        boolean: True if price * volume > minimum, otherwise false
    """

    # Price times volume
    price_volume = ticker_data.price[symbol_name]['regularMarketPrice'] * ticker_data.price[symbol_name]['regularMarketVolume']
    if (price_volume > min_val):
        return True
    else:
        return False

#--------------------------------------------------------------------------------------
def is_new_net_high(symbol_name, ticker_data):
#--------------------------------------------------------------------------------------
    """
    Is the symbol a new 52-week high?

    Parameters:
        symbol(string): The symbol name, e.g. AAPL
        width (Ticker): Ticker object with data for the above symbol

    Returns:
        boolean: True if symbol is 52-week high, otherwise false
    """

    if (ticker_data.price[symbol_name]['regularMarketDayHigh'] >= ticker_data.summary_detail[symbol_name]['fiftyTwoWeekHigh']):
        return True
    else:
        return False

#--------------------------------------------------------------------------------------
def is_new_net_low(symbol_name, ticker_data):
#--------------------------------------------------------------------------------------
    """
    Is the symbol a new 52-week low?

    Parameters:
        symbol(string): The symbol name, e.g. AAPL
        width (Ticker): Ticker object with data for the above symbol

    Returns:
        boolean: True if symbol is 52-week low, otherwise false
    """

    if (ticker_data.price[symbol_name]['regularMarketDayLow'] <= ticker_data.summary_detail[symbol_name]['fiftyTwoWeekLow']):
        return True
    else:
        return False


#--------------------------------------------------------------------------------------
# Test code
#--------------------------------------------------------------------------------------
# sym_name = 'aapl'
# ticker_data = Ticker(sym_name)
# print(f'Symbol name {sym_name} is of type {ticker_data.price[sym_name]["quoteType"]}')

# print(sym.price)

#print(f'Is {sym_name} an equity:', is_symbol_equity(sym_name, ticker_data))

# print(f'Is {sym_name} close > 2:', is_last_close_greater_than_min(sym_name, ticker_data, 2))

# print(f'Is {sym_name} price * volume > 10,000:', is_price_volume_greater_than_min(sym_name, ticker_data, 10000))
