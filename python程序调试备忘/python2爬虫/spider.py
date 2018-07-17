#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


import urllib,re


def download(dest):
    pat='(.*?)\s+>=(.*?).\d+-.*'
    ret=re.compile(pat).findall(dest)
    key=ret[0][0]
    ver=ret[0][1]
    # print(key)
    # print(ver)
    ver_float=float(ver)
    # print(ver_float)


    url='http://rpmfind.net/linux/rpm2html/search.php?query='+key
    data=urllib.urlopen(url).read()
    # print(data)
    # pat2="<td><a href='/linux/fedora/linux/updates/28/Everything/x86_64/Packages/s/samba-4.8.3-1.fc28.x86_64.rpm'>samba-4.8.3-1.fc28.x86_64.rpm</a></td>"
    pat2="<td><a href='([^']*?.x86_64.rpm)'>([^']*?).x86_64.rpm</a></td>"
    # pat2=">([^']*?).x86_64.rpm</a></td>"

    ret2=re.compile(pat2).findall(data)
    # print(len(ret2))
    # print(ret2[0])

    desturl=None
    for i in range(1,10):
        destfloat=ver_float+float('0.'+str(i))
        key=0
        for item in ret2:
            if str(destfloat) in item[1]:
                desturl=item[0]
                key=1
                break
        if key:
            break
    # print(desturl)
    finalurl='http://rpmfind.net'+desturl
    # print(desturl)
    filename=desturl.rsplit('/')[-1]
    # print(filename)
    urllib.urlretrieve(finalurl,filename)

# dest='samba >=4.4.2-38.6.1'  #目标字符
# download(dest)

url="https://www.suse.com/security/cve/CVE-2017-15275/"

data=urllib.urlopen(url).read()
pat="<td>SUSE Linux Enterprise Desktop 12 SP2</td> <td><ul>(.*?)</ul></td>"
ret=re.compile(pat,re.S).findall(data)
rr=ret[0]
rr=rr.replace("&gt;",">")
# print(rr)
pat2='>([^<].*?)</code></li>'
allrpm=re.compile(pat2,re.S).findall(rr)
# print(allrpm)

kk=0
for item in allrpm:
    try:
        download(item)
    except Exception as err:
        print(item)
    kk+=1
    if kk==5:
        break
