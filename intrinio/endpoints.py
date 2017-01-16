import pandas as pd
from intrinio.client import get


def companies(identifier=None, query=None):
    """
    Get companies with optional filtering using parameters.

    Args:
        identifier: Identifier for the legal entity or a security associated
            with the company: TICKER SYMBOL | FIGI | OTHER IDENTIFIER
        query: Search of company name or ticker symbol

    Returns:
        Dataset as a Pandas DataFrame
    """
    if identifier is not None:
        identifier = str.upper(identifier)

    return get('companies', identifier=identifier, query=query)


def securities(identifier=None, query=None, exch_symbol=None):
    """
    Get securities with optional filtering using parameters.

    Args:
        identifier: Identifier for the legal entity or a security associated
            with the company: TICKER SYMBOL | FIGI | OTHER IDENTIFIER
        query: Search of security name or ticker symbol
        exch_symbol: Exchange symbol

    Returns:
        Dataset as a Pandas DataFrame
    """
    if identifier is not None:
        identifier = str.upper(identifier)

    return get('securities', identifier=identifier, query=query,
               exch_symbol=exch_symbol)


def indices(identifier=None, query=None, type=None):
    """
    Get indices with optional filtering using parameters.

    Args:
        identifier: Intrinio symbol associated with the index
        query: Search of index name or symbol
        type: Type of indices: stock_market | economic | sic
    Returns:
        Dataset as a Pandas DataFrame
    """
    if identifier is not None:
        identifier = str.upper(identifier)

    return get('indices', identifier=identifier, query=query, type=type)


def prices(identifier, start_date=None, end_date=None, frequency='daily',
           sort_order='desc'):
    """
    Get historical stock market prices or indices.

    Args:
        identifier: Stock market symbol or index
        start_date: Start date of prices (default no filter)
        end_date: Last date (default today)
        frequency: Frequency of prices: daily (default) | weekly | monthly |
            quarterly | yearly
        sort_order: Order of prices: asc | desc (default)

    Returns:
        Dataset as a Pandas DataFrame
    """
    if identifier is not None:
        identifier = str.upper(identifier)

    df = get('prices', identifier=identifier, start_date=start_date,
             end_date=end_date, frequency=frequency, sort_order=sort_order)
    df.index = pd.DatetimeIndex(df.date)
    df.drop('date', axis=1, inplace=True)
    return df


def news(identifier):
    """
    Get news for a company.

    Args:
        identifier: stock market ticker symbol associated with the company's
            common stock. If the company is foreign, use the stock exchange
            code, followed by a colon, then the ticker.

    Returns:
        Dataset as a Pandas DataFrame
    """
    return get('news', identifier=str.upper(identifier))
