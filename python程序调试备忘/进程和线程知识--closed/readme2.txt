remark: The Queue module has been renamed to queue in Python 3. The 2to3 tool will automatically adapt imports when converting your sources to Python 3.


学习blog:
http://www.cnblogs.com/alex3714/articles/5230609.html

index:
进程、与线程区别
python GIL全局解释器锁
线程

    语法
    join&将线程变为守护进程
    线程锁之Lock\Rlock\信号量
    Event事件　
    queue队列
    生产者消费者模型 

进程

    语法
    进程间通讯
    进程池　　
	


什么是进程：
程序并不能单独运行，只有将程序装载到内存中，系统为它分配资源才能运行，而这种执行的程序就称之为进程。程序和进程的区别就在于：程序是指令的集合，它是进程运行的静态描述文本；进程是程序的一次执行活动，属于动态概念。
在多道编程中，我们允许多个程序同时加载到内存中，在操作系统的调度下，可以实现并发地执行。就是这样的设计，大大提高了CPU的利用率。进程的出现让每个用户感觉到自己独享CPU，因此，进程就是为了在CPU上实现多道编程而提出的。


有了进程为什么还要线程？

进程有很多优点，它提供了多道编程，让我们感觉我们每个人都拥有自己的CPU和其他资源，可以提高计算机的利用率。很多人就不理解了，既然进程这么优秀，为什么还要线程呢？其实，仔细观察就会发现进程还是有很多缺陷的，主要体现在两点上：
进程只能在一个时间干一件事，如果想同时干两件事或多件事，进程就无能为力了。
进程在执行的过程中如果阻塞，例如等待输入，整个进程就会挂起，即使进程中有些工作不依赖于输入的数据，也将无法执行。

例如，我们在使用qq聊天， qq做为一个独立进程如果同一时间只能干一件事，那他如何实现在同一时刻 即能监听键盘输入、又能监听其它人给你发的消息、同时还能把别人发的消息显示在屏幕上呢？你会说，操作系统不是有分时么？但我的亲，分时是指在不同进程间的分时呀， 即操作系统处理一会你的qq任务，又切换到word文档任务上了，每个cpu时间片分给你的qq程序时，你的qq还是只能同时干一件事呀。

再直白一点， 一个操作系统就像是一个工厂，工厂里面有很多个生产车间，不同的车间生产不同的产品，每个车间就相当于一个进程，且你的工厂又穷，供电不足，同一时间只能给一个车间供电，为了能让所有车间都能同时生产，你的工厂的电工只能给不同的车间分时供电，但是轮到你的qq车间时，发现只有一个干活的工人，结果生产效率极低，为了解决这个问题，应该怎么办呢？。。。。没错，你肯定想到了，就是多加几个工人，让几个人工人并行工作，这每个工人，就是线程！

什么是线程(thread)？
线程是操作系统能够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务


无论你启多少个线程，你有多少个cpu, Python在执行的时候会淡定的在同一时刻只允许一个线程运行；
首先需要明确的一点是GIL并不是Python的特性，它是在实现Python解析器(CPython)时所引入的一个概念；


Python threading模块：
1）直接调用与继承式调用
2）Join & Daemon
3）线程锁(互斥锁Mutex)
一个进程下可以启动多个线程，多个线程共享父进程的内存空间，也就意味着每个线程可以访问同一份数据，就可能发生数据一致性的问题，所以就需要对多线程都要访问的数据进行加锁。

GIL VS Lock
机智的同学可能会问到这个问题，就是既然你之前说过了，Python已经有一个GIL来保证同一时间只能有一个线程来执行了，为什么这里还需要lock? 注意啦，这里的lock是用户级的lock,跟那个GIL没关系，具体我们通过下图来看一下+配合我现场讲给大家，就明白了。

