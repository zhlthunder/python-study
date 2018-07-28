#I8350 风扇调速  （BMC shell(root/root)--ushell(zte/zte)--sh 1）
BSP_DbgFanTest(1)    //关闭风扇调速策略
BSP_SetFanPwm(0xff)  //手动设置风扇占空比，参数01-ff
BSP_GetFanRpm()             //读取风机转速

###串口切换(BMC)
BSP_SetPanelUart(1)   //HOST UArt
BSP_SetPanelUart(0)   //BMC UArt
BSP_SetPanelUart(3)   //expander UArt --问下谢焕军，如确认expander的版本信息

###ipmitool 命令行访问：
C:\IPMItool>ipmitool -I lanplus -H 192.168.5.90 -U zteroot -P superuser
No command provided!
Commands:
        raw           Send a RAW IPMI request and print response
        i2c           Send an I2C Master Write-Read command and print response
        spd           Print SPD info from remote I2C device
        lan           Configure LAN Channels
        chassis       Get chassis status and set power state
        power         Shortcut to chassis power commands
        event         Send pre-defined events to MC
        mc            Management Controller status and global enables
        sdr           Print Sensor Data Repository entries and readings
        sensor        Print detailed sensor information
        fru           Print built-in FRU and scan SDR for FRU locators
        gendev        Read/Write Device associated with Generic Device locators sdr
        sel           Print System Event Log (SEL)
        pef           Configure Platform Event Filtering (PEF)
        sol           Configure and connect IPMIv2.0 Serial-over-LAN
        isol          Configure IPMIv1.5 Serial-over-LAN
        user          Configure Management Controller users
        channel       Configure Management Controller channels
        session       Print session information
        sunoem        OEM Commands for Sun servers
        kontronoem    OEM Commands for Kontron devices
        picmg         Run a PICMG/ATCA extended cmd
        fwum          Update IPMC using Kontron OEM Firmware Update Manager
        firewall      Configure Firmware Firewall
        exec          Run list of commands from file
        set           Set runtime variable for shell and exec
        hpm           Update HPM components using PICMG HPM.1 file
        ekanalyzer    run FRU-Ekeying analyzer using FRU files

####在ipmitool下使用sol activate 打开sol功能后，linux系统下，可以直接映射命令行的访问(前提是串口功能要打开才可以)
####linux系统配置好串口后，可以用串口登陆到命令下，进行相关的shell操作
####只连接管理口的情况下，host为list时，可以用sol 功能，直接登录host的命令行


0xff--5700rpm

0xe9--5000rpm
0xd1--4500rpm
0xc1--4100~4200rpm
0xbb--4000rpm
0xa1--3500rpm  
0x8c--3000rpm  

#linux raid控制图形管理工具调用命令
./startupui.sh


#LSI mega 命令行操作
./storcli.exe    /c0    show    all  （查询当前控制器下的盘信息 ，需关注 EID:Slt  用于后续操作）
./storcli.exe /c0 /exxx /sxx    set    good （将此盘转为 Unconfig Good ）
./storcli.exe /c0    /f    all    del （清除新加入盘的 RAID 配置信息 ）
./storcli.exe    /c0    /exxx    /sxx    add    hotsparedrive （盘转为热备盘 ）

#PMC raid命令行配置：
ARCCONF GETCONFIG <Controller#> [AD|LD [LD#]|PD|MC|AL]

#bash默认命令
/usr/local/bin/
/bin/ 

#创建链接命令
ln -s /home/thunder/storcli-linux  /bin/storcli_lnk

#fio 2.1.14 具有gfio模块，编译此模块的方法
cd到fio目录后，用
./configure --enable-gfio
make fio
make gfio
./fio -S (fio server模式)
在另一个终端输入./gfio启动client模式


#gfio 配置脚本中，directory是进行IO测试的目标路径
在第一次创建时，可以看到动态的波形图，第二次测试时，建议把这个文件先删除

#linux下裸盘格式化
mkfs /dev/sdb, 不格式化，有时可能无法进行读写
mkdir /mnt/vfat
mount -t ext2 /dev/sdb /mnt/vfat


