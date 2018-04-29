#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


"""
默认支持的路由系统：
@app.route('/user/<username>')  表示字符串
@app.route('/post/<int:post_id>') 表示整数
@app.route('/post/<float:post_id>') 表示小数
@app.route('/post/<path:path>') 路径
@app.route('/login', methods=['GET', 'POST'])

常用路由系统有以上五种，所有的路由系统都是基于一下对应关系来处理：

DEFAULT_CONVERTERS = {
    'default':          UnicodeConverter,
    'string':           UnicodeConverter,
    'any':              AnyConverter,
    'path':             PathConverter,
    'int':              IntegerConverter,
    'float':            FloatConverter,
    'uuid':             UUIDConverter,
}


"""

from flask import Flask, views, url_for
from werkzeug.routing import BaseConverter

app = Flask(import_name=__name__)

#写转换器类
class RegexConverter(BaseConverter):
    """
    自定义URL匹配正则表达式
    """
    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    def to_python(self, value):
        """
        路由匹配时，匹配成功后传递给视图函数中参数的值
        :param value:
        :return:
        """
        return value

    def to_url(self, value):
        """
        使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
        :param value:
        :return:
        """
        val = super(RegexConverter, self).to_url(value)
        return val

#将RegexConverter 添加到flask中
app.url_map.converters['regex'] = RegexConverter


@app.route('/index/<regex("xb\d+"):nid>')
def index(nid):
    print(url_for('index', nid='888'))
    return 'Index'


if __name__ == '__main__':
    app.run()

