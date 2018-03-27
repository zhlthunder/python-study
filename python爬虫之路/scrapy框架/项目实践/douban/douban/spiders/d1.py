# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import urllib.request
import os

class D1Spider(scrapy.Spider):
    name = 'd1'
    allowed_domains = ['douban.com']
    # start_urls = ['http://douban.com/']
    header={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"}
    #编写start_requests()方法，第一次会默认调取该方法中的请求，即此时start_urls就不是第一个爬取的URL，第一个爬取的URL在下面的函数中定义
    def start_requests(self):
        ##单次追加header的方法
        return [Request("https://accounts.douban.com/login",meta={"cookiejar":1},callback=self.parse,headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"})]
        # return [Request("https://accounts.douban.com/login",meta={"cookiejar":1},callback=self.parse)]
#"cookiejar":1  表示开启cookie

    def parse(self, response):
        #判读是否有验证码
        captcha=response.xpath("//img[@id='captcha_image']/@src").extract()

        if len(captcha)>0:
            print("此时有验证码")
            #将验证码存储到本地
            localpath="D:/thunder/yzm/captcha.png"
            urllib.request.urlretrieve(captcha[0],filename=localpath)

            ##方法1：手动输入验证码
            captcha_val=input("请到D:\thunder\yzm\captcha.png中确认验证码：")

            ##方法2：调用云打码API来识别验证码，因为没有注册，所以这个代码无法执行
            # cmd="c:/python27/python.exe C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python爬虫之路\scrapy框架\项目实践\douban\云打码api\Python调用示例\Python调用示例\YDMPython2.x.py"
            # ret=os.popen(cmd)
            # captcha_val=ret.read()

            ##方法3，自己写python代码实现验证码的识别


            data={
            "captcha-solution":captcha_val,
            "redir":"https://www.douban.com/people/175906194/",
            "form_email":"zhlthunder@163.com",
            "form_password":"zhl040702246",
            }
        else:
        #设置要传递的post信息，此时没有验证码,只需定义用户名及密码
            data={
                "redir":"https://www.douban.com/people/175906194/",
                "form_email":"zhlthunder@163.com",
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


