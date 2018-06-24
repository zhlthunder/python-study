# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import re
import random
from jdgoods.items import JdgoodsItem
from lxml import etree
from scrapy.http import Request

class GoodSpider(scrapy.Spider):
    name = 'good'
    allowed_domains = ['jd.com']
    #将入口url注释掉，使用入口函数(start_requests)来处理第一次访问的网址
    # start_urls = ['http://jd.com/']

    ua=[
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
       ]

    def start_requests(self):

    # #说明，因为UA 代理的有效性的问题，可能需要多次执行后才可以获取一次成功的情况，不要着急。
    #     req1=urllib.request.Request("https://book.jd.com/")
    #     req1.add_header("User-Agent",random.choice(ua))
    #     allpddata=urllib.request.urlopen(req1).read().decode("utf-8","ignore")
    #     print(allpddata)
    #      ##说明：先爬取图书首页，获取所有馆（比如文学馆，教育馆。。）的URL
    #     ##获取方法： 复制文学馆的链接， 在https://book.jd.com/的源码中进行搜索，进行确认可以发现，文学馆链接的关键字段是：p_wenxuezongheguan，所有就在源码中搜索p_wenxuezongheguan ，查找提取规律
    #     pat1='title: [{"NAME":"\u6587\u5b66\u5c0f\u8bf4","URL":"https:\/\/channel.jd.com\/p_wenxuezongheguan.html","YFLAG":"1"}]'
    #     pat1='p_wenxuezongheguan'
    #     # pat1='title: [{"NAME":".*?","URL":".*?\/\/channel.jd.com\/(.*?).html","YFLAG":"1"}]'
    #     allpd=re.compile(pat1).findall(allpddata)
    #     print(allpd)

        # 因为直接爬取https://book.jd.com/ 时，各个馆的URL都在javascript中，提取遇到的点问题，待继续排查，此处先手动获得各个馆的url的方法进行
        allpd=[
        'https://channel.jd.com/p_wenxuezongheguan.html',
         'https://book.jd.com/children.html',
        'https://book.jd.com/education.html',
        'https://book.jd.com/library/socialscience.html',
        'https://channel.jd.com/p_Comprehensive.html',
        'https://channel.jd.com/1713-3267.html',
        'https://book.jd.com/library/life.html',
        'https://channel.jd.com/1713-3262.html',
        'https://book.jd.com/library/science.html',
        'https://channel.jd.com/1713-3287.html',
        'https://channel.jd.com/1713-4855.html',
        'https://channel.jd.com/1713-6929.html',
        'https://channel.jd.com/1713-14669.html',
        ]

        ##step 1:依次爬取各个馆的URL,从源码中提取出每个频道的频道号cat=??
        catall=[] #用于存储所有的频道的编号
        for i in allpd:
            # print(i)
            req2=urllib.request.Request(i)
            req2.add_header("User-Agent",random.choice(self.ua))
            pddata=urllib.request.urlopen(req2).read().decode("utf-8","ignore")
            # print(len(pddata))

            #pat2='href="//list.jd.com/list.html?cat=([0-9,]*?)[&"]'  里面的的？必须替换成.，否则无法提取出来内容
            pat2='href="//list.jd.com/list.html.cat=([0-9,]*?)[&"]'
            catdata=re.compile(pat2).findall(pddata)
            for j in catdata:
                catall.append(j)
        # print(len(catall))
        catall2=set(catall) #使用set()实现去重
        # print(len(catall2))



        ##step 2:依次爬取每个频道的URL,从中获取每个频道的总页数，并存储到一个字典中
        allurl=[] #[{'频道号':"每个频道的总页数"}]
        x=0 ##为了测试，让循环尽快结束
        for m in catall2:
            thispdnum=m
            # print(thispdnum)
            req3=urllib.request.Request("https://list.jd.com/list.html?cat="+str(thispdnum))
            req3.add_header("User-Agent",random.choice(self.ua))
            listdata=urllib.request.urlopen(req3).read().decode("utf-8","ignore")
            # print(len(listdata))
            pat3="<em>共<b>(.*?)</b>"
            allpage=re.compile(pat3).findall(listdata)
            # print(allpage)
            if(len(allpage)>0):
                pass
            else:
                allpage=[1]
            allurl.append({thispdnum:allpage[0]})

            # 为了测试，只遍历前10个  ###此处控制只循环10个频道号
            if(x>5):
                break
            x+=1

        ##step 3:依次爬取每个频道号下的每个页，从中提取需要的最终的信息
        x=0
        for n in catall2:
            page_num=allurl[x][n]
            for p in range(1,int(page_num)+1):
                thispageurl="https://list.jd.com/list.html?cat="+str(n)+"&page="+str(p)
                # print(thispageurl)
                yield Request(thispageurl,callback=self.parse)
                ##为了测试，只取前10个：
                if p >10:  ##此处控制每个频道下只爬取10页
                    break
            x+=1
            if(x==5):   ##此处控制只循环5个频道号
                break


    def parse(self, response):
        item=JdgoodsItem()


        #重要：如果要在这个函数中使用正则表达式对数据进行过滤，需要这么做：
        # listdata=response.body.decode('utf-8','ignore')
        ##下面就可以使用listdata进行正则提取了

        ##提取step 1:获取一级和二级频道
        #频道1，频道2
        #需要提取的字段：
        #  <span class="curr">小说</span>   对应一级频道
        # <span class="curr">科幻小说</span>  对应二级频道
        pd=response.xpath("//span[@class='curr']/text()").extract()
        if(len(pd)==0):
            pd=["缺省","缺省"]
        if(len(pd)==1):
            pda=pd[0]
            pd=[pda,"缺省"]
        pd1=pd[0]
        pd2=pd[1]
        # print(pd1)
        # print(pd2)


        ##提取step2: 提取图书的名字
         # 过滤的样式如下：
  #         <div class="p-name">
  #   <a target="_blank" title="" href="//item.jd.com/11748668.html">
  #     <em>
  #               销售就是要玩转情商：99%的人都不知道的销售软技巧      </em>
  #     <i class="promo-words"></i>
  #   </a>
  # </div>
        ##图书名：经过分析，前三个为热卖图书，需要跳过，即从下标为四的地方开始抓取
        bookname=response.xpath("//div[@class='p-name']/a/em/text()").extract()
        # print(bookname[3]) ##只打印第一本书


        ##提取step3:提取图书价格
        ##价格：价格在源码中没有，需用通过抓包分析来获得
        # 通过抓包分析，发现这个URL中保护价格的信息：
        # 最终得出每个商品价格的最简URL:https://p.3.cn/prices/mgets?callback=jQuery4258333&type=1&skuIds=J_12220352
        allsku=response.xpath("//div[@class='p-addtocart']/a/@data-sku").extract()
        # print(allsku[0])
        ##方法2：使用正则进行提取：
        #allskupat='<a data-sku="(.*?)"'
        # allsku=re.compile(allskupat).findall(listdata)

        ##根据sku爬取价格信息： 此处省略，在下面的的循环中统一处理
        # for ii in allsku:
        #     thisurl='https://p.3.cn/prices/mgets?callback=jQuery4258333&type=1&skuIds=J_'+ii
        #     req31=urllib.request.Request(thisurl)
        #     req31.add_header("User-Agent",random.choice(self.ua))
        #     curent_price=urllib.request.urlopen(req31).read().decode("utf-8","ignore")



        ##提取step 4:提取评论数
        ##也需要通过抓包才可以获取到
        # 获取评论数的精简的url:https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds=11443719
        #此处省略，在下面的的循环中统一处理
        # for ii in allsku:
        #     thisurl='https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds='+ii
        #     req32=urllib.request.Request(thisurl)
        #     req32.add_header("User-Agent",random.choice(self.ua))
        #     current_comment=urllib.request.urlopen(req32).read().decode("utf-8","ignore")


        #提取 step 5:
        #author
        thispage_author=response.xpath("//span[@class='author_type_1']/a/@title").extract()
        # print(thispage_author[0])
        #出版社
        thispage_pub=response.xpath("//span[@class='p-bi-store']/a/@title").extract()
        # print(thispage_pub[0])
        #销售的店家
        thispage_seller=response.xpath("//span[@class='curr-shop']/text()").extract()
        # print(thispage_seller[0])


        ##到此为止，为调试节点1，打印 一级目录、二级目录，每页的第一本书名， 每页第一本书的SKU_ID

        ##处理当前页的数据：
        for n in range(0,len(thispage_seller)):
            name=bookname[n+3]

            thissku=allsku[n]
            priceurl='https://p.3.cn/prices/mgets?callback=jQuery4258333&type=1&skuIds=J_'+str(thissku)
            pricedata=urllib.request.urlopen(priceurl).read().decode('utf-8','ignore')
            pricepat='"p":"(.*?)"'
            price=re.compile(pricepat).findall(pricedata)[0]

            pnuurl='https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds='+str(thissku)
            pnudata=urllib.request.urlopen(pnuurl).read().decode('utf-8','ignore')
            pnupat='"CommentCount":(.*?),'
            pnum=re.compile(pnupat).findall(pnudata)[0]

            author=thispage_author[n]
            pub=thispage_pub[n]
            seller=thispage_seller[n]

            # print(pd1)
            # print(pd2)
            # print(name)
            # print(price)
            # print(pnum)
            # print(author)
            # print(pub)
            # print(seller)

            item["pd1"]=pd1
            item["pd2"]=pd2
            item["name"]=name
            item["price"]=price
            item["pnum"]=pnum
            item["author"]=author
            item["pub"]=pub
            item["seller"]=seller
            yield item   #提交


            ##调试用：
            if n==5:
                break;

    ##经过调试，可以正常打印出各字段的信息；







