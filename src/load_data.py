import urllib
from urllib.request import urlopen
base_url = 'http://export.arxiv.org/api/query?search_query='

def query(term, max_results, heading):
    """Basic Querying"""
    fetch_url = "{0}{1}:{2}&start=0&max_results={3}"
    print(fetch_url.format(base_url,heading,term,max_results))
    print('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=10')
    url = fetch_url.format(base_url,heading,term,max_results)
    return urlopen(url).read()
