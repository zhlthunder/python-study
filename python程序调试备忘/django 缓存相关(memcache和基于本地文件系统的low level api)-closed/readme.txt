
django ��������ģʽ��
# �����������п��� ip �����Կ����ж������ip��������ip��
python manage.py runserver 0.0.0.0:8000

���ʷ�����http://128.1.2.170:8000


1.�����django��ʹ���ļ�ϵͳ��Ϊ���棺  ���˴�����The low-level cache API��Ӧ��ģʽ����
��django ���̵�settings.py�н����������ã�

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/www/html/server/tmp_cache/django_cache',
    }
}


ʹ��cache�ķ�����
��django app�� views.py��ʹ�÷������£�
from django.core.cache import cache   #����cache����

#����ķ����У��ص��עд�뻺��Ͷ�ȡ������֤�Ļ��ڣ��������ֿ��Ժ��ԡ�
from django.core.cache import caches
def login_accounts(request):
    err_msg = {}
    today_str = datetime.date.today().strftime("%Y%m%d")
    verify_code_img_path = "%s/%s" %(settings.VERIFICATION_CODE_IMGS_DIR,
                                     today_str)

    if not os.path.isdir(verify_code_img_path):
        #os.makedirs(verify_code_img_path,exist_ok=True)
        os.makedirs(verify_code_img_path)
    print("session:",request.session.session_key)
    #print("session:",request.META.items())
    random_filename = "".join(random.sample(string.ascii_lowercase,4))
    random_code = verify_code.gene_code(verify_code_img_path,random_filename)
    cache.set(random_filename, random_code,30) ##д�뻺����

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        _verify_code = request.POST.get('verify_code')
        _verify_code_key  = request.POST.get('verify_code_key')

        print("verify_code_key:",_verify_code_key)
        print("verify_code:",_verify_code)
        if cache.get(_verify_code_key) == _verify_code:  ##��ȡ�����е����ݽ�����֤
            print("code verification pass!")

            user =auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                #request.session.set_expiry(60*60)
                #return HttpResponseRedirect(request.GET.get("next") if request.GET.get("next") else "/")
                return HttpResponseRedirect("/monitor/1/")

            else:
                err_msg["error"] = 'Wrong username or password!'

        else:
            err_msg['error'] = "yangzhengma  error!"

    #return render(request,'index.html',{"filename":random_filename, "today_str":today_str, "login_err":err_msg})
    return render_to_response('index.html',{"filename":random_filename, "today_str":today_str, "login_err":err_msg})

 


˵���� ȷ�����ڻ�����ļ�ϵͳĿ¼��/var/www/html/server/tmp_cache/django_cache����django�Ĺ���Ŀ¼�£�
�������Ϊû��Ȩ�޶��޷����ʣ�django����ģʽû��Ȩ�޵����⣬��Ӧ�õ�appache�Ϻ󣬾ͻ�����������⣬�мǣ�



2.Memcached  (����������ʹ��ģʽ������ low-level api��ģʽ)
The fastest, most efficient type of cache supported natively by Django, Memcached is an entirely memory-based cache server, originally developed to handle high loads at LiveJournal.com and subsequently open-sourced by Danga Interactive. It is used by sites such as Facebook and Wikipedia to reduce database access and dramatically increase site performance.

Memcached runs as a daemon and is allotted a specified amount of RAM. All it does is provide a fast interface for adding, retrieving and deleting data in the cache. All data is stored directly in memory, so there��s no overhead of database or filesystem usage.


https://blog.csdn.net/a19881029/article/details/51213249  //Linux��Memcached�İ�װ��ʹ��
1)��װmemcached
Memcached�İ�װ����Libevent�����Ȱ�װLibevent��
    sean@sean:~$ tar -xzf libevent-1.4.14b-stable.tar.gz   
    sean@sean:~$ cd libevent-1.4.14b-stable/  
    sean@sean:~/libevent-1.4.14b-stable$ sudo ./configure -prefix /usr  
    sean@sean:~/libevent-1.4.14b-stable$ sudo make  
    sean@sean:~/libevent-1.4.14b-stable$ sudo make install  
    sean@sean:~/libevent-1.4.14b-stable$ sudo make clean  
	
Libevent���ᱻ��װ��/usr/lib��
    sean@sean:/usr/lib$ cd /usr/lib/  
    sean@sean:/usr/lib$ ll | grep libevent*  
    Binary file libevent-1.4.so.2.2.0 matches  
    libevent.la:dlname='libevent-1.4.so.2'  
    libevent.la:library_names='libevent-1.4.so.2.2.0 libevent-1.4.so.2 libevent.so'  
    Binary file libevent.so matches  
	