那你又问了， 既然用户程序已经自己有锁了，那为什么Cpython还需要GIL呢？加入GIL主要的原因是为了降低程序的开发的复杂度，比如现在的你写python不需要关心内存回收的问题，因为Python解释器帮你自动定期进行内存回收，你可以理解为python解释器里有一个独立的线程，每过一段时间它起wake up做一次全局轮询看看哪些内存数据是可以被清空的，此时你自己的程序 里的线程和 py解释器自己的线程是并发运行的，假设你的线程删除了一个变量，py解释器的垃圾回收线程在清空这个变量的过程中的clearing时刻，可能一个其它线程正好又重新给这个还没来及得清空的内存空间赋值了，结果就有可能新赋值的数据被删除了，为了解决类似的问题，python解释器简单粗暴的加了锁，即当一个线程运行时，其它人都不能动，这样就解决了上述的问题，  这可以说是Python早期版本的遗留问题。


RLock（递归锁）:说白了就是在一个大锁中还要再包含子锁
Semaphore(信号量):互斥锁 同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据 ，比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去。

Timer :This class represents an action that should be run only after a certain amount of time has passed 
Timers are started, as with threads, by calling their start() method. The timer can be stopped (before its action has begun) by calling thecancel() method. The interval the timer will wait before executing its action may not be exactly the same as the interval specified by the user.


Events:通过Event来实现两个或多个线程间的交互，下面是一个红绿灯的例子，即起动一个线程做交通指挥灯，生成几个线程做车辆，车辆行驶按红灯停，绿灯行的规则。

queue队列 :queue is especially useful in threaded programming when information must be exchanged safely between multiple threads.
class queue.Queue(maxsize=0) #先入先出

class queue.LifoQueue(maxsize=0) #last in fisrt out 
class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列

    Constructor for a priority queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.

    The lowest valued entries are retrieved first (the lowest valued entry is the one returned by sorted(list(entries))[0]). A typical pattern for entries is a tuple in the form: (priority_number, data).

exception queue.Empty

    Exception raised when non-blocking get() (or get_nowait()) is called on a Queue object which is empty.

exception queue.Full

    Exception raised when non-blocking put() (or put_nowait()) is called on a Queue object which is full.

Queue.qsize()

Queue.empty() #return True if empty  

Queue.full() # return True if full 

Queue.put(item, block=True, timeout=None)

    Put item into the queue. If optional args block is true and timeout is None (the default), block if necessary until a free slot is available. If timeout is a positive number, it blocks at most timeout seconds and raises the Full exception if no free slot was available within that time. Otherwise (block is false), put an item on the queue if a free slot is immediately available, else raise the Full exception (timeout is ignored in that case).

Queue.put_nowait(item)

    Equivalent to put(item, False).

Queue.get(block=True, timeout=None)

    Remove and return an item from the queue. If optional args block is true and timeout is None (the default), block if necessary until an item is available. If timeout is a positive number, it blocks at most timeout seconds and raises the Empty exception if no item was available within that time. Otherwise (block is false), return an item if one is immediately available, else raise the Empty exception (timeout is ignored in that case).

Queue.get_nowait()

    Equivalent to get(False).

Two methods are offered to support tracking whether enqueued tasks have been fully processed by daemon consumer threads.

Queue.task_done()

    Indicate that a formerly enqueued task is complete. Used by queue consumer threads. For each get() used to fetch a task, a subsequent call to task_done() tells the queue that the processing on the task is complete.

    If a join() is currently blocking, it will resume when all items have been processed (meaning that a task_done() call was received for every item that had been put() into the queue).

    Raises a ValueError if called more times than there were items placed in the queue.

Queue.join() block直到queue被消费完毕


生产者消费者模型:
在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。
为什么要使用生产者和消费者模式

在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

什么是生产者消费者模式

生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。


多进程multiprocessing:
进程间通讯　
不同进程间内存是不共享的，要想实现两个进程间的数据交换，可以用以下方法：
Queues: 使用方法跟threading里的queue差不多
Pipes:The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way).
Managers:A manager object returned by Manager() controls a server process which holds Python objects and allows other processes to manipulate them using proxies.

进程池:
进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。


	
	
	