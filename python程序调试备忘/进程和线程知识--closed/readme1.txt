http://www.cnblogs.com/xuyaping/category/1097636.html


https://www.cnblogs.com/xuyaping/p/6825115.html 这个博客中的主要内容摘录如下：

进程和线程的关系：
在传统操作系统中，每个进程有一个地址空间，而且默认就有一个控制线程。
多线程（即多个控制线程）的概念是，在一个进程中存在多个控制线程，控制该进程的地址空间。 
进程只是用来把资源集中到一起（进程只是一个资源单位，或者说资源集合），而线程才是cpu上的执行单位。
进程是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础。或者说
进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动,进程是系统进行资源分配和调度的一个独立单位。
线程则是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位


并发和并行：
无论是并行还是并发，在用户看来都是'同时'运行的，而一个cpu同一时刻只能执行一个任务。

并行：同时运行，只有具备多个cpu才能实现并行。
并发：是伪并行，即看起来是同时运行，单个cpu+多道技术。

 
 

所有现代计算机经常会在同一时间做很多件事，一个用户的PC（无论是单cpu还是多cpu），都可以同时运行多个任务（一个任务可
以理解为一个进程）。当启动系统时，会秘密启动许多进程：

　　　　启动一个进程来杀毒（360软件）

　　　　启动一个进程来看电影（暴风影音）

　　　　启动一个进程来聊天（腾讯QQ）



所有的这些进程都需被管理，于是一个支持多进程的多道程序系统是至关重要的。

 

多道技术：内存中同时存入多道（多个）程序，cpu从一个进程快速切换到另外一个，使每个进程各自运行几十或几百毫秒，
这样，虽然在某一个瞬间，一个cpu只能执行一个任务，但在1秒内，cpu却可以运行多个进程，这就给人产生了并行的错觉，
即伪并发，以此来区分多处理器操作系统的真正硬件并行（多个cpu共享同一个物理内存）。

同步和异步：
同步就是指一个进程在执行某个请求的时候，若该请求需要一段时间才能返回信息，那么这个进程将会一直等待下去，直到收
到返回信息才继续执行下去；异步是指进程不需要一直等下去，而是继续执行下面的操作，不管其他进程的状态。当有消息返
回时系统会通知进程进行处理，这样可以提高执行的效率。
举个例子，打电话时就是同步通信，发短息时就是异步通信。


进程并发的实现
进程并发的实现在于，硬件中断一个正在运行的进程，把此时进程运行的所有状态保存下来，为此，操作系统维护一张表格，即进程表（process table），每个进程占用一个进程表项（这些表项也称为进程控制块）
该表存放了进程状态的重要信息：程序计数器、堆栈指针、内存分配状况、所有打开文件的状态、帐号和调度信息，以及其他在进程由运行态转为就绪态或阻塞态时，必须保存的信息，从而保证该进程在再次启动时，就像从未被中断过一样。


threading模块:
python的多线程：由于GIL，导致同一时刻同一进程中只能有一个线程运行在一个cpu上，而不能有多个线程同时在一个cpu上运行。
实现多线程的并发需要使用threading模块。


Thread类的实例方法
join()
在子线程完成运行之前，这个子线程的父线程将一直被阻塞。 
用例截取
threads = []
 
t1 = threading.Thread(target=Music,args=('FILL ME',))
t2 = threading.Thread(target=Blog,args=('python',))
 
threads.append(t1)
threads.append(t2)
if __name__ == '__main__':
    for t in threads:
        t.start()　　　　#子进程
 
    t1.join()    #添加堵塞　　　　
 
    print ("all over %s" %ctime())　　#主进程

remark: t.join():线程对象t未执行完，会阻塞你的主线程 ，但不会阻塞子线程，子进程没有任何影响。


setDaemon()　　
将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
当我们在程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程就分兵两路，分别运行，那么当主线程完成。想退出时，会检验子线程是否完成。如果子线程未完成，则主线程会等待子线程完成后再退出。
但是有时候我们需要的是只要主线程 完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以 用setDaemon方法了。
用例截取：
threads = []
 
t1 = threading.Thread(target=Music,args=('FILL ME',))
t2 = threading.Thread(target=Blog,args=('python',))
 
threads.append(t1)
threads.append(t2)
 
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)   # 子进程，注意:一定在start之前设置，设置为守护线程，如果主进程结束就立即结束，不用等待子进程结束
        t.start()
 
    print ("all over %s" %ctime())#主进程
	
