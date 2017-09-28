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
    df = indices(type='Stock_Market')
    assert len(df) > 1


def test_endpoint_prices_with_descending_order():
    df = prices('AAPL', start_date='2015-01-01')
    assert 'date' not in df.columns
    assert len(df) > 500
    assert df.index[0] > df.index[1]


def test_endpoint_prices_with_ascending_order():
    df = prices('AAPL', start_date='2015-01-01', sort_order='asc')
    assert 'date' not in df.columns
    assert len(df) > 500
    assert df.index[0] < df.index[1]


def test_endpoint_news():
    df = news('A')
    assert len(df) > 200
    assert df.summary.str.contains('Agilent', case=False).any()


def test_endpoint_fundamentals():
    df = fundamentals('AC')
    assert len(df) >= 3
    assert (df.fiscal_period == 'FY').all()


def test_endpoint_financials():
    df = financials('AC')
    assert len(df) >= 3
    assert (df.ebit != 0.0).any()


def test_endpoint_financials_quarter_periods():
    df = financials('AC', 'QTR')
    assert len(df) >= 3
    assert (df.ebit != 0.0).any()


def test_endpoint_financials_period_with_first_quarter():
    df = financials_period('AC', 2015, 'Q1')
    assert len(df) == 1
    assert df.ebit[0] > 2000000
    assert df.ebit[0] < 3000000
