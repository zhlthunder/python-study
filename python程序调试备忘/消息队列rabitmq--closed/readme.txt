参考： https://blog.csdn.net/fgf00/article/details/52872730
python(十一)上：RabbitMQ 使用详细介绍 

目录

上节回顾
一、RabbitMQ 消息队列介绍
二、RabbitMQ基本示例.
　　1、Rabbitmq 安装
　　2、基本示例
　　3、RabbitMQ 消息分发轮询
三、RabbitMQ 消息持久化（durable、properties）
　　1、RabbitMQ 相关命令
　　2、消息持久化
四、RabbitMQ 广播模式（exchange）
　　1、fanout 纯广播、all
　　2、direct 有选择的接收消息
　　3、topic 更细致的过滤
　　4、RabbitMQ RPC 实现（Remote procedure call）


上节回顾

主要讲了协程、进程、IO多路复用。
协程和IO多路复用都是单线程的。

epoll  在linux下通过这个模块libevent.so实现
gevent  在底层也是用了libevent.so

gevent可以理解为一个更上层的封装。
使用select或者selectors，每接收或发送数据一次都要select一次

twisted异步网络框架，强大又庞大，不支持python3 (代码量python中排top3)。几乎把所有的网络服务都重写了一遍。


一、RabbitMQ 消息队列介绍
RabbitMQ也是消息队列，那RabbitMQ和之前python的Queue有什么区别么？

python中的 消息队列:
    线程 queue（同一进程下线程之间进行交互）
    进程 Queue（父子进程进行交互 或者 同属于同一进程下的多个子进程进行交互）
如果是两个完全独立的python程序，也是不能用上面两个queue进行交互的，或者和其他语言交互有哪些实现方式呢。 	
【Disk、Socket、其他中间件】这里中间件不仅可以支持两个程序之间交互，可以支持多个程序，可以维护好多个程序的队列。	
像这种公共的中间件有好多成熟的产品：
RabbitMQ
ZeroMQ
ActiveMQ
……

RabbitMQ：erlang语言 开发的。
Python中连接RabbitMQ的模块：pika 、Celery(分布式任务队列) 、haigha 

可以维护很多的队列
RabbitMQ 教程官网：http://www.rabbitmq.com/getstarted.html

几个概念说明：
Broker：简单来说就是消息队列服务器实体。
Exchange：消息交换机，它指定消息按什么规则，路由到哪个队列。
Queue：消息队列载体，每个消息都会被投入到一个或多个队列。
Binding：绑定，它的作用就是把exchange和queue按照路由规则绑定起来。
Routing Key：路由关键字，exchange根据这个关键字进行消息投递。
vhost：虚拟主机，一个broker里可以开设多个vhost，用作不同用户的权限分离。
producer：消息生产者，就是投递消息的程序。
consumer：消息消费者，就是接受消息的程序。
channel：消息通道，在客户端的每个连接里，可建立多个channel，每个channel代表一个会话任务


二、RabbitMQ基本示例.
1.rabbitmq 安装： 请参考 install_follow.txt

2、基本示例
发送端 producer

import pika
# 建立一个实例
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost',5672)  # 默认端口5672，可不写
    )
# 声明一个管道，在管道里发消息
channel = connection.channel()
# 在管道里声明queue
channel.queue_declare(queue='hello')
# RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',  # queue名字
                      body='Hello World!')  # 消息内容
print(" [x] Sent 'Hello World!'")
connection.close()  # 队列关闭



接收端 consumer


import pika
import time

# 建立实例
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
# 声明管道
channel = connection.channel()

# 为什么又声明了一个‘hello’队列？
# 如果确定已经声明了，可以不声明。但是你不知道那个机器先运行，所以要声明两次。
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):  # 四个参数为标准格式
    print(ch, method, properties)  # 打印看一下是什么
    # 管道内存对象  内容相关信息  后面讲
    print(" [x] Received %r" % body)
    time.sleep(15)
    ch.basic_ack(delivery_tag = method.delivery_tag)  # 告诉生成者，消息处理完成

channel.basic_consume(  # 消费消息
        callback,  # 如果收到消息，就调用callback函数来处理消息
        queue='hello',  # 你要从那个队列里收消息
        # no_ack=True  # 写的话，如果接收消息，机器宕机消息就丢了
        # 一般不写。宕机则生产者检测到发给其他消费者
        )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  # 开始消费消息


