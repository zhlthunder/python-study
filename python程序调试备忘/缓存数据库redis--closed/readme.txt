http://www.cnblogs.com/alex3714/articles/6217453.html

�������ݿ����

NoSQL(NoSQL = Not Only SQL)���⼴����������SQL������ָ�ǹ�ϵ�͵����ݿ�,���Ż�����web2.0��վ�����𣬴�ͳ�Ĺ�ϵ���ݿ���Ӧ��web2.0��վ���ر��ǳ����ģ�͸߲�����SNS���͵�web2.0����̬��վ�Ѿ��Ե��������ģ���¶�˺ܶ����Կ˷������⣬���ǹ�ϵ�͵����ݿ��������䱾����ص�õ��˷ǳ�Ѹ�ٵķ�չ��NoSQL���ݿ�Ĳ�������Ϊ�˽�����ģ���ݼ��϶������������������ս�������Ǵ�����Ӧ�����⡣


NoSQL���ݿ���Ĵ����

��ֵ(Key-Value)�洢���ݿ�
��һ�����ݿ���Ҫ��ʹ�õ�һ����ϣ�����������һ���ض��ļ���һ��ָ��ָ���ض������ݡ�Key/valueģ�Ͷ���ITϵͳ��˵���������ڼ򵥡��ײ��𡣵������DBAֻ�Բ���ֵ���в�ѯ����µ�ʱ��Key/value���Ե�Ч�ʵ����ˡ�[3]  �����磺Tokyo Cabinet/Tyrant, Redis, Voldemort, Oracle BDB.

�д洢���ݿ⡣
�ⲿ�����ݿ�ͨ��������Ӧ�Էֲ�ʽ�洢�ĺ������ݡ�����Ȼ���ڣ��������ǵ��ص���ָ���˶���С���Щ�������м��������ŵġ��磺Cassandra, HBase, Riak.
 
�ĵ������ݿ�
�ĵ������ݿ�������������Lotus Notes�칫����ģ�������ͬ��һ�ּ�ֵ�洢�����ơ������͵�����ģ���ǰ汾�����ĵ�����ṹ�����ĵ����ض��ĸ�ʽ�洢������JSON���ĵ������ݿ�� �Կ����Ǽ�ֵ���ݿ�������棬����֮��Ƕ�׼�ֵ�������ĵ������ݿ�ȼ�ֵ���ݿ�Ĳ�ѯЧ�ʸ��ߡ��磺CouchDB, MongoDb. ����Ҳ���ĵ������ݿ�SequoiaDB���Ѿ���Դ��
 
ͼ��(Graph)���ݿ�
ͼ�νṹ�����ݿ�ͬ���������Լ����Խṹ��SQL���ݿⲻͬ������ʹ������ͼ��ģ�ͣ������ܹ���չ������������ϡ�NoSQL���ݿ�û�б�׼�Ĳ�ѯ����(SQL)����˽������ݿ��ѯ��Ҫ�ƶ�����ģ�͡����NoSQL���ݿⶼ��RESTʽ�����ݽӿڻ��߲�ѯAPI��[2]  �磺Neo4J, InfoGrid, Infinite Graph.
��ˣ������ܽ�NoSQL���ݿ������µ��⼸������±Ƚ����ã�1������ģ�ͱȽϼ򵥣�2����Ҫ����Ը�ǿ��ITϵͳ��3�������ݿ�����Ҫ��ϸߣ�4������Ҫ�߶ȵ�����һ���ԣ�5�����ڸ���key���Ƚ�����ӳ�临��ֵ�Ļ�����


redis
����
redis��ҵ��������key-value nosql ���ݿ�֮һ����Memcached���ƣ���֧�ִ洢��value������Ը��࣬����string(�ַ���)��list(����)��set(����)��zset(sorted set --���򼯺�)��hash����ϣ���ͣ�����Щ�������Ͷ�֧��push/pop��add/remove��ȡ���������Ͳ�����ḻ�Ĳ�����������Щ��������ԭ���Եġ��ڴ˻����ϣ�redis֧�ָ��ֲ�ͬ��ʽ��������memcachedһ����Ϊ�˱�֤Ч�ʣ����ݶ��ǻ������ڴ��С��������redis�������ԵİѸ��µ�����д����̻��߰��޸Ĳ���д��׷�ӵļ�¼�ļ��������ڴ˻�����ʵ����master-slave(����)ͬ����

