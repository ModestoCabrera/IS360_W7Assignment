#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Reads HTML Table and returns a Tuple"""

import pprint
import urllib2, argparse, re
from bs4 import BeautifulSoup


def url_download(url):
    """
    Args:
        url_file = request to open url link.

    Returns:
        url_file = file access conenction to url.

    Examples:
        >>> url_download('http://www.google.com'
        >>>
    """
    try:
        url_file = urllib2.urlopen(url)

    except urllib2.HTTPError as url_error:
        print 'Error attempting to load URL'
        raise url_error

    return url_file


def parse_site(url):
    """
    Args:
        data (dict): dictionary holds index keys, and values of data.
        title (list): list holds title of columns of table.

    Returns:
        output (tup): Tuple of title list and data dictionary.

    Examples:
        >>> parse_site(url)
        >>> 
    """
    data = {}
    title = []
    try:
        soup_obj = BeautifulSoup(url, 'html.parser')
        table =  soup_obj.find('table')
        for row in  table.find_all('tr'):
            cell = row.find_all('td')
            if re.search(r"[0-9]", cell[0].text):
                data[cell[0].text] = [cell[1].text, cell[2].text]
            else:
                title = cell[0].text, cell[1].text, cell[2].text
        output = (title, data)
        return output
    except ValueError:
        print 'ValueError Please check URL format'
        raise


def main():
    downfile = url_download("https://www.globalpolicy.org/component/content/article/109/27519.html")
    parse_site(downfile)


if __name__ == '__main__':
    main()
