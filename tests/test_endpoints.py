from intrinio.endpoints import *


def test_endpoint_companies_with_query():
    df = companies(query='Bank')
    assert len(df) > 10
    assert df.name.str.contains('Bank').any()


def test_endpoint_companies_with_identifier():
    df = companies('AAPL')
    assert len(df) == 1
    assert df.name.str.contains('Apple').any()


def test_endpoint_securities_with_identifier():
    df = securities('aapl')
    assert len(df) == 1
    assert df.security_name.str.contains('APPLE', case=False).any()


def test_endpoint_indices_with_identifier():
    df = indices('$spx')
    assert len(df) == 1


def test_endpoint_indices_with_type():
    df = indices(type='stock_market')
    assert len(df) > 1


def test_endpoint_prices_with_identifier_and_descending_order():
    df = prices('AAPL', start_date='2015-01-01')
    assert 'date' not in df.columns
    assert len(df) > 500
    assert df.index[0] > df.index[1]


def test_endpoint_prices_with_identifier_and_ascending_order():
    df = prices('AAPL', start_date='2015-01-01', sort_order='asc')
    assert 'date' not in df.columns
    assert len(df) > 500
    assert df.index[0] < df.index[1]