Redis�ŵ�
    �쳣���� : Redis�Ƿǳ���ģ�ÿ�����ִ�д�Լ110000���ò�����81000��/ÿ��Ķ�ȡ������
    ֧�ַḻ���������� : Redis֧��������������Ա�Ѿ�֪�����б����ϣ������򼯺ϣ���ϣ���������͡�
    ��ʹ����Ӧ���к����׽���ĸ������⣬��Ϊ����֪����Щ���⴦��ʹ�������������͸��ý����
    ��������ԭ�ӵ� : ���� Redis �Ĳ�������ԭ�ӣ��Ӷ�ȷ���������ͻ�ͬʱ���� Redis �������õ����Ǹ��º��ֵ������ֵ����    MultiUtility���ߣ�Redis��һ���๦��ʵ�ù��ߣ������ںܶ��磺���棬��Ϣ���ݶ�����ʹ�ã�Redisԭ��֧�ַ���/���ģ�����Ӧ�ó����У��磺WebӦ�ó���Ự����վҳ���������κζ��ݵ����ݣ�


��װRedis����
Ҫ�� Ubuntu �ϰ�װ Redis�����նˣ�Ȼ�������������
$sudo apt-get update
$sudo apt-get install redis-server

�⽫�����ļ�����ϰ�װRedis
���� Redis

$redis-server
�鿴 redis �Ƿ�������
$redis-cli
�⽫��һ�� Redis ��ʾ��������ͼ��ʾ��
redis 127.0.0.1:6379>
���������ʾ��Ϣ�У�127.0.0.1 �Ǳ�����IP��ַ��6379�� Redis ���������еĶ˿ڡ��������� PING �������ͼ��ʾ��
redis 127.0.0.1:6379> ping
PONG
��˵���������Ѿ��ɹ����ڼ�����ϰ�װ�� Redis��	


Python����Redis

sudo pip install redis
or
sudo easy_install redis
or
Դ�밲װ
  
�����https://github.com/WoLpH/redis-py

��Ubuntu�ϰ�װRedis���������
Ҫ��Ubuntu �ϰ�װ Redis����������Դ� http://redisdesktop.com/download ���ذ�����װ����
Redis ���������������û����������� Redis �������ݡ�



Redis APIʹ��
redis-py ��API��ʹ�ÿ��Է���Ϊ��

    ���ӷ�ʽ
    ���ӳ�
    ����
        String ����
        Hash ����
        List ����
        Set ����
        Sort Set ����
    �ܵ�
    ��������


���ӷ�ʽ
1������ģʽ
redis-py�ṩ������Redis��StrictRedis����ʵ��Redis�����StrictRedis����ʵ�ִ󲿷ֹٷ��������ʹ�ùٷ����﷨�����Redis��StrictRedis�����࣬���������ݾɰ汾��redis-py��

import redis
r = redis.Redis(host='10.211.55.4', port=6379)
r.set('foo', 'Bar')
print r.get('foo')


2�����ӳ�

redis-pyʹ��connection pool�������һ��redis server���������ӣ�����ÿ�ν������ͷ����ӵĿ�����Ĭ�ϣ�ÿ��Redisʵ������ά��һ���Լ������ӳء�����ֱ�ӽ���һ�����ӳأ�Ȼ����Ϊ����Redis�������Ϳ���ʵ�ֶ��Redisʵ������һ�����ӳء�

����
1. String����
redis�е�String�����ڴ��а���һ��name��Ӧһ��value���洢����ͼ��

set(name, value, ex=None, px=None, nx=False, xx=False)	
��Redis������ֵ��Ĭ�ϣ��������򴴽����������޸�
������
     ex������ʱ�䣨�룩
     px������ʱ�䣨���룩
     nx���������ΪTrue����ֻ��name������ʱ����ǰset������ִ��
     xx���������ΪTrue����ֻ��name����ʱ����ǰset������ִ��

setnx(name, value)
����ֵ��ֻ��name������ʱ��ִ�����ò�������ӣ�

setex(name, value, time)
# ����ֵ
# ������
    # time������ʱ�䣨������ �� timedelta����
	
	
psetex(name, time_ms, value)

