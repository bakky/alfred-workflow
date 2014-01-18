# -*- coding: utf-8 -*-

import urllib
import json
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')

def toXmlTrans(trans, phonetic):
    if trans != "":
        toXml(','.join(trans)+ phonetic, '有道翻译')

def toXmlBasic(basic):   
    if basic != "":
        explains = basic['explains']
        for i in explains:
            if i != "":    
                toXml(i, '基本词典')

def toXmlWeb(web):
    if web != "":
        for kv in web:
            key = kv['key']
            value = kv['value']
            toXml(','.join(value), '网络释义:'+ key)

def toXml(title, subtitle):
    print "<item uid=\"YouDao\" valid=\"no\" autocomplete=\"YouDao\">"
    print "    <title>" + title + "</title>"
    print "    <subtitle>" + subtitle + "</subtitle>"
    print "    <icon type=\"fileicon\">/Applications/Dictionary.app</icon>"
    print "</item>"

def toNoResultXml(error):
    print "<item uid=\"YouDao\" valid=\"no\" autocomplete=\"YouDao\">"
    print "    <title>卧槽!竟然暂无结果</title>"
    print "    <subtitle>errorCode:" + str(error) + "</subtitle>"
    print "    <icon type=\"fileicon\">/Applications/Dictionary.app</icon>"
    print "</item>"

theQuery = 'alibaba'
theQuery = theQuery.strip()
url = 'http://fanyi.youdao.com/openapi.do?keyfrom=xxx&key=xxx&type=data&doctype=json&version=1.1&q='+theQuery
ret = json.loads(urllib.urlopen(url.encode('utf-8')).read())
error = ret['errorCode']
print "<?xml version=\"1.0\"?>\n<items>"
if error == 0:
    basic = ret['basic']
    web = ret['web']
    trans = ret['translation']
    if basic.has_key('name'):
        phonetic = '['+basic['phonetic']+']'
    else:
        phonetic = ''
    toXmlTrans(trans, phonetic)
    toXmlBasic(basic)
    toXmlWeb(web)
else:
    toNoResultXml(error)
print "</items>\n"