#!/usr/bin/python
"""
A crude script to download all Project Madurai 
Unicode HTML and PDF files off the main site. This script
scrapes all links from the list page and then removes all
tscii stuff and then proceeds to download the PDF and HTML
files using unix wget.

TODO:
+ do not download files downloaded already
+ download PDF and HTML files to seperate dirs
+ make json out of table data
"""
import os
import requests
from bs4 import BeautifulSoup

baseurl = 'http://www.projectmadurai.org'
scrapeurl = baseurl + '/pmworks.html'
initfile = 'filelist.txt'
secfile = 'works.txt'

page = requests.get(scrapeurl).text
soup = BeautifulSoup(page)
table = soup.find('table', { 'id': 'sortabletable'})

list_file = open(initfile,'w')
for t in table.find_all('a'):
    list_file.write ( t.get('href') + '\n' )
list_file.close()

basket = set()
outfile = open(secfile,'w')
for line in open(initfile,'r'):
    if not 'tscii' in line: # fuck tscii;
        if line not in basket: # bust duplicates;
            outfile.write(line)
            basket.add(line)
outfile.close()

for line in open(secfile,'r'):
    os.system("wget " + baseurl + line)

# Better way
#os.system("wget -B " + baseurl + "-i " + secfile)