# ����ֵ
# ������
    # time_ms������ʱ�䣨���ֺ��� �� timedelta����

mset(*args, **kwargs)
	
��������ֵ
�磺
    mset(k1='v1', k2='v2')
    ��
    mget({'k1': 'v1', 'k2': 'v2'})

get(name)
	
��ȡֵ

mget(keys, *args)
	
������ȡ
�磺
    mget('ylr', 'wupeiqi')
    ��
    r.mget(['ylr', 'wupeiqi'])

getset(name, value)
	
������ֵ����ȡԭ����ֵ

getrange(key, start, end)
	
# ��ȡ�����У������ֽڻ�ȡ�����ַ���
# ������
    # name��Redis �� name
    # start����ʼλ�ã��ֽڣ�
    # end������λ�ã��ֽڣ�
# �磺 "������" ��0-3��ʾ "��"

setrange(name, offset, value)
	
# �޸��ַ������ݣ���ָ���ַ���������ʼ����滻����ֵ̫��ʱ���������ӣ�
# ������
    # offset���ַ������������ֽڣ�һ�����������ֽڣ�
    # value��Ҫ���õ�ֵ

setbit(name, offset, value)

	# ��name��Ӧֵ�Ķ����Ʊ�ʾ��λ���в���
 
# ������
    # name��redis��name
    # offset��λ����������ֵ�任�ɶ����ƺ��ٽ���������
    # value��ֵֻ���� 1 �� 0
 
# ע�������Redis����һ����Ӧ�� n1 = "foo"��
        ��ô�ַ���foo�Ķ����Ʊ�ʾΪ��01100110 01101111 01101111
    ���ԣ����ִ�� setbit('n1', 7, 1)����ͻὫ��7λ����Ϊ1��
        ��ô���ն��������� 01100111 01101111 01101111������"goo"
 
# ��չ��ת�������Ʊ�ʾ��
 
    # source = "������"
    source = "foo"
 
    for i in source:
        num = ord(i)
        print bin(num).replace('b','')
 
    �ر�ģ����source�Ǻ��� "������"��ô�죿
    �𣺶���utf-8��ÿһ������ռ 3 ���ֽڣ���ô "������" ���� 9���ֽ�
       ���ں��֣�forѭ��ʱ��ᰴ�� �ֽ� ��������ô�ڵ���ʱ����ÿһ���ֽ�ת�� ʮ��������Ȼ���ٽ�ʮ������ת���ɶ�����
        11100110 10101101 10100110 11100110 10110010 10011011 11101001 10111101 10010000


getbit(name, offset)
	
# ��ȡname��Ӧ��ֵ�Ķ����Ʊ�ʾ�е�ĳλ��ֵ ��0��1��

bitcount(key, start=None, end=None)
	
# ��ȡname��Ӧ��ֵ�Ķ����Ʊ�ʾ�� 1 �ĸ���
# ������
    # key��Redis��name
    # start��λ��ʼλ��
    # end��λ����λ��

strlen(name)
1
	
# ����name��Ӧֵ���ֽڳ��ȣ�һ������3���ֽڣ�

incr(self, name, amount=1)
	
# ���� name��Ӧ��ֵ����name������ʱ���򴴽�name��amount��������������
 
# ������
    # name,Redis��name
    # amount,��������������������
 
# ע��ͬincrby

incrbyfloat(self, name, amount=1.0)
	
# ���� name��Ӧ��ֵ����name������ʱ���򴴽�name��amount��������������
 
# ������
    # name,Redis��name
    # amount,�������������ͣ�

decr(self, name, amount=1)
	
# �Լ� name��Ӧ��ֵ����name������ʱ���򴴽�name��amount���������Լ���
 
# ������
    # name,Redis��name
    # amount,�Լ�����������

append(key, value)

# ��redis name��Ӧ��ֵ����׷������
 
# ������
    key, redis��name
    value, Ҫ׷�ӵ��ַ���


2. Hash����
hash������ʽ����Щ��pyhton�е�dict,���Դ洢һ������Խ�ǿ������ �� redis��Hash���ڴ��еĴ洢��ʽ����ͼ��

hset(name, key, value)
	
# name��Ӧ��hash������һ����ֵ�ԣ������ڣ��򴴽��������޸ģ�
 
# ������
    # name��redis��name
    # key��name��Ӧ��hash�е�key
    # value��name��Ӧ��hash�е�value
 