3、RabbitMQ 消息分发轮询

    上面的只是一个生产者、一个消费者，能不能一个生产者多个消费者呢？
    可以上面的例子，多启动几个消费者consumer，看一下消息的接收情况。
    采用轮询机制；把消息依次分发
    假如消费者处理消息需要15秒，如果当机了，那这个消息处理明显还没处理完，怎么处理？
    （可以模拟消费端断了，分别注释和不注释 no_ack=True 看一下）
    你没给我回复确认，就代表消息没处理完。

    上面的效果消费端断了就转到另外一个消费端去了，但是生产者怎么知道消费端断了呢？
    因为生产者和消费者是通过socket连接的，socket断了，就说明消费端断开了。

    上面的模式只是依次分发，实际情况是机器配置不一样。怎么设置类似权重的操作？
    RabbitMQ怎么办呢，RabbitMQ做了简单的处理就能实现公平的分发。
    就是RabbitMQ给消费者发消息的时候检测下消费者里的消息数量，如果超过指定值（比如1条），就不给你发了。
    只需要在消费者端，channel.basic_consume前加上就可以了。

channel.basic_qos(prefetch_count=1)  # 类似权重，按能力分发，如果有一个消息，就不在给你发
channel.basic_consume(  # 消费消息


三、RabbitMQ 消息持久化（durable、properties）
1、RabbitMQ 相关命令
rabbitmqctl list_queues  # 查看当前queue数量及queue里消息数量	

2、消息持久化
如果队列里还有消息，RabbitMQ 服务端宕机了呢？消息还在不在？
把RabbitMQ服务重启，看一下消息在不在。
上面的情况下，宕机了，消息就丢了，下面看看如何把消息持久化。 

每次声明队列的时候，都加上durable，注意每个队列都得写，客户端、服务端声明的时候都得写。
# 在管道里声明queue
channel.queue_declare(queue='hello2', durable=True)

测试结果发现，只是把队列持久化了，但是队列里的消息没了。
durable的作用只是把队列持久化。离消息持久话还差一步： 
发送端发送消息时，加上properties
properties=pika.BasicProperties(
    delivery_mode=2,  # 消息持久化
    )
	
	
发送端 producer

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost',5672))  # 默认端口5672，可不写
channel = connection.channel()
#声明queue
channel.queue_declare(queue='hello2', durable=True)  # 若声明过，则换一个名字
#n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello2',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                          )
                      )

print(" [x] Sent 'Hello World!'")
connection.close()


接收端 consumer
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello2', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(10)
    ch.basic_ack(delivery_tag = method.delivery_tag)  # 告诉生产者，消息处理完成

channel.basic_qos(prefetch_count=1)  # 类似权重，按能力分发，如果有一个消息，就不在给你发
channel.basic_consume(  # 消费消息
                      callback,  # 如果收到消息，就调用callback
                      queue='hello2',
                      # no_ack=True  # 一般不写，处理完接收处理结果。宕机则发给其他消费者
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


四、RabbitMQ 广播模式（exchange）

前面的效果都是一对一发，如果做一个广播效果可不可以，这时候就要用到exchange了
exchange必须精确的知道收到的消息要发给谁。exchange的类型决定了怎么处理，
类型有以下几种：

    fanout: 所有绑定到此exchange的queue都可以接收消息
    direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
    topic： 所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息

1、fanout 纯广播、all
需要queue和exchange绑定，因为消费者不是和exchange直连的，消费者是连在queue上，queue绑定在exchange上，消费者只会在queu里获取消息

          |------------------------|
          |            /—— queue <—|—> consumer1
producer —|—exchange1 <bind        |                 
       \  |            \—— queue <—|—> consumer2
        \-|-exchange2    ……        |
          |------------------------|

发送端 publisher 发布、广播		  
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
# 注意：这里是广播，不需要声明queue
channel.exchange_declare(exchange='logs',  # 声明广播管道
                         type='fanout')

# message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message = "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',  # 注意此处空，必须有
                      body=message)
print(" [x] Sent %r" % message)
connection.close()

接收端 subscriber 订阅
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')
# 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(exclusive=True)
# 获取随机的queue名字
queue_name = result.method.queue
print("random queuename:", queue_name)