#常用解压命令：
总结 
1、*.tar 用 tar –xvf 解压 
2、*.gz 用 gzip -d或者gunzip 解压 
3、*.tar.gz和*.tgz 用 tar –xzf 解压 
4、*.bz2 用 bzip2 -d或者用bunzip2 解压 
5、*.tar.bz2用tar –xjf 解压 
6、*.Z 用 uncompress 解压 
7、*.tar.Z 用tar –xZf 解压 
8、*.rar 用 unrar e解压 
9、*.zip 用 unzip 解压


01-.tar格式
解包：[＊＊＊＊＊＊＊]$ tar xvf FileName.tar
打包：[＊＊＊＊＊＊＊]$ tar cvf FileName.tar DirName（注：tar是打包，不是压缩！）

02-.gz格式
解压1：[＊＊＊＊＊＊＊]$ gunzip FileName.gz
解压2：[＊＊＊＊＊＊＊]$ gzip -d FileName.gz
压 缩：[＊＊＊＊＊＊＊]$ gzip FileName

03-.tar.gz格式
解压：[＊＊＊＊＊＊＊]$ tar zxvf FileName.tar.gz
压缩：[＊＊＊＊＊＊＊]$ tar zcvf FileName.tar.gz DirName

04-.bz2格式
解压1：[＊＊＊＊＊＊＊]$ bzip2 -d FileName.bz2
解压2：[＊＊＊＊＊＊＊]$ bunzip2 FileName.bz2
压 缩： [＊＊＊＊＊＊＊]$ bzip2 -z FileName

05-.tar.bz2格式
解压：[＊＊＊＊＊＊＊]$ tar jxvf FileName.tar.bz2
压缩：[＊＊＊＊＊＊＊]$ tar jcvf FileName.tar.bz2 DirName

#linux下软件查询和安装命令
rpm -ql | grep "***"
rpm -e ***卸载软件



#部门dell服务器信息

部门内dell服务器(9MZGY02)
root/  HardTest1
IDRAC ip: 192.168.0.120
（IDRAC:integrated dell remote access controller）

#基本的IPMI 命令和ZTE相同,且ipmi命令格式如下：
ipmitool -H *.*.*.*（管理IP） -I lanplus -U <用户名> -P <密码>


#R5300 测试版本
ftp://10.43.166.8//2015中移动集采测试版本//R5300//中移测试现场所有固件版本

RSS RSS

BMC:BMC_SGLMA_P3_R_V02.01.62.07_201508281414.BIN
EPLD:SGLMA_01_140201_EPLD_102.vpd

#linux 命令：
cat /proc/cpuinfo | grep name | uniq -c | cut -d: -f2
uniq -c:用于计数，显示“重复次数：主板名”
cut -d: -f2 (定义分隔符为：，只输出第二个域field)cut是一个选取命令，就是将一段数据经过分析，取出我们想要的。一般来说，选取信息通常是针对“行”来进行分析的
主要参数
-b ：以字节为单位进行分割。这些字节位置将忽略多字节字符边界，除非也指定了 -n 标志。
-c ：以字符为单位进行分割。
-d ：自定义分隔符，默认为制表符。
-f  ：与-d一起使用，指定显示哪个区域。

#wc:Linux系统中的wc(Word Count)命令的功能为统计指定文件中的字节数、字数、行数，并将统计结果显示输出
命令参数：

-c 统计字节数。

-l 统计行数。

-m 统计字符数。这个标志不能与 -c 标志一起使用。

-w 统计字数。一个字被定义为由空白、跳格或换行字符分隔的字符串。

### HDD 操作命令备注：
sas1064e/sas1068e:cfggen-linux (command:cfggen-linux list;cfggen-linux 0 status；cfggen-linux 0 display)

SAS2(SAS2008/2308): (含linux,windows)
sas2ircu-linux (command:sas2ircu-linux list;sas2ircu-linux 0 status;sas2ircu-linux 0 display)
lsiutil-1.71-linux （command:./lsiutil-1.71-linux-x64 -p1 -a 1,8,16,66,60,0;./lsiutil-1.71-linux-x64 -p1 -a 21,1,2,3,0,0,0）