Ȼ��װMemcached��
    sean@sean:~$ tar -xzf memcached-1.4.25.tar.tar  
    sean@sean:~$ cd memcached-1.4.25/  
    sean@sean:~/memcached-1.4.25$ sudo ./configure -with-libevent=/usr  
    sean@sean:~/memcached-1.4.25$ sudo make  
    sean@sean:~/memcached-1.4.25$ sudo make install  
    sean@sean:~/memcached-1.4.25$ sudo make clean  
Memcached���ᱻ��װ��/usr/local/bin�£�
sean@sean:/usr/local/bin$ ll  
total 544  
drwxr-xr-x  2 root root   4096  4�� 21 21:32 ./  
drwxr-xr-x 10 root root   4096  2�� 18 07:12 ../  
-rwxr-xr-x  1 root root 545998  4�� 21 21:32 memcached* 

2)����memcached����
-m�������memcached������ڴ棬��MΪ��λ

-p�����������TCP�˿ڣ�Ĭ��ֵ��11211

-d���������ػ���������

-vv����ӡ��ϸ��Ϣ

-f���������ӣ�Ĭ��ֵ��1.25��ָ����ֵ�����1��


��������:
 ./memcached -m 64 -p 9999 -d -vv -u root
 
 ��������ӡһЩ��־��Ϣ��
 [root@localhost bin]# ./memcached -m 64 -p 9999 -d -vv -u root
[root@localhost bin]# slab class   1: chunk size        96 perslab   10922
slab class   2: chunk size       120 perslab    8738
slab class   3: chunk size       152 perslab    6898
slab class   4: chunk size       192 perslab    5461
slab class   5: chunk size       240 perslab    4369
slab class   6: chunk size       304 perslab    3449
slab class   7: chunk size       384 perslab    2730
slab class   8: chunk size       480 perslab    2184
slab class   9: chunk size       600 perslab    1747
slab class  10: chunk size       752 perslab    1394
slab class  11: chunk size       944 perslab    1110
slab class  12: chunk size      1184 perslab     885
slab class  13: chunk size      1480 perslab     708
slab class  14: chunk size      1856 perslab     564
slab class  15: chunk size      2320 perslab     451
slab class  16: chunk size      2904 perslab     361
slab class  17: chunk size      3632 perslab     288
slab class  18: chunk size      4544 perslab     230
slab class  19: chunk size      5680 perslab     184
slab class  20: chunk size      7104 perslab     147
slab class  21: chunk size      8880 perslab     118
slab class  22: chunk size     11104 perslab      94
slab class  23: chunk size     13880 perslab      75
slab class  24: chunk size     17352 perslab      60
slab class  25: chunk size     21696 perslab      48
slab class  26: chunk size     27120 perslab      38
slab class  27: chunk size     33904 perslab      30
slab class  28: chunk size     42384 perslab      24
slab class  29: chunk size     52984 perslab      19
slab class  30: chunk size     66232 perslab      15
slab class  31: chunk size     82792 perslab      12
slab class  32: chunk size    103496 perslab      10
slab class  33: chunk size    129376 perslab       8
slab class  34: chunk size    161720 perslab       6
slab class  35: chunk size    202152 perslab       5
slab class  36: chunk size    252696 perslab       4
slab class  37: chunk size    315872 perslab       3
slab class  38: chunk size    394840 perslab       2
slab class  39: chunk size    524288 perslab       2
<26 server listening (auto-negotiate)
<27 server listening (auto-negotiate)

 
 ����־��Ϣ�У����ǿ����˽⵽�ܶණ��

���Ⱦ���memcached���ڴ������ƣ�memcached�Ὣ�ڴ��Ϊ������С��ȵ�slab��ÿ��slab�ְ��̶���С�ֳ�����chunk������slab��ŵ����ӣ�slab��chunk�Ĵ�С��һ����������

����־�п��Կ�����memcached���ڴ��Ϊ��42����С��Ϊ1M��slab����ÿ��slab�ַ�Ϊ��С��ͬ������chunk������slab1��ÿ��chunk�Ĵ�СΪ120B��slab1���ܹ���8738��������chunk����slab42��ÿ��chunk�Ĵ�СΪ1M������slab42��ֻ����һ��chunk������slab��ŵ����ӣ�slab��chunk�Ĵ�С��1.25�ı���������slab1��120��slab2��150��150/120=1.25��������-fָ�����������ӵ�Ĭ��ֵ��

