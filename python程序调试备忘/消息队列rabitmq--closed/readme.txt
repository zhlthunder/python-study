�ο��� https://blog.csdn.net/fgf00/article/details/52872730
python(ʮһ)�ϣ�RabbitMQ ʹ����ϸ���� 

Ŀ¼

�Ͻڻع�
һ��RabbitMQ ��Ϣ���н���
����RabbitMQ����ʾ��.
����1��Rabbitmq ��װ
����2������ʾ��
����3��RabbitMQ ��Ϣ�ַ���ѯ
����RabbitMQ ��Ϣ�־û���durable��properties��
����1��RabbitMQ �������
����2����Ϣ�־û�
�ġ�RabbitMQ �㲥ģʽ��exchange��
����1��fanout ���㲥��all
����2��direct ��ѡ��Ľ�����Ϣ
����3��topic ��ϸ�µĹ���
����4��RabbitMQ RPC ʵ�֣�Remote procedure call��


�Ͻڻع�

��Ҫ����Э�̡����̡�IO��·���á�
Э�̺�IO��·���ö��ǵ��̵߳ġ�

epoll  ��linux��ͨ�����ģ��libevent.soʵ��
gevent  �ڵײ�Ҳ������libevent.so

gevent�������Ϊһ�����ϲ�ķ�װ��
ʹ��select����selectors��ÿ���ջ�������һ�ζ�Ҫselectһ��

twisted�첽�����ܣ�ǿ�����Ӵ󣬲�֧��python3 (������python����top3)�����������е����������д��һ�顣


һ��RabbitMQ ��Ϣ���н���
RabbitMQҲ����Ϣ���У���RabbitMQ��֮ǰpython��Queue��ʲô����ô��

python�е� ��Ϣ����:
    �߳� queue��ͬһ�������߳�֮����н�����
    ���� Queue�����ӽ��̽��н��� ���� ͬ����ͬһ�����µĶ���ӽ��̽��н�����
�����������ȫ������python����Ҳ�ǲ�������������queue���н����ģ����ߺ��������Խ�������Щʵ�ַ�ʽ�ء� 	
��Disk��Socket�������м���������м����������֧����������֮�佻��������֧�ֶ�����򣬿���ά���ö������Ķ��С�	
�����ֹ������м���кö����Ĳ�Ʒ��
RabbitMQ
ZeroMQ
ActiveMQ
����

RabbitMQ��erlang���� �����ġ�
Python������RabbitMQ��ģ�飺pika ��Celery(�ֲ�ʽ�������) ��haigha 

����ά���ܶ�Ķ���
RabbitMQ �̳̹�����http://www.rabbitmq.com/getstarted.html

��������˵����
Broker������˵������Ϣ���з�����ʵ�塣
Exchange����Ϣ����������ָ����Ϣ��ʲô����·�ɵ��ĸ����С�
Queue����Ϣ�������壬ÿ����Ϣ���ᱻͶ�뵽һ���������С�
Binding���󶨣��������þ��ǰ�exchange��queue����·�ɹ����������
Routing Key��·�ɹؼ��֣�exchange��������ؼ��ֽ�����ϢͶ�ݡ�
vhost������������һ��broker����Կ�����vhost��������ͬ�û���Ȩ�޷��롣
producer����Ϣ�����ߣ�����Ͷ����Ϣ�ĳ���
consumer����Ϣ�����ߣ����ǽ�����Ϣ�ĳ���
channel����Ϣͨ�����ڿͻ��˵�ÿ��������ɽ������channel��ÿ��channel����һ���Ự����


����RabbitMQ����ʾ��.
1.rabbitmq ��װ�� ��ο� install_follow.txt

2������ʾ��
���Ͷ� producer

import pika
# ����һ��ʵ��
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost',5672)  # Ĭ�϶˿�5672���ɲ�д
    )
# ����һ���ܵ����ڹܵ��﷢��Ϣ
channel = connection.channel()
# �ڹܵ�������queue
channel.queue_declare(queue='hello')
# RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',  # queue����
                      body='Hello World!')  # ��Ϣ����
print(" [x] Sent 'Hello World!'")
connection.close()  # ���йر�



���ն� consumer


import pika
import time

# ����ʵ��
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
# �����ܵ�
channel = connection.channel()

# Ϊʲô��������һ����hello�����У�
# ���ȷ���Ѿ������ˣ����Բ������������㲻֪���Ǹ����������У�����Ҫ�������Ρ�
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):  # �ĸ�����Ϊ��׼��ʽ
    print(ch, method, properties)  # ��ӡ��һ����ʲô
    # �ܵ��ڴ����  ���������Ϣ  ���潲
    print(" [x] Received %r" % body)
    time.sleep(15)
    ch.basic_ack(delivery_tag = method.delivery_tag)  # ���������ߣ���Ϣ�������

channel.basic_consume(  # ������Ϣ
        callback,  # ����յ���Ϣ���͵���callback������������Ϣ
        queue='hello',  # ��Ҫ���Ǹ�����������Ϣ
        # no_ack=True  # д�Ļ������������Ϣ������崻���Ϣ�Ͷ���
        # һ�㲻д��崻��������߼�⵽��������������
        )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  # ��ʼ������Ϣ