channel.queue_bind(exchange='logs',  # queue绑定到转发器上
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
注意：广播，是实时的，收不到就没了，消息不会存下来，类似收音机。

2、direct 有选择的接收消息
接收者可以过滤消息，只收我想要的消息 

发送端publisher
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')
# 重要程度级别，这里默认定义为 info
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()




接收端subscriber

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
# 获取运行脚本所有的参数
severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)
# 循环列表去绑定
for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()


运行接收端，指定接收级别的参数，例：
python direct_sonsumer.py info warning 
python direct_sonsumer.py warning error


3、topic 更细致的过滤

比如把error中，apache和mysql的分别或取出来

发送端publisher

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()


接收端 subscriber

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()



运行接收端，指定接收哪些消息，例：

python topic_sonsumer.py *.info
python topic_sonsumer.py *.error mysql.*
python topic_sonsumer.py '#'  # 接收所有消息

# 接收所有的 logs run:
# python receive_logs_topic.py "#"

# To receive all logs from the facility "kern":
# python receive_logs_topic.py "kern.*"

# Or if you want to hear only about "critical" logs:
# python receive_logs_topic.py "*.critical"

# You can create multiple bindings:
# python receive_logs_topic.py "kern.*" "*.critical"

# And to emit a log with a routing key "kern.critical" type:
# python emit_log_topic.py "kern.critical" "A critical kernel error"


4、RabbitMQ RPC 实现（Remote procedure call）
不知道你有没有发现，上面的流都是单向的，如果远程的机器执行完返回结果，就实现不了了。
如果返回，这种模式叫什么呢，RPC（远程过程调用），snmp就是典型的RPC
RabbitMQ能不能返回呢，怎么返回呢？既是发送端又是接收端。
但是接收端返回消息怎么返回？可以发送到发过来的queue里么？不可以。
返回时，再建立一个queue，把结果发送新的queue里
为了服务端返回的queue不写死，在客户端给服务端发指令的的时候，同时带一条消息说，你结果返回给哪个queue


RPC client

import pika
import uuid
import time

class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response,  # 只要一收到消息就调用on_response
                                   no_ack=True,
                                   queue=self.callback_queue)  # 收这个queue的消息

    def on_response(self, ch, method, props, body):  # 必须四个参数
        # 如果收到的ID和本机生成的相同，则返回的结果就是我想要的指令返回的结果
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None  # 初始self.response为None
        self.corr_id = str(uuid.uuid4())  # 随机唯一字符串
        self.channel.basic_publish(
                exchange='',
                routing_key='rpc_queue',  # 发消息到rpc_queue
                properties=pika.BasicProperties(  # 消息持久化
                    reply_to = self.callback_queue,  # 让服务端命令结果返回到callback_queue
                    correlation_id = self.corr_id,  # 把随机uuid同时发给服务器
                ),
                body=str(n)
        )
        while self.response is None:  # 当没有数据，就一直循环
            # 启动后，on_response函数接到消息，self.response 值就不为空了
            self.connection.process_data_events()  # 非阻塞版的start_consuming()
            # print("no msg……")
            # time.sleep(0.5)
        # 收到消息就调用on_response
        return int(self.response)

if __name__ == '__main__':
    fibonacci_rpc = FibonacciRpcClient()
    print(" [x] Requesting fib(7)")
    response = fibonacci_rpc.call(7)
    print(" [.] Got %r" % response)
	
	
	
	
RPC server

import pika
import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def on_request(ch, method, props, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(
            exchange='',  # 把执行结果发回给客户端
            routing_key=props.reply_to,  # 客户端要求返回想用的queue
            # 返回客户端发过来的correction_id 为了让客户端验证消息一致性
            properties=pika.BasicProperties(correlation_id = props.correlation_id),
            body=str(response)
    )
    ch.basic_ack(delivery_tag = method.delivery_tag)  # 任务完成，告诉客户端

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')  # 声明一个rpc_queue ,

    channel.basic_qos(prefetch_count=1)
    # 在rpc_queue里收消息,收到消息就调用on_request
    channel.basic_consume(on_request, queue='rpc_queue')
    print(" [x] Awaiting RPC requests")
    channel.start_consuming()

	
	


		  