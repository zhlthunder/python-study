#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import urllib.request
import re

# priceurl='https://p.3.cn/prices/mgets?callback=jQuery4258333&type=1&skuIds=J_12220352'
# pricedata=urllib.request.urlopen(priceurl).read().decode('utf-8','ignore')
# # print(pricedata)
# pricepat='"p":"(.*?)"'
# price=re.compile(pricepat).findall(pricedata)[0]
# print(price)


pnuurl='https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds=11443719'
pnudata=urllib.request.urlopen(pnuurl).read().decode('utf-8','ignore')
pnupat='"CommentCount":(.*?),'
pnum=re.compile(pnupat).findall(pnudata)[0]
print(pnum)