其它方法：
Thread实例对象的方法
  # isAlive(): 返回线程是否活动的。
  # getName(): 返回线程名。
  # setName(): 设置线程名。
 
threading模块提供的一些方法：
  # threading.currentThread(): 返回当前的线程变量。
  # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
  # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
  
  
  
GIL(全局解释器锁)：
GIL加在cpython解释器中， 其他的python解释器不会有GIL。
Python中的线程是操作系统的原生线程，Python虚拟机使用一个全局解释器锁（Global Interpreter Lock）来互斥线程对Python虚拟机的使用。为了支持多线程机制，一个基本的要求就是需要实现不同线程对共享资源访问的互斥，所以引入了GIL。
GIL：在一个线程拥有了解释器的访问权之后，其他的所有线程都必须等待它释放解释器的访问权，即使这些线程的下一条指令并不会互相影响。
在调用任何Python C API之前，要先获得GIL
GIL缺点：多处理器退化为单处理器；优点：避免大量的加锁解锁操作


GIL的早期设计
Python支持多线程，而解决多线程之间数据完整性和状态同步的最简单方法自然就是加锁。 于是有了GIL这把超级大锁，而当越来越多的代码库开发者接受了这种设定后，他们开始大量依赖这种特性（即默认python内部对象是thread-safe的，无需在实现时考虑额外的内存锁和同步操作）。慢慢的这种实现方式被发现是蛋疼且低效的。但当大家试图去拆分和去除GIL的时候，发现大量库代码开发者已经重度依赖GIL而非常难以去除了。有多难？做个类比，像MySQL这样的“小项目”为了把Buffer Pool Mutex这把大锁拆分成各个小锁也花了从5.5到5.6再到5.7多个大版为期近5年的时间，并且仍在继续。MySQL这个背后有公司支持且有固定开发团队的产品走的如此艰难，那又更何况Python这样核心开发和代码贡献者高度社区化的团队呢？


GIL的影响
无论你启多少个线程，你有多少个cpu, Python在执行一个进程的时候会淡定的在同一时刻只允许一个线程运行。
所以，python是无法利用多核CPU实现多线程的。
这样，python对于计算密集型的任务开多线程的效率甚至不如串行(没有大量切换)，但是，对于IO密集型的任务效率还是有显著提升的。

计算密集型：一直在使用CPU。
IO密集型：存在大量IO操作。
对于IO密集型任务，python的多线程能够节省时间。
对于计算密集型任务，python的多线程并没有用。

执行结果：
单线程：
--->time 7.72044500541687            #python3串行运行结果
    ('time', 12.600000143051147)      #python2串行运行结果
多线程：
--->time 7.737437728881836          #python3中多线程运行时间
    ('time', 20.12600016593933)        #python2中多线程运行时间

从上述单线程和多线程运行结果来看，不管在python2或者3中运行结果均显示多线程比单线程运行时间更长。
因为GIL锁限制你只有一个线程执行，切换进程浪费时间，导致多线程费时间更多。
python3中时间差不明显的原因是因为python3改进了GIL锁，但根本没有解决问题。


解决方案
1.python使用多核，即开多个进程。
方法一：协程+多进程。使用方法简单，效率还可以，一般使用该方法。
　　　　协程yield是你自己写的，是自己定义什么时候切换进程。　　
方法二：IO多路复用。使用复杂，但效率很高。不常用。


2.终极思路：换C模块实现多线程，即换一个python解释器，或者换门编程语言避免GIL锁。


多进程：
用multiprocessing替代Thread multiprocessing库的出现很大程度上是为了弥补thread库因为GIL而低效的缺陷。它完整的复制了
一套thread所提供的接口方便迁移。唯一的不同就是它使用了多进程而不是多线程。每个进程有自己的独立的GIL，因此也不会出现进程之间的GIL争抢。

当然multiprocessing也不是万能良药。它的引入会增加程序实现时线程间数据通讯和同步的困难。就拿计数器来举例子，如果我们要多个线程累加同一个变量，对于thread来说，申明一个global变量，用thread.Lock的context包裹住三行就搞定了。而multiprocessing由于进程之间无法看到对方的数据，只能通过在主线程申明一个Queue，put再get或者用share memory的方法。
这个额外的实现成本使得本来就非常痛苦的多线程程序编码，变得更加痛苦了。
总结：因为GIL的存在，只有IO Bound场景下得多线程会得到较好的性能 - 如果对并行计算性能较高的程序可以考虑把核心部分也成C模块，或者索性用其他语言实现 - GIL在较长一段时间内将会继续存在，但是会不断对其进行改进。
所以对于GIL，既然不能反抗，那就学会去享受它吧！


