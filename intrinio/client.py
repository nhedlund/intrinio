import os
import logging
import json
import requests.sessions as sessions
import pandas as pd

username = os.getenv('INTRINIO_USERNAME')
password = os.getenv('INTRINIO_PASSWORD')

page_sizes = {
    'prices': 50000,
    'historical_data': 50000,
    'tags/standardized': 5000,
    'tags/reported': 5000,
    'tags/banks': 5000,
    'financials/standardized': 5000,
    'financials/reported': 5000,
    'financials/banks': 5000,
}

api_base_url = 'https://api.intrinio.com'
default_page_size = 250
log = logging.getLogger(__name__)


def get(endpoint, **parameters):
    """
    Get complete dataset from an endpoint using optional query parameters.

    Args:
        endpoint: Intrinio endpoint, for example: companies
        parameters: Optional query parameters

    Returns:
        Dataset as a Pandas DataFrame
    """
    page_number = 1
    dataset = pd.DataFrame()

    while True:
        page = get_page(endpoint, page_number, **parameters)
        dataset = pd.concat([dataset, page])

        if len(page) == 0 or page_number == page.total_pages:
            return dataset

        page_number += 1


def get_page(endpoint, page_number=1, page_size=None, **parameters):
    """
    Get a dataset page from an endpoint using optional query parameters.

    Args:
        endpoint: Intrinio endpoint, for example: companies
        page_number: Optional page number where 1 is the first page (default 1)
        page_size: Optional page size (default max page size for the endpoint)
        parameters: Optional query parameters

    Returns:
        Dataset page as a Pandas DataFrame with an additional total_pages
        attribute
    """
    response = query(endpoint, page_number, page_size, **parameters)

    if 'data' in response:
        page = pd.DataFrame(response['data'])
        page.total_pages = response['total_pages']
    else:
        page = pd.DataFrame([response])
        page.total_pages = 1

    return page


def query(endpoint, page_number=1, page_size=None, **parameters):
    """
    Send a query request to Intrinio API for a dataset page including page
    count and other metadata using optional query parameters.

    Args:
        endpoint: Intrinio endpoint, for example: companies
        page_number: Optional page number where 1 is the first page (default 1)
        page_size: Optional page size (default max page size for the endpoint)
        parameters: Optional query parameters

    Returns:
        Intrinio endpoint response as a tree of dictionaries, values and lists
    """
    if page_size is None:
        page_size = get_page_size(endpoint)

    url = '{}/{}'.format(api_base_url, endpoint)
    parameters['page_number'] = page_number
    parameters['page_size'] = page_size
    auth = (username, password)

    with sessions.Session() as session:
        response = session.request('GET', url, params=parameters, auth=auth,
                                   verify=True)
    if not response.ok:
        response.raise_for_status()

    return json.loads(response.content.decode('utf-8'))


def get_page_size(endpoint):
    """
    Get page size for a specific endpoint.

    Args:
        endpoint: Intrinio endpoint, for example: companies

    Returns:
        Page size as number of rows
    """
    return page_sizes.get(endpoint.lower(), default_page_size)
