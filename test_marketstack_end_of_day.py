import pytest, requests
from jsonschema import validate

import marketplace_schema

API_KEY = '6a1927ea264d11abdbf882e54f5e717e'
SYMBOL = 'AAPL'

class TestMarketstackEndOfDay():
    @pytest.mark.parametrize('symbol', [(SYMBOL)])
    def test_eod_response_code_only_required(self, symbol):
        response = requests.get(f'http://api.marketstack.com/v2/eod/latest?'
                                f'access_key={API_KEY}&symbols={symbol}')
        response.raise_for_status()

    @pytest.mark.parametrize('symbol, exchange,sort, date_from, date_to, limit,offset',
                             [(SYMBOL, 'XNAS','ASC','2025-08-04', '2020-08-05', '2', '0' ),])
    def test_eod_response_code_full(self, symbol, exchange, sort, date_from, date_to, limit, offset):
        response = requests.get(f'http://api.marketstack.com/v2/eod/latest?access_key='
                                f'{API_KEY}&symbols={symbol}&exchanges={exchange}'
                                f'&limit={limit}&offset={offset}&sort={sort}'
                                f'&date_from={date_from}&date_to={date_to}')
        response.raise_for_status()

    @pytest.mark.parametrize('symbol', [(SYMBOL)])
    def test_eod_schema(self, symbol):
        response = requests.get(f'https://api.marketstack.com/v2/eod/latest?'
                                f'access_key={API_KEY}&symbols={symbol}')
        response.raise_for_status()
        validate(instance=response.json(), schema=marketplace_schema.EOD_SCHEMA)

class TestIntraday():
    @pytest.mark.parametrize('symbol', [(SYMBOL)])
    def test_intraday_response_code_only_required(self, symbol):
        response = requests.get(f'http://api.marketstack.com/v2/intraday/latest?'
                                f'access_key={API_KEY}&symbols={symbol}')
        assert  response.status_code == 403

class TestCommodities():
    @pytest.mark.parametrize('commodity', [('gold')])
    def test_commodity_response_code(self, commodity):
        response = requests.get(f'http://api.marketstack.com/v2/commodities?'
                                f'access_key={API_KEY}&commodity_name={commodity}')
        assert  response.status_code == 403

class TestSplits():
    @pytest.mark.parametrize('symbol', [(SYMBOL)])
    def test_split_response_code_only_required(self, symbol):
        response = requests.get(f'http://api.marketstack.com/v2/splits?'
                                f'access_key={API_KEY}&symbols={symbol}')
        response.raise_for_status()