SAS3008: (含linux,windows)
sas3ircu-linux (command:sas3ircu-linux list;sas3ircu-linux 0 status,sas3ircu-linux 0 display)
lsiutil-1.71-linux （command:./lsiutil-1.71-linux-x64 -p1 -a 1,8,16,66,60,0;./lsiutil-1.71-linux-x64 -p1 -a 21,1,2,3,0,0,0）

LSI MegaRaid (SAS2208/9361-8I...)(含linux,windows)
storcli-linux (command:storcli-linux /c0 show all;storcli-linux /c0 /vall show all;storcli-linux /c0 /eall /sall show all)

PMC 6805/7805:(含linux,windows)
arcconf-linux (command:arcconf-linux  getconfig 1 (AD/PD..))

Disk information checking:
lsscsi;lsblk;diskman** -g;diskman** -d;smartctl -a /dev/sg*/ diskman*** -i /dev/sg*; diskman*** -I /dev/sg*;fdisk -l;df -h;tune2fs -l /dev/sd**;

dmesg; cat /proc/cpuinfo;/var/log/messages;

###driver information check
modinfo mpt2sas --lsi HBA
modinfo megaraid_sas ---lsi megaraid
modinfo aacraid --PMC 6805/7805


####
BMC--OFF SPAN
HOST--IN SPAN

##分区及格式化
parted /dev/sdb--mklabel--gpt--yes--p--mkpart--gpt4t--ext4--1或0--(-1)--P--Q (sdb/sdb1)
mkfs.ext4 /dev/sdb1

一条命令实现：parted /dev/sdb rm 1  删除分区
一条命令实现： parted /dev/sdb mkpart gpt4t ext4 0 4000GB I
 parted /dev/sdb mkpart gpt4t ext4 0 1997GB I

##命令用法举例：
ifconfig eth0 | grep [B,b]cast |awk -F: '{print "IP_address:" $2}' | awk '{print $1}'


###linux引导时提示挂载时间错误的问题
fsck -y /dev/sda1, fsck -y /dev/sda2, fsck -y /dev/sda3

##确认redhat 版本
cat /etc/redhat-release 

##yum更新路径
baseurl=ftp://redhat:redhat@129.0.0.50/

##系统宕机时，查看：
service kdump status/start  记录的日志为：/var/crash
触发的命令：echo c > /proc/sysrq-trigger 
触发之后可以kdump开始记录日志信息

#### linux shell编程循环,和C语言相同
 退出命令：break
  继续：continue

#linux下PMC管理地址：
https://129.0.0.77:8443/maxview/manager/login.xhtml 
(Tomcat Service)

####
kdump是一种先进的基于kexec的内核崩溃转储机制。当系统崩溃时，kdump使用kexec 启动到第二个内核。第二个内核通常叫做捕获内核，以很小内存启动以捕获转储镜像。第一个内核保留了内存的一部分给第二内核启动用。由于kdump利用kexec启动捕获内核，绕过了 BIOS，所以第一个内核的内存得以保留。这是内核崩溃转储的本质。kdump需要两个不同目的的内核，生产内核和捕获内核。生产内核是捕获内核服务的对像。捕获内核会在生产内核崩溃时启动起来，与相应的ramdisk一起组建一个微环境，用以对生产内核下的内存进行收集和转存。注意，在启动时，kdump保留了一定数量的重要的内存，为了计算系统需要的真正最小内存，加上kdump使用的内存数量，以决定真正的最小内存的需求。
为了更好的容错，这个机制最好还是启用 

####查看IO信息
iostat -x -d 2 /dev/sdb
iostat -x -d 2

### scp命令
scp /home/thunder/zhl_jack.txt  root@129.0.0.54:/home/
scp root@129.0.0.54:/home/zhl.txt /home/thunder

###linux系统中如何切换拼音输入法
ctrl+空格

###ftp功能设置：
 1. 先用rpm -qa| grep vsftpd命令检查是否已经安装，如果ftp没有安装，使用yum  -y  install vsftpd 安装,(ubuntu 下使用apt-get install vsftpd)

