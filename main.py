__author__ = 'yangchao'

import urllib2
from bs4 import BeautifulSoup


def main():
    url = "http://www.chiphell.com/forum-80-1.html"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    soup = BeautifulSoup(response)
    all_content = soup.find_all(attrs={"class": "s xst"})

    # print(all_content)

    for content in all_content:
        print(content)


if __name__ == '__main__':
    main()