3��RabbitMQ ��Ϣ�ַ���ѯ

    �����ֻ��һ�������ߡ�һ�������ߣ��ܲ���һ�������߶���������أ�
    ������������ӣ�����������������consumer����һ����Ϣ�Ľ��������
    ������ѯ���ƣ�����Ϣ���ηַ�
    ���������ߴ�����Ϣ��Ҫ15�룬��������ˣ��������Ϣ�������Ի�û�����꣬��ô����
    ������ģ�����Ѷ˶��ˣ��ֱ�ע�ͺͲ�ע�� no_ack=True ��һ�£�
    ��û���һظ�ȷ�ϣ��ʹ�����Ϣû�����ꡣ

    �����Ч�����Ѷ˶��˾�ת������һ�����Ѷ�ȥ�ˣ�������������ô֪�����Ѷ˶����أ�
    ��Ϊ�����ߺ���������ͨ��socket���ӵģ�socket���ˣ���˵�����Ѷ˶Ͽ��ˡ�

    �����ģʽֻ�����ηַ���ʵ������ǻ������ò�һ������ô��������Ȩ�صĲ�����
    RabbitMQ��ô���أ�RabbitMQ���˼򵥵Ĵ������ʵ�ֹ�ƽ�ķַ���
    ����RabbitMQ�������߷���Ϣ��ʱ�����������������Ϣ�������������ָ��ֵ������1�������Ͳ����㷢�ˡ�
    ֻ��Ҫ�������߶ˣ�channel.basic_consumeǰ���ϾͿ����ˡ�

channel.basic_qos(prefetch_count=1)  # ����Ȩ�أ��������ַ��������һ����Ϣ���Ͳ��ڸ��㷢
channel.basic_consume(  # ������Ϣ


����RabbitMQ ��Ϣ�־û���durable��properties��
1��RabbitMQ �������
rabbitmqctl list_queues  # �鿴��ǰqueue������queue����Ϣ����	

2����Ϣ�־û�
��������ﻹ����Ϣ��RabbitMQ �����崻����أ���Ϣ���ڲ��ڣ�
��RabbitMQ������������һ����Ϣ�ڲ��ڡ�
���������£�崻��ˣ���Ϣ�Ͷ��ˣ����濴����ΰ���Ϣ�־û��� 

ÿ���������е�ʱ�򣬶�����durable��ע��ÿ�����ж���д���ͻ��ˡ������������ʱ�򶼵�д��
# �ڹܵ�������queue
channel.queue_declare(queue='hello2', durable=True)

���Խ�����֣�ֻ�ǰѶ��г־û��ˣ����Ƕ��������Ϣû�ˡ�
durable������ֻ�ǰѶ��г־û�������Ϣ�־û�����һ���� 
���Ͷ˷�����Ϣʱ������properties
properties=pika.BasicProperties(
    delivery_mode=2,  # ��Ϣ�־û�
    )
	
	
���Ͷ� producer

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost',5672))  # Ĭ�϶˿�5672���ɲ�д
channel = connection.channel()
#����queue
channel.queue_declare(queue='hello2', durable=True)  # ������������һ������
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


���ն� consumer
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello2', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(10)
    ch.basic_ack(delivery_tag = method.delivery_tag)  # ���������ߣ���Ϣ�������

channel.basic_qos(prefetch_count=1)  # ����Ȩ�أ��������ַ��������һ����Ϣ���Ͳ��ڸ��㷢
channel.basic_consume(  # ������Ϣ
                      callback,  # ����յ���Ϣ���͵���callback
                      queue='hello2',
                      # no_ack=True  # һ�㲻д����������մ�������崻��򷢸�����������
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


�ġ�RabbitMQ �㲥ģʽ��exchange��

ǰ���Ч������һ��һ���������һ���㲥Ч���ɲ����ԣ���ʱ���Ҫ�õ�exchange��
exchange���뾫ȷ��֪���յ�����ϢҪ����˭��exchange�����;�������ô����
���������¼��֣�

    fanout: ���а󶨵���exchange��queue�����Խ�����Ϣ
    direct: ͨ��routingKey��exchange�������Ǹ�Ψһ��queue���Խ�����Ϣ
    topic�� ���з���routingKey(��ʱ������һ�����ʽ)��routingKey��bind��queue���Խ�����Ϣ

1��fanout ���㲥��all
��Ҫqueue��exchange�󶨣���Ϊ�����߲��Ǻ�exchangeֱ���ģ�������������queue�ϣ�queue����exchange�ϣ�������ֻ����queu���ȡ��Ϣ

          |------------------------|
          |            /���� queue <��|��> consumer1
producer ��|��exchange1 <bind        |                 
       \  |            \���� queue <��|��> consumer2
        \-|-exchange2    ����        |
          |------------------------|

���Ͷ� publisher �������㲥		  
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
# ע�⣺�����ǹ㲥������Ҫ����queue
channel.exchange_declare(exchange='logs',  # �����㲥�ܵ�
                         type='fanout')

# message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message = "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',  # ע��˴��գ�������
                      body=message)
print(" [x] Sent %r" % message)
connection.close()

���ն� subscriber ����
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')
# ��ָ��queue����,rabbit���������һ������,exclusive=True����ʹ�ô�queue�������߶Ͽ���,�Զ���queueɾ��
result = channel.queue_declare(exclusive=True)
# ��ȡ�����queue����
queue_name = result.method.queue
print("random queuename:", queue_name)

channel.queue_bind(exchange='logs',  # queue�󶨵�ת������
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
ע�⣺�㲥����ʵʱ�ģ��ղ�����û�ˣ���Ϣ�����������������������

2��direct ��ѡ��Ľ�����Ϣ
�����߿��Թ�����Ϣ��ֻ������Ҫ����Ϣ 

���Ͷ�publisher
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')
# ��Ҫ�̶ȼ�������Ĭ�϶���Ϊ info
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()




���ն�subscriber

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
# ��ȡ���нű����еĲ���
severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)
# ѭ���б�ȥ��
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


���н��նˣ�ָ�����ռ���Ĳ���������
python direct_sonsumer.py info warning 
python direct_sonsumer.py warning error


3��topic ��ϸ�µĹ���

�����error�У�apache��mysql�ķֱ��ȡ����

���Ͷ�publisher

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


���ն� subscriber

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



���н��նˣ�ָ��������Щ��Ϣ������

python topic_sonsumer.py *.info
python topic_sonsumer.py *.error mysql.*
python topic_sonsumer.py '#'  # ����������Ϣ

# �������е� logs run:
# python receive_logs_topic.py "#"

# To receive all logs from the facility "kern":
# python receive_logs_topic.py "kern.*"

# Or if you want to hear only about "critical" logs:
# python receive_logs_topic.py "*.critical"

# You can create multiple bindings:
# python receive_logs_topic.py "kern.*" "*.critical"

# And to emit a log with a routing key "kern.critical" type:
# python emit_log_topic.py "kern.critical" "A critical kernel error"


4��RabbitMQ RPC ʵ�֣�Remote procedure call��
��֪������û�з��֣�����������ǵ���ģ����Զ�̵Ļ���ִ���귵�ؽ������ʵ�ֲ����ˡ�
������أ�����ģʽ��ʲô�أ�RPC��Զ�̹��̵��ã���snmp���ǵ��͵�RPC
RabbitMQ�ܲ��ܷ����أ���ô�����أ����Ƿ��Ͷ����ǽ��նˡ�
���ǽ��ն˷�����Ϣ��ô���أ����Է��͵���������queue��ô�������ԡ�
����ʱ���ٽ���һ��queue���ѽ�������µ�queue��
Ϊ�˷���˷��ص�queue��д�����ڿͻ��˸�����˷�ָ��ĵ�ʱ��ͬʱ��һ����Ϣ˵���������ظ��ĸ�queue


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

        self.channel.basic_consume(self.on_response,  # ֻҪһ�յ���Ϣ�͵���on_response
                                   no_ack=True,
                                   queue=self.callback_queue)  # �����queue����Ϣ

    def on_response(self, ch, method, props, body):  # �����ĸ�����
        # ����յ���ID�ͱ������ɵ���ͬ���򷵻صĽ����������Ҫ��ָ��صĽ��
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None  # ��ʼself.responseΪNone
        self.corr_id = str(uuid.uuid4())  # ���Ψһ�ַ���
        self.channel.basic_publish(
                exchange='',
                routing_key='rpc_queue',  # ����Ϣ��rpc_queue
                properties=pika.BasicProperties(  # ��Ϣ�־û�
                    reply_to = self.callback_queue,  # �÷�������������ص�callback_queue
                    correlation_id = self.corr_id,  # �����uuidͬʱ����������
                ),
                body=str(n)
        )
        while self.response is None:  # ��û�����ݣ���һֱѭ��
            # ������on_response�����ӵ���Ϣ��self.response ֵ�Ͳ�Ϊ����
            self.connection.process_data_events()  # ���������start_consuming()
            # print("no msg����")
            # time.sleep(0.5)
        # �յ���Ϣ�͵���on_response
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
            exchange='',  # ��ִ�н�����ظ��ͻ���
            routing_key=props.reply_to,  # �ͻ���Ҫ�󷵻����õ�queue
            # ���ؿͻ��˷�������correction_id Ϊ���ÿͻ�����֤��Ϣһ����
            properties=pika.BasicProperties(correlation_id = props.correlation_id),
            body=str(response)
    )
    ch.basic_ack(delivery_tag = method.delivery_tag)  # ������ɣ����߿ͻ���

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')  # ����һ��rpc_queue ,

    channel.basic_qos(prefetch_count=1)
    # ��rpc_queue������Ϣ,�յ���Ϣ�͵���on_request
    channel.basic_consume(on_request, queue='rpc_queue')
    print(" [x] Awaiting RPC requests")
    channel.start_consuming()

	
	


		  