# ע��
    # hsetnx(name, key, value),��name��Ӧ��hash�в����ڵ�ǰkeyʱ�򴴽����൱����ӣ�

	
	
hmset(name, mapping)
	
# ��name��Ӧ��hash���������ü�ֵ��
 
# ������
    # name��redis��name
    # mapping���ֵ䣬�磺{'k1':'v1', 'k2': 'v2'}
 
# �磺
    # r.hmset('xx', {'k1':'v1', 'k2': 'v2'})
	

hget(name,key)	
# ��name��Ӧ��hash�л�ȡ����key��ȡvalue


hmget(name, keys, *args)
# ��name��Ӧ��hash�л�ȡ���key��ֵ
 
# ������
    # name��reids��Ӧ��name
    # keys��Ҫ��ȡkey���ϣ��磺['k1', 'k2', 'k3']
    # *args��Ҫ��ȡ��key���磺k1,k2,k3
 
# �磺
    # r.mget('xx', ['k1', 'k2'])
    # ��
    # print r.hmget('xx', 'k1', 'k2')


hgetall(name)
��ȡname��Ӧhash�����м�ֵ

hlen(name)
# ��ȡname��Ӧ��hash�м�ֵ�Եĸ���

hkeys(name)	
# ��ȡname��Ӧ��hash�����е�key��ֵ

hvals(name)
# ��ȡname��Ӧ��hash�����е�value��ֵ

hexists(name, key)	
# ���name��Ӧ��hash�Ƿ���ڵ�ǰ�����key

hdel(name,*keys)	
# ��name��Ӧ��hash��ָ��key�ļ�ֵ��ɾ��

hincrby(name, key, amount=1)	
# ����name��Ӧ��hash�е�ָ��key��ֵ���������򴴽�key=amount
# ������
    # name��redis�е�name
    # key�� hash��Ӧ��key
    # amount����������������

hincrbyfloat(name, key, amount=1.0)	
# ����name��Ӧ��hash�е�ָ��key��ֵ���������򴴽�key=amount
 
# ������
    # name��redis�е�name
    # key�� hash��Ӧ��key
    # amount������������������
 
# ����name��Ӧ��hash�е�ָ��key��ֵ���������򴴽�key=amount


@@@@@��������hash�����ĺ������ܴ�����ȷ��
hscan(name, cursor=0, match=None, count=None)
Start a full hash scan with:
HSCAN myhash 0
Start a hash scan with fields matching a pattern with:
HSCAN myhash 0 MATCH order_*
Start a hash scan with fields matching a pattern and forcing the scan command to do more scanning with:
HSCAN myhash 0 MATCH order_* COUNT 1000

 
	
# ����ʽ������ȡ���������ݴ�����ݷǳ����ã�hscan����ʵ�ַ�Ƭ�Ļ�ȡ���ݣ�����һ���Խ�����ȫ����ȡ�꣬�Ӷ������ڴ汻�ű�
# ������
    # name��redis��name
    # cursor���α꣨�����α����ȡ��ȡ���ݣ�
    # match��ƥ��ָ��key��Ĭ��None ��ʾ���е�key
    # count��ÿ�η�Ƭ���ٻ�ȡ������Ĭ��None��ʾ����Redis��Ĭ�Ϸ�Ƭ����
 
# �磺
    # ��һ�Σ�cursor1, data1 = r.hscan('xx', cursor=0, match=None, count=None)
    # �ڶ��Σ�cursor2, data1 = r.hscan('xx', cursor=cursor1, match=None, count=None)
    # ...
    # ֱ������ֵcursor��ֵΪ0ʱ����ʾ�����Ѿ�ͨ����Ƭ��ȡ���

 

hscan_iter(name, match=None, count=None)	
# ����yield��װhscan������������ʵ�ַ���ȥredis�л�ȡ����
  
# ������
    # match��ƥ��ָ��key��Ĭ��None ��ʾ���е�key
    # count��ÿ�η�Ƭ���ٻ�ȡ������Ĭ��None��ʾ����Redis��Ĭ�Ϸ�Ƭ����  
# �磺
    # for item in r.hscan_iter('xx'):
    #     print item
	
@@@@@@@@@@@@@@@@

3. list
List������redis�е�List�����ڴ��а���һ��name��Ӧһ��List���洢����ͼ����	

