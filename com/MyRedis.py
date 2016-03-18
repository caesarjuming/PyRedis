# coding=utf-8
__author__ = 'Administrator'

import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('name', 'jack')
print(r.get('name'))

""" redis的数据类型
    STRING  字符串，整数，浮点数
    LIST    链表，每个节点都包含了一个字符串
    SET     无序字符串
    HASH    键值对无序散列表
    ZSET    有序集合
"""

r.delete('name')
# nil转成None
print(r.get('name'))