2. service vsftpd start

启动要让FTP每次开机自动启动，运行命令:  chkconfig --level 35 vsftpd on

3. 设置ftp权限

vi  /etc/vsftpd/vsftpd.conf
将anonymous_enable=YES 改为 anonymous_enable=NO
ESC返回,输入“:wq”保存并推出

4. 添加ftp帐号和目录

useradd   -d /alidata/www/wwwroot -s /sbin/nologin pwftp
passwd   pwftp
chmod -R 755 /alidata/www/wwwroot
chown -R  pwftp /alidata/www/wwwroot
/etc/rc.d/init.d/vsftpd restart
然后用帐号pwftp密码123456
测试下就可以登陆ftp了。目录是/alidata/www/wwwroot


####linux系统日志文件确认：
dmesg; /var/log/messages
dmesg | tail (显示尾部的信息)
dmesg -c (清除信息)

#### dd 硬盘测试
测试硬盘写能力：time dd if=/dev/zero of=/dev/sdb bs=8k count=300000  
测试硬盘读能力：time dd if=/dev/sda of=/dev/null bs=8k count=300000
执行过程中用 iostat -x -d 2查看读写， 执行后用dmesg查看是否有错误


#####iostat输出结果确认事项：
cpu属性值说明：

%user：CPU处在用户模式下的时间百分比。

%nice：CPU处在带NICE值的用户模式下的时间百分比。

%system：CPU处在系统模式下的时间百分比。

%iowait：CPU等待输入输出完成时间的百分比。

%steal：管理程序维护另一个虚拟处理器时，虚拟CPU的无意识等待时间百分比。

%idle：CPU空闲时间百分比。

备注：如果%iowait的值过高，表示硬盘存在I/O瓶颈，%idle值高，表示CPU较空闲，如果%idle值高但系统响应慢时，有可能是CPU等待分配内存，此时应加大内存容量。%idle值如果持续低于10，那么系统的CPU处理能力相对较低，表明系统中最需要解决的资源是CPU。

disk属性值说明：

rrqm/s:  每秒进行 merge 的读操作数目。即 rmerge/s

wrqm/s:  每秒进行 merge 的写操作数目。即 wmerge/s

r/s:  每秒完成的读 I/O 设备次数。即 rio/s

w/s:  每秒完成的写 I/O 设备次数。即 wio/s

rsec/s:  每秒读扇区数。即 rsect/s

wsec/s:  每秒写扇区数。即 wsect/s

rkB/s:  每秒读K字节数。是 rsect/s 的一半，因为每扇区大小为512字节。

wkB/s:  每秒写K字节数。是 wsect/s 的一半。

avgrq-sz:  平均每次设备I/O操作的数据大小 (扇区)。

avgqu-sz:  平均I/O队列长度。

await:  平均每次设备I/O操作的等待时间 (毫秒)。

svctm: 平均每次设备I/O操作的服务时间 (毫秒)。

%util:  一秒中有百分之多少的时间用于 I/O 操作，即被io消耗的cpu百分比

备注：如果 %util 接近 100%，说明产生的I/O请求太多，I/O系统已经满负荷，该磁盘可能存在瓶颈。如果 svctm 比较接近 await，说明 I/O 几乎没有等待时间；如果 await 远大于 svctm，说明I/O 队列太长，io响应太慢，则需要进行必要优化。如果avgqu-sz比较大，也表示有当量io在等待。




#### txt文件转换为csv文件命令
sort *.txt > *.csv

###硬盘体检：fsck, e2fsck
fsck/e2fsck -c  (Check for bad blocks and add them to the badblock list)
hdparm -t /dev/sda ( -t   评估硬盘的读取效率。)


###标卡固件更新方法：
1）制作dos启动盘，启动进入DOS后，执行eeupdate回车，显示具体的nic号
2）烧结网卡的固件使用命令如下：eeupdate -nic=x  -data=xxxx.txt

