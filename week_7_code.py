import pprint

import pprint
import sys, urllib2, argparse, re

from bs4 import BeautifulSoup


#  &&&&&&&&& READ CONTENT OF HTML table from a web page into pandas DATAFRAME&&&&&&&&&



#this is where the link is read


def url_download(url):
    try:
        url_file = urllib2.urlopen(url)

    except urllib2.HTTPError as url_error:
        print 'Error attempting to load URL'
        raise url_error

    return url_file


def parse_site(url):
    column1 = []
    column2 = []
    column3 = []
    
    soup_obj = BeautifulSoup(url, 'html.parser')
    table =  soup_obj.find('table')
    for row in  table.find_all('tr'):
        cell = row.find_all('td')
        database += [cell[0].text, cell[1].text, cell[2].text]
    print database


#Some of the rows where not catching, last night using dicts and values. list may not work.
#NOT CATCHING ALL THE ROWS, MUST USE REGEX...
#            try:                
#                database[cells[0].text] = [float(cells[1].text), float(cells[2].text)]
#            except:
#                print cells[0].text, cells[1].text, cells[2].text
#                print 'error here'
#                titles = [cells[0].text, cells[1].text, cells[2].text]
#        pprint.pprint(database)    
###ahhhh i am not done yet, but i will upload it, and finish this tomorow.         
    
    


def main():
    downfile = url_download("https://www.globalpolicy.org/component/content/article/109/27519.html")
    parse_site(downfile)


if __name__ == '__main__':
    main()
