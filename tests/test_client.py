import pandas as pd
import pytest
import intrinio
from requests import HTTPError

from intrinio.client import get, get_page, _query, _web_request, \
    _web_request_cached, get_page_size

intrinio.client.cache_enabled = True

def test_get_companies_data_with_query():
    companies = get('companies', query='Cola')
    assert len(companies) > 1
    assert companies.name.str.contains('Cola').any()


def test_get_companies_data_with_query_that_returns_many_pages():
    companies = get('companies', query='Corp')
    assert len(companies) > get_page_size('companies')
    assert len(companies) > 300
    assert companies.name.str.contains('Corp').any()


def test_get_first_page_of_companies_data():
    companies = get_page('companies')
    assert isinstance(companies, pd.DataFrame)
    assert len(companies) == get_page_size('companies')
    assert companies.total_pages > 1
    assert 'ticker' in companies.columns
    assert 'cik' in companies.columns
    assert 'lei' in companies.columns
    assert 'name' in companies.columns


def test_query_companies():
    response = _query('companies')
    assert isinstance(response, dict)
    assert 'result_count' in response
    assert 'page_size' in response
    assert 'current_page' in response
    assert 'total_pages' in response

    data = response['data']
    assert isinstance(data, list)
    assert isinstance(data[0], dict)
    assert 'ticker' in data[0]
    assert 'cik' in data[0]
    assert 'lei' in data[0]
    assert 'name' in data[0]


def test_get_missing_endpoint():
    with pytest.raises(HTTPError):
        get('missing_endpoint')


def test_query_search_engine():
    response = _web_request('https://bing.com/search', {'q': 'summer'})
    assert 'summer' in response


def test_query_search_engine_cached():
    response = _web_request_cached('https://bing.com/search', {'q': 'summer'})
    assert 'summer' in response


def test_get_page_size_with_defined_endpoint():
    page_size = get_page_size('prices')
    assert page_size == 50000


def test_get_page_size_with_undefined_endpoint():
    page_size = get_page_size('not-defined')
    assert page_size == 250