补充：
通过DOS启动盘烧结网卡MAC方法
1、制作DOS启动U盘（大白菜等软件）
2、将Eeupdate.exe工具和固件映像（例如1G的映像：i350_KX_NO-MNG_1_52.txt）放入U盘s
3、刀片启动进入DOS后，执行eeupdate回车，显示具体的nic号，母板的是0、1
4、烧结网卡的固件使用命令如下
eeupdate -nic=x  -data=xxxx.txt
5、烧结网卡的MAC使用命令如下
eeupdate -nic=x -mac=001122334455


####lsi 2308 固件和bios更新方法
1）将固件和bios 与lsiutil工具放到相同的目录
2）1--查看bios和固件的版本
   2--升级固件
   4--升级bios

####网卡查询：
lspci | grep "Ethernet"
ifconfig -a
ethtool ethx
ethtool -i ethx

#####linux下VNC使用步骤归纳：
1）vnc 软件安装 2）启动VNCserver 3)关闭防火墙 4）修改配置文件/root/.vnc/xstartup,(# unset SESSION_MANAGER   # exec /etc/X11/xinit/xinitrc) 去掉这两行的注释，5）vncserver -kill :1 6）vncserver :1 7）在PC端打开VNC即可使用。

#### fio测试命令：

fio -name=testc -filename=/dev/sda -bs=256k --rw=write -iodepth=32 -runtime=4h  -direct=1 -numjobs=30 -time_based  -ioengine=psync -thread -group_reporting

####常用压缩和解压
tar zcvf servertool~.tar.gz servertool~/
tar xzf  servertool~.tar.gz

#### linux系统下下载的程序
bin文件，可以直接增加执行权限后执行
源码文件，需要编译安装

###centos 7：
systemctl stop firewalld.service #停止
systemctl disable firewalld.service #禁用
之前的版本：
service iptables stop #停止
chkconfig iptables off #禁用

#####netstat | grep ssh

####PMC 6805固件更新方法：
./arcconf romupdate 1 xxxx.ufi

E9000：
机框：129.5.101.143
刀片ip:192.168.12.181  root/123456
E9000自研卡：
raid卡 --S600 S620 S610
FC卡--N500
网卡--N720


######gfio相关
./confiture --enable-gfio
make fio
make gfio
./fio -S
./gfio
每次使用前先删除上次读写的文件，波形不是每次都可以出来，可以用iostat -x -d 2 来查看硬盘是否在进行读写，有时第一次无法正常开始，但第二次就可以了

####libaio
yum install libaio-devel （从本地的光驱ftp中下载）
-- Make clean—make—make install 


#####mcelog:
yum install -y mcelog* 
安装完成后，在/etc下生产mcelog的目录，且目录下有mcelog.conf 文件， 安装之前，没有/etc/mcelog目录

service kdump status --确认kdump是否打开

安装系统的时候安装kdump


###查看串口：
dmesg | grep ttyS* 

####串口配置方法：
/etc/grub.conf中，这个文本（initrd /initramfs-2.6.32-431.el6.x86_64.img）
之前增加 console=ttyS0,115200

/etc/inittab 中，这个文本（id:5:initdefault:）之后增加
co:2345:respawn:/sbin/agetty ttyS0 115200 vt100 init q   /for rhel
co:2345:respawn:/sbin/agetty -L 115200  ttyS0 ansi    /for SLES

/etc/securetty中，文本最后增加ttyS0

重启server后，在串口终端可以看到host的打印信息


####网络性能（netperf）
1)使用软件：netperf-2.6.0.tar.bz2 （tar –jxvf, ./configure; make; make installl）,之后用whereis netperf 和whereis netserver查询软件的信息确认软件已经安装成功
2)服务端运行：netserver -p 10000（端口地址可以任意）
3)客户端运行： netperf -H 128.0.0.62（服务端IP地址） -l 72000（测试时间，单位s） -t TCP_STREAM -p 10000（也可以不指定）
4)使用下面的命令查询命令进程的信息
ps aux | grep netperf
ps aux | grep netserver
5)用ifconfig 查询每个网卡的收发包的信息
6)不要用127.*.*.*的IP地址，这个地址是系统预留给自己的IP地址段
7)用pkill netperf ,pkill netserver 来关闭进程
remark:
两台服务器相互灌包的测试模式：
两台服务器上都运行netserver 
每个服务器分别向对方的两个网口执行netperf命令，增加压力模式