多线程相关的特性追加介绍：

同步锁 (Lock)

锁通常被用来实现对共享资源的同步访问。为每一个共享资源创建一个Lock对象，当你需要访问该资源时，调用acquire方
来获取锁对象（如果其它线程已经获得了该锁，则当前线程需等待其被释放），待资源访问完后，再调用release方法释放
锁：

上锁的作用是这个线程未结束其他线程无法竞争，只能等，是一个串行，运行时间为0.001s*100次。
但与join()不同的是：join()是整个程序是串行的，上锁的话只有公共数据部分加锁，是串行的，程序其他内容还是并行的。

但上锁后的程序很有可能会出现死锁的情况。


死锁与递归锁

所谓死锁：是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程。


解决方法：
在Python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock。这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。直到一个线程所有的acquire都被release，其他的线程才能获得资源。上面的例子如果使用RLock代替Lock，则不会发生死锁：



同步条件 Event对象
线程之间的通信作用
线程的一个关键特性是每个线程都是独立运行且状态不可预测。如果程序中的其 他线程需要通过判断某个线程的状态来确定自己下一步的操作,这时线程同步问题就 会变得非常棘手。为了解决这些问题,我们需要使用threading库中的Event对象。 对象包含一个可由线程设置的信号标志,它允许线程等待某些事件的发生。在 初始情况下,Event对象中的信号标志被设置为假。如果有线程等待一个Event对象,而这个Event对象的标志为假,那么这个线程将会被一直阻塞直至该标志为真。一个线程如果将一个Event对象的信号标志设置为真,它将唤醒所有等待这个Event对象的线程。如果一个线程等待一个已经被设置为真的Event对象,那么它将忽略这个事件, 继续执行。


Semaphore（信号量）
同时只有n个线程可以获得semaphore,即可以限制最大连接数为n)
Semaphore管理一个内置的计数器，
每当调用acquire()时内置计数器-1；
调用release() 时内置计数器+1；
计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。
实例：(同时只有5个线程可以获得semaphore,即可以限制最大连接数为5)：



multiprocessing模块
由于GIL的存在，Python不存在多线程，要充分利用多核资源，就需要使用多进程。
multiprocessing模块是Python中的多进程管理包。
通过multiprocessing.Process对象来创建一个进程，Process对象与Thread对象的用法相同，也有start(), run(), join()的方法。
multiprocessing与threading一样，调用同一套API。



Process类

构造方法：
Process([group [, target [, name [, args [, kwargs]]]]])
　　group: 线程组，目前还没有实现，库引用中提示必须是None； 
　　target: 要执行的方法； 
　　name: 进程名； 
　　args/kwargs: 要传入方法的参数。

实例方法：
　　is_alive()：返回进程是否在运行。
　　join([timeout])：阻塞当前上下文环境的进程，直到调用此方法的进程终止或到达指定的timeout（可选参数）。
　　start()：进程准备就绪，等待CPU调度
　　run()：strat()调用run方法，如果实例进程时未制定传入target，这star执行t默认run()方法。
　　terminate()：不管任务是否完成，立即停止工作进程

属性：
　　daemon：和线程的setDeamon功能一样
　　name：进程名字。
　　pid：进程号。



进程间通讯:
进程队列Queue

from multiprocessing import Process, Queue  #内置模块

 
def f(q,n):
    #q.put([123, 456, 'hello'])
    q.put(n*n+1)  ##存入队列
    print("son process",id(q))
 
if __name__ == '__main__':
    q = Queue()  #try: q=queue.Queue()
    print("main process",id(q))
 
    for i in range(3):
        p = Process(target=f, args=(q,i))
        p.start()
 
    print(q.get())  读取队列
    print(q.get())
    print(q.get())
 
--------------------------------------------
 
main process 43659448
son process 44854072
son process 45116216
5
2
son process 44985144
1



管道(Pipe)---

The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way). For example:

from multiprocessing import Process, Pipe

