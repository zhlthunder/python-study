# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest


class D1Spider(scrapy.Spider):
    name = 'd1'
    allowed_domains = ['douban.com']
    # start_urls = ['http://douban.com/']
    header={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"}
    #编写start_requests()方法，第一次会默认调取该方法中的请求，即此时start_urls就不是第一个爬取的URL，第一个爬取的URL在下面的函数中定义
    def start_requests(self):
        ##单次追加header的方法
        # return [Request("https://accounts.douban.com/login",meta={"cookiejar":1},callback=self.parse,headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"})]

        return [Request("https://accounts.douban.com/login",meta={"cookiejar":1},callback=self.parse)]
#"cookiejar":1  表示开启cookie

    def parse(self, response):
        #判读是否有验证码

        #设置要传递的post信息，此时没有验证码,只需定义用户名及密码
        data={
            "redir":"https://www.douban.com/people/175906194/",
            "form_email":"zhlthunder",
            "form_password":"zhl040702246",
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
        title=response.xpath("/html/head/title/text()").extract()
        print(title)



        # data=response.body
        # fh.write(data)
    #     fh.close()
    #     ##这里是登录成功的页面，而我们要访问的是个人中心，所以需要再提交一个请求，且是登录状态下
    #     print(response.xpath("/html/head/title/text()").extract())
    #     yield Request("http://edu.iqianyue.com/index_user_index.html",callback=self.next2,meta={"cookiejar":True})
    #     #"cookiejar":True 表示要保持登陆状态
    # def next2(self,response):
    #     fh=open("2st_page.html",'wb')
    #     data=response.body
    #     fh.write(data)
    #     fh.close()
    #     print(response.xpath("/html/head/title/text()").extract())
