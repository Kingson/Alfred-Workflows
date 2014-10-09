#! /usr/bin/env python
# coding=utf-8

__author__ = 'kingson'

import sys
import alfred
import requests


def set_cache(query):
    """
    获取头条新闻并缓存
    """
    if query == "headline":
        result = requests.get('http://c.m.163.com/nc/article/headline/T1348647853363/0-20.html').json()
        respone = result['T1348647853363']
        cache1 = []
        for i in range(len(respone)):
            if 'url_3w' in respone[i].keys():
                cache1.append(dict(title=respone[i]['title'], digest=respone[i]['digest'],
                                   url=respone[i]['url_3w']))
        alfred.cache.set('headline.list', cache1, expire=600)
    elif query == "sport":
        result = requests.get('http://c.m.163.com/nc/article/list/T1348649079062/0-20.html').json()
        respone = result['T1348649079062']
        cache2 = []
        for i in range(len(respone)):
            if 'url_3w' in respone[i].keys():
                cache2.append(dict(title=respone[i]['title'], digest=respone[i]['digest'],
                                   url=respone[i]['url_3w']))
        alfred.cache.set('sport.list', cache2, expire=600)
    elif query == "finance":
        result = requests.get('http://c.m.163.com/nc/article/list/T1348648756099/0-20.html').json()
        respone = result['T1348648756099']
        cache3 = []
        for i in range(len(respone)):
            if 'url_3w' in respone[i].keys():
                cache3.append(dict(title=respone[i]['title'], digest=respone[i]['digest'],
                                   url=respone[i]['url_3w']))
        alfred.cache.set('finance.list', cache3, expire=600)
    elif query == "gossip":
        result = requests.get('http://c.m.163.com/nc/article/list/T1348648517839/0-20.html').json()
        respone = result['T1348648517839']
        cache4 = []
        for i in range(len(respone)):
            if 'url_3w' in respone[i].keys():
                cache4.append(dict(title=respone[i]['title'], digest=respone[i]['digest'],
                                   url=respone[i]['url_3w']))
        alfred.cache.set('gossip.list', cache4, expire=600)
    elif query == "keji":
        result = requests.get('http://c.m.163.com/nc/article/list/T1348649580692/0-20.html').json()
        respone = result['T1348649580692']
        cache5 = []
        for i in range(len(respone)):
            if 'url_3w' in respone[i].keys():
                cache5.append(dict(title=respone[i]['title'], digest=respone[i]['digest'],
                                   url=respone[i]['url_3w']))
        alfred.cache.set('keji.list', cache5, expire=600)


def get_cache(query):
    """
    获取缓存信息
    """
    if query == "headline":
        if alfred.cache.timeout('headline.list') == -1:
            set_cache(query)
        return alfred.cache.get('headline.list')
    elif query == "sport":
        if alfred.cache.timeout('sport.list') == -1:
            set_cache(query)
        return alfred.cache.get('sport.list')
    elif query == "finance":
        if alfred.cache.timeout('finance.list') == -1:
            set_cache(query)
        return alfred.cache.get('finance.list')
    elif query == "gossip":
        if alfred.cache.timeout('gossip.list') == -1:
            set_cache(query)
        return alfred.cache.get('gossip.list')
    elif query == "keji":
        if alfred.cache.timeout('keji.list') == -1:
            set_cache(query)
        return alfred.cache.get('keji.list')


def output(query):
    """
    返回结果给Alfred
    """
    workflows = get_cache(query)
    workflows = [w for w in workflows if query]
    feedback = alfred.Feedback()
    for w in workflows:
        feedback.addItem(
            title=w['title'],
            subtitle=w['digest'],
            arg=w['url']
        )
    feedback.output()

if __name__ == '__main__':
    output(sys.argv[1])
