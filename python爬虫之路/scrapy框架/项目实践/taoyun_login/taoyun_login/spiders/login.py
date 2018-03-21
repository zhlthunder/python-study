# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://iqianyue.com/']
    header={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"}
    #编写start_requests()方法，第一次会默认调取该方法中的请求，即此时start_urls就不是第一个爬取的URL，第一个爬取的URL在下面的函数中定义
    def start_requests(self):
        return [Request("http://edu.iqianyue.com/index_user_login.html",meta={"cookiejar":1},callback=self.parse)]
#"cookiejar":1  表示开启cookie

    def parse(self, response):
        #设置要传递的post信息，此时没有验证码,只需定义用户名及密码
        data={
            "number":"thunder",
            "passwd":"123456",
        }
        print("登录中。。。")
        return [FormRequest.from_response(response,
                                          ##设置cookie信息
                                          meta={"cookiejar":response.meta["cookiejar"]},
                                          #设置headers信息模拟成浏览器
                                          headers=self.header,
                                          #设置post表单中的数据
                                          formdata=data,
                                          #设置回调函数，此时回调函数为next()
                                          callback=self.next,
                                          )]
    def next(self,response):
        #如何想获取爬取的全部的信息,赋给一个变量即可
        fh=open("1st_page.html",'wb')
        data=response.body
        fh.write(data)
        fh.close()
        ##这里是登录成功的页面，而我们要访问的是个人中心，所以需要再提交一个请求，且是登录状态下
        print(response.xpath("/html/head/title/text()").extract())
        yield Request("http://edu.iqianyue.com/index_user_index.html",callback=self.next2,meta={"cookiejar":True})
        #"cookiejar":True 表示要保持登陆状态
    def next2(self,response):
        fh=open("2st_page.html",'wb')
        data=response.body
        fh.write(data)
        fh.close()
        print(response.xpath("/html/head/title/text()").extract())