def f(conn):
    conn.send([12, {"name":"xyp"}, 'hello'])
    response=conn.recv()
    print("response",response)
    conn.close()
    print("q_ID2:",id(conn))

if __name__ == '__main__':

    parent_conn, child_conn = Pipe()
    print("q_ID1:",id(child_conn))
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    parent_conn.send("儿子你好!")
    p.join()
	
	
	输出：
	q_ID1: 558333151608
[12, {'name': 'xyp'}, 'hello']
response 儿子你好!
q_ID2: 455503603752


Pipe（）返回的两个连接对象代表管道的两端。 每个连接对象都有send()和recv()方法（等等）。 请注意，如果两个进程（或线程）尝试同时读取或写入管道的同一端，管道中的数据可能会损坏。



Manager
Queue和pipe只是实现了数据交互，并没实现数据共享，即一个进程去更改另一个进程的数据。

from multiprocessing import Process, Manager
 
def f(d, l,n):
 
    d[n] = n   
    d["name"] ="xuyaping"
    l.append(n)
 
    #print("l",l)
 
if __name__ == '__main__':
 
    with Manager() as manager:
 
        d = manager.dict()  ##创建一个字典
 
        l = manager.list(range(5))  ##创建一个列表
        p_list = []
 
        for i in range(10):
            p = Process(target=f, args=(d,l,i))
            p.start()
            p_list.append(p)
 
        for res in p_list:
            res.join()
 
        print(d)
        print(l)
 
 
------------------------------------------------
 
{1: 1, 'name': 'xuyaping', 0: 0, 4: 4, 3: 3, 6: 6, 5: 5, 2: 2, 8: 8, 7: 7, 9: 9}
[0, 1, 2, 3, 4, 1, 0, 4, 3, 6, 5, 2, 8, 7, 9]
因为上述代码中多个进程需要修改字典和列表，所以执行的结果是变化的。


进程池Pool  （其它参考信息：https://www.cnblogs.com/freeman818/p/7154089.html）

进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。
from multiprocessing import Pool
import time
 
def foo(args):
 time.sleep(1)
 print(args)
 
if __name__ == '__main__':
 p = Pool(5)   #创建拥有5个进程数量的进程池
 for i in range(6):
     p.apply_async(func=foo, args= (i,))
 
 p.close()   # 等子进程执行完毕后关闭线程池
 # time.sleep(2)
 # p.terminate()  # 立刻关闭线程池
 p.join()
 
 执行结果：
0
2
1
4
3
5
 
 进程池内部维护一个进程序列，当使用时，去进程池中获取一个进程，如果进程池序列中没有可供使用的进程，那么程序就会等待，直到进程池中有可用进程为止。

进程池中有以下几个主要方法：

    apply：从进程池里取一个进程并执行
    apply_async：apply的异步版本
    terminate:立刻关闭线程池
    join：主进程等待所有子进程执行完毕，必须在close或terminate之后
    close：等待所有进程结束后，才关闭线程池


	
yield和协程 
1.由于是单线程，不能再切换
2.不再有任何锁的概念

请参考：
https://blog.csdn.net/sunflowerduidui/article/details/51820067   通过“生产者-消费者模型”理解Python协程和yield关键字
https://www.cnblogs.com/coder2012/p/4990834.html   Python yield与实现


重要： 1.yield 关键字必须要定义在一个函数中，否则会报错；2.一个函数中如果有yield，那这个函数就是一个生成器；



def func():
   for i in range(10):
       yield i
       print("111111")

rr=func()  ##因为func()中有yield,这个函数就是一个生成器，需要使用next()方法来获取函数的值；
print(rr.__next__())
print(rr.__next__())


结果：
0
111111
1

结果说明：注意理解上面的神奇之处，
执行第一个__next__()时，产生第一个值0(yield 0的返回值)，且函数直接返回了，
执行第二个__next__()时，进入func()函数后，从上一次的断点处继续往下执行，即执行 print("111111")；然后进入下一次循环，执行yield 1,返回1

所以，yield完成了一个天生的程序中断，现场保护，下一次从断点处继续执行的特性，这就是神奇之处；


yield 用例2（send的用法）
def func():
   n=0
   while 1:
       n=yield n
       print("111111")

rr=func()
print(rr.__next__())
print(rr.__next__())
print(rr.send(5))

输出：
0
111111
None
111111
5

