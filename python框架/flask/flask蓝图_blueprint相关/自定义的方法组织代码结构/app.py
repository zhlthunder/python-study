#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import sys,os
sys.path.append(os.path.abspath(__file__))

from views import app


if __name__ == '__main__':
    app.run()

##说明： 直接运行时，发现所有的URL都找不到。
#因为按照目前的代码执行流程，路由关系没有映射之前，监护进程已经运行了
##解决办法，需要在views.__init__导入视图中的其他py文件；