####网络性能测试（ixchariot）
1)使用软件：6endpoint.tar.gz（tar -zxvf/xzf; ./endpoint.install,一直按空格，最后输入：accept_license）安装完毕；
2）调试机上安装windows版本的客户端；
3）测试时，只需在客户端进行设置即可，服务器端不用任何配置
客户端打开，点击图标（两个方框连线）--》填写测试的命名、两个endpoint的IP地址，select script,选择之后修改并保存即可完成自动化测试；

灌包测试实例：
129.00.0.55(server #1)
[root@localhost etc]# ps aux | grep netserver
root     21252  0.0  0.0   8980   372 ?        Ss   16:01   0:00 netserver -p 10000

[root@localhost etc]# ps aux | grep netperf
root     21575 45.3  0.0  11068   956 pts/2    S    16:04  38:08 netperf -H 128.0.0.61 -l 36000 -t TCP_STREAM -p 10000
root     21884 44.6  0.0  11068   956 pts/2    S    16:08  35:45 netperf -H 172.0.0.61 -l 36000 -t TCP_STREAM -p 10000


129.0.0.53(server #1)
[root@localhost network-scripts]# ps aux |grep netserver
root     20672  0.0  0.0   8980   372 ?        Ss   06:23   0:00 netserver -p 10000

[root@localhost network-scripts]# ps aux |grep netperf
root     23043 25.6  0.0  11068   960 pts/3    S+   06:41  17:45 netperf -H 128.0.0.62 -l 72000 -t TCP_STREAM -p 10000
root     23092 25.5  0.0  11068   956 pts/4    S+   06:42  17:29 netperf -H 172.0.0.62 -l 72000 -t TCP_STREAM -p 10000


####硬盘IO测试：（fio）
1)使用软件：fio-2.1.14.tar.bz2
2）现在安装fio(tar -xjf; ./configure; make; make install)
2)安装gfio (./configure --enable-gfio;make fio; make gfio;)
3)执行：
./fio -S  ./gfio

测试前提（硬盘—》创建分区--》格式化（mkfs.ext4  /dev/sdb1）-->挂载 
mount -t ext4 /dev/sdb1 /home/test）

fio -name=testc -filename=/dev/sdb1 -bs=4k --rw=randread -iodepth=32 -size=512m  -direct=1  -ioengine=libaio

经验证，fio和gfio测试结果相当

###libaio
yum install libaio-devel （从本地的光驱ftp中下载）
-- Make clean—make—make install   ==>此时就可以正常使用libaio了


#####Linux 中查看网口流量的利器 -- sar 
sar -n DEV 2

### 服务器故障排查初步步骤：
1、确认服务器是否能够上电，如果完全不能加电，开盖检查cpu、内存、硬盘以及板卡的安装情况；
2、如果能加电，不能启动，看下启动的信息；
3、如果安装了系统无法启动，请确认启动盘选择是正确的

#### 网络端口确认：
netstat -ntl

####
问题：服务器异常关机或 正在跑压力程序不小心按到电源键导致关机后后，开机无法进行图形模式了
   在串口下，可以进入命令行模式； 接显示器时按某个键也可以进入命令行模式

对策：用fsck修复所有分区后，重启就可以进入图形界面了。

####建立快速ftp配置项：
1） useradd  username, passwd username
2) vi /etc/vsftpd/vsftpd.conf
anonymous_enable=no
ascii_upload_enable=YES
3)服务重启，关闭两重安全保障

#####BMC busyBOx的ftp 上传下载命令：
/FLASH2 # ftpput
BusyBox v1.23.2 (2015-06-02 19:14:34 CST) multi-call binary.

Usage: ftpput [OPTIONS] HOST [REMOTE_FILE] LOCAL_FILE

Upload a file to a FTP server

        -v,--verbose            Verbose
        -u,--username USER      Username
        -p,--password PASS      Password
        -P,--port NUM           Port