结果说明：
第一次执行__next__()时，返回yield 0,函数中断；
第二次执行__next__()时，执行print("111111")，进入下一次循环，因为yield n返回的始终是none,所以这次循环时，执行 yield none后中断；
执行send(5)时，先从上次中断的地方继续执行，即执行print("111111")，然后进入下一次循环，需要注意，send(5)会强制把表达式的值设置为5，执行yield 5 后中断。


yield 用例3（send用法追加说明：）
def func():
   n='rr'
   r='b'
   while 1:
       n=yield r
       print("111111")
       print(n)

rr=func()
print(rr.__next__())
print(rr.__next__())
n=5
print(rr.send(n))

执行结果：
b  //第一次获取的结果
111111  //第二次获取的结果
None
b
111111 //第三次获取的结果
5
b

结果说明：
第一次执行 __next__() 时，执行 yield ‘b’,程序中断；
第二次执行 __next__() 时，执行 print("111111") 和（print(n)，其中n为yield r的返回值，一直为None）,下一次循环，执行yield 'b',程序中断；
执行 send(n) 时 ，先把n=5赋值给yield r表达式，即函数中的n=5,然后从上次的断点处开始继续执行：print("111111")，print(n=5),下一次循环，执行yield 'b',程序中断；




1.greenlet
方便手动切换
greenlet机制的主要思想是：生成器函数或者协程函数中的yield语句挂起函数的执行，直到稍后使用next()或send()操作进行恢复为止。可以使用一个调度器循环在一组生成器函数之间协作多个任务。greenlet是python中实现我们所谓的"Coroutine(协程)"的一个基础库.

##下面一段代码的实现机制待继续理解

from greenlet import greenlet
  
def test1():
    print (12)
    gr2.switch()
    print (34)
    gr2.switch()
  
def test2():
    print (56)
    gr1.switch()
    print (78)
  
gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
 
------------------------------
执行结果：
12
56
34
78



2.gevent
自动切换
gevent是第三方库，通过greenlet实现协程
当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。

import gevent
import time
 
def foo():
    print("running in foo")
    gevent.sleep(2)
    print("switch to foo again")
 
def bar():
    print("switch to bar")
    gevent.sleep(5)
    print("switch to bar again")
 
start=time.time()
 
gevent.joinall(
    [gevent.spawn(foo),
    gevent.spawn(bar)]
)
 
print(time.time()-start)
 
--------------------------------------------
 执行结果： （遇到sleep 后自动切换）
running in foo
switch to bar
switch to foo again
switch to bar again
5.010286569595337	


由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成：
##这个用例待继续理解：
from gevent import monkey
monkey.patch_all()
import gevent
from urllib import request
import time
 
def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))
 
start=time.time()
 
gevent.joinall([
        gevent.spawn(f, 'https://itk.org/'),
        gevent.spawn(f, 'https://www.github.com/'),
        gevent.spawn(f, 'https://zhihu.com/'),
])
 
# f('https://itk.org/')
# f('https://www.github.com/')
# f('https://zhihu.com/')
 
print(time.time()-start)
 
------------------------------------------------------------------------
 执行结果：
GET: https://itk.org/
GET: https://www.github.com/
GET: https://zhihu.com/
11785 bytes received from https://zhihu.com/.
12221 bytes received from https://itk.org/.
51166 bytes received from https://www.github.com/.
4.193239688873291




IO模型：
常用模型分为4种：
1.阻塞IO
2.非阻塞IO
3.IO多路复用
4.异步IO

不常用：
驱动信号

阻塞IO和非阻塞IO：
阻塞IO：进程不能做其他的事情
非阻塞IO：等待数据无阻塞

同步IO和异步IO：
有阻塞就是同步IO，所以，
阻塞IO、非阻塞IO、IO多路复用是同步IO
异步IO是异步IO




阻塞IO

全程阻塞，不管是等待数据或者是从内核态拷贝数据到用户态
系统调用两个阶段：
wait for data 阻塞
copy data 阻塞


非阻塞IO
setblocking(False) 设置阻塞状态为非阻塞
固定时间循环发起系统调用，请求不到做自己的事情，等待下次请求，内核态拷贝数据到用户态需要等待
系统调用两个阶段：
wait for data 非阻塞
copy data 阻塞

优点：等待数据无阻塞
缺点：系统调用发送太多；数据不是即时接收的


IO多路复用
全程阻塞，监听多个链接
系统调用select完成wait for data工作
系统调用两个阶段：
wait for data 阻塞
copy data 阻塞
特点：监听多个文件描述符，实现并发

