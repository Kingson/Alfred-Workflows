#! /usr/bin/env python
# coding=utf-8

__author__ = 'kingson'

import sys

import alfred
import requests


def set_cache():
    html = requests.get('http://c.m.163.com/nc/article/headline/T1348647853363/0-20.html').json()
    cache = []
    for i in range(1, 9):
        cache.append(dict(title=html['T1348647853363'][i]['title'], digest=html['T1348647853363'][i]['digest'],
                          url=html['T1348647853363'][i]['url_3w']))
    alfred.cache.set('workflow.list', cache, expire=600)


def get_cache():
    if alfred.cache.timeout('workflow.list') == -1:
        set_cache()
    return alfred.cache.get('workflow.list')

# def filter(w, query):
#     return (
#             len(query)==0 or
#             w['name'].lower().find(query.lower()) >= 0 or
#             w['description'].lower().find(query.lower()) >= 0 or
#             w['author'].lower().find(query.lower()) >= 0
#         )


def search(query):
    workflows = get_cache()
    workflows = [w for w in workflows if query == True]
    feedback = alfred.Feedback()
    for w in workflows:
        feedback.addItem(
            title=w['title'],
            subtitle=w['digest'],
            arg=w['url']
        )
    feedback.output()

if __name__ == '__main__':
    # set_cache()
    search(sys.argv[1])