slab5��ÿ��chunk�Ĵ�СΪ240B������Ҫ���200B������ʱ�����ѡ��slab5�е�һ��chunk������ݣ����slab5�е�chunk����ʹ������ô�죿û��ϵ���ҵ�һ���������ʹ�ã�LRU��least recently used����chunk���������ݴ������У���ʹslab6���п��е�chunk����˵�memcached�б������ݵĴ�С����һ��ʱ���������ӹ��󽫵���memcahed���ڴ�ʹ���ʲ����Ǻܸ�
 

�鿴������������Ϣ��
[root@localhost bin]# ps aux | grep memcached
root     15105  0.0  0.0 115196  1532 ?        Ssl  00:14   0:00 ./memcached -m 64 -p 9999 -d -vv -u root
root     15184  0.0  0.0 103224   864 pts/0    S+   00:20   0:00 grep memcache


3.������memcached���
����memcached�������9999�˿ڣ����ǿ���ͨ��telnet�ķ�ʽ������memcached

    sean@sean:~$ telnet 127.0.0.1 9999  
    Trying 127.0.0.1...  
    Connected to 127.0.0.1.  
    Escape character is '^]'.  
	
֮�����ͨ��������Ӧ��������в���

������add key flag expire length	

add name 1 0 4    //����һ��key
sean    //Ҫ�洢������
STORED  	
	
flag����Ϊһ�����������������������л�����뻺�棬����Ҫȡ��ʱ�����跴���л�����ʱ�ɸ���flag��ֵ������Ӧ�ķ����л�������flag��ֵ��1������Ҫ�����л���ֵΪ2�������л�����ֵΪ3�������л�����

lengthΪ������ֽڳ���

��ѯ��get key
get name  
VALUE name 1 4  
sean  
END 


ɾ����delete key
    delete name  
    DELETED  
	
	
	
ִ����Ϣ������

[root@localhost bin]# telnet 127.0.0.1 9999
Trying 127.0.0.1...
<28 new auto-negotiating client connection
Connected to 127.0.0.1.
Escape character is '^]'.
add name 1 0 4
28: Client using the ascii protocol
<28 add name 1 0 4
sean
>28 STORED
STORED
get name
<28 get name
>28 sending key name
>28 END
VALUE name 1 4
sean
END
delete name
<28 delete name
>28 DELETED
DELETED

�滻��key������ڲ����滻����replace key flag expire length

���ã�key������ִ��������key����ִ���滻����set key flag expire length


�鿴״̬��stats
<28 stats
STAT pid 15105
STAT uptime 1165
STAT time 1523291646
STAT version 1.5.7
STAT libevent 2.1.8-stable
STAT pointer_size 64
STAT rusage_user 0.117982
STAT rusage_system 0.057991
STAT max_connections 1024
STAT curr_connections 2
STAT total_connections 5
STAT rejected_connections 0
STAT connection_structures 3
STAT reserved_fds 20
STAT cmd_get 2
STAT cmd_set 1
STAT cmd_flush 0
STAT cmd_touch 0
STAT get_hits 1
STAT get_misses 1
STAT get_expired 0
STAT get_flushed 0
STAT delete_misses 0
STAT delete_hits 1
STAT incr_misses 0
STAT incr_hits 0
STAT decr_misses 0
STAT decr_hits 0
STAT cas_misses 0
STAT cas_hits 0
STAT cas_badval 0
STAT touch_hits 0
STAT touch_misses 0
STAT auth_cmds 0
STAT auth_errors 0
STAT bytes_read 166
STAT bytes_written 168
STAT limit_maxbytes 67108864
STAT accepting_conns 1
STAT listen_disabled_num 0
STAT time_in_listen_disabled_us 0
STAT threads 4
STAT conn_yields 0
STAT hash_power_level 16
STAT hash_bytes 524288
STAT hash_is_expanding 0
STAT slab_reassign_rescues 0
STAT slab_reassign_chunk_rescues 0
STAT slab_reassign_evictions_nomem 0
STAT slab_reassign_inline_reclaim 0
STAT slab_reassign_busy_items 0
STAT slab_reassign_busy_deletes 0
STAT slab_reassign_running 0
STAT slabs_moved 0
STAT lru_crawler_running 0
STAT lru_crawler_starts 1530
STAT lru_maintainer_juggles 1459
STAT malloc_fails 0
STAT log_worker_dropped 0
STAT log_worker_written 0
STAT log_watcher_skipped 0
STAT log_watcher_sent 0
STAT bytes 0
STAT curr_items 0
STAT total_items 1
STAT slab_global_page_pool 0
STAT expired_unfetched 0
STAT evicted_unfetched 0
STAT evicted_active 0
STAT evictions 0
STAT reclaimed 0
STAT crawler_reclaimed 0
STAT crawler_items_checked 1
STAT lrutail_reflocked 0
STAT moves_to_cold 1
STAT moves_to_warm 0
STAT moves_within_lru 0
STAT direct_reclaims 0
STAT lru_bumps_dropped 0
END

