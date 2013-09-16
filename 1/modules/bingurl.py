__author__ = 'Tavern'
#! -*- coding:utf-8 -*-
import urllib


def get_bing_jpg_url():
    url = r'http://cn.bing.com'
    # open bing website
    page = urllib.urlopen(url)
    if None == page:
        print('open %s error' % url)
        return -1

    # read website content
    data = page.read()
    if not data:
        return -1
    page.close()

    # find jpg path
    posleft = data.find(b'g_img={url:')
    if -1 == posleft:
        print ('jpg url not found')
        return -1
    posright = data.find(b'\'', posleft + 12)
    if -1 == posright:
        print ('jpg url not found')
        return -1

    # get path
    jpgpath = data[posleft + 12: posright].decode("ascii")
    return jpgpath