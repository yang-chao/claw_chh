# encoding: utf-8
__author__ = 'yangchao'

from bs4 import BeautifulSoup
from db_operation import DBHelper
import urllib2
import re
import sched
import time

#初始化sched模块的scheduler类
#第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
s = sched.scheduler(time.time, time.sleep)


def claw_news():
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
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
    print("claw done!")


#enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，给他的参数（注意：一定要以tuple给如，如果只有一个参数就(xx,)）
def perform(inc):
    s.enter(inc, 0, perform, (inc,))
    claw_news()


#15分钟抓取一次
def main(inc=900):
    s.enter(0, 0, perform, (inc,))
    s.run()


if __name__ == '__main__':
    main()