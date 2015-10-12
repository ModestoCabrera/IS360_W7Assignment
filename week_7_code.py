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
        year (list): holds values of the year column
        data (list): holds values of the data cells
        title (list): list holds title of columns of table.

    Returns:
        output (tup): Tuple of title list, year list, and data list.

    Examples:
        >>> parse_site(url)
        >>> 
    """
    year = []
    data = []
    title = []
    try:
        soup_obj = BeautifulSoup(url, 'html.parser')
        table =  soup_obj.find('table')
        for row in  table.find_all('tr'):
            cell = row.find_all('td')
            if re.search(r"[0-9]", cell[0].text):
                year.append(cell[0].text)
                data.append([cell[1].text, cell[2].text])
            else:
                title = cell[0].text, cell[1].text, cell[2].text
        output = (title, year, data)
        return output
    except ValueError:
        print 'ValueError Please check URL format'
        raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='Enter URL Link to access HTML Table.')
    args = parser.parse_args()
    try:
        if args.url:
            fetch_url = url_download(args.url)
            parse_site(fetch_url)
            
    except urllib2.URLError as url_err:
        print 'Invalid URL'
        raise url_err

if __name__ == '__main__':
    main()
