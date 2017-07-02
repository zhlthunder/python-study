#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# python基础-实现购物车程序@@网上

# 需求：
#
#       1. 启动程序后，用户通过账号密码登录，然后打印商品列表。
#
#       2. 允许用户根据商品编号购买商品。
#
#       3. 用户选择商品后，检测余额是否足够，够就直接扣款，不够就提醒充值。
#
#       4. 可随时退出，退出时，打印已购买的商品和余额。

# 1 #!/usr/bin/env python
#   2 # -*- coding: utf-8 -*-
#   3
#   4 count = 0  # 计数器
#   5 username = "aaa"  # 登录用户名
#   6 userpassword = "asd"  # 登录密码
#   7
#   8
#   9 #创建黑名单表
#  10 f=open('name.txt','a')
#  11 f.close()
#  12 #创建用户余额存放地址
#  13 f = open('salary.txt', 'a')
#  14 f.close()
#  15
#  16 f = open("name.txt", "r")
#  17 file_list = f.readlines()
#  18 f.close()
#  19
#  20 lock = []
#  21 name = input("登录用户名:")
#  22
#  23 # 判断用户是否在黑名单
#  24 for i in file_list:
#  25     line = i.strip("\n")
#  26     lock.append(line)
#  27 if name in lock:
#  28     print("您的账号已锁定，请联系管理员。")
#  29     exit()
#  30 else:
#  31     # 如果用户没有在黑名单，判断用户是否存在。
#  32     if name == username:
#  33         # 如果密码连续输错三次，锁定账号。
#  34         while count < 3:
#  35             password = input("登录密码：")
#  36             if name == username and password == userpassword:
#  37                 print("\033[92mWelcome to Mr.wang mall\033[0m")
#  38                 break
#  39             else:
#  40                 print("账号密码不匹配")
#  41                 count += 1
#  42                 if count ==3:
#  43                     print("对不起，您的账号连续输错三次账号已锁定，请联系管理员。")
#  44                     f = open("aaa.txt", "w+")
#  45                     li = ['%s' % username]
#  46                     f.writelines(li)
#  47                     f.close()
#  48                     exit()
#  49         else:
#  50             print("对不起，您的账号连续输错三次账号已锁定，请联系管理员。")
#  51             f = open("name.txt", "w+")
#  52             li = ['%s' % username]
#  53             f.writelines(li)
#  54             f.close()
#  55     else:
#  56         print("用户名不存在，请输入正确的用户名。")
#  57         exit()
#  58
#  59 #用户购买商品列表
#  60 shopping_list = []
#  61 #用户购买物品名称存放列表
#  62 goods = []
#  63 #用户购买物品价格存放列表
#  64 price = []
#  65 #商品价格列表
#  66 product_list = [
#  67     ['Iphone',5800],
#  68     ['Mac Pro',9800],
#  69     ['Bike',800],
#  70     ['Watch',10600],
#  71     ['Coffee',31],
#  72     ['Alex Python',120],
#  73 ]
#  74
#  75 #读取用户的余额，如果首次登陆余额为0
#  76 f1 = open("salary.txt", "r")
#  77 file_list = f1.readlines()
#  78 f1.close()
#  79 salary = []
#  80 if file_list:
#  81     print("")
#  82 else:
#  83     f2 = open("salary.txt", "w")
#  84     f2.write("0")
#  85     f2.close()
#  86 f1 = open("salary.txt", "r")
#  87 fil_list = f1.readlines()
#  88 f1.close()
#  89 for i in fil_list:
#  90     lin = i.strip("\n")
#  91     salary.append(lin)
#  92
#  93 salary = int(salary[0])
#  94
#  95 #商品购买循环
#  96 while True:
#  97                          #循环打印商品目录
#  98                          for j in range(1):
#  99                              print("----shopping list----")
# 100                              for i,ele in enumerate(product_list):
# 101                               print (i,ele[0],ele[1])
# 102                          var = (input("\033[94m请输入你要买的商品序列号(充值：t 余额：b 购买：y 退出：q)：\033[0m"))
# 103                          #判断用户输入的是否为商品序号是否为数字
# 104                          if var.isdigit():
# 105                              var = int(var)
# 106                              #判断用户输入的商品序号是否在范围内
# 107                              if var >=0 and len(product_list) > var:
# 108                                    p = product_list[var]
# 109                                    #判断用户的余额是否足够买想要的商品
# 110                                    if p[1] <= salary:
# 111                                        shopping_list.append(p)
# 112                                        goods.append(p[0])
# 113                                        price.append(p[1])
# 114                                        salary = salary -p[1]
# 115                                        print("\033[94m您购买\033[0m\033[95m%s\033[0m\033[94m已加入购物车后，您的余额还有\033[0m\033[95m%s\033[0m"%(p[0],salary))
# 116                                    else:
# 117                                        print("\033[91m您的余额不足(余额：%s)，请充值后购买(充值：t)。\033[0m"%salary)
# 118                              else:
# 119                                  print("\033[91m没有找到您想要的商品,请重新输入商品编号。\033[0m")
# 120                                  continue
# 121                          elif var == "t":
# 122                             num1 = input("\033[94m请输入充值金额：\033[0m")
# 123                             if num1.isdigit():
# 124                               num1 = int(num1)
# 125                               salary = salary + num1
# 126                               print("您现在的总余额是：",salary)
# 127                             else:
# 128                               print("\033[91m请输入正确的充值金额\033[0m")
# 129                               num1 = input("\033[94m请输入充值金额：\033[0m")
# 130                               continue
# 131                          elif var == "q":
# 132                              exit()
# 133                          elif var == "b":
# 134                              print("\033[91m您当前余额为：%s\033[0m"%salary)
# 135                          elif  var == "y":
# 136                              print("--------shopping list------")
# 137                              goods.sort()
# 138                              s = set(goods)
# 139                              for item in s:
# 140                                  print (" %s     x   %d"%(item,goods.count(item)))
# 141                              sum = 0
# 142                              for j in price:
# 143                                  sum = sum +j
# 144                              print("您总计消费：\033[95m % s\033[0m余额:\033[95m % s\033[0m"%(sum,salary))
# 145                              print("\033[94m欢迎您下次购物\033[0m")
# 146                              f = open("salary.txt", "w+")
# 147                              la = ['%s' %salary]
#                               f.writelines(la)
#                               f.close()
#                               exit()
#                           else:
#                              print("\033[91m请输入正确的商品编号。\033[0m")
#                              continue