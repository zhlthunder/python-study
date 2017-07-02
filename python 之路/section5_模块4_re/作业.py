#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl



# python学习之路之案例---计算器
# 1.运用到的知识点
#
# 　　1.python正则表达式的应用，re.search('pattern',str).group()
#
# 　　2.函数中递归的使用
#
# 　　3.python函数、基本语法、控制语句if ...else ...、for循环语句的使用
#
# 　　4，字符串的格式化、字符串的拼接
#
# 　　5，列表的使用
#
# 　　6.while True：statement  死循环的使用

# 2.代码

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re


#处理乘除
def compute_mul_div(arg):
    #这里需要传入1个arg列表
    value = arg[0]
    #print value
    #mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*]',value)
    #对字符串进行乘除匹配：如1+2*3-3，就匹配：2*3
    mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',value)
    #没匹配到就直接返回
    if not mch:
        return
    #将匹配到的内容保存在content中
    content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',value).group()
    #print content
    #对匹配到的内容进行*、/判断，然后进行相应的计算，如2*3,先分割后计算
    if len(content.split('*'))>1:
        n1,n2 = content.split('*')
        get_value = float(n1) * float(n2)
    else:
        n1,n2 = content.split('/')
        get_value = float(n1) / float(n2)
    #取出匹配内容两头的内容：before，after
    before,after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',value,1)
    #然后拼接成新的字符串
    new_str = "%s%s%s" %(before,get_value,after)
    #把new_str赋值到arg[0]中
    arg[0] = new_str
    #再递归进行乘除计算
    compute_mul_div(arg)

#compute_mul_div(["1+2*3-4",0])

#print compute_mul_div([])

#处理加减
def compute_add_sub(arg):
    #arg = ["3+4-2--4++2",0]
    #对传进来的arg[0]表达式进行第1次处理，将表达式中的++\--变成+，+-、-+变成-，处理完成以后就直接break
    while True:
        if arg[0].__contains__('--') or arg[0].__contains__('+-') or arg[0].__contains__('--') or arg[0].__contains__('-+'):
            arg[0] = arg[0].replace('--','+')
            arg[0] = arg[0].replace('+-','-')
            arg[0] = arg[0].replace('-+','-')
            arg[0] = arg[0].replace('--','+')
        else:
            break
    #然后对传进来的arg[0]表达式进行第2次处理，提取首位为“-”，并将提取的次数保存在arg[1]中
    #并且没提取1次：将表达式中的"+"替换成"-"."-"替换成"+"，然后取arg[0]表达式字符串中第1到最后1位即可赋给arg[0]
    if arg[0].startswith('-'):
        arg[1]+=1
        arg[0] = arg[0].replace('-','&')
        arg[0] = arg[0].replace('+','-')
        arg[0] = arg[0].replace('&','+')
        arg[0] = arg[0][1:]
    value = arg[0]
    #对字符串value进行匹配，匹配加或减两边的内容，如1+2-3，就匹配1+2
    mch = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*',value)
    #如果没匹配到就直接发回
    if not mch:
        return
    #将匹配的内容保存在content中，如1+2
    content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*',value).group()
    #对匹配的内容进行计算：先进行判断+、-，判断后进行分割，分割后在针对+、-进行计算
    if len(content.split('+'))>1:
        n1,n2 =content.split('+')
        get_value = float(n1)+float(n2)
    else:
        n1,n2 =content.split('-')
        get_value = float(n1)-float(n2)
    #取出匹配内容两头的内容，封装在before，after中
    before,after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*',str(value),1)
    #before = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*',value,1)[0]
    #after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*',value,1)[1]
    #将计算后的:before+结果+after，进行拼接，
    new_str = "%s%s%s" %(before,get_value,after)
    #再把拼接后的字符串赋值到arg[0]中，然后再递归进行计算
    arg[0] = new_str
    compute_add_sub(arg)


#compute_add_sub(["1+3-2",0])
#计算取出来的表达式
#"""
def compute(expr):
    #先将表达式封装在inp列表中，列表的第一个元素表示：待处理表达式，第二个元素代表在表达式中首位为-号，然后我们进行提取的次数
    inp = [expr,0]
    #先进行乘除运算
    compute_mul_div(inp)
    #再进行加减运算
    compute_add_sub(inp)

    #判断inp[1]是奇数还是偶数，若是奇数，表明结果为负数，否则为正数
    count = divmod(inp[1],2)
    result = float(inp[0])
    if count[1] == 1:
        result = result * (-1)

    return result

#执行取出表达式
def excute(expr):
    #匹配最里层的括号，如：1+2*(3/(3-2)*2),这里匹配的是（3-2）
    #若没括号了 直接返回表达式
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',expr):
        return expr

    #用正则表达式取出最里括号的内容，并去掉2边的括号，得到新的表达式：content
    content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',expr).group()
    #只取字符串中第1个到倒数第二个之间的内容，即取去掉两侧的括号。如"(2+3)"只取2+3，不取两边的括号
    new_content = content[1:len(content)-1]
    ##将expr按匹配的内容进行分割：得到--before,匹配内容，after,得到content两侧的内容，并赋值给before，after
    new_list = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',expr)
    before = new_list[0]
    after = new_list[2]
    #before,nothing,after = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',expr)

    #将new_content进行计算，计算得到result
    result = compute(new_content)
    #将before+result+after进行拼接，得到new_expr
    new_expr = "%s%s%s" %(before,result,after)
    #最终返回，递归执行excute(new_expr)
    return excute(new_expr)


#主函数
if __name__ == "__main__":
    #将带计算的表达式中的所包含的空格先去掉，得到没有空格的表达式
    str1 = "4*3-10*(3*2-1*9/3)  +10"
    no_space_str = re.sub('\s*','',str1)

    #执行括号处理函数，取出优先计算或处理的内层表达式
    ret = excute(no_space_str)
    #inp = [ret,0]
    #然后对取出来的内层表达式进行计算：包括先处理乘除后处理加减
    final = compute(ret)
    #打印最终计算的值

    print(final)
#"""