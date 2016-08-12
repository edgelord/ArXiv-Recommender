import urllib
from urllib.request import urlopen
import feedparser
base_url = 'http://export.arxiv.org/api/query?search_query='

def query(term, max_results=10, heading='all'):
    """Basic Querying"""
    fetch_url = "{0}{1}:{2}&start=0&max_results={3}"
    print(fetch_url.format(base_url,heading,term,max_results))
    print('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=10')
    url = fetch_url.format(base_url,heading,term,max_results)
    return feedparser.parse(url).entries
