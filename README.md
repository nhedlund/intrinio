# intrinio

[![Build Status](https://travis-ci.org/nhedlund/intrinio.svg?branch=master)](https://travis-ci.org/nhedlund/intrinio)

Unofficial Intrinio API client for Python.
It gives easy access to financial data.

## Setup
Install this package by using the pip tool:

```bash
pip install intrinio
```

Before retrieving data using the package the API username and password has to be
configured, either by setting the username and password attributes of the
intrinio package:

```python
import intrinio
intrinio.username = 'USERNAME_FROM_INTRINIO'
intrinio.password = 'PASSWORD_FROM_INTRINIO'
```

Or by setting the system environment variables:

* INTRINIO_USERNAME
* INTRINIO_PASSWORD

## Quick start
Get prices starting at 2016-01-01 for Apple:

```python
import intrinio
intrinio.prices('AAPL', start_date='2016-01-01')
```

Get company information about Google:

```python
import intrinio
intrinio.companies('GOOG')
```
Get company information about Google using the low level **get** function:

```python
import intrinio
intrinio.get('companies', identifier='GOOG')
```

Get cik, lei, name and ticker of companies with "Bank" in their company name:

```python
import intrinio
intrinio.companies(query='Bank')
```

## Usage
There are a high- and low level functions used to access the Intrinio API.

The high level functions are mostly simple wrappers of the **get** function
that retrieves all data with optional parameters to filter the data. They
might also do some data conversion like for example the prices endpoint
where the date column is used as the index for the Pandas DataFrame.

### Low level functions
For more information about available endpoints and their parameters,
see Intrinio API documentation at: http://docs.intrinio.com/

* get(endpoint, **parameters):

    Get complete dataset from an endpoint using optional query parameters.

    Args:
    
        endpoint: Intrinio endpoint, for example: companies
        parameters: Optional query parameters

    Returns:
        Dataset as a Pandas DataFrame

* get_page(endpoint, page_number=1, page_size=None, **parameters):

    Get a dataset page from an endpoint using optional query parameters.

    Args:
    
        endpoint: Intrinio endpoint, for example: companies
        page_number: Optional page number where 1 is first page (default 1)
        page_size: Optional page size (default max page size for the endpoint)
        parameters: Optional query parameters

    Returns:
        Dataset page as a Pandas DataFrame with an additional total_pages
        attribute

### High level functions


* companies(identifier=None, query=None):

    Get companies with optional filtering using parameters.

    Args:
    
        identifier: Identifier for the legal entity or a security associated
            with the company: TICKER SYMBOL | FIGI | OTHER IDENTIFIER
        query: Search of company name or ticker symbol

    Returns:
        Dataset as a Pandas DataFrame

* securities(identifier=None, query=None, exch_symbol=None):

    Get securities with optional filtering using parameters.

    Args:
    
        identifier: Identifier for the legal entity or a security associated
            with the company: TICKER SYMBOL | FIGI | OTHER IDENTIFIER
        query: Search of security name or ticker symbol
        exch_symbol: Exchange symbol

    Returns:
        Dataset as a Pandas DataFrame

* indices(identifier=None, query=None, type=None):

    Get indices with optional filtering using parameters.

    Args:
    
        identifier: Intrinio symbol associated with the index
        query: Search of index name or symbol
        type: Type of indices: stock_market | economic | sic
        
    Returns:
        Dataset as a Pandas DataFrame

* prices(identifier, start_date=None, end_date=None, frequency='daily',
           sort_order='desc'):
           
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

* news(identifier):

    Get news for a company.

    Args:
 
        identifier: stock market ticker symbol associated with the company's
            common stock. If the company is foreign, use the stock exchange
            code, followed by a colon, then the ticker.

    Returns:
        Dataset as a Pandas DataFrame
 
## Tests
Run the tests using pytest in the root directory of the project:

```bash
py.test
```

Or run the runtests script to also generate a coverage report
(saved to tmp/).

```bash
bin/runtests
```


## Version history

* 0.1: Initial version

## License

* MIT License