r,w,e = select.select([sock,],[],[]) #等待链接
for obj in r:
    conn,addr = obj.accept()


	
inputs = [sock,]
r,w,e = select.select(inputs,[],[]) #inputs监听有变化的套接字 inputs=[sock,conn1,conn2,...]
for obj in r: #第一次[cock,] 第二次[conn1,]
    if obj == sock
        conn,addr = obj.accept()
        inputs.append(conn) #inputs=[sock,conn1,conn2]
    else:
        data = obj.recv(1024)


对于文件描述符（socket套接字）：
1.每一个套接字对象的本质就是一个非零整数，不会变（fb=4）
2.收发数据的时候，对于接收端而言，数据先到内核空间，然后copy到用户空间，同时内核空间的数据被清空
3.根据TCP协议，当发送端接收到接收端的确认信息后，清空内核空间的数据，否则不清空


异步IO
全程无阻塞，实现复杂





IO模型 - IO多路复用实现机制
IO模型 - selectors模块
threading模块 - 队列queue


IO多路复用实现机制
IO多路复用机制：就是单个process可以同时处理多个网络连接的IO，基本原理就是通过select／epoll函数不断轮询所负责的所有socket，当某个socket有数据到达，就通知用户进程。
不同的操作系统提供的函数不同：
    windows系统： select
    linux系统： select、poll、epoll
	
	
	
简单介绍select、poll、epoll三者的特点：

select的缺点有以下三点，会导致效率下降：
    1.每次调用select都要将所有的fd（文件描述符），copy到你的内核空间
    2.遍历所有的fd，是否有数据访问
    3.最大连接数（1024），超出链接不再监听
     
poll：
    与select一样，只是最大连接数没有限制
 
epoll不同于select和poll只有一个函数，epoll通过三个函数实现实现轮询socket：
    1.第一个函数：创建epoll句柄：将所有的fd（文件描述符），copy到你的内核空间，只copy一次
    2.回调函数：为所有fd绑定一个回调函数，一旦有数据访问，触发回调函数，回调函数将fd放入一个链表中（回调函数：某一个函数或者某一个动作，成功完成之后，会触发的函数）
    3.第三个函数：判断链表是否为空
    epoll最大连接数没有上线
	
	
selectors模块
selectors基于select模块实现IO多路复用，调用语句selectors.DefaultSelector()，特点是根据平台自动选择最佳IO多路复用机制，调用顺序：epoll > poll > select
用例（待follow）：

import selectors
import socket
 
def accept(sock, mask):
    conn, addr = sock.accept()
    sel.register(conn, selectors.EVENT_READ, read)  # 将conn和read函数注册到一起，当conn有变化时执行read函数
 
 
def read(conn, mask):
    try:
        data = conn.recv(1000)
        print(data.decode('utf8'))
        inputs = input('>>:').strip()
        conn.send(inputs.encode('utf8'))
    except Exception:
        sel.unregister(conn)
        conn.close()
 
 
sock = socket.socket()
sock.bind(('127.0.0.1', 8080))
sock.listen(100)
sock.setblocking(False)  # 设置为非阻塞IO
 
sel = selectors.DefaultSelector()  # 根据平台自动选择最佳IO多路复用机制
sel.register(sock, selectors.EVENT_READ, accept)  # 将sock和accept函数注册到一起，当sock有变化时执行accept函数
 
while True:
    events = sel.select()  # 监听  [(key1,mask1),(key2),(mask2)]
    for key, mask in events:
        func = key.data  # 1 key.data就是accept   # 2 key.data就是read
        obj = key.fileobj  # 1 key.fileobj就是sock   # 2 key.fileobj就是conn
        func(obj, mask)  # 1 accept(sock,mask)   # 2read(conn,mask)
	
队列queue
队列与线程（和进程）有关，保证多线程信息交换的安全。
队列是一种数据类型（数据结构），可用于存放数据  创建队列语法queue.Queue()，默认是先进先出（FIFO）。
队列的优点：保证线程安全

get与put方法
import queue
 
q = queue.Queue() #创建队列对象q
q.put(123) #将123放入队列中
q.put('hello')
q.get() #将第一个值从队列中取出



join和task_done方法
join()阻塞进程，直到所有任务都完成,需要配合另一个方法task_done()。
task_done() 表示某个任务完成。每一条get语句后需要一条task_done。