�Ƴ٣�
quit

ͨ��get_hits/(get_hits + get_misses)�ܹ����������������


After installing Memcached itself, you��ll need to install a Memcached binding. There are several Python Memcached bindings available; the two most common are python-memcached and pylibmc.
To use Memcached with Django:


https://blog.csdn.net/dutsoft/article/details/71101809  //Python��Ŀʹ��memcached���� 

python-memcached ��װ��أ�
�Ȱ�װsix==1.10.0
�ٰ�װpython-memcached==1.59
��֤�� >>> import memcache


python-memcached ʹ�ã���python����ģʽ�£�
>>> import memcache
>>> mc = memcache.Client(['127.0.0.1:9999'],debug=0)
>>> mc.set("name","thunder")
<28 new auto-negotiating client connection
28: Client using the ascii protocol
<28 set name 0 0 7 
>28 STORED
True
>>> mc.get("name")
<28 get name
>28 sending key name
>28 END
'thunder'
>>> 



��django��Ŀ��ʹ��memcache��Ϊ����ķ�����

    Set BACKEND to django.core.cache.backends.memcached.MemcachedCache or django.core.cache.backends.memcached.PyLibMCCache (depending on your chosen memcached binding)
    Set LOCATION to ip:port values, where ip is the IP address of the Memcached daemon and port is the port on which Memcached is running, or to a unix:path value, where path is the path to a Memcached Unix socket file.

In this example, Memcached is running on localhost (127.0.0.1) port 11211, using the python-memcached binding:

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


��blog/views.py���������£�
import memcache

##login with yanzhengma  using memory as cache

def login_accounts(request):
    mc = memcache.Client(['127.0.0.1:9999'],debug=0)  #��������
    err_msg = {}
    today_str = datetime.date.today().strftime("%Y%m%d")
    verify_code_img_path = "%s/%s" %(settings.VERIFICATION_CODE_IMGS_DIR,
                                     today_str)
    
    if not os.path.isdir(verify_code_img_path):
        os.makedirs(verify_code_img_path)
    print("session:",request.session.session_key)
    #print("session:",request.META.items())
    random_filename = "".join(random.sample(string.ascii_lowercase,4))
    random_code = verify_code.gene_code(verify_code_img_path,random_filename)
    #cache.set(random_filename, random_code,30)
    mc.set(random_filename, random_code) ##�洢

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        _verify_code = request.POST.get('verify_code')
        _verify_code_key  = request.POST.get('verify_code_key')

        print("verify_code_key:",_verify_code_key)
        print("verify_code:",_verify_code)
        if mc.get(_verify_code_key) == _verify_code:  #��ȡУ��
		
            print("code verification pass!")

            user =auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                #request.session.set_expiry(60*60)
                #return HttpResponseRedirect(request.GET.get("next") if request.GET.get("next") else "/")
                return HttpResponseRedirect("/monitor/1/")



            else:
                err_msg["error"] = 'Wrong username or password!'

        else:
            err_msg['error'] = "yangzhengma  error!"

    #return render(request,'index.html',{"filename":random_filename, "today_str":today_str, "login_err":err_msg})
    return render_to_response('index.html',{"filename":random_filename, "today_str":today_str, "login_err":err_msg})






	

�ο��� 
https://docs.djangoproject.com/en/1.10/topics/cache/   django�������õĸ��ַ������ܵĹٷ��ĵ�
https://blog.csdn.net/u011510825/article/details/50394875   redis��Ϊcache�����÷���
https://blog.csdn.net/mrjiajia/article/details/48136385   django�������ø��ַ�������


 Python �� sixģ���� 
 

six : Six is a Python 2 and 3 compatibility library

Sixû���й���Github�ϣ������й�����Bitbucket�ϣ�������Щ�������ص㣬�ص����������á�

������֪ Python 2 �� Python 3 �汾�ķ��Ѹ� Python �������Ǵ����˺ܴ�ķ��գ�Ϊ��ʹ����ͬʱ���������汾������Ҫ���Ӵ����Ĵ��롣 ���� Six �����ˡ��������Ľ�����˵������һ��ר���������� Python 2 �� Python 3 �Ŀ⡣����������� urllib �Ĳ��ַ��������ݣ� str �� bytes ���Ͳ����ݵȡ�֪�������⡣

����Ч����ô����pypi�ϵ���ʮ�����ϣ����¼����������������˵���ˡ�Ҫ֪������ Flask �� Django ����֪���Ŀ⣬��������Ҳֻ�м�ʮ��
