#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import re
url=[]
fh=open("url.txt",'r',encoding="utf-8")
pat1="id=(.*?)&"
for line in fh:
    data=re.compile(pat1).findall(line)
    # print(data[0])
    url.append(data[0])

print(url)