/FLASH2 # ftpput -u zte -p zte 192.168.5.121 parsesel parsesel

/FLASH2 # ftpget
BusyBox v1.23.2 (2015-06-02 19:14:34 CST) multi-call binary.

Usage: ftpget [OPTIONS] HOST [LOCAL_FILE] REMOTE_FILE

Download a file via FTP

        -c,--continue           Continue previous transfer
        -v,--verbose            Verbose
        -u,--username USER      Username
        -p,--password PASS      Password
        -P,--port NUM           Port

/FLASH2 # ftpget -u zte -p zte 192.168.5.121 aa.txt aa.txt


####windows自带DNS 路径：
C:\Windows\System32\drivers\etc\hosts

#####specpower 运行说明：
1）调试机和服务器上都要安装运行java和specpower软件；
32bin windows调试机，安装对应的java(jdk-6u10-rc2-bin-b32-windows-i586-p-12_sep_2008.zip)
64bin windows服务器，直接把ibm_sdk70.zip copy到某个路径下解压后即可，不用安装；java所在的目录：（\ibm_sdk70\jre\bin\java.exe） 
2）copy SPECpower_2008安装文件到系统任意目录
3）在SUT 端：打开cmd窗口，进入java目录路径，运行java命令（java –jar E:\SPEC_2008\setup.jar），之后一路next安装完成；
4）在调试机上，直接双击setup.jar安装即可；

5）不测试温度和功率的情况下的基本设置如下：
SUT端： 将本地的runssj_yd.bat的拷贝并替换掉SPECpower_2008安装目录下ssj目录下的runssj.bat脚本，并做如下修改：
a)?
:: Set the number of JVMs to run
set JVMS=8
(设定JVM线程数，设定原则是JVMS个数一般是由逻辑cpu总数除以4或者2得出，要能被整除)
b)set DIRECTOR_HOST=129.1.6.100(为实际的调试机的IP)
c)set JAVA=C:\eclipseDevelopmentPackage\ibm_sdk70\bin\java (为实际的java程序所在的路径)

控制端设置：
a)set NUM_HOSTS=1   ///(设置待测试设备的数量)
b)
:: Properties file to be passed to Director
::set PROPFILE=SPECpower_ssj_EXPERT.props
set PROPFILE=SPECpower_ssj.props
3)	设置director引导配置文件，在正式测试时一定要选择默认的SPECpower_ssj.props，而在调试过程中，设置为SPECpower_ssj_EXPERT.props后，可以在SPECpower_ssj_EXPERT.props中修改测试的时长，负荷序列等等

c)C:\SPECpower_ssj2008\PTDaemon目录，编辑runpower.bat文件
set DEVICE=0 是默认项，意思是没有接功率仪器的测试

d)打开SPECpower_2008目录，进入ccs目录,如果没有温度传感器，或者功率测试仪，可以在ccs.props将其对应项temp1，pwr1注释掉。
#ccs.ptd = pwr1, temp1

6)执行顺序
在控制端，返回SPECpower_2008安装目录，进入ssj子目录，运行rundirector.bat脚本
切换到SUT端，进入SPECpower_2008安装目录，进入ssj子目录，运行runssj.bat 脚本
切换到控制端，进入SPECpower_2008安装目录，进入ccs子目录，运行runCCS.bat脚本

7）SPECpower_2008完整测试一次，需要73分钟左右；如果使用SPECpower_ssj_EXPERT.props这个按个人需求定制，则时长需自己计算

8）测试完成，在SPECpower_2008安装目录，自动生成result子目录，进入该目录，可以查看结果（自动生成的ssj.0036-main.html文件里，如果没有生成报告请参考此文档查看原因）在result子目录，还有power，ssj_ops等相应的结果

注意事项：
1）IP 要正确，防火墙要关闭；
2）SUT端如果不设置“内存锁定页”，即将administator加到内存锁定中，会导致SUT运行runssj.bat后自动关闭，所以这项一定要设置才可以正常进行测试
3)不监控power的情况下，specpower只可作为一个压力测试软件，测试结果没有任何意义