import queue
 
q = queue.Queue(5)
q.put(10)
q.put(20)
print(q.get())
q.task_done()
print(q.get())
q.task_done()
 
q.join()
 
print("ending!")


其他模式
先进后出：queue.LifoQueue()后进先出（LIFO）

优先级：queue.PriorityQueue()优先级高先出
q.put([1,‘123’]) #1为有限等级，越小越优先




生产者消费者模型

在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。

这就像，在餐厅，厨师做好菜，不需要直接和客户交流，而是交给前台，而客户去饭菜也不需要不找厨师，直接去前台领取即可，这也是一个解耦的过程。


import time,random
import queue,threading
 
q = queue.Queue()
 
def Producer(name):
  count = 0
  while count <10:
    print("making........")
    time.sleep(random.randrange(3))
    q.put(count)
    print('Producer %s has produced %s baozi..' %(name, count))
    count +=1
    #q.task_done()
    #q.join()
    print("ok......")
def Consumer(name):
  count = 0
  while count <10:
    time.sleep(random.randrange(4))
    if not q.empty():
        data = q.get()
        #q.task_done()
        #q.join()
        print(data)
        print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
    else:
        print("-----no baozi anymore----")
    count +=1
 
p1 = threading.Thread(target=Producer, args=('A',))
c1 = threading.Thread(target=Consumer, args=('B',))
# c2 = threading.Thread(target=Consumer, args=('C',))
# c3 = threading.Thread(target=Consumer, args=('D',))
p1.start()
c1.start()
# c2.start()
# c3.start()
 
-----------------------------------------------------------------------------------
 
making........
Producer A has produced 0 baozi..
ok......
making........
Producer A has produced 1 baozi..
ok......
making........
Producer A has produced 2 baozi..
ok......
making........
0
Consumer B has eat 0 baozi...
Producer A has produced 3 baozi..
ok......
making........
Producer A has produced 4 baozi..
ok......
making........
Producer A has produced 5 baozi..
1
Consumer B has eat 1 baozi...
ok......
making........
2
Consumer B has eat 2 baozi...
3
Consumer B has eat 3 baozi...
4
Consumer B has eat 4 baozi...
5
Consumer B has eat 5 baozi...
Producer A has produced 6 baozi..
ok......
making........
6
Consumer B has eat 6 baozi...
Producer A has produced 7 baozi..
ok......
making........
Producer A has produced 8 baozi..
ok......
making........
Producer A has produced 9 baozi..
ok......
7
Consumer B has eat 7 baozi...
8
Consumer B has eat 8 baozi...
9
Consumer B has eat 9 baozi...



总结：

进程：最小的资源管理单位（盛放线程的容器）

线程：最小的执行单位

串行、并行、并发

cpython因为存在GIL导致，同一时刻，同一进程只能有一个线程执行

关于daemon：程序直到不存在非守护线程时退出

同步锁：由于多线程处理公共数据

递归锁

event：一个对象，让多个进程间通信		



应用总结：
1.IO模型中， 主要应用的是IO多路复用 模型，实现的python模块包括： select, poll, epoll,selectors
2.threading中关注 queue模块的应用和 应用实例（生产者和消费者模型）
3.yield和协程
1）单线程模式下，使用yield实现类似“多协程”的工作模型；
2）greenlet是python中实现我们所谓的"Coroutine(协程)"的一个基础库，可以使用一个调度器循环在一组生成器函数之间协作多个任务，为手动切换；
3）gevent为自动切换，是第三方库，通过greenlet实现协程，当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行
4. multiprocessing模块：进程间通讯 （进程队列Queue、管道(pipe)、manager、进程池）
5.多线程，数据同步相关：
同步锁 (Lock)、死锁与递归锁、同步条件 Event对象、Semaphore（信号量）
6.threading模块：
线程对象的创建，join()方法，setDaemon()方法，GIL(全局解释器锁)
7.因为GIL的存在，python中在使用cpython时无法实现真正的多线程解决方案如下：
python使用多核，即开多个进程。
方法一：协程+多进程。使用方法简单，效率还可以，一般使用该方法。 （multiprocssing ,yield）
　　　　协程yield是你自己写的，是自己定义什么时候切换进程。　　
方法二：IO多路复用。使用复杂，但效率很高。不常用。 (select,poll,epoll,selectors)