lpush(name,values)

# ��name��Ӧ��list�����Ԫ�أ�ÿ���µ�Ԫ�ض���ӵ��б�������
 
# �磺
    # r.lpush('oo', 11,22,33)
    # ����˳��Ϊ: 33,22,11
# ��չ��
    # rpush(name, values) ��ʾ�����������
	
	
lpushx(name,value)

# ��name��Ӧ��list�����Ԫ�أ�ֻ��name�Ѿ�����ʱ��ֵ��ӵ��б�������
 
# ���ࣺ
    # rpushx(name, value) ��ʾ�����������

	
llen(name)
# name��Ӧ��listԪ�صĸ���


linsert(name, where, refvalue, value))
# ��name�б��ĳһ��ֵǰ������һ����ֵ
# ������
    # name��redis��name
    # where��BEFORE��AFTER
    # refvalue�����ֵ����������ǰ���������
    # value��Ҫ���������

r.lset(name, index, value)
# ��name��Ӧ��list�е�ĳһ������λ�����¸�ֵ
# ������
    # name��redis��name
    # index��list������λ��
    # value��Ҫ���õ�ֵ


r.lrem(name, value, num)
# ��name��Ӧ��list��ɾ��ָ����ֵ
# ������
    # name��redis��name
    # value��Ҫɾ����ֵ
    # num��  num=0��ɾ���б������е�ָ��ֵ��
           # num=2,��ǰ����ɾ��2����
           # num=-2,�Ӻ���ǰ��ɾ��2��


lpop(name)
# ��name��Ӧ���б������ȡ��һ��Ԫ�ز����б����Ƴ�������ֵ���ǵ�һ��Ԫ��
# ���ࣺ
    # rpop(name) ��ʾ�����������

lindex(name, index)
��name��Ӧ���б��и���������ȡ�б�Ԫ��

lrange(name, start, end)
# ��name��Ӧ���б��Ƭ��ȡ����
# ������
    # name��redis��name
    # start����������ʼλ��
    # end����������λ��


ltrim(name, start, end)
# ��name��Ӧ���б����Ƴ�û����start-end����֮���ֵ
# ������
    # name��redis��name
    # start����������ʼλ��
    # end����������λ��



rpoplpush(src, dst)
# ��һ���б�ȡ�����ұߵ�Ԫ�أ�ͬʱ�����������һ���б�������
# ������
    # src��Ҫȡ���ݵ��б��name
    # dst��Ҫ������ݵ��б��name


blpop(keys, timeout)

# ������б����У����մ�����ȥpop��Ӧ�б��Ԫ�� 
# ������
    # keys��redis��name�ļ���
    # timeout����ʱʱ�䣬��Ԫ�������б��Ԫ�ػ�ȡ��֮�������ȴ��б��������ݵ�ʱ�䣨�룩, 0 ��ʾ��Զ����
# ���ࣺ
    # r.brpop(keys, timeout)�����������ȡ����

	
brpoplpush(src, dst, timeout=0)

# ��һ���б���Ҳ��Ƴ�һ��Ԫ�ز�������ӵ���һ���б�����
# ������
    # src��ȡ����Ҫ�Ƴ�Ԫ�ص��б��Ӧ��name
    # dst��Ҫ����Ԫ�ص��б��Ӧ��name
    # timeout����src��Ӧ���б���û������ʱ�������ȴ��������ݵĳ�ʱʱ�䣨�룩��0 ��ʾ��Զ����


4.set���ϲ���
Set������Set���Ͼ��ǲ������ظ����б�
sadd(name,values)
# name��Ӧ�ļ��������Ԫ��


scard(name)
��ȡname��Ӧ�ļ�����Ԫ�ظ���

sdiff(keys, *args)
�ڵ�һ��name��Ӧ�ļ������Ҳ�������name��Ӧ�ļ��ϵ�Ԫ�ؼ���

sdiffstore(dest, keys, *args)
# ��ȡ��һ��name��Ӧ�ļ������Ҳ�������name��Ӧ�ļ��ϣ��ٽ����¼��뵽dest��Ӧ�ļ�����


sinter(keys, *args)
# ��ȡ��һ��name��Ӧ���ϵĲ���

sinterstore(dest, keys, *args)
# ��ȡ��һ��name��Ӧ���ϵĲ������ٽ�����뵽dest��Ӧ�ļ�����

sismember(name, value)
# ���value�Ƿ���name��Ӧ�ļ��ϵĳ�Ա


smembers(name)
# ��ȡname��Ӧ�ļ��ϵ����г�Ա

smove(src, dst, value)
# ��ĳ����Ա��һ���������ƶ�������һ������

spop(name)
# �Ӽ��ϵ��Ҳࣨβ�����Ƴ�һ����Ա�������䷵��

srandmember(name, numbers)
# ��name��Ӧ�ļ����������ȡ numbers ��Ԫ��

srem(name, values)	
# ��name��Ӧ�ļ�����ɾ��ĳЩֵ

sunion(keys, *args)	
# ��ȡ��һ��name��Ӧ�ļ��ϵĲ���

sunionstore(dest,keys, *args)
# ��ȡ��һ��name��Ӧ�ļ��ϵĲ���������������浽dest��Ӧ�ļ�����



sscan(name, cursor=0, match=None, count=None)
sscan_iter(name, match=None, count=None)
# ͬ�ַ����Ĳ�����������������������ȡԪ�أ������ڴ�����̫��


���򼯺ϣ��ڼ��ϵĻ����ϣ�ΪÿԪ������Ԫ�ص�������Ҫ��������һ��ֵ�����бȽϣ����ԣ��������򼯺ϣ�ÿһ��Ԫ��������ֵ������ֵ�ͷ���������ר������������

    zadd(name, *args, **kwargs)	
    # ��name��Ӧ�����򼯺������Ԫ��
    # �磺
         # zadd('zz', 'n1', 1, 'n2', 2)
         # ��
         # zadd('zz', n1=11, n2=22)

    zcard(name)
    # ��ȡname��Ӧ�����򼯺�Ԫ�ص�����

    zcount(name, min, max)
    # ��ȡname��Ӧ�����򼯺��з��� �� [min,max] ֮��ĸ���

    zincrby(name, value, amount)
    # ����name��Ӧ�����򼯺ϵ� name ��Ӧ�ķ���

    r.zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)
    # ����������Χ��ȡname��Ӧ�����򼯺ϵ�Ԫ��
     
    # ������
        # name��redis��name
        # start�����򼯺�������ʼλ�ã��Ƿ�����
        # end�����򼯺���������λ�ã��Ƿ�����
        # desc���������Ĭ�ϰ��շ�����С��������
        # withscores���Ƿ��ȡԪ�صķ�����Ĭ��ֻ��ȡԪ�ص�ֵ
        # score_cast_func���Է�����������ת���ĺ���
     
	 
    # ���ࣺ
        # �Ӵ�С����
        # zrevrange(name, start, end, withscores=False, score_cast_func=float)
     
        # ���շ�����Χ��ȡname��Ӧ�����򼯺ϵ�Ԫ��
        # zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
        # �Ӵ�С����
        # zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)

    zrank(name, value)	
    # ��ȡĳ��ֵ�� name��Ӧ�����򼯺��е����У��� 0 ��ʼ��
     
    # ���ࣺ
        # zrevrank(name, value)���Ӵ�С����

 

zrem(name, values)	
# ɾ��name��Ӧ�����򼯺���ֵ��values�ĳ�Ա
 
# �磺zrem('zz', ['s1', 's2'])

zremrangebyrank(name, min, max)
# �������з�Χɾ��

zremrangebyscore(name, min, max)
# ���ݷ�����Χɾ��

 

zscore(name, value)
# ��ȡname��Ӧ���򼯺��� value ��Ӧ�ķ���

zinterstore(dest, keys, aggregate=None)	
# ��ȡ�������򼯺ϵĽ��������������ֵͬ��ͬ����������aggregate���в���
# aggregate��ֵΪ:  SUM  MIN  MAX

zunionstore(dest, keys, aggregate=None)
# ��ȡ�������򼯺ϵĲ��������������ֵͬ��ͬ����������aggregate���в���
# aggregate��ֵΪ:  SUM  MIN  MAX

zscan(name, cursor=0, match=None, count=None, score_cast_func=float)
zscan_iter(name, match=None, count=None,score_cast_func=float)
# ͬ�ַ������ƣ�������ַ�������score_cast_func�������Է������в���


�������ò���
delete(*names)	
# ����ɾ��redis�е�������������

exists(name)	
# ���redis��name�Ƿ����

keys(pattern='*')	
# ����ģ�ͻ�ȡredis��name
 
# ���ࣺ
    # KEYS * ƥ�����ݿ������� key ��
    # KEYS h?llo ƥ�� hello �� hallo �� hxllo �ȡ�
    # KEYS h*llo ƥ�� hllo �� heeeeello �ȡ�
    # KEYS h[ae]llo ƥ�� hello �� hallo ������ƥ�� hillo

expire(name ,time)	
# Ϊĳ��redis��ĳ��name���ó�ʱʱ��

rename(src, dst)	
# ��redis��name������Ϊ

move(name, db))	
# ��redis��ĳ��ֵ�ƶ���ָ����db��

randomkey()	
# �����ȡһ��redis��name����ɾ����

type(name)	
# ��ȡname��Ӧֵ������

scan(cursor=0, match=None, count=None)
scan_iter(match=None, count=None)	
# ͬ�ַ�����������������������ȡkey


�ܵ�
redis-pyĬ����ִ��ÿ�����󶼻ᴴ�������ӳ��������ӣ��ͶϿ����黹���ӳأ�һ�����Ӳ����������Ҫ��һ��������ָ�������������ʹ��piplineʵ��һ������ָ������������Ĭ�������һ��pipline ��ԭ���Բ�����


#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
 
pool = redis.ConnectionPool(host='10.211.55.4', port=6379)
 
r = redis.Redis(connection_pool=pool)
 
# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)
 
pipe.set('name', 'alex')
pipe.set('role', 'sb')
 
pipe.execute()



��������


�����ߣ�
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
from monitor.RedisHelper import RedisHelper
 
obj = RedisHelper()
redis_sub = obj.subscribe()
 
while True:
    msg= redis_sub.parse_response()
    print msg

	
�����ߣ�
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
from monitor.RedisHelper import RedisHelper
 
obj = RedisHelper()
obj.public('hello')

����μ���https://github.com/andymccurdy/redis-py/
http://doc.redisfans.com/	


ʲôʱ���ù�ϵ�����ݿ⣬ʲôʱ�� ��NoSQL?
Go for legacy relational databases (RDBMS) when:

    The data is well structured, and lends itself to a tabular arrangement (rows and columns) in a relational database. Typical examples: bank account info, customer order info, customer info, employee info, department info etc etc.
    Another aspect of the above point is : schema oriented data model. When you design a data model (tables, relationships etc) for a potential use of RDBMS, you need to come up with a well defined schema: there will be these many tables, each table having a known set of columns that store data in known typed format (CHAR, NUMBER, BLOB etc).
    Very Important: Consider whether the data is transactional in nature. In other words, whether the data will be stored, accessed and updated in the context of transactions providing the ACID semantics or is it okay to compromise some/all of these properties.
    Correctness is also important and any compromise is _unacceptable_. This stems from the fact that in most NoSQL databases, consistency is traded off in favor of performance and scalability (points on NoSQL databases are elaborated below).
    There is no strong/compelling need for a scale out architecture ; a database that linearly scales out (horizontal scaling) to multiple nodes in a cluster.
    The use case is not for ��high speed data ingestion��.
    If the client applications are expecting to quickly stream large amounts of data in/out of the database then relational database may not be a good choice since they are not really designed for scaling write heavy workloads.
    In order to achieve ACID properties, lots of additional background work is done especially in writer (INSERT, UPDATE, DELETE) code paths. This definitely affects performance.
    The use case is not for ��storing enormous amounts of data in the range of petabytes��.

	
Go for NoSQL databases when:

    There is no fixed (and predetermined) schema that data fits in:
    Scalability, Performance (high throughput and low operation latency), Continuous Availability are very important requirements to be met by the underlying architecture of database.
    Good choice for ��High Speed Data Ingestion��. Such applications (for example IoT style) which generate millions of data points in a second and need a database capable of providing extreme write scalability.
    The inherent ability to horizontally scale allows to store large amounts of data across commodity servers in the cluster. They usually use low cost resources, and are able to linearly add compute and storage power as the demand grows.

source page https://www.quora.com/When-should-you-use-NoSQL-vs-regular-RDBMS 



	