####
  windows操作系统中，可以用2种方法查看系统日志：

         一、开始---控制面板---管理工具---事件查看器---系统日志；

         二、开始---运行---cmd---eventvwr---即可查看系统日志

##### sed命令：

sed -i '/SELINUX/s/enforcing/disabled/g' /etc/selinux/config



service iptables stop



chkconfig iptables off



sed -i '$a\IPADDR=*.*.*.*' ifcfg-eth1



sed -i '$a\NETMASK=' ifcfg-eth1


sed -i'1a\zzzzz' zhl_init.sh 


###########sed:
sed 's/zhuhonglei/good/g' sed_grep.txt
sed 's/^/&id /g' sed_grep.txt 
sed 's/$/&id /g' sed_grep.txt 
sed '/zhuhonglei/a ############' sed_grep.txt
sed '/zhuhonglei/i ############' sed_grep.txt
sed '$ a ##########' sed_grep.txt
sed '/name/s/zhuhonglei/jack/g' sed_grep.txt 
sed -n '1p' sed_grep.txt 
sed -n '$p' sed_grep.txt
sed -n '/zhuhonglei/p' sed_grep.txt
sed '1s/^/& zhuhonglei/g' /etc/sysconfig/iptables  在第一行的开头追加
sed 's/lo/& zhuhonglei/g' /etc/sysconfig/iptables  定位在lo之后追加
sed '/lo/a zhuhonglei' /etc/sysconfig/iptables  匹配有lo的行之后追加

##########grep:
cat sed_grep.txt  | grep "my"
cat sed_grep.txt  | grep "^192.168$"
cat sed_grep.txt  | grep "[0-9]"
cat sed_grep.txt  | grep "[a-z]"
cat sed_grep.txt | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}"
grep -i
grep -n
grep -v
egrep "192|name" sed_grep.txt
grep -E "192|name" sed_grep.txt 

##########awk
cat awk.txt | awk '{print $NF}'
ifconfig eth9 | grep "inet add" | awk '{print $2}'| awk -F: '{print $2}'
ifconfig eth9 | grep "inet add" | awk '{print $2}'| awk -F: '{print "ipaddress:" $2}'
ipmitool -I open sensor | awk -F "|" '{if($1=/Fan FAN1/) printf("%i",$2)}'

##########find
find . -maxdepth 1  -name "*.txt" -mtime -1
find . -maxdepth 1  -name "*.txt" -mtime -1 -exec rm -rf {} \;

####备份与增量备份：
tar -g /home/jack/snapshort -czvf /home/jack/system_full_backup.tar.gz /home/thunder
tar -g /home/jack/snapshort -czvf /home/jack/system_add_backup.tar.gz /home/thunder/

####后台执行且不挂起命令：
nohup ./cron_test.sh (check with aux (cron*))
使用这个命令，打印信息也不输出到终端显示

关闭： kill processID


#######crontab相关
时间确认和同步相关：
date
date -s
ntpdate 129.0.0.50

用CRONTAB，每10分钟运行一次指令 */10  * * * *

编辑：crontab -e 

查看：crontab -l
*/10 * * * * /bin/bash /home/thunder/cron_test.sh >> /home/thunder/log.txt
（可以将crontab里的内容直接在命令行执行，看看效果，如果可以执行再加入crontab中即可）

linux定时任务查看日志：（所有和定时任务相关的动作都记录在里面）
/var/log/cron*是crontab的执行日志


cat /var/log/secure | grep -i password | egrep -o "([0-9]{1,3}\.){3}[0-9]{1,3}" | sort -nr | uniq -c | awk '$1>=4{print $2}'

#######同步命令：
rsync -av /home/jack/ /home/jack1/    保留目标路径下的差异
rsync -aP --delete /home/jack/ /home/jack1/  完全同步


#######linux 下监控软件配置说明：
rpm -ivh 
vi /etc/hardwaremonitor.conf 
rpm -qa | grep hardwaremon*
rpm -e linux-hardwaremon-v00.02.01-2.x86_64
/etc/init.d/hwmd status