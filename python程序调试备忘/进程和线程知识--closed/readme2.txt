remark: The Queue module has been renamed to queue in Python 3. The 2to3 tool will automatically adapt imports when converting your sources to Python 3.


ѧϰblog:
http://www.cnblogs.com/alex3714/articles/5230609.html

index:
���̡����߳�����
python GILȫ�ֽ�������
�߳�

    �﷨
    join&���̱߳�Ϊ�ػ�����
    �߳���֮Lock\Rlock\�ź���
    Event�¼���
    queue����
    ������������ģ�� 

����

    �﷨
    ���̼�ͨѶ
    ���̳ء���
	


ʲô�ǽ��̣�
���򲢲��ܵ������У�ֻ�н�����װ�ص��ڴ��У�ϵͳΪ��������Դ�������У�������ִ�еĳ���ͳ�֮Ϊ���̡�����ͽ��̵���������ڣ�������ָ��ļ��ϣ����ǽ������еľ�̬�����ı��������ǳ����һ��ִ�л�����ڶ�̬���
�ڶ������У���������������ͬʱ���ص��ڴ��У��ڲ���ϵͳ�ĵ����£�����ʵ�ֲ�����ִ�С�������������ƣ���������CPU�������ʡ����̵ĳ�����ÿ���û��о����Լ�����CPU����ˣ����̾���Ϊ����CPU��ʵ�ֶ����̶�����ġ�


���˽���Ϊʲô��Ҫ�̣߳�

�����кܶ��ŵ㣬���ṩ�˶����̣������Ǹо�����ÿ���˶�ӵ���Լ���CPU��������Դ��������߼�����������ʡ��ܶ��˾Ͳ�����ˣ���Ȼ������ô���㣬Ϊʲô��Ҫ�߳��أ���ʵ����ϸ�۲�ͻᷢ�ֽ��̻����кܶ�ȱ�ݵģ���Ҫ�����������ϣ�
����ֻ����һ��ʱ���һ���£������ͬʱ�������»����£����̾�����Ϊ���ˡ�
������ִ�еĹ������������������ȴ����룬�������̾ͻ���𣬼�ʹ��������Щ��������������������ݣ�Ҳ���޷�ִ�С�

���磬������ʹ��qq���죬 qq��Ϊһ�������������ͬһʱ��ֻ�ܸ�һ���£��������ʵ����ͬһʱ�� ���ܼ����������롢���ܼ��������˸��㷢����Ϣ��ͬʱ���ܰѱ��˷�����Ϣ��ʾ����Ļ���أ����˵������ϵͳ�����з�ʱô�����ҵ��ף���ʱ��ָ�ڲ�ͬ���̼�ķ�ʱѽ�� ������ϵͳ����һ�����qq�������л���word�ĵ��������ˣ�ÿ��cpuʱ��Ƭ�ָ����qq����ʱ�����qq����ֻ��ͬʱ��һ����ѽ��

��ֱ��һ�㣬 һ������ϵͳ������һ�����������������кܶ���������䣬��ͬ�ĳ���������ͬ�Ĳ�Ʒ��ÿ��������൱��һ�����̣�����Ĺ���������粻�㣬ͬһʱ��ֻ�ܸ�һ�����乩�磬Ϊ���������г��䶼��ͬʱ��������Ĺ����ĵ繤ֻ�ܸ���ͬ�ĳ����ʱ���磬�����ֵ����qq����ʱ������ֻ��һ���ɻ�Ĺ��ˣ��������Ч�ʼ��ͣ�Ϊ�˽��������⣬Ӧ����ô���أ���������û����϶��뵽�ˣ����Ƕ�Ӽ������ˣ��ü����˹��˲��й�������ÿ�����ˣ������̣߳�

ʲô���߳�(thread)��
�߳��ǲ���ϵͳ�ܹ�����������ȵ���С��λ�����������ڽ���֮�У��ǽ����е�ʵ��������λ��һ���߳�ָ���ǽ�����һ����һ˳��Ŀ�������һ�������п��Բ�������̣߳�ÿ���̲߳���ִ�в�ͬ������


�����������ٸ��̣߳����ж��ٸ�cpu, Python��ִ�е�ʱ��ᵭ������ͬһʱ��ֻ����һ���߳����У�
������Ҫ��ȷ��һ����GIL������Python�����ԣ�������ʵ��Python������(CPython)ʱ�������һ�����


Python threadingģ�飺
1��ֱ�ӵ�����̳�ʽ����
2��Join & Daemon
3���߳���(������Mutex)
һ�������¿�����������̣߳�����̹߳������̵��ڴ�ռ䣬Ҳ����ζ��ÿ���߳̿��Է���ͬһ�����ݣ��Ϳ��ܷ�������һ���Ե����⣬���Ծ���Ҫ�Զ��̶߳�Ҫ���ʵ����ݽ��м�����

GIL VS Lock
���ǵ�ͬѧ���ܻ��ʵ�������⣬���Ǽ�Ȼ��֮ǰ˵���ˣ�Python�Ѿ���һ��GIL����֤ͬһʱ��ֻ����һ���߳���ִ���ˣ�Ϊʲô���ﻹ��Ҫlock? ע�����������lock���û�����lock,���Ǹ�GILû��ϵ����������ͨ����ͼ����һ��+������ֳ�������ң��������ˡ�

���������ˣ� ��Ȼ�û������Ѿ��Լ������ˣ���ΪʲôCpython����ҪGIL�أ�����GIL��Ҫ��ԭ����Ϊ�˽��ͳ���Ŀ����ĸ��Ӷȣ��������ڵ���дpython����Ҫ�����ڴ���յ����⣬��ΪPython�����������Զ����ڽ����ڴ���գ���������Ϊpython����������һ���������̣߳�ÿ��һ��ʱ������wake up��һ��ȫ����ѯ������Щ�ڴ������ǿ��Ա���յģ���ʱ���Լ��ĳ��� ����̺߳� py�������Լ����߳��ǲ������еģ���������߳�ɾ����һ��������py�����������������߳��������������Ĺ����е�clearingʱ�̣�����һ�������߳����������¸������û��������յ��ڴ�ռ丳ֵ�ˣ�������п����¸�ֵ�����ݱ�ɾ���ˣ�Ϊ�˽�����Ƶ����⣬python�������򵥴ֱ��ļ�����������һ���߳�����ʱ�������˶����ܶ��������ͽ�������������⣬  �����˵��Python���ڰ汾���������⡣


RLock���ݹ�����:˵���˾�����һ�������л�Ҫ�ٰ�������
Semaphore(�ź���):������ ͬʱֻ����һ���̸߳������ݣ���Semaphore��ͬʱ����һ���������̸߳������� �����������3���ӣ������ֻ����3�����ϲ������������ֻ�ܵ��������˳����˲����ٽ�ȥ��

Timer :This class represents an action that should be run only after a certain amount of time has passed 
Timers are started, as with threads, by calling their start() method. The timer can be stopped (before its action has begun) by calling thecancel() method. The interval the timer will wait before executing its action may not be exactly the same as the interval specified by the user.


Events:ͨ��Event��ʵ�����������̼߳�Ľ�����������һ�����̵Ƶ����ӣ�����һ���߳�����ָͨ�ӵƣ����ɼ����߳���������������ʻ�����ͣ���̵��еĹ���

queue���� :queue is especially useful in threaded programming when information must be exchanged safely between multiple threads.
class queue.Queue(maxsize=0) #�����ȳ�

class queue.LifoQueue(maxsize=0) #last in fisrt out 
class queue.PriorityQueue(maxsize=0) #�洢����ʱ���������ȼ��Ķ���

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

Queue.join() blockֱ��queue���������


������������ģ��:
�ڲ��������ʹ�������ߺ�������ģʽ�ܹ������������������⡣��ģʽͨ��ƽ�������̺߳������̵߳Ĺ�����������߳�������崦�����ݵ��ٶȡ�
ΪʲôҪʹ�������ߺ�������ģʽ

���߳�����������߾����������ݵ��̣߳������߾����������ݵ��̡߳��ڶ��߳̿������У���������ߴ����ٶȺܿ죬�������ߴ����ٶȺ�������ô�����߾ͱ���ȴ������ߴ����꣬���ܼ����������ݡ�ͬ���ĵ�����������ߵĴ����������������ߣ���ô�����߾ͱ���ȴ������ߡ�Ϊ�˽������������������������ߺ�������ģʽ��

ʲô��������������ģʽ

������������ģʽ��ͨ��һ����������������ߺ������ߵ�ǿ������⡣�����ߺ������߱˴�֮�䲻ֱ��ͨѶ����ͨ����������������ͨѶ����������������������֮���õȴ������ߴ���ֱ���Ӹ��������У������߲���������Ҫ���ݣ�����ֱ�Ӵ�����������ȡ���������о��൱��һ����������ƽ���������ߺ������ߵĴ���������


�����multiprocessing:
���̼�ͨѶ��
��ͬ���̼��ڴ��ǲ�����ģ�Ҫ��ʵ���������̼�����ݽ��������������·�����
Queues: ʹ�÷�����threading���queue���
Pipes:The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way).
Managers:A manager object returned by Manager() controls a server process which holds Python objects and allows other processes to manipulate them using proxies.

���̳�:
���̳��ڲ�ά��һ���������У���ʹ��ʱ����ȥ���̳��л�ȡһ�����̣�������̳�������û�пɹ�ʹ�õĽ����̣���ô����ͻ�ȴ���ֱ�����̳����п��ý���Ϊֹ��


	
	
	