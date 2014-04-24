#! /usr/bin/env python
# coding=utf-8

__author__ = 'kingson'

import sys
import alfred
import requests


def set_cache():
    """
    获取头条新闻并缓存
    """
    html = requests.get('http://c.m.163.com/nc/article/headline/T1348647853363/0-20.html').json()
    respone = html['T1348647853363']
    cache = []
    for i in range(1, len(respone)):
        if 'url_3w' in respone[i].keys():
            cache.append(dict(title=respone[i]['title'], digest=respone[i]['digest'],
                              url=respone[i]['url_3w']))
    alfred.cache.set('workflow.list', cache, expire=600)


def get_cache():
    """
    获取缓存信息
    """
    if alfred.cache.timeout('workflow.list') == -1:
        set_cache()
    return alfred.cache.get('workflow.list')


def output(query):
    """
    返回结果给Alfred
    """
    workflows = get_cache()
    workflows = [w for w in workflows if query == 'headline']
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
