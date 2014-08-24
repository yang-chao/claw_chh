# encoding: utf-8
__author__ = 'yangchao'

import urllib2
from bs4 import BeautifulSoup
from db_operation import DBHelper
import re


def main():
    headers = { 'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    urlreq = urllib2.Request(url="http://www.chiphell.com/forum-80-1.html", headers=headers)
    response = urllib2.urlopen(urlreq)

    soup = BeautifulSoup(response)
    all_thread = soup.findAll(id=re.compile('^normalthread'))

    # 数据库
    db_helper = DBHelper()

    for thread in all_thread:
        content = thread.find(attrs={"class": "new"})
        category = content.em.a.string
        title_tag = content.find('a', {'class': 's xst'})
        title = title_tag.string
        link = title_tag.get('href')
        by_td = thread.find(attrs={'class': 'by'})
        author = by_td.cite.a.string
        time = by_td.em.span.string
        message_count = thread.find(attrs={'class': 'num'}).a.string

        # print(category)
        # print(title)
        # print(link)
        # print(author)
        # print(time)
        # print(message_count)

        db_helper.insert('news', title, link, time, category, author, message_count)

    db_helper.close()


if __name__ == '__main__':
    main()