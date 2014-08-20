__author__ = 'yangchao'

import urllib2
from bs4 import BeautifulSoup


def main():
    headers = { 'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    urlreq = urllib2.Request(url="http://www.chiphell.com/forum-80-1.html", headers=headers)
    response = urllib2.urlopen(urlreq)

    soup = BeautifulSoup(response)
    all_content = soup.find_all(attrs={"class": "s xst"})

    for content in all_content:
        print(content)
        print(content.text)
        print(content.get('href'))


if __name__ == '__main__':
    main()