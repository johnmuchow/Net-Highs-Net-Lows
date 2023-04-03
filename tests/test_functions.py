import sys
sys.path.append('..')

import pytest
import functions as f
from yahooquery import Ticker

def test_is_symbol_equity():

    ticker_data = Ticker('AAPL')
    result = f.is_symbol_equity('AAPL', ticker_data)
    assert result == True

    ticker_data = Ticker('ARKK')
    result = f.is_symbol_equity('ARKK', ticker_data)
    assert result == False

def test_is_last_close_greater_than_min():

    ticker_data = Ticker('AAPL')
    result = f.is_last_close_greater_than_min('AAPL', ticker_data, 2)
    assert result == True

    result = f.is_last_close_greater_than_min('AAPL', ticker_data, 10000)
    assert result == False

def test_is_price_volume_greater_than_min():

    ticker_data = Ticker('AAPL')
    result = f.is_price_volume_greater_than_min('AAPL', ticker_data, 10000)
    assert result == True

    result = f.is_price_volume_greater_than_min('AAPL', ticker_data, 100000000000000)
    assert result == False

