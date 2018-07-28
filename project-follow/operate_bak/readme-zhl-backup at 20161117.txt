
############################################################

使用linux系统下的ipmitool查看串口信息：
安装ipmitool工具
modprobe ipmi_devintf
配置和目标BMC地址相同的网段的IP地址，确认可以ping通
用telnet登陆目标BMC地址后，port 10000,zte/zte--sh1--BSP_SetPanelUart(1)切换目标主机的串口到host端
ipmitool -I lanplus -H 192.168.5.78(目标BMC地址) -U zteroot -P superuser sol activate



##############################################################
5300 串口相关配置总结：
使用BMC的地址进行telnet port 10000 访问: zte/zte, 
进入admin # 目录
如果直接连接host串口线，在串口界面下查看的初始状态也是 admin # --串口下, 即两种方式功能相同
执行sh 1, 切换到bsproc# 目录，
再执行如下命令，进行串口切换： 
###串口切换(BMC)  或使用uartswi() 进行 host和BMC 两者之间的切换
BSP_SetPanelUart(1)   //HOST UArt
BSP_SetPanelUart(0)   //BMC UArt
BSP_SetPanelUart(3)   //expander UArt

####串口配置方法：
/etc/grub.conf中，这个文本（initrd /initramfs-2.6.32-431.el6.x86_64.img）
之前增加 console=ttyS0,115200   --只用这条也可以完成配置。

{/etc/inittab 中，这个文本（id:5:initdefault:）之后增加
co:2345:respawn:/sbin/agetty ttyS0 115200 vt100 init q   /for rhel
co:2345:respawn:/sbin/agetty -L 115200  ttyS0 ansi    /for SLES

/etc/securetty中，文本最后增加ttyS0

重启server后，在串口终端可以看到host的打印信息

在ipmitool中查看串口的方法：
ipmitool -I lanplus -H 192.168.5.78 -U zteroot -P superuser sol activate (开启命令)
ipmitool -I lanplus -H 192.168.5.78 -U zteroot -P superuser sol deactivate（关闭命令）



查看串口设备：dmesg | grep ttyS* 
查看串口个数： dmesg |gre ttyS*
查看串口驱动：cat /proc/tty/driver/serial
查看串口的波特率等配置信息： stty -a -F /dev/ttyS0
查看串口权限： ls -l /dev/ttyS*
################################################
5300 串口打印确认：
5300 串口：
使用BMC的地址进行telnet port 10000 访问: zte/zte, 
进入admin # 目录

如果直接连接host串口线，在串口界面下查看的初始状态也是 admin # --串口下

执行sh 1, 切换到bsproc# 目录，

再执行如下命令，进行串口切换：
###串口切换(BMC)
BSP_SetPanelUart(1)   //HOST UArt
BSP_SetPanelUart(0)   //BMC UArt
BSP_SetPanelUart(3)   //expander UArt --问下谢焕军，如确认expander的版本信息

##########################################################

5300 expander固件信息只能通过串口读取：
1、服务器接串口，在串口下，从admin-->bsproc(使用sh 1)，然后运行命令“uartswi()”切换到host串口
2、通过telnet（port 10000）zte zte--sh 1 --登录到bmc，切换到“bsproc”进程，运行如下命令修改寄存器的值：
[bsproc]# wrepld(0x12,3)
会有提示信息
[bsproc]Write Offset 0x0012 : Value = 0x0003.  //1是host，2未知，3是expander串口
[bsproc]Read  Offset 0x0012 : Value = 0x0003.
[bsproc]value = '&' = 38 = 0x26
[bsproc]ushell command finished
3、在串口下敲回车键即可查看串口信息。--此时为expander的串口信息：
4. 执行rssgetfwversion查询expander固件版本信息；

##########################################################################################

#I8350 风扇调速  （BMC shell-port24(root/root)--ushell(zte/zte)--sh 1--BSP_SetPanelUart(1)

（BMC shell-port10000(root/superuser)--ushell(zte/zte)--sh 1--BSP_SetPanelUart(1)


BSP_DbgFanTest(1)    //关闭风扇调速策略
BSP_SetFanPwm(0xff)  //手动设置风扇占空比，参数01-ff
BSP_GetFanRpm()             //读取风机转速

###串口切换(BMC)
BSP_SetPanelUart(1)   //HOST UArt
BSP_SetPanelUart(0)   //BMC UArt
BSP_SetPanelUart(3)   //expander UArt --问下谢焕军，如确认expander的版本信息
uartswitch()

########################
admin提示符下，输入 sh 1，进入bspproc进程，uartswitch()，切换到了host串口、
/etc/grub.conf中，这个文本（initrd /initramfs-2.6.32-431.el6.x86_64.img）
之前增加 console=ttyS0,115200

另一个方法：
直接在BMC串口下输入 sh 1
BSP_SetPanelUart(1) ,即可实现串口切换


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
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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

使用gfio的方法：
硬盘—》创建分区--》格式化（mkfs.ext4  /dev/sdb1）-->挂载 
mount -t ext4 /dev/sdb1 /home/test



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
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
####
BMC--OFF SPAN
HOST--IN SPAN

##分区及格式化
parted /dev/sdb--mklabel--gpt--yes--p--mkpart--gpt4t--ext4--1或0--(-1)--P--Q (sdb/sdb1)
mkfs.ext4 /dev/sdb1

一条命令实现：parted /dev/sdb rm 1  删除分区
一条命令实现： parted /dev/sdb mkpart gpt4t ext4 0 4000GB I
 parted /dev/sdb mkpart gpt4t ext4 0 1997GB I

一条命令实现： 
parted /dev/sdb mkpart gpt4t ext4 0 4000GB I   :4TB (如何提示无法识别设备文件，可以加上mklabel gpt命令)
parted /dev/sdb mkpart gpt4t ext4 0 2996GB I  ：3TB  (如何提示无法识别设备文件，可以加上mklabel gpt命令)
parted /dev/sdb mkpart gpt4t ext4 0 1997GB I  ：2TB  (如何提示无法识别设备文件，可以加上mklabel gpt命令)

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
service name: stor_agent  stor_cimserver


####
kdump是一种先进的基于kexec的内核崩溃转储机制。当系统崩溃时，kdump使用kexec 启动到第二个内核。第二个内核通常叫做捕获内核，以很小内存启动以捕获转储镜像。第一个内核保留了内存的一部分给第二内核启动用。由于kdump利用kexec启动捕获内核，绕过了 BIOS，所以第一个内核的内存得以保留。这是内核崩溃转储的本质。kdump需要两个不同目的的内核，生产内核和捕获内核。生产内核是捕获内核服务的对像。捕获内核会在生产内核崩溃时启动起来，与相应的ramdisk一起组建一个微环境，用以对生产内核下的内存进行收集和转存。注意，在启动时，kdump保留了一定数量的重要的内存，为了计算系统需要的真正最小内存，加上kdump使用的内存数量，以决定真正的最小内存的需求。
为了更好的容错，这个机制最好还是启用 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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
dd if=/dev/zero of=/dev/sdb  快速硬盘读写确认命令
测试硬盘写能力：time dd if=/dev/zero of=/dev/sdb bs=8k count=300000  
测试硬盘读能力：time dd if=/dev/sda of=/dev/null bs=8k count=300000
执行过程中用 iostat -x -d 2查看读写， 执行后用dmesg查看是否有错误


#####iostat输出结果确认事项：
cpu属性值说明：

%user：CPU处在用户模式下的时间百分比。

%nice：CPU处在带NICE值的用户模式下的时间百分比。
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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
fsck/e2fsck -c  (Check for bad blocks and add them to the badblock list)
hdparm -t /dev/sda ( -t   评估硬盘的读取效率。)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
hdparm -tT /dev/sda


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
1）用rpm包 进行vnc 软件安装 2）启动VNCserver, 输入vncserver命令后配置密码，配置后生成文件： /root/.vnc/xstartup  3)关闭防火墙 4）修改配置文件/root/.vnc/xstartup,(# unset SESSION_MANAGER   # exec /etc/X11/xinit/xinitrc) 去掉这两行的注释，5）vncserver -kill :1 6）vncserver :1 7）在PC端打开VNC即可使用。

#### fio测试命令：

fio -name=testc -filename=/dev/sdb -bs=64k --rw=write -iodepth=32 -runtime=80h  -direct=1 -numjobs=8 -time_based  -ioengine=libaio -thread -group_reporting=1

###对系统盘压力测试用例（******）--running版本
fio -name=testc -filename=/home/tmp_io/tmp -bs=256k -rw=randrw -rwmixread=50 -iodepth=16 -direct=1 -numjobs=8 -runtime=24h -size=5G -time_based -ioengine=libaio -thread -group_reporting

####常用压缩和解压
tar zcvf servertool~.tar.gz servertool~/
tar xzf  servertool~.tar.gz


####linux进程后台执行命令 nohup (另一个作用是让所有的命令同时并发执行)
nohup命令：如果你正在运行一个进程，而且你觉得在退出帐户时该进程还不会结束，那么可以使用nohup命令。该命令可以在你退出帐户/关闭终端之后继续运行相应的进程。nohup就是不挂起的意思( no hang up)。 　
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
该命令的一般形式为：nohup command & 　　使用nohup命令提交作业
 如果使用nohup命令提交作业，那么在缺省情况下该作业的所有输出都被重定向到一个名为nohup.out的文件中，除非另外指定了输出文件： 　　
nohup command > myout.file 2>&1 & 　　
在上面的例子中，输出被重定向到myout.file文件中。 　　
使用 jobs 查看任务。 　　
使用 fg %n　关闭。 　　
另外有两个常用的ftp工具ncftpget和ncftpput，可以实现后台的ftp上传和下载，这样我就可以利用这些命令在后台上传和下载文件了。 

nohup *.sh &
一般在用户登出的同时，会给所执行的程序下达停止指令；而用 nohup 等命令后，会将该命令交给其他用户。


####linux下驱动升级和回退操作步骤如下：
举例更新mpt2sas的驱动，
首先在/lib/modules/2.6.32-431.el6.x86_64/extra/路径下创建mpt2sas目录，pmc则为创建aacraid的目录；
然后将编译生成的mpt2sas.ko拷贝到上一步创建的目录
第3步，执行depmod -a；
第4步，执行modprobe mpt2sas
第5步，进入/boot目录，执行mkinitrd initramfs-2.6.32-431.el6.x86_64.img 2.6.32-431.el6.x86_64 --force，完成后执行lsinitrd  initramfs-2.6.32-431.el6.x86_64.img | grep mpt2sas确认驱动路径与预期一致；也可以通过modinfo mpt2sas来查看版本信息，确认驱动更新成功；
第6步骤，重启，确认驱动版本信息，开展测试。

回退方法：
1.rm -rf extra/   删除extra目录；
2.depmod -a
3.执行modinfo aacraid ，查看驱动模块以及更新；

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
######################igb ixgbe网卡驱动使用rpm -Uvh升级失败的应对策略：按如下步骤进行网卡驱动升级：
1、查看系统自带驱动模块版本
    # modinfo ixgbe | grep version
    2、安装新驱动程序
    # rpm -Uvh ixgbe-4.2.1-1.rhel7.0.x86_64.rpm
    3、确认ixgbe驱动模块版本已更新
    # modinfo ixgbe | grep version
	4. modprobe -r ixgbe
	5. modprobe -v ixgbe
	6. mkinitrd initramfs-3.10.0-123.el7.x86_64.img 3.10.0-123.el7.x86_64 --force 更新内核映像文件
	7.确认内核中驱动的版本：
	   lsinitrd initramfs-3.10.0-123.el7.x86_64.img | grep -i ixgbe.ko

####测试中发现，如果不更新内核映像文件，重启后，用ethtool -i 查询网卡的驱动，还是老的驱动，即使将老的驱动文件更名后也没用，必须更新内核映像文件；



==>所有的驱动中，只有raid/sas驱动更新过程中自动进行mkinitrd 的操作，是因为
raid/sas驱动必须上电时就加载，启动后无法更新raid/sas驱动，而其它的驱动，则可以在系统启动后
再加载更新；

结论：初步推断这个问题是由于内核映像中有老驱动的话，开机后就不会自动加载/lib下的新的驱动版本，
对于内核映像中没有的驱动，开机后会自动加载/lib下对应的驱动版本

centos7.0的内核映像文件中：
有igb ,ixgbe,aacraid等驱动；
无lpfc, megaraid_sas, mpt3sas, 

redhat6.5的内核映像文件中：
无igb ,ixgbe，所以也没有出现reboot后， 网卡驱动还原为老驱动的问题，

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



####
modprobe -l| grep “” ：查看当前可以加载的模块（即驱动已经安装）
lsmod | grep ＂＂　查看当前已经加载的模块
modprobe 驱动名    挂载驱动
modprobe -r 驱动名  卸载驱动

驱动更新相关总结说明：
1）使用modprobe -l | grep *** 查看系统中存在的驱动模块
2）modinfo **  查看驱动版本，和驱动是否加载没关系，查看的是当前默认路径下驱动的信息（即depmod -a 识别的路径）
2）lsmod | grep ** 查看依据加载的驱动模块
3）modprobe -r ***  卸载驱动
4）从官网下载驱动的源文件，比如是ixgbe-4.1.2.tar.gz
5）tar -xzf ixgbe-4.1.2.tar.gz;  cd ./src; make ,此时在当前路径下就有ixgbe.ko驱动模块，用modinfo +绝对路径可以查看新驱动的版本信息；
6）将新驱动copy到/lib/modules/2.6.32-431.el6.x86_64/extra/新建的dir/下，
7）执行depmod -a  ，修改配置文件默认识别的驱动路径,优先识别层级比较浅的驱动模块；
8）modprobe ixgbe.ko 加载驱动，modinfo ixgbe.ko 查看驱动的路径和版本信息
9）重新编制内核文件mkinitrd initramfs-2.6.32-431.el6.x86_64.img 2.6.32-431.el6.x86_64 --force，（这个是重新封包核心的命令，例如你自己修改了一个设备的驱动，如果这个驱动要加入核心级别的话，就需要对核心进行重新封包，把新加的配置编译到核心内部去）

###驱动rpm包方式更新的方法：
rpm -Uvh *.rpm


Linux：.c文件编译为.ko文件
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 1st time
写个my.c和一个Makefile文件，然后make编译一下，就成功了，生成my.ko

再加载一下insmod my.ko     dmesg|grep module 看到模块初始化时候的打印

卸载模块rmmod my.ko  dmesg|grep module  看模块卸载时候的打印

####grep 命令说明
 grep -v **** 反向输出，即输出不包含关键词的所有line
 grep -i *** 表示忽略大小写
 grep ***直接按关键字过滤

###关闭进程命令
kill  PID
pkill command

###linux 磁盘分析工具命令：baobab

##rpm包安装相关：
如果用-i 安装过程中提示与现有文件冲突，或需要依赖一些其它的文件等等，而终止安装,可以使用
rpm -i --force --nodeps 可以忽略所有依赖关系和文件问题，什么包 
都能安装上，但这种强制安装的软件包不能保证完全发挥功能

##卸载rpm包：rpm -e 包名，包名可以包含版本号等信息（可以不用完全名），但是不可以有后缀.rpm 
如何卸载过程中提示错误“这个软件被其他软件需要，不能随便卸载”，可以用rpm -e --nodeps强制卸载

##已安装的包查询 rpm -qa | grep ***
##已安装的包的安装路径查询 rpm -ql ** （无.rpm的包名）

###驱动查询相关
uname -a
lspci | grep -i lsi
rpm -qa | grep -i mpt2sas
modinfo mpt2sas
rpm -e  ***卸载驱动
rpm -Uvh ** 更新驱动

####硬盘格式化命令说明
mk2fs -t ext4 和 mkfs.ext4  两个命令相同功能


###秘钥设置相关：
ssh-keygen
ssh-copy-id -i /root/.ssh/id_rsa.pub 129.0.0.77（要登陆的目标主机的IP）
如何发生error,用这个命令可以解决
rm -rf /root/.ssh/known_hosts


###linux系统时间同步命令，及设置命令
 ntpdate -u 129.0.0.50
 date -s 10:18:00


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

####PMC 6805固件更新方法：及BIOS ,两个同时升级的。
./arcconf romupdate 1 xxxx.ufi   reboot后生效

E9000：
机框：129.5.101.143
刀片ip:192.168.12.181  root/123456
E9000自研卡：
raid卡 --S600 S620 S610
FC卡--N500
网卡--N720


######gfio相关
./confiture --enasble-gfio
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
之前增加 console=ttyS0,115200   --只用这条也可以完成配置。

{/etc/inittab 中，这个文本（id:5:initdefault:）之后增加
co:2345:respawn:/sbin/agetty ttyS0 115200 vt100 init q   /for rhel
co:2345:respawn:/sbin/agetty -L 115200  ttyS0 ansi    /for SLES

/etc/securetty中，文本最后增加ttyS0}

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


remark:执行时提示下面的error，注意关闭防火墙，当遇到问题时，优先检查防火墙和selinux是否关闭
[root@localhost netperf-2.6.0]# netperf -H 126.0.0.61 -l 60 -t TCP_STREAM -p 10000
establish control: are you sure there is a netserver listening on 126.0.0.61 at port 10000?
establish_control could not establish the control connection from 0.0.0.0 port 0 address family AF_UNSPEC to 126.0.0.61 port 10000 address family AF_INET



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

fio -name=testc -filename=/dev/sdb1 -bs=256k --rw=write -iodepth=32 -runtime=8h  -direct=1 -numjobs=30 -time_based  -ioengine=libaio -thread -group_reporting

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
rpm -ivh **.rpm (install)
vi /etc/hardwaremonitor.conf  (配置)
rpm -qa | grep hardwaremon* （查询）
rpm -e linux-hardwaremon-v00.02.01-2.x86_64 （卸载）
/etc/init.d/hwmd status （执行）


###dmesg:
kernel会将开机信息存储在ring buffer中。若是开机时来不及查看信息，可利用dmesg来查看。开机信息亦保存在/var/log目录中，名称为dmesg的文件里。
最简单的就是把下面的脚本放到crontab里去定期运行:

cat /var/log/dmesg >>/目录/dmesg.txt  #将dmesg的信息重定向到dmesg.txt


####linux日志文件：
 以下介绍的是20个位于/var/log/ 目录之下的日志文件。其中一些只有特定版本采用，如dpkg.log只能在基于Debian的系统中看到。

/var/log/messages — 包括整体系统信息，其中也包含系统启动期间的日志。此外，mail，cron，daemon，kern和auth等内容也记录在var/log/messages日志中。
/var/log/dmesg — 包含内核缓冲信息（kernel ring buffer）。在系统启动时，会在屏幕上显示许多与硬件有关的信息。可以用dmesg查看它们。
/var/log/auth.log — 包含系统授权信息，包括用户登录和使用的权限机制等。
/var/log/boot.log — 包含系统启动时的日志。
/var/log/daemon.log — 包含各种系统后台守护进程日志信息。
/var/log/dpkg.log – 包括安装或dpkg命令清除软件包的日志。
/var/log/kern.log – 包含内核产生的日志，有助于在定制内核时解决问题。
/var/log/lastlog — 记录所有用户的最近信息。这不是一个ASCII文件，因此需要用lastlog命令查看内容。
/var/log/maillog /var/log/mail.log — 包含来着系统运行电子邮件服务器的日志信息。例如，sendmail日志信息就全部送到这个文件中。
/var/log/user.log — 记录所有等级用户信息的日志。
/var/log/Xorg.x.log — 来自X的日志信息。
/var/log/alternatives.log – 更新替代信息都记录在这个文件中。
/var/log/btmp – 记录所有失败登录信息。使用last命令可以查看btmp文件。例如，”last -f /var/log/btmp | more“。
/var/log/cups — 涉及所有打印信息的日志。
/var/log/anaconda.log — 在安装Linux时，所有安装信息都储存在这个文件中。
/var/log/yum.log — 包含使用yum安装的软件包信息。
/var/log/cron — 每当cron进程开始一个工作时，就会将相关信息记录在这个文件中。
/var/log/secure — 包含验证和授权方面信息。例如，sshd会将所有信息记录（其中包括失败登录）在这里。
/var/log/wtmp或/var/log/utmp — 包含登录信息。使用wtmp可以找出谁正在登陆进入系统，谁使用命令显示这个文件或信息等。
/var/log/faillog – 包含用户登录失败信息。此外，错误登录命令也会记录在本文件中。
 除了上述Log文件以外， /var/log还基于系统的具体应用包含以下一些子目录：

    /var/log/httpd/或/var/log/apache2 — 包含服务器access_log和error_log信息。
    /var/log/lighttpd/ — 包含light HTTPD的access_log和error_log。
    /var/log/mail/ –  这个子目录包含邮件服务器的额外日志。
    /var/log/prelink/ — 包含.so文件被prelink修改的信息。
    /var/log/audit/ — 包含被 Linux audit daemon储存的信息。
    /var/log/samba/ – 包含由samba存储的信息。
    /var/log/sa/ — 包含每日由sysstat软件包收集的sar文件。
    /var/log/sssd/ – 用于守护进程安全服务。

除了手动存档和清除这些日志文件以外，还可以使用logrotate在文件达到一定大小后自动删除。可以尝试用vi，tail，grep和less等命令查看这些日志文件。 

##############
####服务器两个IP 设为相同的网段的IP 地址，只接一个网口，缺可以ping通两个IP地址：
==》紧记：不要在一台主机的两块网卡上配置两个同网段的IP，要丢包的，回包地址不是乱了嘛
{服务器系统radhat 5.5
eth0 10.0.135.1
eth1  10.0.135.2
现在网线插网口1，却能PING通这2个IP
现在是想通过网线来切换IP，插哪个网口使用哪个IP
==》不要在一台主机的两块网卡上配置两个同网段的IP，要丢包的，回包地址不是乱了嘛。
==》谢谢~~~现在的目的就是想要在一个服务器上做切换IP，一个网口对应一个IP，现在出现的问题就是插入第一个网口，第二个IP也能PING通，插第二个网口2个IP反而都PING不通，有没有办法解决插入哪个网口就激活哪个IP？
==》1）现在出现的问题就是插入第一个网口，第二个IP也能PING通。这个又要扯到Linux的arp响应机制了（和arp_ignore，arp_filter等参数有关），如果只是要各自通各自的，简单点只要设置net.ipv4.conf.all.arp_ignore=1应该就可以。


2）插第二个网口2个IP反而都PING不通，有没有办法解决插入哪个网口就激活哪个IP

这个你看下机器的route table就明白了，那是因为所有出去的包都走了第一个网口（eth0），拔了这个网口的网线，所有包都出不去了；如果要做到插哪个网口通哪个，要针对eth0和eth1手工设置路由。}

############磁阵配置管理：
磁阵操作步骤：
查看物理盘（数据盘表示已经添加到虚拟盘中；空闲盘表示可以创建虚拟盘）
-->用空闲盘创建虚拟盘（设名称，级别，成员盘）
-->创建卷（将虚拟盘划分为不同的存储区域，这些存储区域称为卷）
         （当虚拟盘状态非正正正常常常，或虚拟盘剩余容量为0时，不允许创建卷。）
          （创建卷时先选择虚拟盘，再设置卷名，容量等信息）
-->设置映射关系(将卷和主机加入到映射组，在映射组里组成主机和卷的对应关系，在主机上访问卷。从
主机上看，一个卷映射为一个磁盘驱动器。)
                (加入映射组的卷称为LUN。)

定位磁阵的方法：
在系统管理-->ping 中，提供从控制器端口向主机发送Ping报文的功能

############# PMC 7805 命令行下创建raid:
./arcconf-linux create 1 logicaldrive name raid1_test max 1 0 2 0 3
                   Ctrl-ID Create-RAID               RAID-Size RAID-Level    [Channel-device ID]
Reported Channel,Device(T:L)       : 0,28(28:0)
./arcconf-linux delete 1 logicaldrive 1
                     Ctrl-ID    Delete-RAID        LogicalDrive ID
Logical device number 0

############windows 下IOMETER使用说明：
1.拷贝文件到服务器路径下，解压后修改文件夹名字（删除中文部分）
2.测试步骤：
a)Disk targets下，每一个worker都选中要测试的物理盘，如sda,  然后选中顶层manager,设置maximum disk size  (扇区数的计算：16G=16*1024*1024*2sectors)   1sector=512Byte
b) 设定测试程序(IO读写要求 数据块大小为4K，256K，1024K，分别包括100%顺序读 100%顺序写 100%随机读 100%随机写)
c)Test setup 中设置测试时间，缓存等待时间(ex:RunTime 时间等于5分钟;Ramp Up Time 15s)
d)display 选项下，选中1s 的刷新频率
--》就可以了，另外，可以把测试的数据保存为配置文件，下次就不用再逐个设置了。

remark:
在windows下直接打开IOmeter时，系统盘显示为黄色（C盘+系统预留部分）， 蓝色的为物理盘，此时在windows的资源管理中，用物理盘创建逻辑盘后，蓝色的物理盘转为为黄色的逻辑盘，就可以对它进行读写测试了。
如果是对服务器端的linux系统使用iometer时，请注意要对蓝色的物理盘进行读写操作，这是和windows不同的部分。

第一次需要准备时间去创建16G的文件，之后就不需要了


#############remote execute:
ssh 129.0.0.55 "lsblk;ifconfig"
ssh 129.0.0.55 lsblk;ifconfig

##############
ESX、vSphere、ESXI的区别

现在来讲vSphere就是ESXI，只是两种叫法而已，我们来看看VMware服务器虚拟化产品的历程。
Vmware 服务器虚拟化第一个产品叫ESX，该产品只有60天测试，没有官方认可的免费版。后来Vmware在4版本的时候推出了ESXI，ESXI和ESX的版本最大的技术区别是内核的变化，ESXI更小，更安全，从其他方面来说ESXI可以在网上申请永久免费的license，但是两个版本的收费版功能是完全一样的。
从4版本开始VMware把ESX及ESXi产品统称为vSphere，但是VMware从5版本开始以后取消了原来的ESX版本，所以现在来讲的话vSphere就是ESXI，只是两种叫法而已。一般官方文档中以称呼vSphere为主。
 
推出                                         ESX和ESXI并存时代                     ESXI时代
Vmware ESX（60天测试,没有认可的免费版）------〉Vmware version 4  ESXI-----------〉  version 4 vSphere-------->version 5后取消了ESX版本（只剩ESXI)     官方称ESXI为vSphere

ESX和ESXI的最大技术区别 ：内核的变化。  ESXI更小、更安全，可以申请永久免费的licence


###############
故障定位：
mcelog(直接执行，如果提示没有命令，用yum安装)
dmesg(直接执行)
messages
serial
==mcelog
服务器硬件检测（采用mcelog）
mcelog 是 x86 的 Linux 系统上用来检查硬件错误，特别是内存和CPU错误的工具。 安装方式 yum install mcelog 运行 mcelog 查看日志方式 /var/log/mcelog

##########################
PCI 设备操作相关
lspci | grep -i emulex
lspci -vvv -s  84:00.0
lspci -vvv -s  84:00.0

#####################emulex FC连接状态备注：
FC卡：未连光纤时，一个绿灯闪烁
错误连接光纤后，一个绿灯闪烁
正确连接光纤后，绿灯常亮，黄灯闪烁

#############网卡分为哪几种？以太网卡、FC网卡、ISCSI网卡
HBA卡：FC-HBA卡（俗称：光纤通道HBA卡）、iSCSI-HBA卡（RJ45接口）
以太网卡：光纤接口的以太网卡（俗称：光纤以太网卡）

我对iSCSI协议的理解是，原端服务器iSCSI协议将SCSI设备、命令和数据封装成了标准的TCP/IP包，然后通过TCP/IP协议进行传输，目标端存储通过iSCSI协议将标准TCP/IP包解包成SCSI设备、命令和数据。 
    对于服务器网卡来说，网卡驱动只能识别和处理TCP/IP包，要将SCSI设备、命令和数据打包成标准TCP/IP包，就需要一个软件来实现，这 个软件就是我们看到的initiator软件。在较老的操作系统，标准的软件包里不包含initator软件包，需要额外下载安装， 如：windows2003系统要普通网卡支持iSCSI协议，就需要安装Initiator-2.08-build3825-x86fre.exe软 件。 
    initator软件安装后，需要占用服务器CPU来处理SCSI协议封装为TCP/IP协议，这样，将降低服务器的计算能力。 
    使用iSCSI HBA卡后，对SCSI协议的封装交由独立的iSCSI HBA卡硬件处理，不再占用服务器CPU，减少对服务器性能的影响。 
    因此，标准的网卡要传输iSCSI协议的TCP/IP，必须要安装initator软件。iSCSI HBA卡的功能就是释放服务器计算资源，提供独立的硬件处理SCSI协议封装为TCP/IP协议。
linux:scsi-target-utils-1.0.24-10.el6.x86_64.cpio
win:Initiator-2.08-build3825-x86fre.exe

############# windows2012开启睡眠功能：
 powercfg /H on

#####################################
以7805为列，说明驱动更新方法：
windows: 系统安装过程中，用U盘加载驱动； 系统已经安装后，在系统下，设备管理器，选择7805，更新驱动
linux：系统安装过程中，用U盘制作驱动盘；系统已经安装后，在系统下，使用rpm包使用rpm -Uvh来更新；

#############################suse相关
suse 关闭防火墙：
SuSEfirewall2 stop   本次有效命令

chkconfig --list | grep fire
用下面两条命令关闭setup 和init的所有项目即可；
chkconfig --level 3 SuSEfirewall2_setup off （上面查询到哪个level on 就关闭哪个level）
chkconfig --level 3 SuSEfirewall2_init  off 

############################suse 相关：
service network restart  网卡重启命令
网卡配置文件目录：/etc/sysconfig/network



###############suse zypper 工具配置
1）挂载光驱
2）mkdir /mnt/iso
   mount -o loop /dev/sr0 /mnt/iso/
3）cd /etc/zypp/repos.d/
   mv SUSE-Linux-Enterprise-Server-11-SP1\ 11.1.1-1.152.repo SUSE-Linux-Enterprise-Server-11-SP1\ 11.1.1-1.152.repobak      #改名备份
4)
zypper ar file:///mnt/iso/suse/ update

5)vi update.repo 
[update]
name=update
enabled=1
autorefresh=1
baseurl=file:/mnt/iso/suse/
type=plaindir
keeppackages=0

6)zypper repos
7)
zypper clean 
zypper refresh  #update过程时间较长 （有时即使zypper refresh 配置异常，也可以进行安装操作）

8)zypper install gcc*


＃＃＃＃＃＃＃＃＃＃＃＃＃
#######################
BMC 内核管理模块相关
sh 6 -->oam
可以执行：uptiime  :top等系统命令



bios-->shell 命令行：
pci -i 84 00 00 -b
pci -b

##########################硬盘IO读写，待更新（2015/11/28）
raid 卡：
write through --不用卡的cache
write back--用卡的cache
一般带电池时，需要测试write back的性能；

一般只要当硬盘数据比较多（20多个以上）时，卡才可能成为瓶颈

ramp time: 只的是硬盘中的cache, 一般设置为30s以上

比如硬盘的cache为128M

128M/ 250MB/s * 60= 30s左右

测试数据块的大小，要尽量大， 用fio测试时，时间尽量在30min以上，因为硬盘写入时，可能会先写入外磁道，而外磁道的转速快，所以写入比较快；相对来说内道的速度回比较慢；

可以先测单盘的性能，对比硬盘的规格书上的参数；

而raid的性能，可以参考如下：
raid 0: 读写都是单盘*N
raid 5: 读写都是单盘*N-1
raid 1: 写等于单盘， 读为单盘的*2

raid10(先0后1)：写性能等于0的部分


说明：
direct=1 指的是系统缓存，比如是指内存的部分，IO读写时，先写入到内存中；
ramp_time 指的是硬盘的cache缓存，是硬盘上带的缓存；
raid 卡：
write through --不用卡的cache
write back--用卡的cache

####网上搜索的一些信息，待完善
5400转的笔记本硬盘：50-90MB每秒

7200转的台式机硬盘：90-190MB每秒

机械硬盘，一般的7200转的台式机硬盘来说读取110M写入90M，存取时间14ms（1ms=100000ns
希捷新酷鱼3TB硬盘的持续读写速度分别为155.2MB/秒和152.3MB/秒

主流的7200转的机械硬盘，一般是170M－200M左右。读写速度是一样的。


常见硬盘IOPS参考值(数据仅供参考)：
　　2,5" 10.000 rpm  SAS 113  IOPS
　　2,5" 15.000 rpm SAS 156 IOPS
　　3,5" 15.000 rpm SAS 146  IOPS
　　
　　2,5" 5.400 rpm SATA 71 IOPS
　　3,5" 7.200 rpm SATA 65 IOPS
　　
　　3,5" 10.000 rpm U320 104 IOPS
　　3,5" 15.000 rpm U320 141 IOPS
　　
　　3,5" 10.000 rpm FC 125 IOPS
　　3,5" 15.000 rpm FC 150 IOPS
　　
　　3,5" 10.000 rpm FATA 119 IOPS


读写性能：
RAID 0：最好（因并行性而提高）
RAID 1： 	

读和单个磁盘无区别，

写则要写两边

RAID 5：
读：RAID 5＝RAID 0

（相近似的数据读取速度）

写：RAID 5<对单个

磁盘进行写入操作

（多了一个奇偶校验信息写入

RAID 10：

 	

读：RAID 10＝RAID 0

写：RAID 10＝RAID 1




######################################
############################
initrd.img、vmlinux和 vmlinuz

initrd.img是一个小的映象，包含一个最小的linux系统。通常的步骤是先启动内核，然后内核挂载initrd.img，并执行里面的脚本来进一步挂载各种各样的模块，然后发现真正的root分区，挂载并执行/sbin/init...

initrd.img当然是可选的了，如果没有initrd.img,内核就试图直接挂载root分区。

说initrd.img文件还会提到另外一个名角---vmlinuz。vmlinuz是可引导的、压缩的内核。“vm”代表 “Virtual Memory”。Linux 支持虚拟内存，不像老的操作系统比如DOS有640KB内存的限制。Linux能够使用硬盘空间作为虚拟内存，因此得名“vm”。另外：vmlinux是未压缩的内核，vmlinuz是vmlinux的压缩文件。

为什么要initrd.img

系统内核vmlinuz被加载到内存后开始提供底层支持，在内核的支持下各种模块，服务等被加载运行。这样当然是大家最容易接受的方式，曾经的linux就是这样的运行的。假设你的硬盘是scsi 接口而你的内核又不支持这种接口时，你的内核就没有办法访问硬盘，当然也没法加载硬盘上的文件系统，怎么办？把内核加入scsi驱动源码然后重新编译出一个新的内核文件替换原来vmlinuz。

需要改变标准内核默认提供支持的例子还有很多，如果每次都需要编译内核就太麻烦了。所以后来的linux就提供了一个灵活的方法来解决这些问题---initrd.img。initrd.img文件就是个ram disk的映像文件。ramdisk是用一部分内存模拟成磁盘，让操作系统访问。ram disk是标准内核文件认识的设备(/dev/ram0)文件系统也是标准内核认识的文件系统。内核加载这个ram disk作为根文件系统并开始执行其中的"某个文件"（2.6内核是 init文件）来加载各种模块，服务等。经过一些配置和运行后，就可以去物理磁盘加载真正的root分区了，然后又是一些配置等，最后启动成功。也就是你只需要定制适合自己的 initrd.img 文件就可以了。这要比重编内核简单多了，省时省事低风险。

#############rhel 配置本地光驱为yum安装源的方法：
1）挂载光驱；2） ls /dev/sr0 确认光驱设备符号；3） mkdir /mnt/iso；4） mount -o loop /dev/sr0 /mnt/iso；
（cd /etc/yum.repos.d/； cp rhel-source.repo rhel-source.repobak；）
5）vi rhel-source.repo：
[baseurl=file:///mnt/iso
enabled=1]

##############配置系统下可以看到7805下的物理盘的设置
1）PMC BIOS中要设置Controller mode 为raid:expose raw
2) 用arcconf getconfig 1 PD查询物理盘的状态，必须是Raw (Pass Through)才可以，
如果是ready, 需要用命令arcconf uninit 1 0 1 将状态从ready-->raw，
这样sd*设备中就可以看到物理盘了。

 Usage: SETCONTROLLERMODE <Controller#> <Controller Mode> [nologs]
 ===================================================================================

 Change a controller's mode.

    Controller Modes  : 0  - RAID: Expose RAW
                      : 1  - Auto Volume Mode
                      : 2  - HBA Mode
                      : 3  - RAID: Hide RAW
                      : 4  - Simple Volume Mode



############################系统驱动管理相关：
1）驱动名称相关
LSI9207-8i\9217-8i   mpt2sas
LSI 1064E\1068E      mptsas
LSI SAS2008\SAS2308  mpt2sas
LSI SAS3008          mpt3sas

SAS2008      megaraid sas
LSI 9260-8i\9271-8i\9361-8i  megaraid sas
PMC6805\7805    aacraid

---网卡
intel 82571   e1000e
intel i350\82576\82580   igb
realtek RTL8111F   r8168
broadcom 5718   tg3

intel 82599  ixgbe
broadcom 57810s   bnx2x
intel XL710   i40e

---FC 卡
emulex IOC540  lpfc

emulex lpe1250\lpe12000  lpfc
qlogic QLE2560\QLE2563   qla2***

2)rpm 包相关：

-ivh 安装
-Uvh 升级
-q 列出指定已安装rpm软件包名
-qa 列出所有已安装rpm软件包名
-qi 列出指定已安装rpm 软件包信息
-qpl 列出rpm软件包内文件信息
-qpi 列出rpm软件包的描述信息
-qf 查询指定文件属于哪个rpm软件包
-e删除包

3）rpm数据库相关，如果rpm系统出现问题，不能安装和查询时，使用下面两个命令初始化rpm数据库
rpm --initdb
rpm --rebuilddb (rebuild过程比较慢)

驱动安装完成后，可以重启服务器来加载新的驱动，也可以手动加载新的驱动，以网卡为例：
modprobe -r igb (卸载原有内核驱动)
modprobe -v igb (加载新安装的驱动)
ethtool -i eth1 查询新的驱动是否加载成功


###############################################
/boot目录：
vmlinuz*** ：是kernel 文件，kernel主要负责的是北桥、南桥、CPU及内存，可见它们都是整个主机最重要的硬件核心部分，kernel 
如果处了问题，系统肯定无法启动起来

initrd**： initrd的全名是initial ram disk，就是启动系统所需加载的虚拟磁盘；

在系统启动过程中，kernel、initrd和system module是依次加载的。initrd包含一部分内核模块，主要是一些关键的外部硬件，如 
SATA、SCSI和USB等外设。它如果失败当然也会影响系统启动。
而system module这些系统中的模块，是与支持和启动无很大关系的硬件有关，如果没有这些硬件设备的支持，系统也可以启动完成， 
只是存在功能上的缺失，如声卡、网卡、显卡等。这些系统模块也可以在启动后，以modprobe的方式载入模块使用；

.vmlinuz 内核文件
 linux内核引导文件是指/boot/vmlinuxz-* 文件，它是一个可进行系统引导的压缩级内核文件，/boot/vmlinux 则是一个非压缩级别的内核引导文件。其中文件名中的vm代表虚拟内存，既是将硬盘虚拟化成内存来使用。但是，操作系统使用虚拟内存时有一定的空间限制，比如，dos就是640kb的虚拟内存大小限制。可以用file命令来查看内核文件  
   file /boot/vmlinuz-*

.initrd.img 映像文件
  linux的内核映像文件时initrd.img. 对vmlinuz内核文件解压之后，在真正的根文件系统“/”启动之前，initrd.img文件会被加载到内存中。当然了，initrd.img 文件主要应用于livecd的制作以及系统初始化工作，像加载内核模块和挂载根文件系统等等。
  因为linux的设备都可以说是赌赢一个文件，linux中需要使用哪块存储盘，就可以使用mount /mnt/cdrom（当然此方式是采用镜像挂载）来进行挂载。
此时我们可以使用mkinitrd命令来制作initrd.img映像文件，可以通过file.


尽管内核是 Linux 的核心，但文件却是用户与操作系统交互所采用的主要工具。这对 Linux 来说尤其如此，这是因为在 UNIX 传统中，它使用文件 I/O 机制管理硬件设备和数据文件。


/boot目录下文件介绍：
config-2.6.22.6-1  是当前内核的配置文件 用于内核编译使用
initrd-2.6.22.6-1.img  当前内核的initrd ,即初始化ramdisk文件 里面放了一些启动时候要加载的驱动等等
system.map-2.6.22.6-1 系统设备映射
vmlinzu-2.6.22.6-1 当前内核文件
memtest86+-1.65 内存测试软件
message 启动时候可以加载的一些说明 消息之类的 没意义

grub目录 里面存放grub引导管理器所必须的配置文件，各种文件系统的驱动文件

##################################################nmon 信息采集工具相关
linux版本下，使用nmon_linux_14i.tar.gz 对应redhat的版本，或直接使用nmon_x86_64_rhel6，使用步骤：
1）增加执行权限；
2）运行命令：./ nmon_x86_fedora5 –fT –s 10 –c 120
上面命令的含义是，-f输出文件，-T输出最耗资源的进程，-s收集数据的时间间隔，-c收集次数

如果想在后台运行nmon，则可用：
nohup ./ nmon_x86_fedora5 –fT –s 10 –c 120

如果想结束该进程，可使用：
ps –aef|grep *nmon*
命令查出该进程ID，然后使用：
kill -9 进程ID

3）命令测试结束后，可得到*.nmon的文件，利用SSH工具或者FTP工具将该文件下载到本地。
4）打开nmon analyser v334.xls，点击analysis nmon data打开文件即可（有时需要设置宏的安全级别才可以）

###############################硬盘fio性能测试和nmon组合使用举例：
./nmon_x86_64_rhel6 -fT -s 10 -c 180

write:
fio -name=testc -filename=/dev/sdb1 -ioengine=libaio -numjobs=8 -iodepth=32 --rw=write -bs=2m -time_based -runtime=30m  -direct=1 -group_reporting=1

read:
fio -name=testc -filename=/dev/sdb1 -ioengine=libaio -numjobs=8 -iodepth=32 --rw=read -bs=2m -time_based -runtime=30m  -direct=1 -group_reporting=1

randrw:
fio -name=testc -filename=/dev/sdb1 -ioengine=libaio -numjobs=8 -iodepth=32 --rw=randrw -rwmixread=50 -bs=2m -time_based -runtime=30m  -direct=1 -group_reporting=1


###################################PMC 内部EPLD配置查询相关：
上电找不到7805卡---厂商说明：
- Resolved an issue where the Adaptec by PMC RAID controller would not be discovered during boot on some 
motherboard vendors. This fix also requires additional flashing of the CPLD (version 10) through the use 
of ARCCONF command "arcconf cpld 1 flashupdate", where "1" represents the controller number that the CPLD 
will be upgraded on. Be aware that a system reboot or power off may be required after performing the CPLD 
update procedure.


升级方法：
  1)查看当前cpld版本(最新版本为Version 10)
   ./arcconf cpld  1   version  
          //load version是使用版本，flash version是保存的版本。

  2）升级7805的cpld版本
   先升级7805的固件，再升级cpld，因为固件中包括了最新的cpld版本。

   ./arcconf  romupdate 1  xxx.UFI  

   ./arcconf cpld  1   flashupdate     //升级完后，重启等待CPLD更新，不能断电！！！，会自动再次重启，
                                                                        //上电后，再用1）再查看下，load version和flash version版本要一致，且均为10。

###################################
####################
含光纤通讯模块PCIE卡指示灯说明
dell 57810  
 没连接光纤时：两个灯都不亮
 闭环：一个绿灯常亮
 通讯时：一个绿灯常亮，一个绿灯快速闪烁
 
 LPE12000 FC卡：
 没连接光纤时：一个绿灯常亮
 通讯时：一个绿灯常亮，一个黄灯快速闪烁，且闪烁频率和速度有关
 
 ############################更换网卡后，修改linux网卡名称的方法：
 正常来说，Linux在识别网卡时第一张会是eth0，第二张才是eth1。有时候我们使用虚拟机克隆技术后网卡的信息就会改变，新克隆出来的虚拟主机网卡名字可能变为eth1.无论我们怎么修改都无法改变，这就对我们使用N台虚拟机进行HA-heartbeat实验时造成了困扰。

在这里成这样是因为复制系统的过程中复制的文件已经有一个网卡在/etc/udev/rules.d/70-persistent-net.rules被识别成了eth0，而虚拟机中的识别成了eth1。

解决方法：

1.编辑/etc/udev/rules.d/70-persistent-net.rules,找到与ifconfig -a得出的MAC相同的一行（NAME='eth1'这一行），把它改为"NAME=eth0 "，然后把上面一行（NAME='eth0'）删除掉。

vim /etc/udev/rules.d/70-persistent-net.rules

SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:0c:29:bb:41:2b", ATTR{type}=="1", KERNEL=="eth*", NAME="eth0"
多个网卡时类似执行

==》直接reboot，网卡的名称就自动变更了。

2.编辑/etc/sysconfig/network-script/ifcfg-eth0,把MAC改为正确的，把UUID删掉。
==》修改相关网卡的MAC和 删除UUID
==》重启网卡即可



########################################################
网口ping不通的情况下，优先检查IP， MAC
##################################################

###########################iscsi配置相关
配置服务器和磁阵IP， ping通
确认iscsi服务已经安装
iscsiadm -m discovery -t sendtargets -p 126.0.0.11
iscsiadm -m node -T iqn.2099-01.cn.com.zte:usp.spr11-4c:09:b4:b0:39:fe -p 126.0.0.11:3260 –l
在磁阵端确认initiation的iqn,应和下面的相关，并在磁阵端配置映射关系
/etc/iscsi/initiatorname.iscsi  确认host的iqn name
service *** restart 重启服务后就可以看到映射的存储设备了。

#################### 硬盘smart信息查看工具
yum install sg3*
sg3_utils-1.28-5.el6.x86_64
sg再按tab可以看到很多其它的命令，需继续研究

sg_inq /dev/sg3 --page=0xb1 提取转速信息
目前监控软件 9000~12000:识别成10000
sg_map

##########################################

#########################iperf使用
测试单线程TCP

server端：
iperf -s -p 12345 （-i 1 -M）

client端：
iperf -c server_ip -p 12345 -i 1 -t 10  (-w 20k)

-c：客户端模式，后接服务器ip

-p：后接服务端监听的端口

-i：设置带宽报告的时间间隔，单位为秒

-t：设置测试的时长，单位为秒

-w：设置tcp窗口大小，一般可以不用设置，默认即可 

测试多线程TCP:

iperf -c server_ip -p 12345 -i 1 -t 3 -P 2 
(两个线程测试，server端不变)


#############################################
###megaraid 9361-8i 配置命令
storcli /c0 add vd type=r1 drives=14:0-1
storcli /c0 add vd type=r5 drives=10:0,1,9,10
storcli /c0/v1 del
storcli /cx set alarm=<on|off|silence> 
storcli set help | grep alarm
###unconfig bad 相关设置
storcli /c0 /e14 /s4 et good
storcli /c0 /fall show
storcli /c0 /fall del

storcli /c0 /e14 /s9 delete hotsparedrive
storcli /c0 /e14 /s4 add hotsparedrive
##When you initialize drives, all the data from the drives is cleared.
storcli /cx[/ex]/sx show initialization
storcli /cx[/ex]/sx start initialization
storcli /cx[/ex]/sx stop initialization
##The Storage Command Line Tool supports the following commands to locate a drive and activate the physical disk 
activity LED:
storcli /cx[/ex]/sx start locate
storcli /cx[/ex]/sx stop locate

/cx show restorehotspare
/cx show rebuildrate



######################################################
Linux系统修复 
type1:
Fsck –y /dev/sda1
Fsck –y /dev/sda2
e2fsck /dev/mapper/VolGroup-lv_root
e2fsck /dev/mapper/VolGroup-lv_swap
e2fsck /dev/mapper/VolGroup-lv_home

type 2:
error: 
fsck.ext4:Unable to resolve 'UUID-25b5bc3d-****' /dev/mapper/VolGroup-lv_home:clean,599/32997376 files,2451565/131989504 blocks  【FAILED】

解决办法：
mount -o remount,rw /回车
编辑/etc/fstab，把无法挂载的分区（即上面提示的那个分区）那一行行首用#注释掉或将那一行直接删除掉，重新启动就OK了

type 3:

error:
Setting hostname localhost.localdomain: [ok]
Checking root filesystem
/ contains afile system with errors,check forced.
/:
Inode 228119 has illegal block(s).
/: UNEXPECTED INCONSISTENCY; RUN fsck MANUALLY.
(i.e.,without -a or -p options)
[FAILED]
***An error occurred during the file system check.
***Dropping you to a shell;the system will reboot
***when you leave the shell.
***Warning - SELinux is active
***Disabling security enforcement for system recovery.
***Run 'setenforce 1' to reenable.
Give root password fpr maintenance
(or type Control-D to continue):

solution:
step1：输入root密码，然后按确认
step2：输入“mount -o ro /”命令，得到一些关于mount的信息（具体有啥用我现在还不明白）
step3：输入“fsck -c /”命令，屏幕上会出现一些checking的信息，如果有Fix<y>？的提示，直接输入y后确认。最后会出现让你reboot的提示。
step4：输入reboot后回车。

################################################################
#####数据盘发生IO error时,会将同一控制器下的系统盘也重新挂载为只读，出于对数据保护，此时只能通过reboot来解决； 或者是系统盘发生IO error,比如在对数据盘进行fio读写时，如果拔出raid1的一个成员盘后，也可能发生系统盘的IO error,此时也会重新挂载为read only，也需要进行reboot;
[root@localhost ~]# dmesg |grep -i only
Write protecting the kernel read-only data: 10240k
EXT4-fs (dm-0): Remounting filesystem read-only


###########################################################

####9361
StorCLI /c0 download file=mr3108fw.rom  固件更新命令
StorCLI /c0 download file=mr3108fw.rom noverchk (如果从高版本回退到低版本，需要加上noverchk)
storcli /c0 add vd type=r1 drives=14:0-1
storcli /c0/v1 del
storcli /cx set alarm=<on|off|silence> 
storcli set help | grep alarm
###unconfig bad 相关设置
先删除foreign的raid后，盘应该会自动变成UG,如果没有，再用set good命令
storcli /c0 /fall show (显示foreign的raid）
storcli /c0 /fall del(删除foreign的raid）
storcli /c0 /e14 /s4 set good 
说明：有时直接查询fall show,没有外来盘，当将盘set good后可以显示外来盘
storcli /c0 /e14 /s9 delete hotsparedrive
storcli /c0 /e14 /s4 add hotsparedrive
##When you initialize drives, all the data from the drives is cleared.
storcli /cx[/ex]/sx show initialization
storcli /cx[/ex]/sx start initialization
storcli /cx[/ex]/sx stop initialization
##The Storage Command Line Tool supports the following commands to locate a drive and activate the physical disk 
activity LED:
storcli /cx[/ex]/sx start locate
storcli /cx[/ex]/sx stop locate

/cx show restorehotspare
/cx show rebuildrate
pmc:
arcconf task start 1 device 0 70 initialize

strocli查询物理盘协商速率
./storcli-linux /c0 /eall /sall  show  all
###sas3008
sas3ircu list
sas3ircu 0 create  raid1 max 2:0 2:1  yes no
sas3ircu 0 deletevolume vol_id yes no
sas3ircu 0 delete  (delte all)
sas3ircu 0 display
sas3ircu 0 status
lsituil 

###7805:
./arcconf-linux create 1 logicaldrive max 1 0 2 0 3
./arcconf-linux delete 1 logicaldrive 1
 arcconf task start 1 device 0 7 initialize (raw-->ready
arcconf uninit 1 0 2    (ready-->raw)
控制器信息获取命令：
arcconf SAVESUPPORTARCHIVE


mount -o remount,rw /




#######
如何解决linux文件系统read-only的状况。 
当你把一个根目录挂载到别的分区上的时候，如果不进行umount动作，这个文件系统很可能成为一个read-only系统，不能进行任何的写和读的动作。显示为Read-only file system,可以使用如下的命令解决这个问题。
mount -o remount,rw /

#################################################
centos7/rhel7 网络配置相关：
ifconfig -a
nmcli dev show
nmcli dev status
ip addr add 129.0.0.13/8 dev ens46f0
#############################################
# ip link show                # 显示网络接口信息
# ip link set eth0 upi           # 开启网卡
# ip link set eth0 down          # 关闭网卡
# ip link set eth0 promisc on      # 开启网卡的混合模式
# ip link set eth0 promisc offi     # 关闭网卡的混个模式
# ip link set eth0 txqueuelen 1200   # 设置网卡队列长度
# ip link set eth0 mtu 1400        # 设置网卡最大传输单元
# ip addr show                # 显示网卡IP信息
# ip addr add 192.168.0.1/24 dev eth0 # 设置eth0网卡IP地址192.168.0.1
# ip addr del 192.168.0.1/24 dev eth0 # 删除eth0网卡IP地址

# ip route list                 # 查看路由信息
# ip route add 192.168.4.0/24  via  192.168.0.254 dev eth0 # 设置192.168.4.0网段的网关为192.168.0.254,数据走eth0接口
# ip route add default via  192.168.0.254  dev eth0    # 设置默认网关为192.168.0.254
# ip route del 192.168.4.0/24      # 删除192.168.4.0网段的网关
# ip route del default          # 删除默认路由


####################################################
###############################################

【驱动目录】	--【驱动描述】
Emulex FC		--Emulex标准FC卡驱动程序，适用于Emulex LPe12000系列FC HBA卡。 lpfc
Intel IGB		--Intel千兆网卡驱动程序，适用于Intel i350千兆网卡。 igb
Intel IXGBE		--Intel万兆网卡驱动程序，适用于Intel 82599万兆网卡。 ixgbe
LSI RAID		--LSI RAID卡驱动程序，适用于LSI 9361 RAID卡。          megaraid_sas
LSI SAS3		--LSI SAS三代控制器驱动程序，适用于LSI SAS3008控制器。   mpt3sas
MGA G200		--Matrox MGA G200显卡驱动程序，适用于Pilot3集成显卡。
NetXtreme II	--Broadcom NetXtreme II万兆网卡驱动程序，适用于BCM57810万兆网卡。
PMC RAID		--Adaptec RAID卡驱动程序，适用于PMC 6805\7805 RAID卡。    aacraid


驱动说明：
    kmod-elx-lpfc-10.6.144.21-1.rhel7u0.x86_64.rpm	
    --Emulex标准FC卡驱动
    elx-lpfc-vector-map-1-1.rhel7.noarch.rpm		
    --可选包，改善LPFC驱动性能优化I/O通道CPU负载均衡，根据需要选择是否安装

RPM包安装步骤：
    以default内核为例，安装命令如下：
    1、查看系统自带驱动模块版本
    # modinfo lpfc | grep version
    2、安装新驱动程序
    # rpm -Uvh kmod-elx-lpfc-10.6.144.21-1.rhel7u0.x86_64.rpm
    3、确认驱动模块版本已更新
# modinfo lpfc | grep version


驱动说明：
    igb-5.3.3.2-1.el7.0.x86_64.rpm	
    --Intel i350 千兆网卡控制器驱动

RPM包安装步骤：
    1、查看系统自带驱动模块版本
    # modinfo igb | grep version
    2、安装新驱动程序
    # rpm -Uvh igb-5.3.3.2-1.el7.0.x86_64.rpm
    3、确认igb驱动模块版本已更新
    # modinfo igb | grep version


驱动说明：
    ixgbe-4.2.1-1.rhel7.0.x86_64.rpm	
    --Intel 82599 万兆网卡控制器驱动

RPM包安装步骤：
    1、查看系统自带驱动模块版本
    # modinfo ixgbe | grep version
    2、安装新驱动程序
    # rpm -Uvh ixgbe-4.2.1-1.rhel7.0.x86_64.rpm
    3、确认ixgbe驱动模块版本已更新
    # modinfo ixgbe | grep version

驱动说明：
    kmod-megaraid_sas-06.705.06.00_el7.0-1.x86_64.rpm	
    --LSI SAS2208 RAID驱动
    
RPM包安装步骤： 
    以default内核为例，安装命令如下：
    1、查看系统自带驱动模块版本
    # modinfo megaraid_sas | grep version
    2、安装新驱动程序
    # rpm -Uvh kmod-megaraid_sas-06.705.06.00_el7.0-1.x86_64.rpm
    3、确认驱动模块版本已更新
    # modinfo megaraid_sas | grep version

驱动说明：
    kmod-mpt3sas-11.00.00.00_el7.0-1.x86_64.rpm	
    --LSI SAS3008 控制器驱动

RPM包安装步骤： 
    以default内核为例，如下：
    1、查看系统自带驱动模块版本
    # modinfo mpt3sas | grep version
    2、安装新驱动程序
    # rpm -Uvh kmod-mpt3sas-11.00.00.00_el7.0-1.x86_64.rpm	
    3、确认驱动模块版本已更新
    # modinfo mpt3sas | grep version

驱动说明：
	xorg-x11-drv-mga-1.6.3-6.el7.x86_64.rpm
	--MGA G200显卡驱动程序

RPM包安装步骤：
	1、安装mga驱动包
		#rpm -ivh xorg-x11-drv-mga-1.6.3-6.el7.x86_64.rpm
	
	2、修改grub文件
		#vi /etc/default/grub
	在GRUB_CMDLINE_LINUX这行添加mgag200.modeset=0，保存文件后执行命令：
		# grub2-mkconfig -o /boot/grub2/grub.cfg
	重启系统后生效
	
	3、确认驱动是否加载成功，查看xorg日志：
		# cat /var/log/Xorg.0.log | grep mga
		[  3564.594] Kernel command line: BOOT_IMAGE=/vmlinuz-3.10.0-229.el7.x86_64 root=/dev/mapper/rhel-root ro rd.lvm.lv=rhel/swap crashkernel=auto rd.lvm.lv=rhel/root rhgb quiet mgag200.modeset=0
		[  3564.608] (II) LoadModule: "mga"
		[  3564.608] (II) Loading /usr/lib64/xorg/modules/drivers/mga_drv.so
		[  3564.609] (II) Module mga: vendor="X.Org Foundation"
		[  3564.609] (II) MGA: driver for Matrox chipsets: mga2064w, mga1064sg, mga2164w,
		        mga2164w AGP, mgag100, mgag100 PCI, mgag200, mgag200 PCI,
		        mgag200 SE A PCI, mgag200 SE B PCI, mgag200 EV Maxim,
		        mgag200 ER SH7757, mgag200 eW Nuvoton, mgag200eH, mgag400, mgag550
		[  3564.627] (--) MGA(0): Chipset: "mgag200 SE A PCI"
		[root@localhost /]# 

	如果执行上述步骤后，查看到“LoadModule: "mga"”，则表示mga驱动加载成功。否则需要再执行如下步骤：
	4、生成xorg配置文件
		#Xorg -configure :1
	5、修改xorg配置文件
		#vi /root/xorg.conf.new
		确认 Section "Device" 中的 驱动为mga，如果不是，修改为mga：
		Section "Device"
		        ### Available Driver options are:-
		        ### Values: <i>: integer, <f>: float, <bool>: "True"/"False",
		        ### <string>: "String", <freq>: "<f> Hz/kHz/MHz",
		        ### <percent>: "<f>%"
		        ### [arg]: arg optional
		        #Option     "SWcursor"                  # [<bool>]
		        …………
		        Identifier  "Card0"
		        Driver      "mga"
		        BusID       "PCI:10:0:0"
		EndSection
	
	6、使用修改后的xorg配置
		# mv /root/xorg.conf.new /etc/X11/
	
	7、重新启动图形界面
		#init 3
		再执行 
		#init 5
	8、查看日志确认mga驱动加载成功。
		# cat /var/log/Xorg.0.log | grep mga

驱动安装说：
no need extra driver, use the bnx2x driver of CentOS7u0 kernel.

# modinfo bnx2x | grep version
version:        1.78.19-0
srcversion:     494067C7E7547631B3C209F
vermagic:       3.10.0-123.el7.x86_64 SMP mod_unload modversions

驱动说明：
    kmod-aacraid-RHEL7.0-1.2.1-41024.x86_64.rpm	
    --Adaptec RAID控制器驱动

RPM包安装步骤： 
    1、查看系统自带驱动模块版本
    # modinfo aacraid | grep version
    2、安装新驱动程序
    # rpm -Uvh kmod-aacraid-RHEL7.0-1.2.1-41024.x86_64.rpm
    3、确认驱动模块版本已更新
    # modinfo aacraid | grep version


#########################################################
###################
centos7 yum 配置说明：
建一个备份的目录，将/etc/yum.repos.d路径下的所有配置源文件都放到备份目录下，创建新目录文件：CentOS-Media.repo
#CentOS-Media.repo
#
[c6-media]
name=CentOS-$releaseber - Media
baseurl=file:///mnt
gpgcheck=0
enabled=1

######################################################
linux 快捷方式处理相关：

1.先在终端中输入whereis zend studio,找到可执行文件。
2.然后用ln命令建立连接到桌面就可以了。

通过ln命令实现
ln -s /mnt/hgfs/share/ /home/liup/桌面/share

linux查找可执行文件的方法
查看当前目录下文件的类型，用ls -F
们来看看ls -F的作用：
######################################################
-F开关对可执行文件添加一个*号，为目录添加一个/号，为符号链接添加一个@号。


1.先在终端中输入whereis zend studio,找到可执行文件。
2.然后用ln命令建立连接到桌面就可以了。

通过ln命令实现
ln -s /mnt/hgfs/share/ /home/liup/桌面/share

linux查找可执行文件的方法
查看当前目录下文件的类型，用ls -F
们来看看ls -F的作用：

-F开关对可执行文件添加一个*号，为目录添加一个/号，为符号链接添加一个@号。



##################################7805命令行配置参数：
###7805:
./arcconf-linux create 1 logicaldrive max 1 0 2 0 3
./arcconf-linux delete 1 logicaldrive 1
 arcconf task start 1 device 0 7 initialize (raw-->ready
arcconf uninit 1 0 2    (ready-->raw)
arconf setstate 1 device 0 7 HSP logicaldrive 0


###################################linux Usb驱动盘制作命令：
1. 	Write driver diskette image on USB(For example: RHEL 6.6 x86_64 iso image: aacraid-driverdisk-1.2.1-XXXXX-RHEL6.6-x86_64.iso)
2. 	Start installing the RHEL 6.x or CentOS 6.x
3. 	When the first installation screen appears, insert the USB driver disk.
4. 	Type this command at the Boot: prompt and press Enter:
		linux dd
5. 	Select Yes to indicate that you have a driver disk, then select the driver image from the USB drive
   	(typically, /dev/sda).

##########################################
SSD测试预置条件：
######################
To zero out and condition a drive sequentially for performance testing, use the following command twice: 
Preparing the Drive 
dd if=/dev/zero of=/dev/nvme0n1 bs=1M oflag=direct  
（SSD盘由nand flash组成，写过地方必须先擦出才能再写，这些特性使得没有写过的盘性能很高，而写过一段时间后，性能有很大的跌落，故在测试SSD读写稳定性时，要先对盘进行大块顺序写一到二遍（称为pre-condition，bs=1m, rw=write）。
可以在Diskio工具中的batch.sh脚本中指定这个pre-condition写操作。
）
硬盘分区方法
#parted   /dev/sdx    mklabel  gpt  
一般先对整个硬盘先分区，且分区的起始地址一定要4K对齐，否则影响性能
# parted /dev/sdx  unit  kib  mkpart  primary 1024 100%  
//测试时硬盘所有空间在一个分区下，且分区起始地址要4k对齐
#parted   /dev/sdx  unit  kib  print 

#####################################################
PCIE ssd操作相关：
intel 400G&800G
  hgst  1.6TB&3.2TB

hgst:
卸载原驱动：
sudo rpm -qa | grep nvme-hgst
rpm --erase "name of rpm"

安装：
rpm -ivh **.rpm
modprobe nvme-hgst
#######intel
isdct.exe show –a –intelssd 
######hgst
lspci 
ls /dev/nvme*
hdm scan
hdm get-info --path /dev/nvme0n1
hdm get-smart
 --path /dev/nvme0n1
hdm generate-report  --path /dev/nvme0n1
hdm manage-firmware  --path /dev/nvme0
hdm manage-firmware --path /dev/nvme0 --load --file KMGNP110_HHHL_1.6TB-pcie.BIN
hdm manage-firmware --path /dev/nvme0  --list
【升级后异常说明】：
  升级后，发现Slot 4 = KMGNP110 为Pending状态，所以重启，在/dev/下找不到nvme0设
  掉电，再上电，刚开始找不到，等了一会，lspci查看，找到了nvme卡，在/dev/也找到了对应的设备。





######################
To zero out and condition a drive sequentially for performance testing, use the following command twice: 
Preparing the Drive 
dd if=/dev/zero of=/dev/nvme0n1 bs=1M oflag=direct  
（SSD盘由nand flash组成，写过地方必须先擦出才能再写，这些特性使得没有写过的盘性能很高，而写过一段时间后，性能有很大的跌落，故在测试SSD读写稳定性时，要先对盘进行大块顺序写一到二遍（称为pre-condition，bs=1m, rw=write）。
可以在Diskio工具中的batch.sh脚本中指定这个pre-condition写操作。
）
硬盘分区方法
#parted   /dev/sdx    mklabel  gpt  
一般先对整个硬盘先分区，且分区的起始地址一定要4K对齐，否则影响性能
# parted /dev/sdx  unit  kib  mkpart  primary 1024 100%  
//测试时硬盘所有空间在一个分区下，且分区起始地址要4k对齐
#parted   /dev/sdx  unit  kib  print 


#################################################
############################问题备份：
##############linux grub菜单之后，一直黑屏无法启动问题###
现象描述：
linux 系统启动后，可以进行grub菜单，但继续启动后，会黑屏,左上角一个光标一直闪烁，
重启后，在grub菜单下设置单用户模式启动，也是一样的现象；

初步判定这个问题是文件系统损坏，可能是由于异常关机造成的；
可以识别到硬盘，所以MBR正常；
可以进入grub菜单，所以grub次引导程序正常；

解决对策：
在BMC 下用命令将服务器的串口切换到host端：
方1：（BMC shell-port24(root/root)--ushell(zte/zte)--sh 1--BSP_SetPanelUart(1)
方2：（BMC shell-port10000(root/superuser)--ushell(zte/zte)--sh 1--BSP_SetPanelUart(1)
方3：直接在BMC串口下输入 sh 1 且到[BMCMGR] ，输入BSP_SetPanelUart(1) ,即可实现串口切换

前提是host端也开启了串口功能，如何之前没有开启，可以启动后进入grub,编辑配置菜单增加console=ttyS0,115200来开启串口
Give root password for maintenance
(or type Control-D to continue): 

1)进入后发现/boot分区时空的，
使用以下命令修复后还是没用，
Fsck –y /dev/sda1
Fsck –y /dev/sda2
e2fsck /dev/mapper/VolGroup-lv_root
e2fsck /dev/mapper/VolGroup-lv_swap
e2fsck /dev/mapper/VolGroup-lv_home

2)再执行以下命令后，改为命令行启动：
mount -o remount,rw /回车

3)使用光盘修复功能重新创建/boot分区后，详细请参考百度

使用上述3钟方法后没有立即回复，过了一段时间后，重新启动这块盘，从命令行进入了。
==》具体原因有待继续研究，恢复的具体原因不是太清楚。
#################################################################
########################################
大分区格式化时提示报错 (ext4的分区大于16T就无法支持了)
[root@localhost zhl]# mkfs.ext4 /dev/sdl1
mke2fs 1.41.12 (17-May-2010)
mkfs.ext4: Size of device /dev/sdl1 too big to be expressed in 32 bits
	using a blocksize of 4096.

在/etc/mke2fs.conf文件，ext4配置中去开启64位功能

ext4 = {
features = has_journal,extent,huge_file,flex_bg,uninit_bg,dir_nlink,extra_isize
auto_64-bit_support = 1      ###新增加行，告诉系统使用64位方式进行格式化。避免mkfs.ext4直接报错。
inode_size = 256
}

########################################
CentOS使用mkfs.ext4快速格式化大容量硬盘，快速格式化命令：
mkfs.ext4  -T largefile /dev/xxx

######################################
问:1 如何查看当前的Linux服务器的运行级别？

答: ‘who -r’ 和 ‘runlevel’ 命令可以用来查看当前的Linux服务器的运行级别。

问:2 如何查看Linux的默认网关？

答: 用 “route -n” 和 “netstat -nr” 命令，我们可以查看默认网关。除了默认的网关信息，这两个命令还可以显示当前的路由表。

问:3 如何在Linux上重建初始化内存盘镜像文件？

答: 在CentOS 5.X / RHEL 5.X中，可以用mkinitrd命令来创建初始化内存盘文件，举例如下：

    # mkinitrd -f -v /boot/initrd-$(uname -r).img $(uname -r)

如果你想要给特定的内核版本创建初始化内存盘，你就用所需的内核名替换掉 ‘uname -r’ 。

在CentOS 6.X / RHEL 6.X中，则用dracut命令来创建初始化内存盘文件，举例如下：

    # dracut -f

以上命令能给当前的系统版本创建初始化内存盘，给特定的内核版本重建初始化内存盘文件则使用以下命令：

    # dracut -f initramfs-2.x.xx-xx.el6.x86_64.img 2.x.xx-xx.el6.x86_64

问:4 cpio命令是什么？

答: cpio就是复制入和复制出的意思。cpio可以向一个归档文件（或单个文件）复制文件、列表，还可以从中提取文件。

问:5 patch命令是什么？如何使用？

答: 顾名思义，patch命令就是用来将修改（或补丁）写进文本文件里。patch命令通常是接收diff的输出并把文件的旧版本转换为新版本。举个例子，Linux内核源代码由百万行代码文件构成，所以无论何时，任何代码贡献者贡献出代码，只需发送改动的部分而不是整个源代码，然后接收者用patch命令将改动写进原始的源代码里。

创建一个diff文件给patch使用，

    # diff -Naur old_file new_file > diff_file

旧文件和新文件要么都是单个的文件要么都是包含文件的目录，-r参数支持目录树递归。

一旦diff文件创建好，我们就能在旧的文件上打上补丁，把它变成新文件：

    # patch < diff_file

问:6 aspell有什么用 ?

答: 顾名思义，aspell就是Linux操作系统上的一款交互式拼写检查器。aspell命令继任了更早的一个名为ispell的程序，并且作为一款免费替代品 ，最重要的是它非常好用。当aspell程序主要被其它一些需要拼写检查能力的程序所使用的时候，在命令行中作为一个独立运行的工具的它也能十分有效。

问:7 如何从命令行查看域SPF记录？

答: 我们可以用dig命令来查看域SPF记录。举例如下：

    linuxtechi@localhost:~$ dig -t TXT google.com

问:8 如何识别Linux系统中指定文件(/etc/fstab)的关联包？

答: 

    # rpm -qf /etc/fstab

以上命令能列出提供“/etc/fstab”这个文件的包。

问:9 哪条命令用来查看bond0的状态？

答: 

    cat /proc/net/bonding/bond0

问:10 Linux系统中的/proc文件系统有什么用？

答: /proc文件系统是一个基于内存的文件系统，其维护着关于当前正在运行的内核状态信息，其中包括CPU、内存、分区划分、I/O地址、直接内存访问通道和正在运行的进程。这个文件系统所代表的并不是各种实际存储信息的文件，它们指向的是内存里的信息。/proc文件系统是由系统自动维护的。

问:11 如何在/usr目录下找出大小超过10MB的文件？

答: 

    # find /usr -size +10M

问:12 如何在/home目录下找出120天之前被修改过的文件？

答: 

    # find /home -mtime +120

问:13 如何在/var目录下找出90天之内未被访问过的文件？

答: 

    # find /var \! -atime -90

问:14 在整个目录树下查找文件“core”，如发现则无需提示直接删除它们。

答:

    # find / -name core -exec rm {} \;

问:15 strings命令有什么作用？

答: strings命令用来提取和显示非文本文件中的文本字符串。（LCTT 译注：当用来分析你系统上莫名其妙出现的二进制程序时，可以从中找到可疑的文件访问，对于追查入侵有用处）

问:16 tee 过滤器有什么作用 ?

答: tee 过滤器用来向多个目标发送输出内容。如果用于管道的话，它可以将输出复制一份到一个文件，并复制另外一份到屏幕上（或一些其它程序）。

    linuxtechi@localhost:~$ ll /etc | nl | tee /tmp/ll.out

在以上例子中，从ll输出可以捕获到 /tmp/ll.out 文件中，并且同样在屏幕上显示了出来。

问:17 export PS1 = ”$LOGNAME@hostname:\$PWD: 这条命令是在做什么？

答: 这条export命令会更改登录提示符来显示用户名、本机名和当前工作目录。

问:18 ll | awk ‘{print $3,”owns”,$9}’ 这条命令是在做什么？

答: 这条ll命令会显示这些文件的文件名和它们的拥有者。

问:19 :Linux中的at命令有什么用？

答: at命令用来安排一个程序在未来的做一次一次性执行。所有提交的任务都被放在 /var/spool/at 目录下并且到了执行时间的时候通过atd守护进程来执行。

问:20 linux中lspci命令的作用是什么？

答: lspci命令用来显示你的系统上PCI总线和附加设备的信息。指定-v，-vv或-vvv来获取越来越详细的输出，加上-r参数的话，命令的输出则会更具有易读性。

###########################################################################
########################at 命令：
ntpdate -s 129.0.0.150

指令：at
定时任务，指定一个时间执行一个任务，只能执行一次。
# yum -y install at

# ps -ef | grep atd ##查看是否开启atd
# /etc/init.d/atd start ##开启atd
# chkconfig --level 2345 atd on ##设置atd开机启动
service atd status
任务执行结果在：/var/spool/at/spool

语法：# at [参数] [时间]
at> 执行的指令
退出at命令 ctrl+d

查询当前的等待任务，被执行之后就不会显示
# atq

删除系统中由at建立的正在等待被执行的任务
# atrm 任务的工作号
例如：# atrm 17

常见参数：
-m ：当指定的任务被完成之后，将给用户发送邮件，即使没有标准输出
-I ：atq的别名
-d ：atrm的别名
-v ：显示任务将被执行的时间
-c ：打印任务的内容到标准输出
-V ：显示版本信息
-q ：后面加<列队> 使用指定的列队
-f ：后面加<文件> 从指定文件读入任务而不是从标准输入读入
-t ：后面<时间参数> 以时间参数的形式提交要运行的任务

时间：定义出什么时候要进行at的任务，格式有：
1、HH:MM
说明：在今日的 HH:MM 时刻进行，若该时刻已超过，则明天的 HH:MM 进行此任务。
ex> 04:00

2、HH:MM YYYY-MM-DD
说明：规定在某年某月的某一天的特殊时刻进行该项任务
ex> 04:00 2009-03-17

3、HH:MM[am|pm] [Month] [Date]
说明：规定在某年某月某日的某时刻进行该项任务
ex> 04pm March 17

4、HH:MM[am|pm] + number [minutes|hours|days|weeks]
说明：规定在某个时间点再加多少时间后才进行该项任务
ex> now + 5 minutes
ex> 04pm + 3 days

时间格式扩展：
at允许使用一套相当复杂的指定时间的方法。
1、能够接受在当天的hh:mm（小时:分钟）式的时间指定。假如该时间已过去，那么就放在第二天执行。
2、能够使用midnight（深夜），noon（中午），teatime（饮茶时间，一般是下午4点）等比较模糊的词语来指定时间。
3、能够采用12小时计时制，即在时间后面加上AM（上午）或PM（下午）来说明是上午还是下午。
4、能够指定命令执行的具体日期，指定格式为month day（月 日）或mm/dd/yy（月/日/年）或dd.mm.yy（日.月.年），指定的日期必须跟在指定时间的后面。
5、能够使用相对计时法。指定格式为：now + count time-units ，now就是当前时间，time-units是时间单位，这里能够是minutes（分钟）、hours（小时）、days（天）、weeks（星期）。count是时间的数量，几天，几小时。
6、能够直接使用today（今天）、tomorrow（明天）来指定完成命令的时间。

限制用户的使用权限
前提：很多主机被所谓的攻击破解后，最常发现的就是他们的系统当中多了很多的黑客程序，这些程序非常可能运用一些计划任务来运行或搜集你的系统运行信息，并定时的发送给黑客。所以，除非是你认可的帐号，否则先不要让他们使用 at 命令
at命令使用的控制文件来限制用户的使用控制
控制文件目录：/etc/at.allow和/etc/at.deny
控制文件使用规则：
1：先找寻 /etc/at.allow 这个文件，写在这个文件中的使用者才能使用 at ，没有在这个文件中的使用者则不能使用 at (即使没有写在 at.deny 当中);
2：如果 /etc/at.allow 不存在，就寻找 /etc/at.deny 这个文件，若写在这个 at.deny 的使用者则不能使用 at ，而没有在这个 at.deny 文件中的使用者就可以使用 at 命令。
3：如果两个文件都不存在，那么只有 root 可以使用 at 这个命令。
4：在一般的 distributions 当中，由于假设系统上的所有用户都是可信任的， 因此系统通常会保留一个空的 /etc/at.deny 文件，意思是允许所有人使用 at 命令的意思。
5：如果不希望有某些使用者使用 at 的话，将那个使用者的帐号写入 /etc/at.deny 即可！ 一个帐号写一行。
# vi /etc/at.allow

注意事项
1、如果at的指令输出的路径有误 则会把结果以邮件的形式发送给用户
2、当一个任务创建了会被分配到一个任务号，而且会在/var/spool/at里面排队。不建议使用vi编辑器去修改，容易出错。

例子：
实例1：三天后的下午 5 点锺执行 /bin/ls
# at 5pm + 3 days
at> /bin/ls
at> <EOT>
job 7 at 2013-01-08 17:00

实例2：明天17点钟，输出时间到指定文件内
# at 17:20 tomorrow
at> date > /root/doiido.log
at> <EOT>
job 8 at 2013-01-06 17:20

实例3：计划任务设定后，在没有执行之前用atq命令来查看系统没有执行工作任务
# atq
8 2013-01-06 17:20 a root
7 2013-01-08 17:00 a root

实例4：删除已经设置的任务
# atq
8 2013-01-06 17:20 a root
7 2013-01-08 17:00 a root
# atrm 7
# atq
8 2013-01-06 17:20 a root

实例5：显示已经设置的任务内容
# at -c 8
#!/bin/sh
# atrun uid=0 gid=0
# mail root 0
echo "hello"
date > doiido.log

扩展指令batch
batch为，at命令的特殊版本，在执行的任务会占用大量资源的时候用，只在cpu需求低于cpu能力80%的时候使用
# batch
at> echo "hi" > /dev/tty2
batch创建的任务也是通过atq查看，atrm删除 

#############################################################
install.wim:
C:\Program Files\Windows AIK\Tools\PETools>dism /get-wiminfo /wimfile:C:\Users\A
dministrator\Desktop\2008r2_new-install\install.wim

C:\Program Files\Windows AIK\Tools\PETools>dism /mount-wim /wimfile:h:\wims\inst
all.wim /index:1 /mountdir:h:\mount

C:\Program Files\Windows AIK\Tools\PETools>dism /image:h:\mount /add-driver /dri
ver:h:\drivers\ /recurse /forceunsigned

C:\Program Files\Windows AIK\Tools\PETools>dism /unmount-wim /mountdir:h:\mount
/commit

boot.wim:
手动添加驱动的方法如下：
集成前的准备工作：（1）装有windows AIK（2）peimg
1，下载所需的驱动。
2，找到启动映像boot..wim,可以从系统安装光盘里找到或从wds服务器中导出到D盘根目录下
3，在BOOT.WIM所在的目录下新建一个文件夹：boot
4，在安装Windows AIK的计算机上执行命令：imagex /mountrw d:\boot.wim 2 d:\boot
5，成功后执行命令：peimg /inf=x:\netdrivers\chipset.inf d:\boot\windows，这是把驱动加载到WIM文件释放的目录中（/inf=x:\netdrivers\chipset.inf,等号后边为驱动程序中inf文件所在的路径）。
  www.2cto.com  
6，成功后执行打包命令：imagex /unmount /commit d:\boot。
最后把更新后的WIM文件导入到WDS服务中就可以了（直接复制粘贴覆盖原来的boot.wim也可以）。

#####################################################################
BMC 中文件传输命令

DTF 中配置ftp server的路径，用户名及密码

BMC-->HOST
ftpput -u -p ip parsesel parsesel

host --> bmc
ftpget -u -p ip parsesel parsesel

#####################################################################
###############################
iperf使用说明：
tar xvfz iperf-xxx.tar.gz
cd /iperf-xxx
./configure
make
make install

iperf -s

iperf -c 126.0.0.11 -i 2 -t 60 -p 5001 -P5

在被测服务器上执行命令iperf -s，客户端服务器执行iperf -c x.x.x.x -i n1 -t n2 -p 端口号 -P 线程数，
其中x.x.x.x代表服务端对接网口的IP地址，n1的数值表示每隔n1秒打印一次，n2表示测试时间以秒为单位；
###################################################################
################################重要问题确认：
suse11.3 接磁阵无法识别设备的问题，
所有的配置都正常，也查看到设备已经连接，但在系统下就是看不到设备，
最后确认为光纤的问题， 虽然光纤的灯闪烁正常，但光纤确认还是有问题
#######################################################

SATA速率：

SATA 1.0/1.0a (1.5Gb/s)      150MB/s
SATA 2.0         (3.0Gb/s)      375MB/s
SATA 3.0         (6.0Gb/s)      750MB/s

SAS速率：
 SAS (V2.0/3.0: 6Gbps/12Gbps)

########################################################
linux wget命令：
wget ftp://192.167.5.241/BMC_SGLMA_P3_R_V01.03.63.04_201511250330.BIN --ftp-user=zte --ftp-password=zte

#######################################################
###########################################网卡绑定：
redhat6.5----------------------------------
[root@localhost network-scripts]# cat ifcfg-bond0 
DEVICE=bond0
TYPE=Ethernet
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=no
IPADDR=124.0.0.99
NETMASK=255.0.0.0
BONDING_OPTS="mode=1 miimon=100"

[root@localhost network-scripts]# cat ifcfg-eth2
DEVICE=eth2
HWADDR=4C:09:B4:14:74:58
TYPE=Ethernet
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=no
MASTER=bond0
SLAVE=yes
[root@localhost network-scripts]# cat ifcfg-eth3
DEVICE=eth3
HWADDR=4C:09:B4:14:74:59
TYPE=Ethernet
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=no
MASTER=bond0
SLAVE=yes
[root@localhost network-scripts]# 

绑定后查询信息：
[root@localhost network-scripts]# ifconfig
bond0     Link encap:Ethernet  HWaddr 4C:09:B4:14:74:58  
          inet addr:124.0.0.99  Bcast:124.255.255.255  Mask:255.0.0.0
          inet6 addr: fe80::4e09:b4ff:fe14:7458/64 Scope:Link
          UP BROADCAST RUNNING MASTER MULTICAST  MTU:1500  Metric:1
          RX packets:787267 errors:0 dropped:0 overruns:0 frame:0
          TX packets:4876510 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:51959616 (49.5 MiB)  TX bytes:7382943688 (6.8 GiB)

eth2      Link encap:Ethernet  HWaddr 4C:09:B4:14:74:58  
          UP BROADCAST RUNNING SLAVE MULTICAST  MTU:1500  Metric:1
          RX packets:787266 errors:0 dropped:0 overruns:0 frame:0
          TX packets:4876475 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:51959530 (49.5 MiB)  TX bytes:7382941870 (6.8 GiB)
          Memory:dfb20000-dfb40000 

eth3      Link encap:Ethernet  HWaddr 4C:09:B4:14:74:58  
          UP BROADCAST RUNNING SLAVE MULTICAST  MTU:1500  Metric:1
          RX packets:1 errors:0 dropped:0 overruns:0 frame:0
          TX packets:35 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:86 (86.0 b)  TX bytes:1818 (1.7 KiB)
          Memory:dfb00000-dfb20000 

[root@localhost network-scripts]# cat /proc/net/bonding/bond0 
Ethernet Channel Bonding Driver: v3.6.0 (September 26, 2009)

Bonding Mode: fault-tolerance (active-backup)
Primary Slave: None
Currently Active Slave: eth2
MII Status: up
MII Polling Interval (ms): 100
Up Delay (ms): 0
Down Delay (ms): 0

Slave Interface: eth2
MII Status: up
Speed: 1000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: 4c:09:b4:14:74:58
Slave queue ID: 0

Slave Interface: eth3
MII Status: up
Speed: 1000 Mbps
Duplex: full
Link Failure Count: 1
Permanent HW addr: 4c:09:b4:14:74:59
Slave queue ID: 0






Suse11sp3---------------------------
linux-f5lc:/etc/sysconfig/network # cat ifcfg-bond0 
BOOTPROTO='static'
IPADDR='124.0.0.100'
NETMASK='255.0.0.0'
STARTMODE='onboot'
BONDING_MASTER='yes'
BONDING_MODULE_OPTS='mode=1 miimon=100'
BONDING_SLAVE0='eth3'
BONDING_SLAVE1='eth5'
USERCONTROL='no'

linux-f5lc:/etc/sysconfig/network # cat ifcfg-eth3
BOOTPROTO='no'
NAME='Intel Ethernet controller'
HWADDR='20:14:12:04:00:09'
STARTMODE='auto'
USERCONTROL='no'


linux-f5lc:/etc/sysconfig/network # cat ifcfg-eth5
BOOTPROTO='no'
NAME='Intel Ethernet controller'
HWADDR='20:14:12:04:00:0B'
STARTMODE='auto'
USERCONTROL='no'

remark: 默认情况下， 两个成员网卡的配置文件不做特殊设置即可；

设置后查询：
linux-f5lc:/etc/sysconfig/network # ifconfig
bond0     Link encap:Ethernet  HWaddr 20:14:12:04:00:09  
          inet addr:124.0.0.100  Bcast:124.255.255.255  Mask:255.0.0.0
          inet6 addr: fe80::2214:12ff:fe04:9/64 Scope:Link
          UP BROADCAST RUNNING MASTER MULTICAST  MTU:1500  Metric:1
          RX packets:30163349 errors:2 dropped:33 overruns:0 frame:2
          TX packets:12709349 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:44710954910 (42639.6 Mb)  TX bytes:13695251304 (13060.8 Mb)
eth3      Link encap:Ethernet  HWaddr 20:14:12:04:00:09  
          UP BROADCAST RUNNING SLAVE MULTICAST  MTU:1500  Metric:1
          RX packets:30163311 errors:2 dropped:8 overruns:0 frame:2
          TX packets:12709301 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:44710952554 (42639.6 Mb)  TX bytes:13695247740 (13060.8 Mb)

eth5      Link encap:Ethernet  HWaddr 20:14:12:04:00:09  
          UP BROADCAST RUNNING SLAVE MULTICAST  MTU:1500  Metric:1
          RX packets:38 errors:0 dropped:25 overruns:0 frame:0
          TX packets:48 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:2356 (2.3 Kb)  TX bytes:3564 (3.4 Kb)

linux-f5lc:/etc/sysconfig/network # cat /proc/net/bonding/bond0 
Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011)

Bonding Mode: fault-tolerance (active-backup)
Primary Slave: None
Currently Active Slave: eth3
MII Status: up
MII Polling Interval (ms): 100
Up Delay (ms): 0
Down Delay (ms): 0

Slave Interface: eth3
MII Status: up
Speed: 1000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: 20:14:12:04:00:09
Slave queue ID: 0

Slave Interface: eth5
MII Status: up
Speed: 1000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: 20:14:12:04:00:0b
Slave queue ID: 0

####################################################
网卡性能测试：MTU相关
在ubuntu下修改mtu为大于1500的值，会出错。
sudo ifconfig eth0 mtu 9000
提示：
SIOCSIFMTU: Invalid argument
怀疑是网卡驱动问题，
终端中输入
lspci
得知使用的网卡芯片是Intel 82573L

从intel网站下载最新版驱动：http://downloadcenter.intel.com/ ... e&DwnldId=15817  

解压并切换到src目录下，执行
make install
新编译生成的e1000e.ko被安装至 /lib/modules/'uname -r'/kernel/drivers/net/e1000e/e1000e.ko
试试新编译的驱动吧，先卸载当前使用的驱动
sudo rmmod e1000e
然后安装新生成的驱动
sudo modprobe e1000e
激活网卡
sudo ifconfig eth0 up
设置mtu
sudo ifconfig eth0 mtu 9000
输入ifconfig eth0查看，mtu已经设置成功。

至此，大功已经告成一半了。
ubuntu系统启动加载内核已经编好的e1000e.ko，要想使系统启动自动加载新编译的驱动，修改/etc/modules，
在下面添加如下两行：
-r e1000e
e1000e
第一行是先卸载内核已经加载的模块，
第二行是加载新生成的模块。


MTU=1500，设置网卡的MAC帧最大传输单位大小。

MTU : 1500-->9000
测试的BW: 940Mbit/s -->990Mbit/s

########################################################################
为 vsftp启动vsftp: 500 oops:missing value in config file for :Allow anonymous FTP

Vsftp.conf文件配置错误。
注意这里的内容前面不要空格，=号前后不要有空格。
=后面一定要有内容。
否则注释掉。

######################################################
vsftp配置相关：
关闭防火墙：
[root@localhost vsftpd]# iptables -L -n
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination   

关闭selinux:
[root@localhost vsftpd]# sestatus
SELinux status:                 disabled
[root@localhost vsftpd]# getenforce
Disabled
[root@localhost vsftpd]# setenforce 0
setenforce: SELinux is disabled
[root@localhost vsftpd]# 

修改配置文件：
匿名用户相关设置：
anonymous_enable=YES
anon_upload_enable=YES
anon_mkdir_write_enable=YES
#anon_other_write_enable=YES

系统用户相关设置：
local_enable=YES
write_enable=YES

登陆确认：
在dos下运行ftp ip
在ssh 下运行 ftp ip都可以

匿名用户用： ftp或anonymous ,对应家目录为/var/ftp
这个家目录只可以下载，没有修改或上传的权限，匿名用户如果要上传，可以对pub目录进行修改，
root@localhost vsftpd]# ls -ld /var/ftp
drwxr-xr-x 3 root root 4096 Apr  6 00:39 /var/ftp
[root@localhost vsftpd]# ls -ld /var/ftp/pub
drwxrwxr-x+ 3 root root 4096 Apr  6 00:52 /var/ftp/pub

[root@localhost vsftpd]# finger ftp
Login: ftp            			Name: FTP User
Directory: /var/ftp                 	Shell: /sbin/nologin
Never logged in.
No mail.
No Plan.
[root@localhost vsftpd]# 

[root@localhost vsftpd]# setfacl -m u:ftp:rwx /var/ftp/pub
[root@localhost vsftpd]# getfacl /var/ftp/pub
getfacl: Removing leading '/' from absolute path names
# file: var/ftp/pub
# owner: root
# group: root
user::rwx
user:ftp:rwx
group::r-x
mask::rwx
other::r-x
之后就匿名用户就可以对pub目录进行上传和修改了；

#######################################################################
######################################
服务器上硬盘长时间使用时会进入spindown的状态（类似standby状态） 3天左右

-------------------------------------------------------------------------
EID:Slt DID State DG       Size Intf Med SED PI SeSz Model            Sp 
-------------------------------------------------------------------------
8:0     163 UGood -  278.875 GB SAS  HDD N   N  512B AL13SEB300       D  
8:5     162 UGood -  278.875 GB SAS  HDD N   N  512B AL13SEB300       D  
8:7     164 UGood -  278.875 GB SAS  HDD N   N  512B AL13SEB300       D  
8:30    165 Onln  0  278.875 GB SAS  HDD N   N  512B AL13SEB300       U  
-------------------------------------------------------------------------
EID-Enclosure Device ID|Slt-Slot No.|DID-Device ID|DG-DriveGroup
DHS-Dedicated Hot Spare|UGood-Unconfigured Good|GHS-Global Hotspare
UBad-Unconfigured Bad|Onln-Online|Offln-Offline|Intf-Interface
Med-Media Type|SED-Self Encryptive Drive|PI-Protection Info
SeSz-Sector Size|Sp-Spun|U-Up|D-Down|T-Transition|F-Foreign
UGUnsp-Unsupported|UGShld-UnConfigured shielded|HSPShld-Hotspare shielded

 ./storcli-linux /c0 /e14 /s4 spinup

[root@localhost bin]# ./storcli-linux help | grep -i spin
storcli /cx[/ex]/sx spinup
storcli /cx[/ex]/sx spindown
storcli /cx show spinupdrivecount
storcli /cx set spinupdrivecount=<value> 
storcli /cx show spinupdelay
storcli /cx set spinupdelay=<value> 

################################################################


######
查看错误访问日志：
cat /var/log/secure

###################################################################

cp -n  用于negelect交换信息的；

############################################################swap相关：
free查看内存和swap信息
fdisk /dev/sd* 创新一个新的分区，
使用-l查看分区类型，并用-t 命令将分区类型设置为swap
mkswap /dev/sd** 将新创建的分区格式化为swap的文件系统
swapon /dev/sd** 启动新创建的swap分区
free查看swap分区信息；

###################################################################
	1.休眠及唤醒相关：
	如果无法休眠，提示not enough free swap
	可以先卸载现在的swap 分区  swapoff -a
	再创建一个大的swap 分区挂载即可；
	直接采用创建大swap分区追加到现有的swap分区上，确认还是无法休眠；
	
	网卡相关设置；
	“Supports wake-on: pumbg”项表明支持wake on lan，“wake-on: g”项表明此功能已经打开，“wake-on: d”表明此功能关闭，可以使用命令 “ethtool -s eth* wol g”将其打开
	
	 目前开，I350 两个网口，只有一个网卡可以设置打开wol功能； 不能设置的，默认是不支持网络唤醒功能；
	 
	 唤醒方法：
	 使用MAGPAC.EXE， 选择唤醒指定计算机，广播地址保持默认”255.255.255.255“，输入指定网卡的MAC地址即可；

############################################################################################

readme for zxusp:

1.zxusp 磁盘配置说明：
 SATA硬盘直接连接到磁阵上，在web下确认物理硬盘，无法识别到；SATA磁盘需要DSPAM子卡，子卡也是安装在硬盘盒里
的，用于从SATA转换成SAS的， 因为一般磁阵都是默认进行双通道访问的；
 SAS盘可以直接连接，连接后，在web下确认为被识别为非兼容盘， 需要进入ushell 做相关兼容化处理才可以变成兼容盘；

可以用tcpmapping 进行远程映射：telnet 访问： 10.43.167.90  port 121 ，让存储的人帮忙处理；

具体的步骤如下：


 1、进入 ushell； （telnet 磁阵管理口IP 10000  zte/zte, 或者用port23访问后切换到ushell）
 2、进入 dm 进程  sh 11 （进入dm）
 3、调用 dmDebugListAllPdIndex() 函数查看磁盘列表
 4、为每个磁盘调用 dmDebugClearPdMda() 函数清除元数据，参数是 Serial Number
   例如 dmDebugClearPdMda("6SJ41W950000B219B10A") ...
 5、复位后进dm进程，再次重建每个磁盘 dmDebugInitPdMda()，此时每个盘都是空闲盘

应该不需要重启
##############################################################################################

parted gpt分区学习
新盘挂载过程：
1. 分区
创建分区表
创建分区
sudo parted /dev/sdb mklabel gpt
sudo parted -s — /dev/sdb mkpart primary 0 -1s
sudo parted -s — /dev/sdb mkpart primary 0 100% 

2. mkfs
sudo blkid |grep c1d|awk -F\” ‘{print $2,$1}’|awk -F: ‘{print “sudo mkfs.ext3 -U”,$1,”&”}’ 

sudo mkfs.ext3 -u 886dfecd-478c-4520-831f-b211ad5b3247 /dev/sdb1 &
sudo mkfs.ext3 -u 1da4342e-ee15-41d4-820f-754e7c67e1b4 /dev/sdc1 &
3. fstab
vim /etc/fstab
4. mount
mount -a
一、parted的命令方式
Parted 命令分为两种模式：命令行模式和交互模式。
1、命令行模式： parted [option] device [command] ,该模式可以直接在命令行下对磁盘进行分区操作，比较适合编程应用。如：
# parted /dev/sdb print –显示磁盘/dev/sdb分区。
2、交互模式：parted [option] device
# parted /dev/sdb      –进入交互模式，建议使用交互模式，尤其是对parted命令不是很熟悉的情况下。
二、常用的2种分区表：MBR与GPT区别。
MBR：MBR分区表(即主引导记录)大家都很熟悉，是过去我们使用windows时常用的。
所支持的最大卷：2T，而且对分区有限制：最多4个主分区或3个主分区加一个扩展分区
GPT： GPT（即GUID分区表）。是源自EFI标准的一种较新的磁盘分区表结构的标准，是未来磁盘分区的主要形式。与MBR分区方式相比，具有如下优点。
突破MBR 4个主分区限制，每个磁盘最多支持128个分区。支持大于2T的分区，最大卷可达18EB。
三、parted命令常用功能。
当在命令行输入parted后，进入parted命令的交互模式。输入help会显示帮助信息。下面就简单介绍一下常用的功能
1、Check 简单检查文件系统。建议用其他命令检查文件系统，比如fsck
2、Help 显示帮助信息
3、mklabel 创建分区表， 即是使用msdos（MBR）还是使用gpt，或者是其他方式分区表
4、 mkfs 创建文件系统。该命令不支持ext3 格式，因此建议不使用，最好是用parted分好区，然后退出parted交互模式，用其他命令进行分区，比如：mkfs.ext3
5、mkpart 创建新分区。
格式：mkpart PART-TYPE  [FS-TYPE]  START  END
PART-TYPE 类型主要有primary（主分区）, extended（扩展分区）, logical（逻辑区）. 扩展分区和逻辑分区只对msdos。
fs-type   文件系统类型，主要有fs32，NTFS，ext2，ext3等
start end 分区的起始和结束位置。
6、mkpartfs 建立分区及其文件系统。目前还不支持ext3文件系统，因此不建议使用该功能。最后是分好区后，退出parted，然后用其他命令建立文件系统。
7、print 输出分区信息。该功能有3个选项，
free 显示该盘的所有信息，并显示磁盘剩余空间
number 显示指定的分区的信息
all 显示所有磁盘信息
8、resize 调整指定的分区的大小。目前对ext3格式支持不是很好，所以不建议使用该功能。
9、rescue 恢复不小心删除的分区。如果不小心用parted的rm命令删除了一个分区，那么可以通过rescue功能进行恢复。恢复时需要给出分区的起始和结束的位置。然后parted就会在给定的范围内去寻找，并提示恢复分区。
10、rm 删除分区。命令格式 rm  number 。如：rm 3 就是将编号为3的分区删除
11、select 选择设备。当输入parted命令后直接回车进入交互模式是，如果有多块硬盘，需要用select 选择要操作的硬盘。如：select /dev/sdb
12、set 设置标记。更改指定分区编号的标志。标志通常有如下几种：boot  hidden   raid   lvm 等。
boot 为引导分区，hidden 为隐藏分区，raid 软raid，lvm 为逻辑分区。
如：set 3  boot  on   设置分区号3 为启动分区
注：以上内容为parted常用的功能，由于该工具目前对ext3支持得不是很好，因此有些功能无法应用，比如move（移动分区）和resize等。
四、parted分区功能事例。
1、用命令模式 为/dev/sdb创建gpt类型文件分区表,并分500G分区。然后为该分区创建ext3文件系统。并将该分区挂载在/test文件夹下。
#  parted  /dev/sdb  mklabel     —创建分区表
#  parted  /dev/sdb  mkpart  ext3  0  500000    —创建500G分区/dev/sdb1
# mkfs.ext3  /dev/sdb1      —-将分区/dev/sdb1格式化成ext3格式文件系统
# mount  /dev/sdb1 /test   —将/dev/sdb1 挂载在/test下
如果让系统自动挂载/dev/sdb1 需手工编辑/etc/fstab文件。并在文件末尾添加如下内容：
/dev/sdb1             /test                ext3    defaults        0 0
2、创建大小为4G的交互分区。由于已经创建了500G的/dev/sdb1 ,因此再创建的分区为/dev/sdb2
# parted /dev/sdb mkpart swap 500000 504000  —创建4G分区/dev/sdb2
# mkswap  /dev/sdb2   —-将/dev/sdb2创建为交换分区
# swapon /dev/sdb2   —-激活/dev/sdb2
如果让系统自动挂载/dev/sdb2这个交换分区，需手工编辑/etc/fstab文件。并在文件末尾添加如下内容：
/dev/sdb2             swap                swap    defaults        0 0
3、恢复被误删除的分区(也可以参考testdisk命令)。由于parted直接写磁盘，因此一旦不小心删除了某一分区，建议立即用rescue恢复。下面通过事例来理解恢复过程。
# parted /dev/sdb mkpart ext3 504000 514000 —-创建10G分区/dev/sdb3
# mkfs.ext3 /dev/sdb3  —将/dev/sdb3格式化成ext3文件系统。
# parted /dev/sdb rm 3 —-删除/dev/sdb3
# parted /dev/sdb rescue 504000 514000    —依照屏幕提示，输入yes即可恢复被误删除分区
有关Linux GPT 分区的一些操作。
# parted /dev/sdb
GNU Parted 1.8.1
Using /dev/sdb
Welcome to GNU Parted! Type ‘help’ to view a list of commands.
(parted) select /dev/sdb
选择操作磁盘sdb
(parted) mklabel gpt
将MBR磁盘格式化为GPT
(parted) mkpart primary 0 100
划分一个起始位置为0大小为100M的主分区
(parted) mkpart primary 100 200
划分一个起始位置为100M大小为100M的主分区
(parted) mkpart primary 0 -1
划分所有空间到一个分区
(parted) print
打印当前分区
(parted) quit
可能还会用到的一些命令
(parted) mklable msdos
如果要反过来.将GPT磁盘转化为MBR磁盘
在这样分完分区后,还要使用mkfs.ext3来进行格式化
#partprobe
#mkfs.ext3 -F /dev/sdb1
记的哦，因为fdisk是不支持GPT磁盘，所以使用fdisk -l来查看磁盘刚才的分区是没有用的. 挂载之后可以用df-h查看分区使用情况。
###########################################################################################################

使用parted命令对齐分区，以获得最佳性能:

在Linux系统上的大型存储阵列上创建分区(译者注：实际上是对从阵列上划分给系统的LUN分区，系统将每个LUN识别为一个磁盘)，会遇到两大常见问题。第一个问题很容易，使用fdisk命令得到的错误信息已经提示了解决问题的办法：

    WARNING: The size of this disk is 8.0 TB (7970004230144 bytes).
    DOS partition table format can not be used on drives for volumes
    larger than (2199023255040 bytes) for 512-byte sectors. Use parted(1) and GUID 
    partition table format (GPT).

译者注：磁盘大小是8TB。DOS分区表格式不能在超过2TB（512个字节的扇区）的卷上使用。请使用parted命令和GUID分区表格式（GPT）
答案是：使用parted命令。如果你的系统上没有parted，请安装它吧！

第二个问题是来自parted的警告：
    (parted) mklabel gpt
    (parted) mkpart primary 0 100%
    Warning: The resulting partition is not properly aligned for best performance.
    Ignore/Cancel?
译者注：生成的分区没有正确地对齐以实现最佳性能。忽略/取消？

不论你使用怎样的数字组合，这条错误信息都不断地出现。你尝试选择了忽略，但错误根本没被忽略。

网上有一些讨论这个问题的帖子，惠普官方帮助论坛上的一个帖子真正戳中了问题的核心。（译者注：文中提到的惠普论坛帖子现已无法访问）

下面是正确对齐分区的快速分步指南。它是那个惠普帖子的提炼总结，希望大家能快速上手。这个方法对大多数阵列行之有效（实际上它适用于我所见过的所有阵列）；在惠普的帖子中还提到了更多可行的配置选项，我在这里只列出最常用的配置。

1.获得你阵列的alignment参数（记得要将sdb替换为系统内核看到的设备名称）

    # cat /sys/block/sdb/queue/optimal_io_size
    1048576
    # cat /sys/block/sdb/queue/minimum_io_size
    262144
    # cat /sys/block/sdb/alignment_offset
    0
    # cat /sys/block/sdb/queue/physical_block_size
    512

2.把optimal_io_size的值与alignment_offset的值相加，之后除以physical_block_size的值。在我的例子中是：(1048576 + 0) / 512 = 2048。

3.这个数值是分区起始的扇区。新的parted命令应该写成类似下面这样

mkpart primary 2048s 100%

2048s中的字母s是很有意义的：它告诉parted，你的输入是2048扇区，而不是2048字节，也不是2048兆字节。

4.如果一切顺利，分区将会被成功创建并没有任何警告信息。然后你就可以检查分区是否对齐了（如有必要，请将下面命令中的1替换为合适的分区号）。

    (parted) align-check optimal 1                                            
    1 aligned

正如我之前暗示的，会有一些特例，上面的做法对那些特例并不奏效：例如，如果optimal_io_size是0


###################################################################################################

FCIP,FCoE,iSCSI之间的区别


网络中有许多的概念，比如FC, FCP, FCIP, FCoE等，这些概念内容交叉很容易混淆。刚接触的时候很难分清楚之间的联系和区别。
在SAN网络当中，目前比较流行的连接协议分为两种，一种是FC，另一种是ISCSI。这两种协议各有利弊。FC的稳定性和性能高，但是昂贵，扩展性相对 较差。ISCSI便宜，扩充性好。在实际的环境中有时候需要高性能和高扩展性。这个时候就很难取舍。与和熊掌不可兼得嘛。
解决这个困境的答案也许在于PoP（协议中的协议），也就是将一个协议打包到另外一个协议中。在这里我们就有聊FCIP和FCoE。这两个协议都是将FC连接协议打包到IP类网络中。区别在于，FCIP将FC包在四层TCP/IP层打包，但是FCoE在二层打包。
也就是FCIP将数据交由TCP/IP包，FCoE则是直接封装在帧里。
我们看到的区别在于，FCIP可以路由，而FCoE不行。只能通过MAC地址进行定位。在远距离数据传输的时候FCIP是可以实现的，但是FCIP的开销 也是很大的。效率不会很高。FCoE虽然不能远距离连接，但是在本地LAN中可以实现很高的速度。这对于服务器应用来讲是很重要的。我们可以使用FCIP 进行容灾，用FCoE提供数据访问。
随着10G的高速以太网的出现FCoE的性能还会有很显著的提高。未来的SAN网络是不是会和LAN网络融合，我们拭目以待

##########################################################################################

linux下网络唤醒其他主机(wol)  

1.要使用的工具安装：
yum install wol
2.用法：
wol 目标mac 地址
3.说明：
目标机器要开启wol功能
 linux下使用ethtool工具来查看：

ethtool eth* 查看网卡信息


如上图所示，eth0默认没有开启wol功能
    Supports Wake-on: pumbg  //是否支持wol
    Wake-on: g                          //是否开启wol以及是何种模式（d 表示禁用，g表示响应magic packet的唤醒）

接下来开启eth0的wol功能
ethtool -s eth0 wol g   //s表示改变参数的意思


最后，就可以在同一个局域网上的其他电脑上发送magic packet包来唤醒这台机器了。
我一般都是写一个简单的脚本来开启机房的服务器，毕竟mac地址的记忆和每次的输入好麻烦啊
#!/bin/bash
wol 目标mac地址

注意：对于网卡的操作要使用root用户。

#########################################################################################

LVM related:
fdisk /dev/sdb --n--p--1--+5G--L--t (8e:linux LVM)
先创建PV:pvcreate /dev/sdb1 /dev/sdb2
创建 VG:  vgcreate myvg /dev/sdb{1,2} [--physicalextentsize PhysicalExtentSize]
vgdisplay
创建LV: 
lvcreate -L 500M -n mydata myvg   （需要指定大小和LV_name 及所用的VG）
lvcreate -l 100%VG -n lvdata -m0 datavg  //使用vg的全部空间创建lv的命令；

lvdisplay
lvs
lsblk
新创建的LV的访问目录 ll /dev/myvg/mydata  --》/dev/mapper/myvg-mydata
对这个分区的操作和其它分区一样，进行格式化和挂载即可；
mkfs.ext2 /dev/myvg/mydata
mount /dev/myvg/mydata /mnt
pvdisplay ：可以查看到每个PV的使用情况，对于没有使用的PV，可以进行移除，操作如下：

先保护数据：
[root@zte mnt]# pvmove /dev/sdb2
  No data to move for myvg
从VG中删除PV：
[root@zte mnt]# vgreduce myvg /dev/sdb2
  Removed "/dev/sdb2" from volume group "myvg"

最后再删除PV
[root@zte mnt]# pvremove /dev/sdb2
  Labels on physical volume "/dev/sdb2" successfully wiped
VG扩展：
vgextend myvg /dev/sdb3  (会自动匹配PE的大小)
LV扩展：
lvextend -L 1G /dev/myvg/mydata  扩展逻辑卷到1G
文件系统边界扩展 （df -lhp查看）
resize2fs /dev/myvg/mydata 扩展成和物理空间一样大，可以在不卸载的情况下进行扩展；
文件系统边界缩小，必须要先卸载，并进行文件系统的检测；

检测文件系统命令：

fsck:进行元数据和数据的匹配检测，也适用于ext2文件系统
e2fsck:针对ext2文件系统可以使用这个，功能更强，

-f 前置检测  -p 自动修复 -y 对所有选择回答yes
-a == -p 

umount /mnt
e2fsck -f /dev/myvg/mydata
逻辑边界缩减：resize2s /dev/myvg/mydata 200M
物理边界缩减  lvreduce -L 200M /dev/myvg/mydata
lvs 进行查看确认
mount /dev/myvg/mydata /mnt 查看内部数据是否有问题；

remark:--删除lv vg pv的过程：
delete lv: lvremove /dev/datavg/lvdata
delete vg: vgremove datavg
delete pv: pvremove /dev/nvme0n1 /dev/nvme1n1

[root@localhost home]# lvs
  LV      VG       Attr       LSize   Pool Origin Data%  Move Log Cpy%Sync Convert
  lv_home VolGroup -wi-ao---- 503.91g                                             
  lv_root VolGroup -wi-ao----  50.00g                                             
  lv_swap VolGroup -wi-ao----   4.00g                                             
  lvdata  datavg   -wi-a-----   2.91t  

[root@localhost home]# lvremove /dev/datavg/lvdata
Do you really want to remove active logical volume lvdata? [y/n]: y
  Logical volume "lvdata" successfully removed
[root@localhost home]# lvs
  LV      VG       Attr       LSize   Pool Origin Data%  Move Log Cpy%Sync Convert
  lv_home VolGroup -wi-ao---- 503.91g                                             
  lv_root VolGroup -wi-ao----  50.00g                                             
  lv_swap VolGroup -wi-ao----   4.00g 


[root@localhost home]# vgs
  VG       #PV #LV #SN Attr   VSize   VFree
  VolGroup   1   3   0 wz--n- 557.91g    0 
  datavg     2   0   0 wz--n-   2.91t 2.91t
[root@localhost home]# vgremove datavg
  Volume group "datavg" successfully removed
[root@localhost home]# vgs
  VG       #PV #LV #SN Attr   VSize   VFree
  VolGroup   1   3   0 wz--n- 557.91g    0 

[root@localhost home]# pvs
  PV           VG       Fmt  Attr PSize   PFree
  /dev/nvme0n1          lvm2 a--    1.46t 1.46t
  /dev/nvme1n1          lvm2 a--    1.46t 1.46t
  /dev/sda2    VolGroup lvm2 a--  557.91g    0 
[root@localhost home]# pvremove /dev/nvme0n1 /dev/nvme1n1
  Labels on physical volume "/dev/nvme0n1" successfully wiped
  Labels on physical volume "/dev/nvme1n1" successfully wiped
[root@localhost home]# pvs
  PV         VG       Fmt  Attr PSize   PFree
  /dev/sda2  VolGroup lvm2 a--  557.91g    0 



issue1:
[root@localhost ~]# pvcreate /dev/sdb1
  Can't open /dev/sdb1 exclusively.  Mounted filesystem?
[root@localhost ~]# mkfs.ext2 /dev/sdb1
mke2fs 1.41.12 (17-May-2010)
/dev/sdb1 is apparently in use by the system; will not make a filesystem here!

[root@localhost ~]# dmsetup status
myvg-mydata: 0 1024000 linear 

[root@localhost ~]# dmsetup remove myvg-mydata
[root@localhost ~]# dmsetup status
No devices found



@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@md常规配置方法：
mdadm -C /dev/md0 -a yes -l 0 -n 2 /dev/nvme0n1 /dev/nvme1n1
查看：
lsblk
mdadm -D /dev/md0
cat /proc/mdstat

删除raid:
mdadm -S /dev/md0    // 停止raid
mdadm --zero-superblock /dev/sdb5,对于其他分区格式也一样。   //删除元数据

[root@localhost home]# mdadm -C /dev/md0 -a yes -l 0 -n 2 /dev/nvme0n1 /dev/nvme1n1
mdadm: /dev/nvme0n1 appears to be part of a raid array:
       level=container devices=0 ctime=Thu Jan  1 08:00:00 1970
mdadm: /dev/nvme1n1 appears to be part of a raid array:
       level=container devices=0 ctime=Thu Jan  1 08:00:00 1970
Continue creating array? md
Continue creating array? (y/n) y
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md0 started.
[root@localhost home]# lsblk
NAME                        MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
sda                           8:0    0 558.4G  0 disk  
?..sda1                        8:1    0   500M  0 part  /boot
?..sda2                        8:2    0 557.9G  0 part  
  ?..VolGroup-lv_root (dm-0) 253:0    0    50G  0 lvm   /
  ?..VolGroup-lv_swap (dm-1) 253:1    0     4G  0 lvm   [SWAP]
  ?..VolGroup-lv_home (dm-2) 253:2    0 503.9G  0 lvm   /home
nvme0n1                     252:0    0   1.5T  0 disk  
?..md0                         9:0    0   2.9T  0 raid0 
nvme1n1                     252:64   0   1.5T  0 disk  
?..md0                         9:0    0   2.9T  0 raid0 



[root@localhost home]# mdadm -D /dev/md0
/dev/md0:
        Version : 1.2
  Creation Time : Wed Nov 16 22:53:14 2016
     Raid Level : raid0
     Array Size : 3125364736 (2980.58 GiB 3200.37 GB)
   Raid Devices : 2
  Total Devices : 2
    Persistence : Superblock is persistent

    Update Time : Wed Nov 16 22:53:14 2016
          State : clean 
 Active Devices : 2
Working Devices : 2
 Failed Devices : 0
  Spare Devices : 0

     Chunk Size : 512K

           Name : localhost.localdomain:0  (local to host localhost.localdomain)
           UUID : 1782cc23:cedbeb60:f6b59060:83179ab2
         Events : 0

    Number   Major   Minor   RaidDevice State
       0     252        0        0      active sync   /dev/nvme0n1
       1     252       64        1      active sync   /dev/nvme1n1


[root@localhost home]# cat /proc/mdstat 
Personalities : [raid0] 
md0 : active raid0 nvme1n1[1] nvme0n1[0]
      3125364736 blocks super 1.2 512k chunks
      
unused devices: <none>

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#####MD 相关：
mdadm -S /dev/md0   //停止软raid
mdadm --assemble --scan //重新组织raid


###MD with imsm
mdadm -S /dev/md0   //停止软raid
mdadm --assemble --scan //重新组织raid
mdadm -I /dev/md/imsm0  //确认不可用：



@@@杂项
mdadm --assemble --scan

mdadm --examine /dev/md/imsm0

mdadm --create --verbose --level=5 --raid-devices=3 --chunk=64 --auto=mdp /dev/md0 /dev/sd[bcd]

mdadm -C /dev/md/imsm /dev/nvme0n1 /dev/nvme1n1 -n2 -e imsm 
mdadm -C /dev/md0 /dev/md/imsm -n 2 -l 0 -c 128
@@

###MD with imsm配置相关：
需要安装mdadm-3.3.2-5及以上版本的mdadm, 才可以使用imsm选项

//创建container:
mdadm -C /dev/md/imsm /dev/nvme0n1 /dev/nvme1n1 -n 2 -e imsm   
(此时/dev/md/imsm -->/dev/md127, 此时的imsm和md127都只是container,不是最终的raid设备，需要执行下面的创建raid的命令，利用container创建一个raid设备，才可以最终使用)
//使用一个新的md名称创建raid0
mdadm -C /dev/md0 /dev/md/imsm -n 2 -l 0 -c 128

//清除RSTe raid信息：
step1 : 停止所有的raid containers and  volumes
mdadm --stop /dev/md0
mdadm --stop /dev/md127

step2:清除superblock
mdadm --zero-superblock /dev/nvme0n1
mdadm --zero-superblock /dev/nvme1n1

step3: 确认 cat /proc/mdstat中没有任何信息了即可；

[root@localhost home]# mdadm -C /dev/md/imsm /dev/nvme0n1 /dev/nvme1n1 -n 2 -e imsm
mdadm: container /dev/md/imsm prepared.
[root@localhost home]# lsblk
NAME                        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda                           8:0    0 558.4G  0 disk 
?..sda1                        8:1    0   500M  0 part /boot
?..sda2                        8:2    0 557.9G  0 part 
  ?..VolGroup-lv_root (dm-0) 253:0    0    50G  0 lvm  /
  ?..VolGroup-lv_swap (dm-1) 253:1    0     4G  0 lvm  [SWAP]
  ?..VolGroup-lv_home (dm-2) 253:2    0 503.9G  0 lvm  /home
nvme0n1                     259:0    0   1.5T  0 disk 
nvme1n1                     259:1    0   1.5T  0 disk 

//此时生成的md127只是一个container，不可以进行读写：
[root@localhost home]# sudo ls /dev/md*
/dev/md127

/dev/md:
autorebuild.pid  imsm  md-device-map
[root@localhost home]# mdadm -D /dev/md127
/dev/md127:
        Version : imsm
     Raid Level : container
  Total Devices : 2

Working Devices : 2

  Member Arrays :

    Number   Major   Minor   RaidDevice

       0     259        0        -        /dev/nvme0n1
       1     259        1        -        /dev/nvme1n1



[root@localhost home]# mdadm -C /dev/md127 /dev/md/imsm -n 2 -l 0 -c 128   //不可以使用md127继续创建raid0，需要使用一个新的设备名：
mdadm: /dev/md127 is already in use.
[root@localhost home]# mdadm -I /dev/md/imsm
[root@localhost home]# lsblk
NAME                        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda                           8:0    0 558.4G  0 disk 
?..sda1                        8:1    0   500M  0 part /boot
?..sda2                        8:2    0 557.9G  0 part 
  ?..VolGroup-lv_root (dm-0) 253:0    0    50G  0 lvm  /
  ?..VolGroup-lv_swap (dm-1) 253:1    0     4G  0 lvm  [SWAP]
  ?..VolGroup-lv_home (dm-2) 253:2    0 503.9G  0 lvm  /home
nvme0n1                     259:0    0   1.5T  0 disk 
nvme1n1                     259:1    0   1.5T  0 disk 

//因为md127不是最终的md设备，所以无法进行读写；
[root@localhost home]# dd if=/dev/md127 of=/dev/null bs=2M
0+0 records in
0+0 records out
0 bytes (0 B) copied, 0.000203909 s, 0.0 kB/s


[root@localhost home]# mdadm -C /dev/md0 /dev/md/imsm -n 2 -l 0 -c 128
mdadm: array /dev/md0 started.
[root@localhost home]# lsblk
NAME                        MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
sda                           8:0    0 558.4G  0 disk  
?..sda1                        8:1    0   500M  0 part  /boot
?..sda2                        8:2    0 557.9G  0 part  
  ?..VolGroup-lv_root (dm-0) 253:0    0    50G  0 lvm   /
  ?..VolGroup-lv_swap (dm-1) 253:1    0     4G  0 lvm   [SWAP]
  ?..VolGroup-lv_home (dm-2) 253:2    0 503.9G  0 lvm   /home
nvme0n1                     259:0    0   1.5T  0 disk  
?..md0                         9:0    0   2.9T  0 raid0 
nvme1n1                     259:1    0   1.5T  0 disk  
?..md0                         9:0    0   2.9T  0 raid0 

[root@localhost home]# mdadm -D /dev/md0
/dev/md0:
      Container : /dev/md/imsm, member 0
     Raid Level : raid0
     Array Size : 3125620736 (2980.82 GiB 3200.64 GB)
   Raid Devices : 2
  Total Devices : 2

          State : clean 
 Active Devices : 2
Working Devices : 2
 Failed Devices : 0
  Spare Devices : 0

     Chunk Size : 128K


           UUID : f3454a0a:73db03fa:a9dd8f10:cb85b8d0
    Number   Major   Minor   RaidDevice State
       0     259        1        0      active sync   /dev/nvme1n1
       1     259        0        1      active sync   /dev/nvme0n1


[root@localhost home]# dd if=/dev/md0 of=/dev/null bs=2M
^C2231+0 records in
2230+0 records out
4676648960 bytes (4.7 GB) copied, 2.41709 s, 1.9 GB/s


[root@localhost home]# fdisk -l


Disk /dev/nvme0n1: 1600.3 GB, 1600321314816 bytes
64 heads, 32 sectors/track, 1526185 cylinders
Units = cylinders of 2048 * 512 = 1048576 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000


Disk /dev/nvme1n1: 1600.3 GB, 1600321314816 bytes
64 heads, 32 sectors/track, 1526185 cylinders
Units = cylinders of 2048 * 512 = 1048576 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000


Disk /dev/md0: 3200.6 GB, 3200635633664 bytes
2 heads, 4 sectors/track, 781405184 cylinders
Units = cylinders of 8 * 512 = 4096 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 131072 bytes / 262144 bytes
Disk identifier: 0x00000000


@@@说明 imsm md127 md0之间的关系：
[root@localhost home]# sudo ls /dev/md*
/dev/md0  /dev/md127

/dev/md:
autorebuild.pid  imsm  md-device-map
[root@localhost home]# sudo ls -l /dev/md/imsm 
lrwxrwxrwx. 1 root root 8 Nov 17 18:15 /dev/md/imsm -> ../md127



[root@localhost home]# mdadm --examine /dev/md127
/dev/md127:
          Magic : Intel Raid ISM Cfg Sig.
        Version : 1.3.00
    Orig Family : 259f0cbc
         Family : 259f0cbc
     Generation : 00000002
     Attributes : All supported
           UUID : 3d12d40c:79e26511:6daea831:d4c2a83a
       Checksum : 86b70693 correct
    MPB Sectors : 1
          Disks : 2
   RAID Devices : 1

  Disk00 Serial : 547400CW3P2CGN-2
          State : active
             Id : 00000000
    Usable Size : 3125621262 (1490.41 GiB 1600.32 GB)

[0]:
           UUID : f3454a0a:73db03fa:a9dd8f10:cb85b8d0
     RAID Level : 0
        Members : 2
          Slots : [UU]
    Failed disk : none
      This Slot : 0
     Array Size : 6251241472 (2980.82 GiB 3200.64 GB)
   Per Dev Size : 3125621248 (1490.41 GiB 1600.32 GB)
  Sector Offset : 0
    Num Stripes : 12209458
     Chunk Size : 128 KiB
       Reserved : 0
  Migrate State : idle
      Map State : normal
    Dirty State : clean

  Disk01 Serial : 547400CW3P2CGN-1
          State : active
             Id : 00000000
    Usable Size : 3125621262 (1490.41 GiB 1600.32 GB)
##########################################################

######################################################################################

9361卡下raid空间扩展相关：
storcli /cx/vx expand size=<value> [expandarray]  storcli /c0 /v0 expand size=100GB expandarray  (100G为增量)
storcli /cx/vx|vall show expansion      storcli /c0 /v0 show expansion  查询信息中，只有OCE 为YES时才可以执行扩展
raid大小调整后，需要重新挂载后，系统下才可以识别到调整后的raid的容量
#######################################################################################

分区上报命令： partprobe 或 partx 命令，执行后用 cat /proc/parttion查询结果；
[root@localhost ~]# partprobe /dev/sdb
Warning: WARNING: the kernel failed to re-read the partition table on /dev/sdb (Device or resource busy).  As a result, it may not reflect all of your changes until after reboot.
[root@localhost ~]# partx /dev/sdb
# 1:        63- 10506509 ( 10506447 sectors,   5379 MB)
# 2:  10506510- 21013019 ( 10506510 sectors,   5379 MB)
# 3:         0-       -1 (        0 sectors,      0 MB)
# 4:         0-       -1 (        0 sectors,      0 MB)

##########################################################################################
SAS3008 -R5300 12 盘下挂硬盘的识别方法：
总结：
SAS盘的WWN号就是SAS地址，是全球唯一的标识；
SATA盘接在系统中，查询到的SAS地址是expander下行口的地址，不是SATA本身的地址,一般为**01，**02..，
和SAS地址的最后一位和槽位号相同，即SAS协议对SATA盘的协商有问题；
8盘的环境接SATA盘，需要再确认下

SATA 盘：
[root@localhost bin]# diskman -i /dev/sdb
WWN(ata address)       : 5000cca243c4169b
Sas3ircu 0 display:
SAS Address                             : 50019c6-0-0000-0001
GUID                                    : 5000cca243c4169b
[root@localhost bin]# sudo ls -l /dev/disk/by-id
lrwxrwxrwx. 1 root root  9 Oct 21 14:19 wwn-0x5000cca243c4169b -> ../../sdb

SAS盘：
[root@localhost ~]# diskman -i /dev/sdd
WWN(sas address)          : 5000039678026872
SAS3ircu 0 display:
SAS Address                             : 5000039-6-7802-6872
  GUID                                    : 5000039678026871
Ls –ls  /dev/disk/by-id
lrwxrwxrwx 1 root root  9 Apr 20  2016 wwn-0x5000039678026871 -> ../../sdd

SAS3008下做了raid的情况：
  Volume wwid                             : 0825cbe1673b777f
lrwxrwxrwx 1 root root  9 Apr 20 07:45 wwn-0x600508e0000000007f773b67e1cb2508 -> ../../sde

###############################################################################################
#############################################AL13SXB60EN 中有一个块读取时会发生报错
硬盘问题备注：
[root@localhost ~]# smartctl -a /dev/sdc
smartctl 5.43 2012-06-30 r3573 [x86_64-linux-2.6.32-431.el6.x86_64] (local build)
Copyright (C) 2002-12 by Bruce Allen, http://smartmontools.sourceforge.net

Vendor:               TOSHIBA 
Product:              AL13SXB60EN     
Revision:             0101
User Capacity:        600,127,266,816 bytes [600 GB]
Logical block size:   512 bytes
Logical Unit id:      0x5000039678026871
Serial number:        8540A002FWSB
Device type:          disk
Transport protocol:   SAS
Local Time is:        Wed Apr 20 07:44:21 2016 CST
Device supports SMART and is Disabled
Temperature Warning Disabled or Not Supported
SMART Health Status: OK

Current Drive Temperature:     35 C
Drive Trip Temperature:        65 C
Manufactured in week 32 of year 2015
Specified cycle count over device lifetime:  50000
Accumulated start-stop cycles:  8
Specified load-unload count over device lifetime:  600000
Accumulated load-unload cycles:  9
Elements in grown defect list: 0

Error counter log:
           Errors Corrected by           Total   Correction     Gigabytes    Total
               ECC          rereads/    errors   algorithm      processed    uncorrected
           fast | delayed   rewrites  corrected  invocations   [10^9 bytes]  errors
read:          0        4         7         0          0       4749.719           7
write:         0        0         0         0          0       1421.202           0
verify:        0        0         0         0          0          1.460           0

[root@localhost bin]# diskman -s /dev/sdd    发生问题的盘
Permanent defect  (p-list): 572
Grown defect list (g-list): 0

Smart Status(ASC/ASCQ)    : 0x0/0x0 

UncorrectedWriteErr       : 0
UncorrectedReadErr        : 6    (有6个不可恢复的读错误，可能重新写一下这些问题扇区，就能恢复)
UncorrectedvVerifyErr     : 0
NonMediumErr              : 2


[root@localhost bin]# dd if=/dev/sdd of=/dev/null bs=1M iflag=direct
dd: reading `/dev/sdd': Input/output error
1072+0 records in
1072+0 records out
1124073472 bytes (1.1 GB) copied, 5.78488 s, 194 MB/s
[root@localhost bin]# 

dmesg:

[root@localhost bin]# dmesg
sd 2:0:5:0: [sdd] Unhandled sense code
sd 2:0:5:0: [sdd] Result: hostbyte=DID_OK driverbyte=DRIVER_SENSE
sd 2:0:5:0: [sdd] Sense Key : Medium Error [current] 
Info fld=0x2186e1
sd 2:0:5:0: [sdd] Add. Sense: Read retries exhausted
sd 2:0:5:0: [sdd] CDB: Read(10): 28 00 00 21 84 00 00 04 00 00
sd 2:0:5:0: [sdd] Unhandled sense code
sd 2:0:5:0: [sdd] Result: hostbyte=DID_OK driverbyte=DRIVER_SENSE
sd 2:0:5:0: [sdd] Sense Key : Medium Error [current] 
Info fld=0x2186e1
sd 2:0:5:0: [sdd] Add. Sense: Read retries exhausted
sd 2:0:5:0: [sdd] CDB: Read(10): 28 00 00 21 84 00 00 04 00 0

##########################################################################

###########################################
查询rpm 包的安装路径：
[root@localhost TOOL]# ll scli-1.7.2-7.i386.rpm 
-rwxrwxrwx. 1 root root 3213061 Apr 20 16:44 scli-1.7.2-7.i386.rpm

[root@localhost TOOL]# rpm -ql scli
/opt/QLogic_Corporation/SANsurferCLI/adapters.properties
/opt/QLogic_Corporation/SANsurferCLI/fcscli-exitcodes.txt
/opt/QLogic_Corporation/SANsurferCLI/flashcfg.properties
/opt/QLogic_Corporation/SANsurferCLI/lib.tgz
/opt/QLogic_Corporation/SANsurferCLI/menu.properties
/opt/QLogic_Corporation/SANsurferCLI/nvramdefs.tgz
/opt/QLogic_Corporation/SANsurferCLI/readme.txt
/opt/QLogic_Corporation/SANsurferCLI/scli
/opt/QLogic_Corporation/SANsurferCLI/sfcli.properties

####################################################
######################################
rpm 命令汇总：
rpm -ql | grep "***"
rpm -e ***卸载软件

驱动rpm包方式更新的方法：
rpm -Uvh *.rpm

##rpm包安装相关：
如果用-i 安装过程中提示与现有文件冲突，或需要依赖一些其它的文件等等，而终止安装,可以使用
rpm -i --force --nodeps 可以忽略所有依赖关系和文件问题，什么包 
都能安装上，但这种强制安装的软件包不能保证完全发挥功能

rpm -qa | grep hardwaremon* （查询）

2)rpm 包相关：

-ivh 安装
-Uvh 升级
-q 列出指定已安装rpm软件包名
-qa 列出所有已安装rpm软件包名
-qi 列出指定已安装rpm 软件包信息
-qpl 列出rpm软件包内文件信息
-qpi 列出rpm软件包的描述信息
-qf 查询指定文件属于哪个rpm软件包
-e删除包

查询安装路径：
scli-1.7.2-7.i386.rpm 
rpm -ql scli
###########################################################
######lspci 查询的信息确认：
		LnkCap:	Port #2, Speed 5GT/s, Width x4, ASPM L0s L1, Exit Latency L0s <4us, L1 <32us  --设备支持的速率---显示的是当前设备支持的能力
		LnkSta:	Speed 5GT/s, Width x4, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-      --协商后的速率-----显示的是当前设备link的状态
		LnkCtl2: Target Link Speed: 5GT/s, EnterCompliance- SpeedDis-                               --pcie slot支持的速率---LCTL2—Link Control 2 Register  控制当前链路状态的寄存器
  
LnkCap--设备的link能力寄存器--显示设备的link能力
LnkCtl--设备的link控制寄存器--用于控制设备处于哪一种link状态
LnkSta--设备的link状态寄存器--显示当前设备link后处于什么链路状态

##############################################################
 查看 SELinux状态及关闭SELinux 

查看SELinux状态：

1、/usr/sbin/sestatus -v      ##如果SELinux status参数为enabled即为开启状态

SELinux status:                 enabled

2、getenforce                 ##也可以用这个命令检查

关闭SELinux：

1、临时关闭（不用重启机器）：

setenforce 0                  ##设置SELinux 成为permissive模式

                              ##setenforce 1 设置SELinux 成为enforcing模式

2、修改配置文件需要重启机器：

修改/etc/selinux/config 文件

将SELINUX=enforcing改为SELINUX=disabled

重启机器即可
###############################################################

SATA HDD性能参考：
技术支持提到的：2.5   110~130左右  3.5 180~200左右

#################################################################
################alias 相关：
alias
vi /etc/profile
在文档最后加上： alias ss='service network restart'
. /etc/profile   声明配置文件中变量
再执行alias可以查看到刚定义的别名了

命令行下快捷键：
ctrl +a 切换到行首
ctrt+e 切换到行尾
ctrl+k 删除光标后的内容
ctrt+u 删除光标前的内容

##########################vi编辑命令：
删除当前行到行尾：
  命令模式：dG
末行模式：:.,$d

命令行模式下：
按o在当前行下新建一行
按O 在当前行上一行新建一行
按u撤销操作；
按h:左移一位  j:下移一位 k:上移一位 l:右移一位
1.上下左右移动光标：

    h：左    l：右    k：上    j：下

2.删除一行：dd

3.删除一个字符：x

4.删除一个换行符：J

5.在光标下方新建一行，并且进入插入模式：o（小写字母o）

6.在光标上方新建一行，并且进入插入模式：O（大写字母O）

7.光标移动到下一单词的词首：w

8.光标移动到前一单词的词首：b

9.光标移动到下一单词的词尾：e

10.光标移动到前一单词的词尾：ge

11.移动到当前行第一个字符：0（数字0）

12.移动到当前行的第一个非空字符：^

13.移动到当前行的行尾：$

14.移动到本行中的指定字符：fc（c就是要找到的这个字符）

15.向左移动到本行中的指定字符：Fc（c就是要找到的这个字符）

16.向右移动到本行中的指定字符：tc（c就是要找到的这个字符）

17.括号匹配：%    

    这个需要解释一下：假设有下面一行：（a + b） × c，假设当前光标在左括号（上，在普通模式下输入%命令就会使光标自动跳转到右括号）上。

18.移动到指定行：30G（30就是行号）

19.移动到文件末尾：G

20.移动到文件头：gg或者1G

21.定位到文件的位置的百分之多少：30%（30就是要定位的比例）

22.移动到当前这一屏幕的开头：H（H代表Head的意思）

23.移动到当前这一屏幕的中间：M（M代表Middle的意思）

24.移动到当前这一屏幕的末尾：L（L代表Last的意思）

25.将屏幕向上移动半屏幕：ctrl+U

26.将屏幕向下移动半屏幕：ctrl+D

27.向前滚动一屏幕：ctrl+F

28.反向滚动一屏幕：ctrl+B

29.将光标所在行滚动到当前屏幕顶部：zt

30.将光标所在行滚动到当前屏幕底部：zb

31.将光标所在行滚动到当前屏幕中部：zz

32.撤销undo上次操作：u

33.重做redo上次操作：ctrl+R
############################################################
######vi末行模式：
：set nu   :set nonu
u#撤消上一步操作
/Fedora#查找Fedora字符
:s /Fedora/Redhat #将Fedora字符替换为Redhat(只替换在光标所在的行)
:1,.s/redhat/fedora
#.号表示当前行,即光标所在行
#将第1行到当前行(.)第一次出现的redhat字符代替为fedora
:1,.s/redhat/fedora/g
#将第1行到当前行(.)所有出现的redhat字符代替为fedora,g全局标志
:1,$s/redhat/fedora/g
#$表示最后一行
#将第1行到最后一行所有出现的redhat字符代替为fedora
:%s/redhat/fedora/g
#同上一个命令

##########################################################
##################硬盘相关说明：
日立全球存储技术(HGST)
1: WD 2: SEAGATE 3: HGST    WD和HGST 2011年合并，合并后出货量占到全球HDD市场的48%.

HDD:　WD、hgst、seagate、toshiba
ssd: intel、hgst、其它

toshiba: 
2.5INCH---AL13SEB(10K,512n,64MB,SAS2)/AL13SXB(15K,512n,64MB,SAS2)
          /AL14SEB(10K,(512n/512e/4kn),128MB,SAS3)
3.5INCH--MG03ACA(SATA,7.2K,512n,64MB)/MG03SCA(SAS,7.2K,512n,64MB)
     /MG04ACA(SATA,7.2K,512e,128MB)/MG04SCA(SAS,7.2K,(512e,4kn),128MB)

wd:WD****
hgst:HUC**/HUA**/HTE**/HUS**
seagate:ST**
####################################################
#######################kick start install配置相关########
suse11.0~suse12.1

label suse11.3
  kernel suse11.3/linux
  append initrd=suse11.3/initrd install=nfs://129.16.5.11/mnt/install/suse11.3  autoyast=nfs://129.16.5.11/mnt/install/suse11.3/suse11.3.xml  splash=silent showopts

rh6.2~rh7.1;centos7.0

label rh6.5
  kernel rh6.5/vmlinuz
  append ks=nfs:129.16.5.11:/mnt/install/rh6.5/ks.cfg ksdevice=link initrd=rh6.5/initrd.img


label tlinux2.0
  kernel tlinux2.0/vmlinuz
  append ks=nfs:129.16.5.11:/mnt/install/tlinuz2.0/ks.cfg ksdevice=link initrd=tlinux2.0/initrd.img

label cgslV5.01.20.I1
  kernel cgslV5.01.20.I1/vmlinuz
  append ks=nfs:129.16.5.11:/mnt/install/cgslV5.01.20.I1/ks.cfg ksdevice=link initrd=cgslV5.01.20.I1/initrd.img
  
label fedora
  kernel fedora/vmlinuz
  append ks=nfs:129.16.5.11:/mnt/install/fedora/ks.cfg ksdevice=link initrd=fedora/initrd.img

label ubuntu
  kernel ubuntu12.04/linux
  append ks=nfs:129.16.5.11:/mnt/install/ubuntu12.04/ks.cfg ksdevice=link initrd=ubuntu12.04/initrd.gz --quiet

#########################################################################################
#########dd命令实现系统盘完全copy的问题#####
dd if=/dev/sdb of=/dev/sdc 后两个盘的分区信息如下：
且使用sdc作为系统盘时，需要进行2308 BIOS配置菜单下设置sdc为启动盘盘可以成功启动；


   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1   *           1          64      512000   83  Linux
Partition 1 does not end on cylinder boundary.
/dev/sdb2              64       72841   584582144   8e  Linux LVM




   Device Boot      Start         End      Blocks   Id  System
/dev/sdc1   *           1          64      512000   83  Linux
Partition 1 does not end on cylinder boundary.
/dev/sdc2              64       72841   584582144   8e  Linux LVM

######################################################################################
#########dd命令实现系统盘完全copy的问题#####
dd if=/dev/sdb of=/dev/sdc 后两个盘的分区信息如下：
且使用sdc作为系统盘时，需要进行2308 BIOS配置菜单下设置sdc为启动盘盘可以成功启动；
sdb:
   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1   *           1          64      512000   83  Linux
Partition 1 does not end on cylinder boundary.
/dev/sdb2              64       72841   584582144   8e  Linux LVM
sdc:
   Device Boot      Start         End      Blocks   Id  System
/dev/sdc1   *           1          64      512000   83  Linux
Partition 1 does not end on cylinder boundary.
/dev/sdc2              64       72841   584582144   8e  Linux LVM

type2: 600G的系统盘--》300G盘上，查到到两个盘的分区表信息完全一样，
所以300G的盘中文件系统破损，无法正常启动；
time dd if=/dev/sdb of=/dev/sdc bs=256k iflag=direct
dd: writing `/dev/sdc': No space left on device
300000000000 bytes (300 GB) copied, 2015.96 s, 149 MB/s

type3:600G的系统盘--》900G盘上,复制后，两个盘的分区表信息完全一样
time dd if=/dev/sdd of=/dev/sdb bs=256k iflag=direct
600127266816 bytes (600 GB) copied, 3682.71 s, 163 MB/s

##########################################################

#####################网络相关工具：
[root@localhost home]# mii-tool eth2
eth2: negotiated 100baseTx-FD, link ok
[root@localhost home]# ethtool eth2  （可以查到速率及连接状态，但是没有协商的速率）
	Link detected: yes
#############################Linux netstat命令详解
Netstat 命令用于显示各种网络相关信息，如网络连接，路由表，接口状态 (Interface Statistics)，masquerade 连接，多播成员 (Multicast Memberships) 等等；
列出所有端口 (包括监听和未监听的)：
列出所有端口 netstat -a      列出所有 tcp 端口 netstat -at     列出所有 udp 端口 netstat -au
列出所有处于监听状态的 Sockets：
  只显示监听端口 netstat -l   只列出所有监听 tcp 端口 netstat -lt 只列出所有监听 udp 端口 netstat -lu

显示每个协议的统计信息：
显示所有端口的统计信息 netstat -s    显示 TCP 或 UDP 端口的统计信息 netstat -st 或 -su

在 netstat 输出中显示 PID 和进程名称 netstat -p
netstat -p 可以与其它开关一起使用，就可以添加 “PID/进程名称” 到 netstat 输出中，这样 debugging 的时候可以很方便的发现特定端口运行的程序。

在 netstat 输出中不显示主机，端口和用户名 (host, port or user)
当你不想让主机，端口和用户名显示，使用 netstat -n。将会使用数字代替那些名称。
持续输出 netstat 信息   netstat -c
显示核心路由信息 netstat -r
 找出程序运行的端口 netstat -ap | grep ssh
找出运行在指定端口的进程  netstat -an | grep ‘：80‘
显示网络接口列表 netstat -i
显示详细信息，像是 ifconfig 使用 netstat -ie:
IP和TCP分析:
查看连接某服务端口最多的的IP地址
netstat -nat | grep "192.168.1.15:22" |awk '{print $5}'|awk -F: '{print $1}'|sort|uniq -c|sort -nr|head -20
TCP各种状态列表:
netstat -nat |awk '{print $6}'
先把状态全都取出来,然后使用uniq -c统计，之后再进行排序。
netstat -nat |awk '{print $6}'|sort|uniq -c
netstat -nat |awk '{print $6}'|sort|uniq -c|sort -rn
####################################lsof
lsof(list open files)是一个列出当前系统打开文件的工具。在linux环境下，任何事物都以文件的形式存在，通过文件不仅仅可以访问常规数据，还可以访问网络连接和硬件。所以如传输控制协议 (TCP) 和用户数据报协议 (UDP) 套接字等，系统在后台都为该应用程序分配了一个文件描述符，无论这个文件的本质如何，该文件描述符为应用程序与基础操作系统之间的交互提供了通用接口。因为应用程序打开文件的描述符列表提供了大量关于这个应用程序本身的信息，因此通过lsof工具能够查看这个列表对系统监测以及排错将是很有帮助的。


##################################################################################tee命令

ifconfig | tee /home/aa.out

###############################################################################
fio读写参数说明：
fio -name=testc -directory=/home/test -ioengine=sync -numjobs=8 -iodepth=32 --rw=read -bs=256k -size=500M -runtime=30m -direct=1 -group_reporting=1

fio -name=testc -filename=/dev/sdb -ioengine=libaio -numjobs=8 -iodepth=32 --rw=read -bs=4k -time_based -runtime=30m  -direct=1 -group_reporting=1


说明：
-directory=/home/test 对目录读写， 要先创建 test目录，而不是文件；
-filename=/dev/sdb  对设备进行读写；

 -size=500M -runtime=30m 这两个参数同时存在时，以小的为准，即如果读完500M的时间小于30m,以读完500M的时间为准；


fio -name=testc -directory=/home/test -ioengine=sync -numjobs=8 -iodepth=32 --rw=read -bs=256k -size=500M -time_based -runtime=30m -direct=1 -group_reporting=1


-size=500M -time_based -runtime=30m ： 但如果这三个参数同时存在，读写的大小还是500M，但以时间为准，即500M读写完了，还没到30m,则要重复读取这个500M的空间；
###################################################################################
########################标准输入输出：
输入输出默认指向当前的操作终端：

[root@localhost ~]# sudo ls -l /dev/std*
lrwxrwxrwx. 1 root root 15 May 26 20:50 /dev/stderr -> /proc/self/fd/2
lrwxrwxrwx. 1 root root 15 May 26 20:50 /dev/stdin -> /proc/self/fd/0
lrwxrwxrwx. 1 root root 15 May 26 20:50 /dev/stdout -> /proc/self/fd/1

[root@localhost ~]# sudo ls -l /proc/self/fd/?
ls: cannot access /proc/self/fd/3: No such file or directory
lrwx------. 1 root root 64 May 28 17:31 /proc/self/fd/0 -> /dev/pts/1
lrwx------. 1 root root 64 May 28 17:31 /proc/self/fd/1 -> /dev/pts/1
lrwx------. 1 root root 64 May 28 17:31 /proc/self/fd/2 -> /dev/pts/1

[root@localhost ~]# ps
  PID TTY          TIME CMD
23793 pts/1    00:00:00 bash
66069 pts/1    00:00:00 p

ls -l > aa  覆盖输出重定向
ls -l >> aa  追加输出重定向

###确认标准输出方向：
tail -f /var/log/messages > aa
ctrl+z //将任务挂起到后台
[root@localhost ~]# tail -f /var/log/messages > aa
^Z
[1]+  Stopped                 tail -f /var/log/messages > aa
[root@localhost ~]# ps
  PID TTY          TIME CMD
23793 pts/1    00:00:00 bash
66451 pts/1    00:00:00 tail
66575 pts/1    00:00:00 ps

[root@localhost ~]# sudo ls -l /proc/66451/fd/?
lrwx------. 1 root root 64 May 28 17:35 /proc/66451/fd/0 -> /dev/pts/1
l-wx------. 1 root root 64 May 28 17:35 /proc/66451/fd/1 -> /root/aa
lrwx------. 1 root root 64 May 28 17:34 /proc/66451/fd/2 -> /dev/pts/1
lr-x------. 1 root root 64 May 28 17:35 /proc/66451/fd/3 -> /var/log/messages
lr-x------. 1 root root 64 May 28 17:35 /proc/66451/fd/4 -> inotify

###stdin重定向，适用于哪些不支持执行操作文件的命令：
[root@localhost ~]# tr 'a-z' 'A-Z' /etc/passwd   //NG
tr: extra operand `/etc/passwd'
Try `tr --help' for more information.

tr 'a-z' 'A-Z' < /etc/passwd  // ok


mail -s 'root to hello'  root < /etc/passwd 发送邮件
执行mail 命令，找到指定的邮件标题后，输入对应的数字就可以查看了


ls -l /etc/passwd /etc/sadfaf 1>aa 2>bb  //输入输出分别定位到不同的文件中；
ls -l /etc/passwd /etc/sadfaf &>aa  //使用&&符号将stdout 和stderrout定位到相同的文件中；
ls -l /etc/passwd /etc/sadfaf &>>aa  //使用&&符号将stdout 和stderrout定位到相同的文件中(追加不覆盖)

##### <<定义输入截止符，否则就要手动按ctrl+D 来结束；

[root@localhost ~]# cat << END    //使用输出截止符，并将输出定向到标准输出
> 1111111111
> 22222222222
> END
1111111111
22222222222


[root@localhost ~]# cat << END >aa  //使用输出截止符，并将输出定向到文件；
> 1111111111111
> 222222222222
> END
[root@localhost ~]# cat aa
1111111111111
222222222222


###管道命令： 会将前一个命令的stdout(不包含stderrout) 作为第二个命令的stdin，
如果第一个命令有stderrout,为防止干扰，可以先用 2>/dev/null将 stderrout过滤掉
ls -l /etc/passwd /etc/aaa | grep a

##部分命令不支持管道符，需要采用xargs命令：

[root@localhost ~]# which find | rpm -qf
rpm: no arguments given for query
[root@localhost ~]# which find | xargs rpm -qf
findutils-4.4.2-6.el6.x86_64
[root@localhost ~]# 


##使用管道时，文件定位方向的查看：
[root@localhost ~]# tail -f /var/log/messages | grep May   
May 28 12:31:50 localhost kernel: sdg:
May 28 12:31:50 localhost kernel: sdf:
May 28 12:31:50 localhost kernel: sdh: unknown partition table
May 28 12:31:50 localhost kernel: unknown partition table
May 28 12:31:50 localhost kernel: unknown partition table
May 28 12:31:50 localhost kernel: sd 0:0:5:0: [sdg] Attached SCSI disk
May 28 12:31:50 localhost kernel: sd 0:0:7:0: [sdf] Attached SCSI disk
May 28 12:31:51 localhost kernel: sd 0:0:8:0: [sdh] Attached SCSI disk
May 28 12:31:51 localhost MR_MONITOR[5394]: <MRMON139> Controller ID:  0   Deleted VD:  #012    0
May 28 12:31:51 localhost MR_MONITOR[5394]: <MRMON136> Controller ID:  0   Global Hot Spare disabled:  #012    -:-:7
^Z  
[1]+  Stopped                 tail -f /var/log/messages | grep May
[root@localhost ~]# ps
  PID TTY          TIME CMD
23793 pts/1    00:00:00 bash
68771 pts/1    00:00:00 tail
68772 pts/1    00:00:00 grep
68773 pts/1    00:00:00 ps
[root@localhost ~]# sudo ls -l /proc/68771/fd/?
lrwx------. 1 root root 64 May 28 17:54 /proc/68771/fd/0 -> /dev/pts/1
l-wx------. 1 root root 64 May 28 17:54 /proc/68771/fd/1 -> pipe:[517626]
lrwx------. 1 root root 64 May 28 17:54 /proc/68771/fd/2 -> /dev/pts/1
lr-x------. 1 root root 64 May 28 17:54 /proc/68771/fd/3 -> /var/log/messages
lr-x------. 1 root root 64 May 28 17:54 /proc/68771/fd/4 -> inotify
[root@localhost ~]# sudo ls -l /proc/68772/fd/?
lr-x------. 1 root root 64 May 28 17:54 /proc/68772/fd/0 -> pipe:[517626]
lrwx------. 1 root root 64 May 28 17:54 /proc/68772/fd/1 -> /dev/pts/1
lrwx------. 1 root root 64 May 28 17:54 /proc/68772/fd/2 -> /dev/pts/1
[root@localhost ~]# fg
tail -f /var/log/messages | grep May
^C
[root@localhost ~]# 

#################################################################
###############7805 下查看expander 信息，及phy 信息；
执行arcconf getconfig 1 pd ，查询expander信息：
     Device #9
         Device is an Enclosure services device
         Reported Channel,Device(T:L)       : 2,0(0:0)
         Enclosure ID                       : 0
         Expander ID                        : 0
         Enclosure Logical Identifier       : 50019C600000003F
         Expander SAS Address               : 50019C600000003F
         Type                               : SES2
         Vendor                             : ZTE CORP
         Model                              : 720381 EvBd 255
         Firmware                           : 1
         Status of Enclosure services device
            Temperature Sensor Status 1     : Unknown
            Speaker status                  : Not available

[root@localhost home]# arcconf smp 

 Usage: SMP <Controller#> <Expander# CommandType1>      [ASCII]
        SMP <Controller#> <Expander# CommandType2 PHY#> [ASCII]
 ==============================================================
 Expander#            : Expander ID to whom the command needs to be sent

 PHY#                 : The PHY Identifier (ONLY for Discover and PHY Error Log Request)

 We Support the following SMP Command Types
 CommandType1         : RGR   - Report General Request
                      : RMR   - Report Manufacturer Request

 CommandType2         : DR    - Discover Request
                      : RPELR - Report PHY Error Log Request

 ASCII                : Displays ASCII Dump along with Hex Dump of the SMP Response

##arcconf smp  1  0 DR 0 //12盘环境为，0-11
##arcconf smp  1  0 rpelr 0  //12盘环境为，0-11

################################################################
#############################linux 开机启动配置方法：
redhat : 将命令追加到 /etc/rc.local 文件的最后
suse: 将命令追加到 /etc/rc.d/after.local文件的最后，
 如果上述文件不存在，就自己创建一下
###################################################

#######################################################################################################
windows 下磁盘配置命令：从裸盘到系统下可识别的盘（diskpart工具介绍说明：）
DISKPART> list disk

  磁盘 ###  状态           大小     可用     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  磁盘 0    联机              279 GB      0 B
* 磁盘 1    脱机              557 GB   557 GB

DISKPART> select disk 1

磁盘 1 现在是所选磁盘。

DISKPART> online disk

DiskPart 成功使所选磁盘联机。

DISKPART> list disk

  磁盘 ###  状态           大小     可用     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  磁盘 0    联机              279 GB      0 B
* 磁盘 1    联机              557 GB   557 GB

DISKPART> clean

DiskPart 成功地清除了磁盘。

DISKPART> create volume simple

指定的磁盘不是动态的。
请指定一个动态磁盘，然后再试一次。


DISKPART> convert dynamic                    // 第一次确认时，在这边卡住了，试了几次都没有成功，后来确认是当前的操作盘发生了变更，用list disk确认下当前操作盘的信息即可；

DiskPart 已将所选磁盘成功地转更换为动态格式。


DISKPART> create volume simple

DiskPart 成功地创建了卷。


DISKPART> assign letter=E

DiskPart 成功地分配了驱动器号或装载点。

DISKPART> format fs=ntfs label="new volume" quick

  100 百分比已完成

DiskPart 成功格式化该卷。

此时在系统下就可以看到磁盘设备了；

执行list volume,查看到新创建的卷为 “new volume”
DISKPART> list volume

  卷 ###      LTR  标签         FS     类型        大小     状态       信息
  ----------  ---  -----------  -----  ----------  -------  ---------  --------
  卷     0         系统保留         NTFS   磁盘分区         350 MB  正常
 系统
  卷     1     C                NTFS   磁盘分区         279 GB  正常         启
动
* 卷     2     E   new volume   NTFS   简单           557 GB  正常

执行list disk,查询到信息挂载的设备名：

DISKPART> list disk

  磁盘 ###  状态           大小     可用     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  磁盘 0    联机              279 GB      0 B
* 磁盘 1    联机              557 GB      0 B   *

############################################################################################

dos下的字符串过滤命令
ipconfig /all | findstr "DNS "

##########################################################
pcie ssd获取温度：
isdct dump -intelssd 0 datatype=nvmelog logid=197 | grep -i current
hdm generate-report --path=/dev/nvme1 | grep -i tempe


########################################################burnin test 使用说明：
主要用来测试 cpu, ram, disk, network

软件安装完毕后，在system information界面下，可以查看到服务器的详细配置信息；

手动测试配置项菜单：
configuraton -test selection& duty cycles and test perferences

1) cpu 
 主要包含两种测试类型：
指令测试（不选maximum heat,其它可选的都选上）
发热测试（只选maximum heat）
其它选项保持默认，不需要配置即可；

test selection& duty cycles :
可以设定时间或cycles, 哪个持续时间长以哪个为准；
某个测试项所占的比率，可以设定为100%

比如只选cpu, 设为100%
测试发热时，可以看 temperature 曲线的变化来查看加压的情况；
测试指令时，一般选2~3 cycles即可；

2)RAM
模式分为：
standard选项，会把内存空间都用完；
multi-process torture test： 选择这个选项时，下面的multi-process torture test setting 才可以进行配置；
     number of processes ： 填入逻辑CPU的数目
     % of RAM  : 设定每个逻辑cpu所占用的内存比率，
	  预期值：逻辑cpu数目* 每个占用用比率《=空闲的内存百分比，否则系统会发生卡死；
  	  （理论上：大于100% 会用到 虚拟内存，所有理论上大于100%也没有关系）
	  
	  
remark: 内存测试的流程，先将内存写满，然后读取并校验； 

test pattern: 可以选择测试码型，可以直接用默认的即可；

ram（标准）：只有部分cpu在加压；
ram(multi-process):每个cpu都在加压	 
且使用自动化脚本进行测试时，只能使用标准模式；
内存测试，一般设置cycle；


3）disk
为防止数据破坏，所以一般不选物理盘，选逻辑盘
如果确认硬盘中的数据没用，也可以直接选择物理盘；

选中c盘： 即选中 test this drive
test mode: 可以选择不同的测试算法，默认即可；
file size: 写的文件的大小占整个硬盘空间的百分比；
block size: 块大小
slow drive threshold: 最小带宽门限，可以不设置；
测试流程：先写入，然后读取再进行校验，　所有和使用iometer等工具不同，iometer只进行数据的写入或读取，并
统计BW及iops，而不进行数据的校验； 所有，这两种测试的测试方法不同；

４）网卡
测试模式：
 standard network test 
  发包并验证，不关心BW，只关心链路是否可靠； （loop 测试）
 advanced network test
 选择要测试的网卡，远端要打开endpoint 软件,在display endpoint处可以看到对端的网口信息；选择对应的
 网口后就可以进行ping包测试了， 发包并验证，不关心BW，只关心链路是否可靠
  备注： 
  1.如果调整机上一个网卡配置了多个IP地址，在endpoint处只能显示一个IP地址，所有要为被测机配置和
  看到的这个IP相同的IP地址，并选中这个IP地址才可以；
  2.成功开始测试后，在endpoint的窗口下，可以看到两台机器的IP地址信息，及测试带宽的信息等；
  
 
 
 其它设置项：
 1)error设置：主要设置发现错误时是否停止；
  reported whea hardware error要选中；
  
 2）logging:  max file size（lines）设置下；
 
 自动化测试执行方法： test --execute file ,选择脚本。
 
 脚本设计框架： loop N {cpu， ram, disk network}

 
 
 测试脚本sample1：
 
 安装上面的方法，手动设置配置参数后，选择file-save test config as， 保存设置的配置文件；
 
 然后编辑脚本文件（MyScript-自动测试脚本.bits）如下：
 
 LOAD "C:\Users\Administrator\Documents\PassMark\BurnInTest\LastUsed.bitcfg"  
 RUN CONFIG   

 测试脚本sample2：
SETERRORS ACTION STOP WINDOWS BLOCK
SETLOG LOG YES NAME "HardTest" PREFIX "R5300R3-" TIME yes REPORT TEXT LOGLEVEL YES TRACELEVEL A2 SUM YES LINES 1000000 PERIODIC 1 FILE ACCUMULATE
LOOP 3
{
SETDURATION  30
SETDUTYCYCLE  CPU  100
SETCPU GP no FPU no PRIME no MAX_HEAT yes MMX no 3DNOW no SSE no SSE2 no SSE3 no SSE4_1 no SSE4_2 no SSE4A no AES no
RUN CPU

SETCYCLES 30
SETDUTYCYCLE  CPU  100
SETCPU GP yes FPU yes PRIME yes MAX_HEAT no MMX yes 3DNOW yes SSE yes SSE2 yes SSE3 yes SSE4_1 yes SSE4_2 yes SSE4A yes AES yes
RUN CPU

SETDURATION  30
SETDUTYCYCLE  MEMORY  100
SETRAM TYPE STANDRAD PATTERN CYCLIC PRETEST no LOG yes
RUN MEMORY

SETCYCLES 1
SETDUTYCYCLE  DISK  100
SETDISK DISK g: MODE CYCLIC SLOW 0 FILE 2 BLOCK 256 SMART YES SEEK 10
RUN DISK

SETCYCLES 3
SETDUTYCYCLE  NETWORK  100
SETNETWORK ADD1 "192.168.5.2" ERROR EVERYPACKET TIMEOUT 4
RUN NETWORK
}


加载方法： test-excute scripts, 选择脚本即可
 
 #########################################################################################
#################rpm related
which perl

[root@localhost VMC]# which perl
/usr/bin/perl
[root@localhost VMC]# rpm -qf /usr/bin/perl
perl-5.16.3-283.el7.x86_64

[root@localhost VMC]# rpm -qa | grep -i perl

查询perl的安装后的路径
[root@localhost VMC]# rpm -ql perl




##################zxve相关说明：

1.本身已经安装了vnc服务：
rpm -ql tigervnc-server
但还没有配置启动，需要进行配置和启动才可以;
直接执行vnc命令，配置下密码即可；

[root@localhost VMC]# service vncserver status
Redirecting to /bin/systemctl status  vncserver.service
vncserver.service
   Loaded: not-found (Reason: No such file or directory)
   Active: inactive (dead)

   2. 直接执行 virsh查询到的 ID号可能是错误的
   [root@localhost VMC]# virsh list
 Id    Name                           State
----------------------------------------------------
 2     vmc                            running

 因为用vnc访问ip：2看到是 host的桌面而不是虚机的桌面，
 改成访问ip:1 看到的是虚机的桌面，且已经在安装系统，停在光盘设备检测的界面了；
 
 3. 用vnc访问虚机桌面时，第一次窗口显示不全，需要关闭后，第二次再打开是，显示正常了；

##############################################################
#####################cpu ,内存，io性能评估：
可能出现CPU瓶颈的应用有邮件服务器、动态web服务器等
可能出现内存瓶颈的有打印服务器、数据库服务器、静态web服务器等
i) load average这个输出值，这三个值的大小一般不能大于系统CPU的个数
ii) cpu性能评估
vmstat:
r列表示运行和等待cpu时间片的进程数，这个值如果长期大于系统CPU的个数，说明CPU不足，需要增加CPU。 
b列表示在等待资源的进程数，比如正在等待I/O、或者内存交换等。
 根据经验，us+sy的参考值为80%，如果us+sy大于 80%说明可能存在CPU资源不足。 
iii)内存：
free –m   应用程序可用内存/系统物理内存>70%时，表示系统内存资源非常充足，不影响系统性能
Vmstat:   一般情况下，si、so的值都为0, 如果si、so的值长期不为0，则表示系统内存不足。需要增加系统内存。
Iiii)磁盘：
Sar –d 或iostat –x –d
svctm的值与await很接近，表示几乎没有I/O等待，磁盘性能很好，如果await的值远高于svctm的值，则表示I/O队列
等待太长，系统上运行的应用程序将变慢，此时可以通过更换更快的硬盘来解决问题。 
%util项的值也是衡量磁盘I/O的一个重要指标，如果%util接近100%，表示磁盘产生的I/O请求太多，I/O系统已经满
负荷的在工作，该磁盘可能存在瓶颈。长期下去，势必影响系统的性能，可以通过优化程序或者通过更换更高、
更快的磁盘来解决此问题。

LOAD:
指标：< CPU个数 * 核心数 * 0.7   网上也有指标：< CPU个数 * 核心数 * 0.5
伪四核。 intel的i3或者i5有双核四线程的cpu，也就是每个核心可以几乎同时运行两个线程。当四核用。
真四核。 intel和amd都有的，就是四核四线程。
核心数相当于大脑数量，线程数相当于一个大脑能同时处理多少件事情（左右手同时画方和画圆知道不？）

###################################################################

 Linux下yum命令详解
主要功能是更方便的添加/删除/更新RPM包.
它能自动解决包的倚赖性问题.
它能便于管理大量系统的更新问题
一、yum list|more               列出所有包文件，可搭配grep查询软件包，如yum list |grep kernel
二、yum info xxx                 显示包xxx详细信息，即使xxx没有安装
三、yum update kernel       用yum升级内核
四、yum update                 全面升级系统
五、yum list available         列出升级源上所有可以安装的包(List all packages in the yum repositories available to be installed.)
六、yum list updates           列出升级源上所有可以更新的包(List all packages with updates available in the yum repositories.)
七、yum list installed          列出已经安装的包
八、yum install xxx              安装xxx包
九、yum update xxx            升级xxx包
十、yum remove xxx            删除xxx包

#####################################################################
linux下 cpu 逻辑核的查看方法：
cat /proc/cpuinfo  | grep -i processor | wc -l    可以查出所有的逻辑核的数目（即线程数目）
 

8/9#########linux系统下软raid配置命令 mdadm
multidisk --md
/dev/md*
man mdadm

Options :
-l: raid level
-n: numbers of disks to make raid
-c: chunk size （一般是bs的整数倍）
-a: automatic make md disk
-x: numbers of disks for spare

##创建软raid:mdadm -C /dev/md0 -a yes -l 0 -n 2 /dev/sdc{1,2}
   Device Boot      Start         End      Blocks   Id  System
/dev/sdc1               1         523     4200966   fd  Linux raid autodetect
/dev/sdc2             524        1046     4200997+  fd  Linux raid autodetect

mdadm -C /dev/md0 -a yes -l 0 -n 2 /dev/sdc{1,2}

##查看：cat /proc/mdstat 
##查看详细信息：mdadm -D /dev/md0

mkfs.ext /dev/md0
mkdir /test1
mount /dev/md0 /test1
[root@localhost bin]# cd /test1
[root@localhost test1]# ls
lost+found


watch -n 1 'cat /proc/mdstat'


##管理模式：
--remove(-r) --add (-a) --fault(-f)

##set fault manually
[root@localhost ~]# mdadm /dev/md0 -f /dev/sdc8
mdadm: set /dev/sdc8 faulty in /dev/md0

md0 : active raid1 sdc8[1](F) sdc7[0]
      2102400 blocks super 1.2 [2/1] [U_]
##remove disks
[root@localhost ~]# mdadm /dev/md0 -r /dev/sdc8
mdadm: hot removed /dev/sdc8 from /dev/md0

##add disks
[root@localhost ~]# mdadm /dev/md0 -a /dev/sdc8
mdadm: added /dev/sdc8

mkfs.ext3 -b 4096 -E stride=16 /dev/md0  //指定扩展选项stride 的格式化命令


###创建完raid后，执行：mdadm  -D --scan 扫描所有软raid的信息：并写入配置文件：
mdadm -D --scan >> /etc/mdadm.conf

[root@localhost ~]# mdadm  -D --scan
ARRAY /dev/md/localhost.localdomain:0 metadata=1.2 name=localhost.localdomain:0 UUID=d3d489f3:373b6f4a:b9622d54:fc8f0f31
ARRAY /dev/md/localhost.localdomain:0_0 metadata=1.2 name=localhost.localdomain:0 UUID=f212a10d:93791182:6c4b4e58:08ee11c0
ARRAY /dev/md0 metadata=1.2 name=localhost.localdomain:0 UUID=2dd4a619:d2f01b6c:f25cfce7:a151e7fc
[root@localhost ~]# mdadm -D --scan >> /etc/mdadm.conf

##stop 软raid命令：
mdadm -S /dev/md0
stop 软raid 命令，stop之后就看不到这个raid信息了；

##编辑了配置文件后，执行mdadm -A /dev/md0 --scan 能自动进行raid的组装操作
[root@localhost ~]# mdadm -A /dev/md0 --scan
mdadm: /dev/md0 has been started with 2 drives.

############################################################################
8.9###linux mysql 相关知识总结：
yum install mysql* -y
涉及的两个主要的包：
mysql-server.x86_64 
mysql-test.x86_64 （或 mysql-client）

service mysqld start
netstat -ntpl | grep -i 3306(Mysql默认的端口是3306)

#登陆mysql
启动命令： mysql
mysql [-u username] [-h host] [-p[password]] [dbname] 
username 与 password 分别是 MySQL 的用户名与密码，mysql的初始管理帐号是root，没有密码，注意：这个root用户不是Linux的系统用户。
MySQL默认用户是root，由于 初始没有密码，第一次进时只需键入mysql即可。 

##MySQL的几个重要目录
它的数据库文件、配置文件和命令文件分别在不同的目录
--数据库目录
/var/lib/mysql/ 
--配置文件 
/usr/share /mysql（mysql.server命令及配置文件）
--相关命令 
/usr/bin(mysqladmin mysqldump等命令)
--启动脚本
/etc/rc.d/init.d/（启动脚本文件mysql的目录


##修改登录密码
设置密码命令：usr/bin/mysqladmin -u root password 'new-password'  （因为开始时root没有密码， 所以-p旧密码一项就可以省略了）

修改密码格式：mysqladmin -u用户名 -p旧密码 password 新密码  (如果报错，用Q&A解决办法)


## 启动服务：
service mysqld start/stop/restart
chkconfig mysqld on 
chkconfig --list | grep -i mysql

##更改mysql数据库文件存储目录
比如从默认的/var/lib/mysql -->/home/data
1）service mysqld stop
2）mv /var/lib/mysql　/home/data/  （可能的步骤： chown -R mysql:mysql /home/data）
3)修改配置文件：
mv /etc/my.cnf /etc/my.cnf.bak
cp /usr/share/mysql/my-medium.cnf　/etc/my.cnf
vi /etc/my.cnf
将其中两次出现的“socket=” 处修改为：
socket  = /home/data/mysql/mysql.sock
4）vi /etc/rc.d/init.d/mysqld
将其中对应的位置修改为：
get_mysql_option mysqld datadir "/home/data/mysql"
5）
service mysqld restart
可以正常启动，则表示OK


##数据库常用操作命令：
show databases;
use mysql;
show tables;

建库：create database zhl;
建表：
use zhl;
//在刚创建的aaa库中建立表name,表中有id(序号，自动增 长)，xm（姓名）,xb（性别）,csny（出身年月）四个字段 
create table student (id int(3) auto_increment not null primary key,xm char(8),xb char(2),csny date);
//在刚创建的aaa库中建立表name,表中有id(序号，自动增 长)，xm（姓名）,xb（性别）,csny（出身年月）四个字段 
//向表中增加记录：
insert into student values('','jack','male','1999-11-11');
//用select命令来验证结果
select * from student;
//修改记录：
update student set csny='1000-1-1' where xm='tom';
//删除记录：
delete from student where xm='tom';
//删库和删表
drop database 库名; 
drop table 表名；


##增加mysql用户
//增加一个用户user_1密码为123，让他可以在任何主机上登录，并对所有数据库有查询、插入、修改、删除的权限。首先用以root用户连入MySQL，然后键入以下命令
mysql> grant select,insert,update,delete on *.* to user_1@"%" Identified by "123";

[root@localhost test1]# mysql -u root -p
Enter password: 
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)

Q&A解决办法：
# /etc/init.d/mysql stop
# mysqld_safe --user=mysql --skip-grant-tables --skip-networking &
# mysql -u root mysql
mysql> UPDATE user SET Password=PASSWORD(’newpassword’) where USER=’root’;
mysql> FLUSH PRIVILEGES;
mysql> quit
# /etc/init.d/mysql restart 
# mysql -uroot -p
Enter password: <输入新设的密码newpassword>
mysql> 
备注：使用这种方法后，不再支持匿名登陆了，即直接使用mysql 就无法登陆了；


####增加新用户及解决新用户无法登陆问题
----解决新用户无法登陆问题：
增加普通用户后，用root用户先登陆，然后执行：
mysql> use mysql
mysql> delete from user where user='';
mysql> flush privileges;
意思是删除匿名用户。 

---<<<<用户管理：>>>>>>
1）创建用户：
命令:CREATE USER 'username'@'host' IDENTIFIED BY 'password'; 
说明:username - 你将创建的用户名, host - 指定该用户在哪个主机上可以登陆,如果是本地用户可用localhost, 如果想让该用户可以从任意远程主机登陆,可以使用通配符%. password - 该用户的登陆密码,密码可以为空,如果为空则该用户可以不需要密码登陆服务器. 

范例：create user 'test'@'%' identified by '123';

2）授权：
命令:GRANT privileges ON databasename.tablename TO 'username'@'host
说明: privileges - 用户的操作权限,如SELECT , INSERT , UPDATE 等(详细列表见该文最后面).如果要授予所的权限则使用ALL.;databasename - 数据库名,tablename-表名,如果要授予该用户对所有数据库和表的相应操作权限则可用*表示, 如*.*. 
grant all on *.* to 'test'@'%';

remark: 此时验证在另外一台主机上，使用mysql -u test -p -h 128.0.0.201 ，可以访问目标主机上的数据库文件；

注意:用以上命令授权的用户不能给其它用户授权,如果想让该用户可以授权,用以下命令:
GRANT privileges ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION; 

3）设置与更改用户密码
命令:SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');如果是当前登陆用户用SET PASSWORD = PASSWORD("newpassword"); 

4）撤销用户权限 
命令: REVOKE privilege ON databasename.tablename FROM 'username'@'host'; 
说明: privilege, databasename, tablename - 同授权部分. 
例子: REVOKE SELECT ON *.* FROM 'pig'@'%';

注意: 假如你在给用户'pig'@'%'授权的时候是这样的(或类似的):GRANT SELECT ON test.user TO 'pig'@'%', 则在使用REVOKE SELECT ON *.* FROM 'pig'@'%';命令并不能撤销该用户对test数据库中user表的SELECT 操作.相反,如果授权使用的是GRANT SELECT ON *.* TO 'pig'@'%';则REVOKE SELECT ON test.user FROM 'pig'@'%';命令也不能撤销该用户对test数据库中user表的Select 权限. 

5）删除用户 
命令: DROP USER 'username'@'host';
####################################################################
##apache 命令帮助文档
可以直接访问： /www/apache/orge
也可以采用如下方法：
yum -y install httpd-manual
然后访问本地web地址即可；
安装后的manual文件在 /var/www目录下，使用中心主机的IP进行访问即可：
http://128.0.0.66/manual/

也可以在任意的虚拟主机后面追加manual来进行方法即可；
http://hello.b.com/manual/

###默认虚拟主机的定义
<VirtualHost 128.0.0.66:80>
   ServerName _default
   DocumentRoot "/www/default"
</VirtualHost>

###location的使用
<Location /status>
    SetHandler server-status    //server-status是apache内置的handler
	Order Deny,Allow
	Deny from all
	Allow from .foo.com
</Location>

directory 定义的是本地文件系统路径
location定义的是一个URL路径

配置实例，vi /etc/httpd/conf/httpd.conf中，启用以下handler:
 <Location /server-status>
    SetHandler server-status
    Order allow,deny
    Allow from all
</Location>

httpd -t 进行语法检查；
service httpd restart重启服务
然后使用IP/server-status 这个handler进行访问：
http://128.0.0.66/server-status
这里查看是的是服务器的状态信息，所以一般只允许特定的用户进行查看；


##https实例：
http是明文的协议；
https是加密传输协议；监听在443端口；

client 和 server端的通信流程，

先client先发起进行3次TCP/IP通信来建立TCP/IP的会话；
然后建立ssl会话（协商需要使用的加密算法--server端将自己的证书发送给服务器端--客户端验证证书，如果验证通过，
生成一个随机的对称秘钥发送给服务器端--客户端发起URL资源请求--服务器端将客户端请求的内容，用客户端发送过来的
对称秘钥加密后会送给客户端）

所以，其中的关键环节，sever要发送自己的证书给客户端，且客户端可以验证通过；所以需要服务器有一个可用的证书；
所以我们要找一个第三方的证书颁发机构，给我的服务器发证；且客户端需要将这个证书存放到本地上，用来验证其它人的
证书；
 

操作流程：
1）使用openssl 建立一个CA， 一个CA都会有自签的证书；
2）服务器端需要生成秘钥，然后将公钥发送给CA,由CA负责签署生成证书，然后发送给服务器；
3）服务器端需要配置使自己能够使用这个证书，并在客户端请求时，可以将证书发送给客户端，
4） 客户端使用自己保存的CA的证书来验证这个证书

CA和server放在同一台主机上也是可以的；
或者是找两台主机，一个做CA，一个做http server;

SSL的会话是无法基于主机名来区分的，只能基于IP进行；
这就意味着，如果我的主机只有一个IP地址，那它就只能为一个主机提供ssl会话功能；

###配置过程：
使用httpd -M 查看其中没有 对应的SSL模块，需要安装；
yum install mod_ssl
查看安装文件：
rpm -ql mod_ssl
[root@localhost default]# rpm -ql mod_ssl
/etc/httpd/conf.d/ssl.conf
/usr/lib64/httpd/modules/mod_ssl.so
/var/cache/mod_ssl
/var/cache/mod_ssl/scache.dir
/var/cache/mod_ssl/scache.pag
/var/cache/mod_ssl/scache.sem


#配置CA ，即需要生成自签证书
1）cd /etc/pki/CA

再执行(umask 077;openssl genrsa -out private/cakey.pem 2048) 生成私钥
[root@localhost CA]# (umask 077;openssl genrsa -out private/cakey.pem 2048)
Generating RSA private key, 2048 bit long modulus
...........................................+++
....................................+++
e is 65537 (0x10001)
[root@localhost CA]# ls -l private/
total 4
-rw-------. 1 root root 1675 Aug 14 15:38 cakey.pem
2）生成自签证书；
先编辑配置文件：
[root@localhost pki]# pwd
/etc/pki
[root@localhost pki]# vi tls/openssl.cnf 
定位到：[ req_distinguished_name ]，修改以下信息：
 countryName_default             = CN
stateOrProvinceName_default     = Henan
localityName_default    = Zhengzhou
0.organizationName_default      = MageEdu
organizationalUnitName_default  =Tech

再次 cd /etc/pki/CA
执行：openssl req -new -x509 -key private/cakey.pem -out cacert.pem -days 3655 生成自签证书
-days 是证书的有效期
[root@localhost CA]# openssl req -new -x509 -key private/cakey.pem -out cacert.pem -days 3655
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [CN]:
State or Province Name (full name) [Henan]:
Locality Name (eg, city) [Zhengzhou]:
Organization Name (eg, company) [MageEdu]:
Organizational Unit Name (eg, section) [Tech]:
Common Name (eg, your name or your server's hostname) []:ca.magedu.com   //要颁发给的主机，此处是给自己的
Email Address []:admin@magedu.com
[root@localhost CA]# ls
cacert.pem  certs  crl  newcerts  private
[root@localhost CA]# 

要让这个证书作为自签证书来使用，需要修改openssl中的部分配置信息：
cd /etc/pki
vi tls/openssl.conf文件：
定位到 [ CA_default ]，做如下修改：
dir             = /etc/pki/CA           # Where everything is kept
certs           = $dir/certs            # Where the issued certs are kept
crl_dir         = $dir/crl              # Where the issued crl are kept
database        = $dir/index.txt        # database index file.

certificate     = $dir/cacert.pem       # The CA certificate
serial          = $dir/serial           # The current serial number

再 cd  /etc/pki/CA 下，创建上面涉及到的几个目录：
 mkdir certs crl newcerts
 再创建两个文件：
 [root@localhost CA]# touch index.txt
[root@localhost CA]# echo 01 > serial
[root@localhost CA]# ls
cacert.pem  certs  crl  index.txt  newcerts  private  serial

##然后对httpd 服务进行配置：
cd /etc/httpd/
mkdir ssl
cd ssl
 执行  (umask 077; openssl genrsa 1024 > httpd.key) 生成秘钥  //此处用>,而不是上面的-out,两个类似
 [root@localhost ssl]# ll
total 4
-rw-------. 1 root root 887 Aug 14 16:15 httpd.key

再生成证书颁发请求：
[root@localhost ssl]# openssl req -new -key httpd.key -out httpd.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [CN]:
State or Province Name (full name) [Henan]:
Locality Name (eg, city) [Zhengzhou]:
Organization Name (eg, company) [MageEdu]:
Organizational Unit Name (eg, section) [Tech]:
Common Name (eg, your name or your server's hostname) []:hello.zhl.com
Email Address []:hello@zhl.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
[root@localhost ssl]# 
此时已经生成证书签署请求；
然后使用本地CA签发证书： 执行openssl ca -in /etc/httpd/ssl/httpd.csr -out /httpd.crt -days 3650签发证书：

[root@localhost ssl]# openssl ca -in /etc/httpd/ssl/httpd.csr -out /httpd.crt -days 3650
Using configuration from /etc/pki/tls/openssl.cnf
Check that the request matches the signature
Signature ok
Certificate Details:
        Serial Number: 1 (0x1)
        Validity
            Not Before: Aug 14 08:27:12 2016 GMT
            Not After : Aug 12 08:27:12 2026 GMT
        Subject:
            countryName               = CN
            stateOrProvinceName       = Henan
            organizationName          = MageEdu
            organizationalUnitName    = Tech
            commonName                = hello.zhl.com
            emailAddress              = hello@zhl.com
        X509v3 extensions:
            X509v3 Basic Constraints: 
                CA:FALSE
            Netscape Comment: 
                OpenSSL Generated Certificate
            X509v3 Subject Key Identifier: 
                75:98:69:33:EA:56:38:DD:DF:00:3B:7D:A3:A9:46:EC:F6:99:11:1D
            X509v3 Authority Key Identifier: 
                keyid:30:DB:00:20:2C:83:34:31:58:C3:13:6B:3B:7B:C9:47:FB:B8:4D:98

Certificate is to be certified until Aug 12 08:27:12 2026 GMT (3650 days)
Sign the certificate? [y/n]:y


1 out of 1 certificate requests certified, commit? [y/n]y
Write out database with 1 new entries
Data Base Updated
[root@localhost ssl]# 

且此时在CA目录下可以看到对应的证书签发信息；

[root@localhost ssl]# cd /etc/pki/CA/
[root@localhost CA]# ls
cacert.pem  crl        index.txt.attr  newcerts  serial
certs       index.txt  index.txt.old   private   serial.old
[root@localhost CA]# cat index.txt
V	260812082712Z		01	unknown	/C=CN/ST=Henan/O=MageEdu/OU=Tech/CN=hello.zhl.com/emailAddress=hello@zhl.com
[root@localhost CA]# cat serial
02
将证书复制到 ssl目录下：
[root@localhost CA]# cd /etc/httpd/ssl/
[root@localhost ssl]# ls
httpd.csr  httpd.key
[root@localhost ssl]# cp /httpd.crt .
[root@localhost ssl]# ls
httpd.crt  httpd.csr  httpd.key


然后再配置服务器可以使用颁发的证书：
 cd /etc/httpd/conf.d/
  vi ssl.conf 进行编辑
  <VirtualHost 128.0.0.66:443>
  ServerName hello.zhl.com
  DocumentRoot "/www/zhl.com"
  ErrorLog logs/ssl_error_log
TransferLog logs/ssl_access_log    //对应http的 customlog
LogLevel warn
  SSLEngine on
 SSLProtocol all -SSLv2   //不支持sslv2
 
 SSLCertificateFile /etc/httpd/ssl/httpd.crt  //签发的证书的位置
 SSLCertificateKeyFile /etc/httpd/ssl/httpd.key //私钥
 
 
 检查语法： httpd -t
  重启服务器： service httpd restart重启服务
  确认443端口已经开始监听：
  [root@localhost conf.d]# netstat -ntpl | grep 443
tcp        0      0 :::443                      :::*                        LISTEN      419/httpd 

直接用https://hello.zhl.com/ 访问时，提示此连接不受信任；
即本地PC不信任这个证书；处理方法如下：
需要将CA的证书导入到本地：
cd cd /etc/pki/CA/
将cacert.pem 证书传输到本地；
在本地PC上，将文件名改为 cacert.crt， 修改后文件图标会变成证书的图标，本来就应该使用这个扩展名；
直接双击这个文件，点击 “安装证书”，选择证书存储位置 “受信任的根证书颁发机构”，其它选默认即可完成证书的导入；
此时再用ttps://hello.zhl.com/  这个访问就可以正常访问了
###############################################################

//9361 下使用命令行，可以查看到MSM tool中显示的日志的信息：（4个盘做的raid5）
先执行storcli /c0 delete termlog 删除历史log
再执行storcli /c0 show termlog
先拔出第一个盘，日志中显示被拔出盘的sas address和 raid降级的信息
08/17/16  0:35:41: C0:EVT#67035-08/17/16  0:35:41: 112=Removed: PD 0c(e0x0a/s1)
08/17/16  0:35:41: C0:EVT#67036-08/17/16  0:35:41: 248=Removed: PD 0c(e0x0a/s1) Info: enclPd=0a, scsiType=0, portMap=00, sasAddr=50019c6000000041,0000000000000000
08/17/16  0:35:41: C0:EVT#67037-08/17/16  0:35:41: 114=State change on PD 0c(e0x0a/s1) from ONLINE(18) to FAILED(11)
08/17/16  0:35:41: C0:EVT#67038-08/17/16  0:35:41:  81=State change on VD 00/1 from OPTIMAL(3) to DEGRADED(2)
08/17/16  0:35:41: C0:EVT#67039-08/17/16  0:35:41: 251=VD 00/1 is now DEGRADED
08/17/16  0:35:41: C0:LoadBalance 0
再拔出一个盘，日志中显示被拔出盘的sas address和 raid offline的信息
08/17/16  0:43:05: C0:EVT#67042-08/17/16  0:43:05: 112=Removed: PD 0b(e0x0a/s0)
08/17/16  0:43:05: C0:EVT#67043-08/17/16  0:43:05: 248=Removed: PD 0b(e0x0a/s0) Info: enclPd=0a, scsiType=0, portMap=00, sasAddr=50019c6000000040,0000000000000000
08/17/16  0:43:05: C0:EVT#67044-08/17/16  0:43:05: 114=State change on PD 0b(e0x0a/s0) from ONLINE(18) to FAILED(11)
08/17/16  0:43:05: C0:EVT#67045-08/17/16  0:43:05:  81=State change on VD 00/1 from DEGRADED(2) to OFFLINE(0)

对应

   0 Active 6.0Gb/s   0x50019c6000000040 
   0 Active 6.0Gb/s   0x50019c6000000049 
   0 Active 6.0Gb/s   0x50019c600000004a 
   0 Active 6.0Gb/s   0x50000396083ae336 


9361 涉及log的命令：
[root@localhost InfoDiagnose]# storcli help | grep -i log
storcli /cx show eventloginfo
storcli /cx set termlog[=on|off|offthisboot]
storcli /cx show termlog [type=config|contents]
storcli /cx delete termlog
storcli /cx[/ex]/sx show diag paniclog [Query] | [ExtractSlot=x] 
storcli /cx[/ex]/sx show diag smartlog [file=filepath] 
storcli /cx[/ex]/sx show diag errorlog [file=filepath] 
storcli /cx show dequeuelog file=<filepath>

#############################################################################################
磁阵配置命令：
登录磁阵的telnet，（登录用户名密码：zte/zte）输入：tcs_debug.sh 128  4321 100这条命令;
若需关闭，则输入:tcs_debug.sh 128  0,再重启磁阵即可。

#######zte 磁阵配置方法：
--映射方法：
在FC协议处查询FC卡的WWPN，用WWPN创建一个主机，
查看物理盘（数据盘表示已经添加到虚拟盘中；空闲盘表示可以创建虚拟盘）
-->用空闲盘创建虚拟盘（设名称，级别，成员盘）
-->创建卷（将虚拟盘划分为不同的存储区域，这些存储区域称为卷）
         （当虚拟盘状态非正常时，或虚拟盘剩余容量为0时，不允许创建卷。）
          （创建卷时先选择虚拟盘，再设置卷名，容量等信息）
-->设置映射关系(将卷和主机加入到映射组，在映射组里组成主机和卷的对应关系，在主机上访问卷。从主机上看，一个卷映射为一个磁盘驱动器。)

---使用虚拟内存的方法：

登录磁阵的telnet，（登录用户名密码：zte/zte）;su 切换到root 用户； 
开启虚拟内存的命令：tcs_debug.sh 128  4321 100;  （配置后，在系统下fdisk -l能看到100G左右大小的盘；）
关闭虚拟内存的命令:tcs_debug.sh 128  0, 有时还要重启磁阵才可以生效
#############################################################################################

#####vmware 虚拟机常用配置命令：
连按2下tab键查看系统支持的命令
fdisk -l
lspci
sas2ircu-linux 0 display
uname -a

/tmp/servertool~/bin # lspci | grep -i network
0000:07:00.0 Network controller: Realtek Realtek 8168 Gigabit Ethernet [vmnic0]
0000:08:00.0 Network controller: Realtek Realtek 8168 Gigabit Ethernet [vmnic1]
0000:81:00.0 Network controller: Intel Corporation 82599EB 10-Gigabit SFI/SFP+ Network Connection [vmnic2]
0000:81:00.1 Network controller: Intel Corporation 82599EB 10-Gigabit SFI/SFP+ Network Connection [vmnic3]
/tmp/servertool~/bin # lspci | grep -i emulex
0000:04:00.0 Serial bus controller: Emulex Corporation Emulex LPe1250 8Gb PCIe Fibre Channel Adapter [vmhba2]
/tmp/servertool~/bin # lspci | grep -i 2008
0000:01:00.0 Mass storage controller: LSI LSI2008 [vmhba1]
/tmp/servertool~/bin # 

###vmware查看HBA卡、网卡驱动、firmware版本信息
在 ESXi 5.x 中，swfw.sh 命令随 vm-support 支持包收集工具一起提供。swfw.sh 命令可用来识别连接到主机的硬件的固件和驱动程序版本。要运行此命令，请使用该路径：

# /usr/lib/vmware/vm-support/bin/swfw.sh

/tmp # find / -name "swfw.sh"
/usr/lib/vmware/vm-support/bin/swfw.sh


###Identifying the firmware of a Qlogic or Emulex FC HBA：
/usr/lib/vmware/vmkmgmt_keyval/vmkmgmt_keyval -a   //查询emulex HBA卡信息：

###获取主机总线适配器当前使用的驱动程序类型
/usr/lib/vmware/vmkmod # esxcfg-scsidevs -a
vmhba0  ahci              link-n/a  sata.vmhba0                             (0:0:31.2) Intel Corporation Patsburg 6 Port SATA AHCI Controller
vmhba1  mpt2sas           link-n/a  sas.50015ebe0012973f                    (0:1:0.0) LSI Logic / Symbios Logic LSI2008
vmhba2  lpfc              link-up   fc.20000090fa61b583:10000090fa61b583    (0:4:0.0) Emulex Corporation LPe1250 8Gb Fibre Channel Host Adapter
vmhba32 ahci              link-n/a  sata.vmhba32                            (0:0:31.2) Intel Corporation Patsburg 6 Port SATA AHCI Controller
vmhba33 ahci              link-n/a  sata.vmhba33                            (0:0:31.2) Intel Corporation Patsburg 6 Port SATA AHCI Controller
vmhba34 ahci              link-n/a  sata.vmhba34                            (0:0:31.2) Intel Corporation Patsburg 6 Port SATA AHCI Controller
vmhba35 ahci              link-n/a  sata.vmhba35                            (0:0:31.2) Intel Corporation Patsburg 6 Port SATA AHCI Controller
vmhba36 ahci              link-n/a  sata.vmhba36                            (0:0:31.2) Intel Corporation Patsburg 6 Port SATA AHCI Controller
注意：第二列显示针对 HBA 配置的驱动程序。

###要查看正在使用的驱动程序的版本，请运行以下命令
esxcli software vib list   查看所有驱动模块及版本信息
/usr/lib/vmware/vmkmod # esxcli software vib list | grep -i lpfc
lpfc                           10.0.100.1-1vmw.550.0.0.1331820       VMware  VMwareCertified   2014-05-02  
scsi-lpfc820                   8.2.3.1-129vmw.550.0.0.1331820        VMware  VMwareCertified   2014-05-02

####驱动更新命令esxcli software vib

/usr/lib/vmware/vmkmod # esxcli software 
Usage: esxcli software {cmd} [cmd options]

Available Namespaces:
  sources               Query depot contents for VIBs and image profiles
  acceptance            Retrieve and set the host acceptance level setting
  profile               Display, install, update or validates image profiles
  vib                   Install, update, remove, or display individual VIB packages
  
  /usr/lib/vmware/vmkmod # esxcli software vib
Usage: esxcli software vib {cmd} [cmd options]

Available Commands:
  get                   Displays detailed information about one or more installed VIBs
  install               Installs VIB packages from a URL or depot. VIBs may be installed, upgraded, or downgraded. WARNING: If your
                        installation requires a reboot, you need to disable HA first.
  list                  Lists the installed VIB packages
  remove                Removes VIB packages from the host. WARNING: If your installation requires a reboot, you need to disable HA first.
  update                Update installed VIBs to newer VIB packages. No new VIBs will be installed, only updates. WARNING: If your installation
                        requires a reboot, you need to disable HA first.

###查看驱动详细信息：  vmkload_mod -s mpt2sas
/usr/lib/vmware/vmkmod # vmkload_mod -s mpt2sas |grep Version
 Version: Version 14.00.00.00.3vmw, Build: 1623387, Interface: 9.2 Built on: Feb 21 2014
  
  #### vmkload_mod 驱动查看相关命令：
/usr/lib/vmware/vmkmod # vmkload_mod
Missing module name.
Usage: vmkload_mod <options> <module> <param_name=value ...>
Options:
   -h --help
   -l --list
   -m --mod-name <name>
   -s --showinfo
   -u --unload
   -v --verbose <level>
/usr/lib/vmware/vmkmod # 


###可以使用以下 命令检查 ESXi/ESX 主机版本：

# vmware -v


###要确定推荐用于网卡的驱动程序，必须使用 vmkchdev 命令获取供应商 ID (VID)、设备 ID (DID)、子供应商 ID (SVID) 和子设备 ID (SDID)：

# vmkchdev -l |grep vmhba1

000:16.0 1000:0030 15ad:1976 vmkernel vmhba1


###要使用一个命令获取系统中所有 HBA 的供应商信息，请使用以下命令：

# for a in $(esxcfg-scsidevs -a |awk '{print $1}') ;do vmkchdev -l |grep $a ;done

###获取网卡驱动程序和固件信息
//获取网络接口卡和名称列表
ESXi/ESX 4.x 中 用esxcfg-nics -l ； 在 ESXi 5.x 中用esxcli network nic list；
/usr/lib/vmware/vmkmod # esxcfg-nics -l  或 esxcli network nic list
Name    PCI           Driver      Link Speed     Duplex MAC Address       MTU    Description                   
vmnic0  0000:07:00.00 r8168       Up   100Mbps   Full   4c:09:b4:b0:bc:ac 1500   Realtek Realtek 8168 Gigabit Ethernet
vmnic1  0000:08:00.00 r8168       Up   100Mbps   Full   4c:09:b4:b0:bc:ad 1500   Realtek Realtek 8168 Gigabit Ethernet
vmnic2  0000:81:00.00 ixgbe       Down 0Mbps     Full   90:e2:ba:c0:c1:24 9000   Intel Corporation 82599EB 10-Gigabit SFI/SFP+ Network Connection
vmnic3  0000:81:00.01 ixgbe       Down 0Mbps     Half   90:e2:ba:c0:c1:25 1500   Intel Corporation 82599EB 10-Gigabit SFI/SFP+ Network Connection

//使用 ethtool -i 命令显示一个网络接口的可用信息
/usr/lib/vmware/vmkmod # ethtool  vmnic0
Settings for vmnic0:
	Supported ports: [ TP ]
	Supported link modes:   10baseT/Half 10baseT/Full 
	                        100baseT/Half 100baseT/Full 
	                        1000baseT/Full 
	Supports auto-negotiation: Yes
	Advertised link modes:  10baseT/Half 10baseT/Full 
	                        100baseT/Half 100baseT/Full 
	                        1000baseT/Full 
	Advertised auto-negotiation: Yes
	Speed: 100Mb/s
	Duplex: Full
	Port: Twisted Pair
	PHYAD: 0
	Transceiver: internal
	Auto-negotiation: on
	Supports Wake-on: pumbg
	Wake-on: g
	Current message level: 0x00000033 (51)
	Link detected: yes
/usr/lib/vmware/vmkmod # ethtool  -i vmnic0
driver: r8168
version: 8.013.00-NAPI
firmware-version: 
bus-info: 0000:07:00.0


###要通过 ethtool -i 同时获取所有网络适配器的信息，可运行以下命令：

for a in $(esxcfg-nics -l|awk '{print $1}'|grep [0-9]) ;do ethtool -i $a;done

在 ESXi 5.x 中，还可以使用以下命令:
esxcli network nic get -n vmnic#
/usr/lib/vmware/vmkmod # esxcli network nic get -n vmnic0
   Advertised Auto Negotiation: true
   Advertised Link Modes: 10baseT/Half, 10baseT/Full, 100baseT/Half, 100baseT/Full, 1000baseT/Full
   Auto Negotiation: true
   Cable Type: Twisted Pair
   Current Message Level: 51
   Driver Info: 
         Bus Info: 0000:07:00.0
         Driver: r8168
         Firmware Version: 
         Version: 8.013.00-NAPI
   Link Detected: true
   Link Status: Up 
   Name: vmnic0
   PHYAddress: 0
   Pause Autonegotiate: false
   Pause RX: false
   Pause TX: false
   Supported Ports: TP
   Supports Auto Negotiation: true
   Supports Pause: false
   Supports Wakeon: true
   Transceiver: internal
   Wakeon: MagicPacket(tm)
   
   
   ####

    要确定推荐用于网卡的驱动程序，必须使用 vmkchdev 命令获取供应商 ID (VID)、设备 ID (DID)、子供应商 ID (SVID) 和子设备 ID (SDID)

    # vmkchdev -l |grep vmnic0

    002:01.0 8086:100f 15ad:0750 vmkernel vmnic0

    在本例中，值分别为：


    要使用一个命令获取系统中所有网卡的供应商信息，请使用：

    # for a in $(esxcfg-nics -l |awk '{print $1}' |grep [0-9]) ;do vmkchdev -l |grep $a ;done
     

    VID = 8086

    DID = 100f

    SVID = 15ad

    SDID = 0750

现在可以在 VMware Compatibility Guide 中搜索供应商 ID (VID)、设备 ID (DID)、子供应商 ID (SVID) 和子设备 ID (SDID)。在某些情况下，
可能需要执行文本搜索，以将范围缩小到特殊卡。注意：可以使用以下 命令检查 ESXi/ESX 主机版本：# vmware -v通过 ESXi/ESX 版本和网络类型，
可以了解要使用的驱动程序的版本。VMware downloads page 提供了所有驱动程序更新


####Additional Information

这些脚本信息仅适用于 ESXi 5.x。
要在 esxi5.x 中使用一个命令获取系统中所有 HBA 的驱动程序版本，请使用：	
esxcli storage core adapter list|awk '{print $1}'|
grep [0-9]|while read a;do vmkload_mod -s $a|grep -i version;done
要在 esxi5.x 中使用一个命令获取系统中所有 HBA 的供应商信息，请使用：
esxcli storage core adapter list|awk '{print $1}'
|grep [0-9]|while read a;do vmkchdev -l |grep $a ;done
要在 esxi5.x 中通过 ethtool -i 一次获取所有网络适配器的信息，可运行以下命令：
esxcli network nic list | awk '{print $1}'|grep [0-9]|while read a;do ethtool -i $a;done
要在 esxi5.x 中使用一个命令获取系统中所有网卡的供应商信息，请使用：
esxcli network nic list | awk '{print $1}'|grep [0-9]|while read a;do vmkchdev -l|grep $a;done

####vm-support tool：  （重点关注：nicinfo.sh    swfw.sh）
/usr/lib/vmware/vm-support/bin # ls
altlocaltgz.sh               dump-vmdk-rdm-info.sh        hostd.sh                     partedUtil.sh                vFlash.sh
cat-newest-vmkernel-core.sh  dump-vmfs-traces.sh          localtgz.sh                  smartinfo.sh
debug-hung-vm                dump-vxlan-stats-info.sh     nicinfo.sh                   swfw.sh


####驱动升级：
/usr/lib/vmware # esxcli software vib list | grep aacraid
scsi-aacraid                   1.1.5.1-9vmw.550.0.0.1331820          VMware  VMwareCertified   2014-05-02  

升级步骤：将.vib的文件上传到/var/log/vmware 目录下，记住必须是这个目录才可以，如果放在其他的目录，升级时会报错：

/var/log/vmware # esxcli software vib install -v vmware-esxi-drivers-scsi-aacraid-550.5.2.1.41024.-1.5.5.1331820.x86_64.vib -f --maintenance-mode
Installation Result
   Message: The update completed successfully, but the system needs to be rebooted for the changes to be effective.
   Reboot Required: true
   VIBs Installed: Adaptec_Inc_bootbank_scsi-aacraid_5.5.5.2.1.41024-1OEM.550.0.0.1331820
   VIBs Removed: VMware_bootbank_scsi-aacraid_1.1.5.1-9vmw.550.0.0.1331820
   VIBs Skipped: 
   //提示需要重启 才可以生效,重启后验证生效
   ~ # esxcli software vib list | grep aacraid
scsi-aacraid                   5.5.5.2.1.41024-1OEM.550.0.0.1331820  Adaptec_Inc  VMwareCertified   2014-09-27

###################################################################################
yum install net-snmp net-snmp-utils -y

vi /etc/snmp/snmpd.conf 
tcp: mib-2 6

view    systemview    included   .1.3.6.1.2.1.1
view    systemview    included   .1.3.6.1.2.1.25.1.1

snmpwalk -v 2c -c public localhost

[root@localhost mibs]# hostname
zhl.com
[root@localhost mibs]# snmpwalk -v 2c -c public localhost system.sysName.0
SNMPv2-MIB::sysName.0 = STRING: zhl.com





[root@localhost home]# snmptranslate -T
snmptranslate: option requires an argument -- 'T'
invalid option: -?
USAGE: snmptranslate [OPTIONS] OID [OID]...


 -T TRANSOPTS		Set various options controlling report produced:
			  B:  print all matching objects for a regex search
			  d:  print full details of the given OID
			  p:  print tree format symbol table
			  a:  print ASCII format symbol table
			  l:  enable labeled OID report
			  o:  enable OID report
			  s:  enable dotted symbolic report
			  z:  enable MIB child OID report
			  t:  enable alternate format symbolic suffix report

@@
snmptranslate -Tp
snmptranslate -Ta
snmptranslate -To


###########################################################################################
#####################################
硬盘smart信息确认：
 启动SMART
# smartctl --smart=on --offlineauto=on --saveauto=on /dev/sda
smartctl -a /dev/sda
SMART Health Status: OK   #版本的不通这里显示的也不一样。
Elements in grown defect list: 0  #才是出坏道，俗称成长坏道。
 Non-medium errorcount:       51  #非介质错误。意思是说不是盘的问题，一般是电缆、传输、校验问题，可以忽略的。

可以用命令直接查看硬盘的好坏:
 smartctl -H /dev/sda

Badblocks工具测试正常，无坏道信息：
 badblocks命令可以检查磁盘装置中损坏的区块。执行该指令时须指定所要检查的磁盘装置，及此装置的磁盘区块数。
badblocks -s//显示进度  -v//显示执行详细情况   /dev/sda1
badblocks -s//显示进度 -w//以写去检测 -v//显示执行详细情况 /dev/sda2
注意，不能以写的方式检测已经挂载的硬盘

badblocks -s -v /dev/sda
但是，如果您检测过程中在某一个区块停滞不前，而后报告中提示有坏块，那么杯具了……您的磁盘有坏道了。
不论是什么类型的坏道，均建议您首先进行数据备份！把重要数据进行备份然后再尝试修复。如果您有重要数据却无法读取（磁盘出现异常），那么请立即停止使用此磁盘并找专业人员进行修复。


 使用hdparm测试   测试硬盘读写速度
# hdparm -Tt /dev/sda
 语法：

hdparm [-CfghiIqtTvyYZ][-a <快取分区>][-A <0或1>][-c <I/O模式>][-d <0或1>][-k <0或1>][-K <0或1>][-m <分区数>][-n <0或1>][-p <PIO模式>][-P <分区数>][-r <0或1>][-S <时间>][-u <0或1>][-W <0或1>][-X <传输模式>] [设备]

-a<快取分区> 设定读取文件时，预先存入块区的分区数，若不加上<快取分区>选项，则显示目前的设定。 -A<0或1> 启动或关闭读取文件时的快取功能。-c<I/O模式> 设定IDE32位I/O模式。 -C 检测IDE硬盘的电源管理模式。-d<0或1> 设定磁盘的DMA模式。-f 将内存缓冲区的数据写入硬盘，并清楚缓冲区。 -g 显示硬盘的磁轨，磁头，磁区等参数。-h 显示帮助。-i 显示硬盘的硬件规格信息，这些信息是在开机时由硬盘本身所提供。 -I 直接读取硬盘所提供的硬件规格信息。-k<0或1> 重设硬盘时，保留-dmu参数的设定。 -K<0或1> 重设硬盘时，保留-APSWXZ参数的设定。-m<磁区数> 设定硬盘多重分区存取的分区数。 -n<0或1> 忽略硬盘写入时所发生的错误。-p<PIO模式> 设定硬盘的PIO模式。 -P<磁区数> 设定硬盘内部快取的分区数。-q 在执行后续的参数时，不在屏幕上显示任何信息。 -r<0或1> 设定硬盘的读写模式。-S<时间> 设定硬盘进入省电模式前的等待时间。-t 评估硬盘的读取效率。 -T 平谷硬盘快取的读取效率。-u<0或1> 在硬盘存取时，允许其他中断要求同时执行。-v 显示硬盘的相关设定。 -W<0或1> 设定硬盘的写入快取。-X<传输模式>  设定硬盘的传输模式。-y 使IDE硬盘进入省电模式。 -Y 使IDE硬盘进入睡眠模式。-Z 关闭某些Seagate硬盘的自动省电功能。


可以使用sg_vpd命令查看硬盘转速，sg_vpd命令是sg3_utils其中一个工具.
sg_vpd /dev/sda

 关于smart检测硬盘命令补充:

smartctl -a <device> 检查该设备是否已经打开SMART技术。 smartctl -s on <device> 如果没有打开SMART技术，使用该命令打开SMART技术。 smartctl -t short <device> 后台检测硬盘，消耗时间短； smartctl -t long <device> 后台检测硬盘，消耗时间长； smartctl -C -t short <device> 前台检测硬盘，消耗时间短； smartctl -C -t long <device> 前台检测硬盘，消耗时间长。其实就是利用硬盘SMART的自检程序。 smartctl -X <device> 中断后台检测硬盘。 smartctl -l selftest <device> 显示硬盘检测日志。 smartctl -l error <device> 显示硬盘错误汇总。

首先通过dmesg工具，确认一下硬盘的设备符号。如果显示为sdb，则代表SATA和SCSI
smartctl -i /dev/sda 确认硬盘是否打开了SMART支持

 SMART support is: Enabled                          //表示启用了smart支持

如果看到SMART support is: Disabled表示SMART未启用，执行如下命令，启动SMART

# smartctl --smart=on --offlineauto=on --saveauto=on /dev/sda

 smartctl 5.40 2010-10-16 r3189 [i386-redhat-linux-gnu] (local build)

Copyright (C) 2002-10 by Bruce Allen, http://smartmontools.sourceforge.net

=== START OF ENABLE/DISABLE COMMANDS SECTION ===

SMART Enabled.

SMART Attribute Autosave Enabled.

SMART Automatic Offline Testing Enabled every four hours.

现在硬盘的SMART功能已经被打开，执行如下命令查看硬盘的健康状况

smartctl -H /dev/sda
 smartctl 5.40 2010-10-16 r3189 [i386-redhat-linux-gnu] (local build)

Copyright (C) 2002-10 by Bruce Allen, http://smartmontools.sourceforge.net

=== START OF READ SMART DATA SECTION ===

SMART overall-health self-assessment test result: PASSED

请注意result后边的结果：PASSED，这表示硬盘健康状态良好；如果这里显示Failure，那么最好立刻给服务器更换硬盘。SMART只能报告磁盘已经不再健康，但是报警后还能继续运行多久是不确定的。通常，SMART报警参数是有预留的，磁盘报警后，不会当场坏掉，一般能坚持一段时间，有的硬盘SMART报警后还继续跑了好几年，有的硬盘SMART报错后几天就坏了。但是一旦出现报警，侥幸心里是万万不能的……

 #smartctl -A   /dev/sda  查看硬盘的详细信息

#smartctl -s on  /dev/sda  如果没有打开SMART技术，使用该命令打开SMART技术。

#smartctl -t short  /dev/sda  后台检测硬盘，消耗时间短；

#smartctl -t long  /dev/sda   后台检测硬盘，消耗时间长；

#smartctl -C -t  /dev/sda   short前台检测硬盘，消耗时间短；

#smartctl -C -t  /dev/sda   long前台检测硬盘，消耗时间长。其实就是利用硬盘SMART的自检程序。

#smartctl -X   /dev/sda      中断后台检测硬盘。

#smartctl -l selftest  /dev/sda  显示硬盘检测日志。

#smartctl -l error   /dev/sda    显示硬盘错误汇总。


 如果需要定期登录到服务器上运行smartctl比较麻烦时，linux还提供了系统进程smartd，编辑配置文件：1    vi  /etc/smartd.conf

这个配置文件中大部分可能是注释掉的说明，只需要写入和当前硬盘相关的配置即可：

/dev/sda -H  -m  test@test123123.com  //监控磁盘的健康状态,当SMART中报告PASSED的时候不理睬。一旦出现Failure，立刻用邮件通知用户指定的邮箱

 /dev/sda -a -m  admin@example.com,root@localhost  //监控磁盘的所有属性,当SMART中报告PASSED的时候不理睬。一旦出现Failure，立刻用邮件通知用户指定的邮箱 

 /dev/twa0 -d 3ware,0 -a -s L/../../7/00 //监控3ware 9000控制器上的第一个ATA磁盘的所有属性,在每个礼拜天的00:00--01:00进行长格式的自我检测

 /dev/sg2 -d areca,1 -a  -s L/../(01|15)/./22 //监控Areca Raid控制器上的第一个SATA磁盘的所有属性,在每个礼拜月的第1天和第15天的22:00--23:00进行长格式的自我检测

 -s (O/../.././(00|06|12|18)|S/../.././01|L/../../6/03) //在每天的00:00,06:00,12:00,18:00进行离线的自检，并在每天的01:00-02:00进行短格式的自检，并在每个礼拜6的03:00-04:00进行长格式的自检 

配置好smartd.conf后需执行

/etc/init.d/smartd restart 即可生效

其他和smartd.conf相关的配置可参见:


硬盘错误举例：
1. UncorrectedReadErr--对应为硬盘错误；此时用dd读写会发生error;

[root@localhost bin]# diskman -s /dev/sdc
Permanent defect  (p-list): 859
Grown defect list (g-list): 0

Smart Status(ASC/ASCQ)    : 0x0/0x0 

UncorrectedWriteErr       : 0
UncorrectedReadErr        : 0
UncorrectedvVerifyErr     : 0
NonMediumErr              : 4

[root@localhost bin]# diskman -s /dev/sdd    发生问题的盘
Permanent defect  (p-list): 572
Grown defect list (g-list): 0

Smart Status(ASC/ASCQ)    : 0x0/0x0 

UncorrectedWriteErr       : 0
UncorrectedReadErr        : 6
UncorrectedvVerifyErr     : 0
NonMediumErr              : 2

2.smartctl 信息中的成长坏道
Elements in grown defect list: 0  #才是出坏道，俗称成长坏道。
而：Non-medium errorcount:       51  #非介质错误。意思是说不是盘的问题，一般是电缆、传输、校验问题，可以忽略的。


 使用smartctl查dell服务器坏道实录 


一、执行命令：

# smartctl -a /dev/sda

smartctl version 5.38[x86_64-redhat-linux-gnu] Copyright (C) 2002-8 Bruce Allen

Home page ishttp://smartmontools.sourceforge.net/

 

Device: SEAGATE  ST3300657SS      Version: ES64

Serial number: 6SJ175BR

Device type: disk

Transport protocol: SAS

Local Time is: Tue Feb 21 15:23:46 2012 CST

Device supports SMART and is Enabled

Temperature Warning Disabled or NotSupported

SMART Health Status: OK

 

Current Drive Temperature:     40 C

Drive Trip Temperature:        68 C

Elements in grown defect list: 16

Vendor (Seagate) cache information

 Blocks sent to initiator = 1990352432

 Blocks received from initiator = 2738959193

 Blocks read from cache and sent to initiator = 35795691

 Number of read and write commands whose size <= segment size =423851654

 Number of read and write commands whose size > segment size = 0

Vendor (Seagate/Hitachi) factoryinformation

 number of hours powered up = 7208.00

 number of minutes until next internal SMART test = 58

 

Error counter log:

          Errors Corrected by          Total   Correction     Gigabytes    Total

               ECC          rereads/    errors  algorithm      processed    uncorrected

          fast | delayed   rewrites  corrected invocations   [10^9 bytes]  errors

read:  1029069625       28         0 1029069653   1029069653       1016.060           0

write:         0        0         0         0          0       8091.799           0

verify:  126342        0         0   126342     126342          3.000           0

 

Non-medium error count:       13

 

SMART Self-test log

Num Test              Status                 segment  LifeTime LBA_first_err [SK ASC ASQ]

    Description                             number   (hours)

# 1 Background long   Failed insegment -->      24    7196        435567298 [0x30x11 0x0]

# 2 Background short  Completed                  16    7194                 - [-   -   -]

# 3 Background short  Completed                  16    7170                 - [-   -   -]

# 4 Background short  Completed                  16    7146                 - [-   -   -]

# 5 Background short  Completed                  16    7122                 - [-   -   -]

# 6 Background long   Completed                  16    7100                 - [-   -   -]

# 7 Background short  Completed                  16    7098                 - [-   -   -]

# 8 Background short  Completed                  16    7074                 - [-   -   -]

# 9 Background short  Completed                  16    7050                 - [-  -    -]

#10 Background long   Completed                  16    7028                 - [-   -   -]

#11 Background short  Completed                  16    7026                 - [-   -   -]

#12 Background short  Completed                  16    7002                 - [-   -   -]

#13 Background short  Completed                  16    6978                 - [-   -   -]

#14 Background short  Completed                  16    6954                 - [-   -   -]

#15 Background long   Completed                  16    6932                 - [-   -   -]

#16 Background short  Completed                  16    6930                 - [-   -   -]

#17 Background short  Completed                  16    6906                 - [-   -   -]

#18  Backgroundshort  Completed                  16    6882                 - [-   -   -]

#19 Background long   Completed                  16    6860                 - [-   -   -]

#20 Background short  Completed                  16    6858                 - [-   -   -]

 

Long (extended) Self Test duration: 3200seconds [53.3 minutes]

 

二、查看硬盘分区

#fdisk –lu

Disk/dev/sda: 300.0 GB, 300000000000 bytes

255heads, 63 sectors/track, 36472 cylinders, total 585937500 sectors

Units = sectors of 1 * 512 = 512 bytes

 

   Device Boot      Start         End      Blocks  Id  System

/dev/sda1   *         63      208844      104391  83  Linux

/dev/sda2         208845   585922679   292856917+ 8e  Linux LVM

三、确认坏区位置

# echo 'scale=5;(435567298 - 208845) * 512/4096'|bc    *512是1个Units512字节，/4096是每个块设备是4096字节

54419806.62500 处于第五个扇区，8个扇区1个块，0.125*5=0.625

说明在54419806这个块的第5个扇区有问题，接下来查看下出问题的地方是否有文件使用了

 

四、查看是否有文件在使用坏区

# debugfs

debugfs 1.39 (29-May-2006)

debugfs: open /dev/mapper/VolGroup00-LogVol02 #打开/dev/mapper/VolGroup00-LogVol02

debugfs:  icheck 54419806                  # Print a listing of the inodes which use the one or more blocks specified on the command line

Block  Inode number

54419806        50659332

debugfs:  ncheck 50659332               # Take the requested list of inode numbers, and print alisting of pathnames to those inodes.

Inode  Pathname

50659332        /database/jhl_2918_x5/mysql/ibdata1  #找到了有文件处于坏区位置

debugfs:  


#############################raid成员盘信息获取说明：
SAS3008/PMC7805 :使用sg设备；
LSI9361 :使用megacli的下面的方法进行；

对于raid成员盘，使用smartctl 工具查询物理盘smart信息的方法：
然后使用MegaCLI64 来查询你的物理磁盘的ID号。
Virtual Drive: 0 代表你的第一个RAID VD， PD 0 代表这个VD里面的第一块物理磁盘。
./MegaCli64 -LdPdInfo -aALL   查询到 “Device Id: 0”

再执行 smartctl -a -d megaraid,N /dev/sd*
N 用Device ID 号替换  X用你RAID盘在系统中识别的编号替换。

smartctl -a -d megaraid,0 /dev/sda    就可以查询到成员盘的smart信息了。


配置实例：
[root@localhost megacli(9271 and 9361)]# MegaCli64 -LdPdInfo -aALL | grep "Device Id"
Device Id: 9
Device Id: 15
Device Id: 10
Device Id: 11
Device Id: 16

[root@localhost megacli(9271 and 9361)]# smartctl -a -d megaraid,11 /dev/sdc
smartctl 5.43 2012-06-30 r3573 [x86_64-linux-2.6.32-431.el6.x86_64] (local build)
Copyright (C) 2002-12 by Bruce Allen, http://smartmontools.sourceforge.net

/dev/sdc [megaraid_disk_11] [SAT]: Device open changed type from 'megaraid' to 'sat'
Smartctl open device: /dev/sdc [megaraid_disk_11] [SAT] failed: SATA device detected,
MegaRAID SAT layer is reportedly buggy, use '-d sat+megaraid,N' to try anyhow
[root@localhost megacli(9271 and 9361)]# smartctl -a -d sat+megaraid,11 /dev/sdc



LBA写入

lba是逻辑地址，pba是物理地址。

硬盘上的空间分为一个一个的扇区，每扇区512字节，把空间以扇区为单位，从0编到结尾，就可以根据地址进行访问，lba值就对应了扇区位置。

在victoria里，可以在扫描的开始和结束两个窗口填写lba值，填入你想扫描的空间开始和结束即可，一般缺省值就是硬盘的0扇和结尾扇区。

LBA是Logincal Block Addeessing 简写,是硬盘容量或地址的一个参数。

LBA 

LBA(Logical Block Address),中文名称：逻辑区块地址。是描述电脑存储设备上数据所在区块的通用机制，一般用在像硬盘这样的辅助记忆设备。
LBA可以意指某个数据区块的地址或是某个地址所指向的数据区块。电脑上所谓一个逻辑区块通常是512或1024位组。ISO-9660格式的标准CD则以2048位组为一个逻辑区块大小。



fdisk -l显示信息详解

[root@www.linuxidc.com ~]# fdisk -l
Disk /dev/sda: 10.7 GB, 10737418240 bytes
255 heads, 63 sectors/track, 1305 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00044938
  Device Boot      Start        End      Blocks  Id  System
/dev/sda1  *          1        638    5120000  83  Linux
Partition 1 does not end on cylinder boundary.
/dev/sda2            638        893    2048000  83  Linux
Partition 2 does not end on cylinder boundary.
/dev/sda3            893        1020    1024000  82  Linux swap / Solaris
Partition 3 does not end on cylinder boundary.
/dev/sda4            1020        1306    2292736    5  Extended
/dev/sda5            1021        1306    2291712  83  Linux

解析：
Disk /dev/sda: 10.7 GB, 10737418240 bytes
块设备名称为/dev/sda，此设备的大小为10.7GB，这个数字不是特别精确，我系统是10GB；10737418240 bytes这是转换成字节后的大小，即：10737418240/1024/1024/1024=10GB (注：bytes=B，表示“字节”，bit=b，表示“位”)
255 heads, 63 sectors/track, 1305 cylinders
255 heads：表示磁头数为255
63 sectors/track：表示每磁道上有63个扇区
1305 cylinders：表示共有1305个柱面，柱面是分区的最小单位
Units = cylinders of 16065 * 512 = 8225280 bytes

16065=255*63 因为每一个磁头都是在同一个柱面的，63表示每个磁道上的扇区数量，这两个数的乘积表示一个柱面上的扇区数量；所以16065*512表示一个柱面的大小是8225280字节
Sector size (logical/physical): 512 bytes / 512 bytes
表示一个扇区的大小是512字节

总结：所以一个磁盘的大小=一个柱面大小*柱面的总数=磁头数量*每个磁道上的扇区数*一个扇区大小*柱面总数

即：磁盘大小=8225280*1305=10733990400bytes=9.99GB=255*63*512*1305
上例中显示出我们的磁盘只有1305个柱面，但下边的分区信息中出现了1306个柱面数，不必太在意，linux显示的这些数据不会十分精确。



###################lsi9271,lsi9361 check with megacli
 MegaCli常用参数介绍 

MegaCli -adpCount 【显示适配器个数】

MegaCli -AdpGetTime –aALL 【显示适配器时间】

MegaCli -AdpAllInfo -aAll     【显示所有适配器信息】

MegaCli -LDInfo -LALL -aAll    【显示所有逻辑磁盘组信息】

MegaCli -PDList -aAll    【显示所有的物理信息】

MegaCli -AdpBbuCmd -GetBbuStatus -aALL |grep ‘Charger Status’ 【查看充电状态】

MegaCli -AdpBbuCmd -GetBbuStatus -aALL【显示BBU状态信息】

MegaCli -AdpBbuCmd -GetBbuCapacityInfo -aALL【显示BBU容量信息】

MegaCli -AdpBbuCmd -GetBbuDesignInfo -aALL    【显示BBU设计参数】

MegaCli -AdpBbuCmd -GetBbuProperties -aALL    【显示当前BBU属性】

MegaCli -cfgdsply -aALL    【显示Raid卡型号，Raid设置，Disk相关信息】

磁带状态的变化，从拔盘，到插盘的过程中。 

Device         |Normal|Damage|Rebuild|Normal

Virtual Drive     |Optimal|Degraded|Degraded|Optimal

Physical Drive     |Online|Failed –> Unconfigured|Rebuild|Online

看几个示例：

MegaCli -PDList -aALL

这是用来看物理硬盘的信息的

MegaCli -LDPDInfo -aall

这是用来看逻辑设备(我把LD称之为Logical Device)和物理硬盘之间的关系的

MegaCli -CfgLdAdd -r(0|1|5) [E:S, E:S, ...] -aN

这是用来建立新的raid 0,1,5的虚拟设备的命令

MegaCli -LDBI -ProgDsply -LALL -aALL

这是用来看raid的building进度的
一般在linux下用MegaCli来维护dell机器的raid。也可以在windows下用：
%SystemRoot%\system32\GAMSERV\megacli -adpeventlog -getevents -f d:\%computername%_nvram.log -aall  （要装Mylex Global Array Manager软件）

############################LBA详解
LBA(Logical Block Addressing)逻辑块寻址。在 LBA 模式下，我们知道硬盘上的一个数据区域由它所在的磁头、柱面（也就是磁道）和扇区所唯一确定。
早期系统就是直接使用磁头柱面和扇区来对硬盘进行寻址（这称为CHS寻址），这需要分别存储每个区域的三个参数（这称为3D参数），
使用时再分别读取三个参数，然后再送到磁盘控制器去执行。由于系统用8b来存储磁头地址，用10b来存储柱面地址，用6b来存储扇区地址，
而一个扇区共有512B，这样使用CHS寻址一块硬盘最大容量为256 * 1024 * 63 * 512B = 8064 MB(1MB = 1048576B)（若按1MB=1000000B来算就是8.4GB）。
随着硬盘技术的进步，硬盘容量越来越大，CHS模式无法管理超过8064 MB的硬盘，因此工程师们发明了更加简便的LBA寻址方式。在LBA地址中，
地址不再表示实际硬盘的实际物理地址（柱面、磁头和扇区）。LBA编址方式将CHS这种三维寻址方式转变为一维的线性寻址，
它把硬盘所有的物理扇区的C/H/S编号通过一定的规则转变为一线性的编号，系统效率得到大大提高，避免了烦琐的磁头/柱面/扇区的寻址方式。
在访问硬盘时，由硬盘控制器再将这种逻辑地址转换为实际硬盘的物理地址。
在这三种硬盘模式中，现在 LBA 模式使用最多。 　　
LBA与C/H/S 之间的转换: 　　
设NS为每磁道扇区数，NH为磁头数，C、H、S分别表示磁盘的柱面、磁头和扇区编号，LBA表示逻辑扇区号，div为整除计算，mod为求余计算，则： 　　
LBA=NH×NS×C+NS×H+S-1； 　　
C=(LBA div NS)div NH； 　　
H=(LBA div NS)mod NH； 　　
S=(LBA mod NS)+1 　　
例如 LBA = 0 则 CHS = 0/0/1 　　
从C/H/S到LBA的计算公式： 　　LBA=（C-CS）*PH*PS+（H-HS）*PS+(S-SS) 

IDE SATA SCSI SAS 这些是指硬盘的接口物理形式，
AHCI PATA ISCSI 这些是硬盘的接口的规范，可以以不同的物理形式出现。
　　SATA接口： Serial ATA（SATA, Serial Advanced Technology Attachment），亦称串行ATA，是串行SCSI（SAS：Serial Attached SCSI）的孪生兄弟，
两者的排线兼容，SATA硬盘可接上SAS接口。它是一种电脑总线，主要功能是用作主板和大量存储设备（如硬盘及光盘驱动器）之间的数据传输之用。
串行接口还具有结构简单、支持热插拔的优点。 


################################scsi设备确认：
系统下识别到的scsi_Host:  /sys/class/scsi_host
lrwxrwxrwx. 1 root root 0 May 18 17:16 host0 -> ../../devices/pci0000:00/0000:00:01.0/0000:01:00.0/host0/scsi_host/host0   (emulex1_1)
lrwxrwxrwx. 1 root root 0 May 18 17:16 host1 -> ../../devices/pci0000:00/0000:00:01.0/0000:01:00.1/host1/scsi_host/host1    (emulex1_2)
lrwxrwxrwx. 1 root root 0 May 18 17:16 host10 -> ../../devices/pci0000:80/0000:80:02.2/0000:85:00.0/host10/scsi_host/host10   (LSI9361)
lrwxrwxrwx. 1 root root 0 May 18 17:16 host2 -> ../../devices/pci0000:00/0000:00:03.0/0000:06:00.0/host2/scsi_host/host2     (emulex2_1)
lrwxrwxrwx. 1 root root 0 May 18 17:16 host3 -> ../../devices/pci0000:00/0000:00:03.0/0000:06:00.1/host3/scsi_host/host3      (emulex2_2)
lrwxrwxrwx. 1 root root 0 May 18 17:16 host4 -> ../../devices/pci0000:00/0000:00:02.0/0000:02:00.0/host4/scsi_host/host4    (SAS3008)
lrwxrwxrwx. 1 root root 0 May 18 17:16 host5 -> ../../devices/pci0000:00/0000:00:03.2/0000:07:00.0/host5/scsi_host/host5    (PMC7805)
lrwxrwxrwx. 1 root root 0 May 18 17:16 host6 -> ../../devices/pci0000:00/0000:00:1f.2/host6/scsi_host/host6    (Intel Corporation Wellsburg 6-Port SATA Controller [AHCI mode])
lrwxrwxrwx. 1 root root 0 May 18 17:16 host7 -> ../../devices/pci0000:00/0000:00:1f.2/host7/scsi_host/host7   (Intel Corporation Wellsburg 6-Port SATA Controller [AHCI mode])
lrwxrwxrwx. 1 root root 0 May 18 17:16 host8 -> ../../devices/pci0000:00/0000:00:1f.2/host8/scsi_host/host8  (Intel Corporation Wellsburg 6-Port SATA Controller [AHCI mode])
lrwxrwxrwx. 1 root root 0 May 18 17:16 host9 -> ../../devices/pci0000:00/0000:00:1f.2/host9/scsi_host/host9   (Intel Corporation Wellsburg 6-Port SATA Controller [AHCI mode])


[root@localhost scsi_host]# lspci | grep "00:1f.2"
00:1f.2 SATA controller: Intel Corporation Wellsburg 6-Port SATA Controller [AHCI mode] (rev 05)
[root@localhost scsi_host]# lspci | grep -i sas
02:00.0 Serial Attached SCSI controller: LSI Logic / Symbios Logic SAS3008 PCI-Express Fusion-MPT SAS-3 (rev 02)
07:00.0 RAID bus controller: Adaptec Series 7 6G SAS/PCIe 3 (rev 01)
85:00.0 RAID bus controller: LSI Logic / Symbios Logic MegaRAID SAS-3 3108 [Invader] (rev 02)
[root@localhost scsi_host]# lspci | grep -i emulex
01:00.0 Fibre Channel: Emulex Corporation Saturn-X: LightPulse Fibre Channel Host Adapter (rev 03)
01:00.1 Fibre Channel: Emulex Corporation Saturn-X: LightPulse Fibre Channel Host Adapter (rev 03)
06:00.0 Fibre Channel: Emulex Corporation Saturn-X: LightPulse Fibre Channel Host Adapter (rev 03)
06:00.1 Fibre Channel: Emulex Corporation Saturn-X: LightPulse Fibre Channel Host Adapter (rev 03)


#############################intel pcie ssd
[root@localhost zhl]# isdct show -a -intelssd | grep -i index
Index: 0

isdct dump -destination aa.csv -o json -intelssd 0 DataType=identify

isdct dump -intelssd 0 datatype=nvmelog logid=197

logid:
specifies which nvme log to parse. this is only required if datatype=nvmelog. valid values are:
1:error log information
2:smart/health information
3:firmware slot information
197: temperature statistics
202:smart attributes


###################################fc配置说明：
ramdisk相关的配置：
telnet manage_ip port 23  zte/zte
su
tcs_debug.sh 128  4321 100  开启100G的ramdisk
可以要连续执行两次，提示 "TCs loop test is already started" 表示功能已经开启
执行后，可能用fdisk -l查看设备的大小还是之前映射的磁阵上物理盘的大小，但用smartctl工具查看已经修改过了：
[root@localhost host3]# smartctl -a /dev/sdg
smartctl 5.43 2012-06-30 r3573 [x86_64-linux-2.6.32-431.el6.x86_64] (local build)
Copyright (C) 2002-12 by Bruce Allen, http://smartmontools.sourceforge.net
before:
Vendor:               ZTE     
Product:              ZXUSP           
Revision:             V1.0
User Capacity:        299,452,334,080 bytes [299 GB]
Logical block size:   512 bytes
Logical Unit id:      0x028d0a77857495f00x50028d0a77857495
Serial number:        28d0a77857495f02
Device type:          disk
Transport protocol:   iSCSI
Local Time is:        Thu May 19 11:27:01 2016 HKT
Device supports SMART and is Enabled
Temperature Warning Enabled
SMART Health Status: OK

Error Counter logging not supported
Device does not support Self Test logging

after:
[root@localhost host3]# smartctl -a /dev/sdg
smartctl 5.43 2012-06-30 r3573 [x86_64-linux-2.6.32-431.el6.x86_64] (local build)
Copyright (C) 2002-12 by Bruce Allen, http://smartmontools.sourceforge.net

Vendor:               ZTE USP 
Product:              SPR11 Ramdisk   
Revision:             1.00
User Capacity:        107,374,182,400 bytes [107 GB]
Logical block size:   512 bytes
Serial number:        ZTE USP SPR11 Ramdisk
Device type:          disk
Local Time is:        Thu May 19 11:39:08 2016 HKT
Device does not support SMART

Error Counter logging not supported
Device does not support Self Test logging

关闭ramdisk命令： tcs_debug.sh  128 0 
有时要连续执行两次，提示 “TCS loop test is already stopped”

备注： 无论是使用映射的物理盘还是ram disk,配置完成后，都需要插拔光纤就可以识别了；

###########################################################################################
nfs服务配置：
yum install nfs* -y

[root@localhost ~]# cat /etc/exports 
/home/vpshare *(insecure,rw,async,no_root_squash)

service nfs start

############################################################
@@@@linux环境变量配置相关：
vi /etc/profile
在最后加入如下一行：
export PATH=$PATH:/usr/sbin/ocmanager/
执行  . /etc/profile 或source /etc/profile 立即生效，

##########################################################


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@所有服务器直接无秘钥访问配置方法：
打通SSH，设置ssh无密码登陆（所有节点之间可以无秘钥自由访问）：

1）在主节点（或任一个节点）上执行 ssh-keygen -t rsa 一路回车，生成无密码的密钥对；

2）将公钥添加到认证文件中： cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys ，并设置authorized_keys的访问权限： chmod 600 ~/.ssh/authorized_keys ；

3）scp  上面的认证文件到所有节点：

scp ~/.ssh/authorized_keys root@*.*.*.*:~/.ssh/

==>这样所有节点之间就可以相互访问了；

####################################################################

@@@@@@@@@@@@@@@@@@@@@@@@YUM源配置命令：
cd /etc/yum.repos.d/
rm -rf *
cat >> /etc/yum.repos.d/iso.repo << EOF
[server]
name=server
baseurl=file:///mnt
enabled=1
gpcheck=0
EOF

验证yum:
yum clean all  #清理旧库信息
yum update   #yum资源库更新 
yum list  #测试新库，如果列出软件包则正常

@@@@@@@@@@@@配置CPU超频

在系统中配置cpu超频或者在BIOS中配置超频
cat >> /etc/rc.local << EOF
modprobe acpi_cpufreq 
awk  '/^processor/ {system("echo performance > /sys/devices/system/cpu/cpu" $3 "/cpufreq/scaling_governor")}' /proc/cpuinfo 
EOF


配置实例：
 cat /etc/rc.local 
modprobe acpi_cpufreq 
awk  '/^processor/ {system("echo performance > /sys/devices/system/cpu/cpu"$3"/cpufreq/scaling_governor")}' /proc/cpuinfo 

执行source /etc/rc.local后：
查询 cat /proc/cpuinfo | grep "cpu MHz"
全是cpu MHz		: 2401.000 了，已经配置为超频模式了；

备注说明：

官网查询到的信息，
E5-2630 v3
处理器基本工作频率：2.4Ghz,
最大睿频频率：3.2Ghz,

在PTU 软件中查询到的信息：
 Max Turbo 01C:32x, 02C:32x, 03C:30x, 04C:29x, 05C:28x, 06C:27x, 07C:26x, 08C:26x
 上面的参数说明：这个ＣＰＵ总共有8个core,当一个core工作时，最大睿频频率为3.2Ghz,以此类推；
 默认是八个核工作，也可以通过命令设置一个core工作；


==> 所有的核设置为ondemand模式时，有少部分核工作频率为2.4G，但工作于2.4G的核的数目不固定，是变动的。

remark:
使用cpufreq工具给CPU临时调整主频

使用cpufreq工具给CPU临时调整主频
 
现代的CPU和主板都有节电技术，在CPU低负荷工作的会自动降频。如果需要临时设置主频和工作模式，可使用cpufreq手动调整。这个模式将在重启后失效，如果需要长期调整请修改/etc/sysconfig/cpuspeed。
  www.2cto.com  
lsmod | grep "acpi_cpufreq"
 
执行上面的命令检查是否加载acpi_cpufreq模块，若是没有加载则可以使用yum去安装此模块
 
yum install -y cpufreq-utils.x86_64
 modprobe acpi_cpufreq  #经过试验此模块不支持intel xeon处理器，只有只有P4-clockmod这个模块支持xeon处理器，但是前提要自己动手编译内核。。。
 
查看当前CPU工作频率和状态：
  www.2cto.com  
cpufreq-info
执行以上命令，输出如下结果：
 
cpufrequtils 005: cpufreq-info (C) Dominik Brodowski 2004-2006
Report errors and bugs to cpufreq@vger.kernel.org, please.
analyzing CPU 0:
  driver: acpi-cpufreq
  CPUs which need to switch frequency at the same time: 0
  hardware limits: 1.60 GHz - 2.60 GHz
  available frequency steps: 2.60 GHz, 2.50 GHz, 2.40 GHz, 2.30 GHz, 2.20 GHz, 2.10 GHz, 2.00 GHz, 1.90 GHz, 1.80 GHz, 1.70 GHz, 1.60 GHz
  available cpufreq governors: ondemand, userspace, performance
  current policy: frequency should be within 1.60 GHz and 2.60 GHz.
                  The governor "ondemand" may decide which speed to use
                  within this range.
  current CPU frequency is 1.60 GHz (asserted by call to hardware).
 
The governor "ondemand" 表示CPU频率的策略。CPU有三种策略，onemand（表示系统可以通过动态调整频率，降低功耗，具体的调整策略和内核的功耗管理算法有关），userspace（表示用户可以自己设定cpu的频率），performance（表示CPU总是在最高主频下工作）。
  www.2cto.com  
current CPU frequency is 1.60 GHz 表示当前正在运行的主频。
 
调整CPU工作模式：
1、调整整体工作模式
 
cpufreq-set -g performance
执行以上命令，表示让CPU总是在最高主频下工作（不节能，但高性能）。执行完毕后，可再次执行cpufreq-info查看CPU的工作策略和当前主频。
 
2、手工0号核心的指定最大频率和最小频率
 
cpufreq-set -c 0 -g userspace -d 180000 -u 240000
执行以上命令，设定 0号核心 为 用户自定义，并设置最小频率为1.8GHz，最大频率2.4GHz


################
文件系统相关：
编辑/etc/mke2fs.conf文件，去掉ext4的has_journal
挂载：mount /dev/sdb1  /data1 -o rw,noatime,barrier=0

remark:
Linux文件系统的barrier：启用还是禁用 




大多数当前流行的Linux文件系统，包括EXT3和EXT4，都将文件系统barrier作为一个增强的安全特性。它保护数据不被写入日记。但 是，在许多情况下，我们并不清楚这些barrier是否有用。本文就为什么要在你的Linux系统上启用barrier做出了解释。

Linux日志和barrier功能

要理解barrier，你首先需要理解文件系统日志功能。常用的文件系统使用日志功能来保证文件系统的完整性。该功能背后的思路很简单：在写入新的 数据块到磁盘之前，会先将元数据写入日志。预先将元数据写入日志可以保证在写入真实数据前后一旦发生错误，日志功能能很容易地回滚到更改之前的状态。这个 方法确保了不会发生文件系统崩溃的情况。

单独使用日志功能不能保证没有任何差错。现在的磁盘大都有大容量的缓存，数据不会立即写入到磁盘中，而是先写入到磁盘缓存中。到这一步，磁盘控制器 就能更加高效地将其复制到磁盘中。这对性能来说是有好处的，但是对日志功能来说则相反。为了保证日志百分之百可靠，它必须绝对保证元数据在真实数据写入之 前被预先写入。这就是我们要介绍文件系统barrier的原因。

我们很容易理解使用barrier的根本原因：barrier本身禁止在barrier之后写入数据，真实的数据块将在barrier被写入之前完 全写入磁盘。使用barrier可以确保文件系统的完整性，因为barrier功能在EXT4文件系统中是默认启用的(除非你的操作系统更改了这个默认设 置)。

Linux文件系统的barrier：启用还是禁用?

你可以通过/proc/mounts文件来监控文件系统barrier的当前状态;对于每一个挂载的文件系统，打开这个文件都能看到所有的挂载选项。如果你看到barrier=1，那么你的文件系统就正在使用barrier功能。下列信息是一个文件系统的例子：

/dev/sda1 /boot ext4 rw,seclabel,relatime,barrier=1,data=ordered 0 0/dev/mapper/luks-3e67401f-44c6-4a27-a1bf-cdf0dcf45f65 /home ext4 rw,seclabel,noatime,barrier=1,data=ordered 0 0

文件系统barrier何时不工作?

Barrier的问题在于，它不能应用于所有条件下。如果设备映射器作为存储层的优先级使用，那么文件系统barrier就无法工作了，因为设备映 射器不支持barrier。所以，哪怕你的文件系统默认支持barrier，还是无法在逻辑卷、软RAID或者多路径磁盘上运行该功能(RED HAT和所有相关的Linux版本都将barrier作为默认选项)。

解决这个问题的方案之一就是避免使用设备映射器。所以在安装服务器时，你需要充分考虑配置选项。首先，你不该使用LVM安装服务器，而应该选择用传 统的分区方式。接着，你不能使用和设备映射器配合工作的多路径磁盘，它会在SAN上创建多个冗余路径。某些情况下，SAN供应商会提供一个专有驱动器作为 选择，但不是所有供应商都提供该选项。最好的办法是采用智能硬件。

使用barrier保护的风险之一是，在系统中断时，数据会留在缓存中，而永不会写入文件系统。一个简单的电池备份控制器可以避免这个问题。当服务器使用的这个控制器出故障了，磁盘控制器仍然能保证变更操作，这充分排除了barrier使用的需要。

使用barrier的另一个不利之处在于，你需要付出降低性能的代价。如果你需要顶级的性能，那么你可以用挂载选项-o barrier=0来关闭barrier功能，比如：mount /dev/sda2 -o barrier=0 /data。

文件系统barrier功能非常有用，但是不能和设备映射器配合工作。如果你需要使用这类设备，但是又想要保证文件系统完整性，那么你可以用电池备 份磁盘控制器。如果你的硬件不支持这个，那么你只能避免使用设备映射器，这样才能用barrier功能来保障文件系统完整性。还有，如果你希望得到更好的 系统性能，最好也不要开启barrier功能，它会降低系统运行速度。


元数据metadata 对IO有多大影响？
日志文件系统（journaling file systems）可防止系统崩溃时导致的数据不一致问题。对文件系统元数据（metadata）的更改都被保存在一份单独的日志里，当发生 系统崩溃时可以根据日志正确地恢复数据。除此之外，日志使系统重新启动时不必进行文件系统的检查，从而缩短了恢复时间。

所以说元数据就是数据的数据。
任何文件系统中的数据分为数据和元数据。数据是指普通文件中的实际数据，而元
数据指用来描述一个文件的特征的系统数据，诸如访问权限、文件拥有者以及文件数据
块的分布信息(inode...)等等。在集群文件系统中，分布信息包括文件在磁盘上的位置以及磁盘在集群中的位置。用户需要操作一个文件必须首先得到它的元数据，才能定位到文件的位置并且得到文件的内容或相关属性。
2． 元数据管理方式
         元数据管理有两种方式。集中式管理和分布式管理。集中式管理是指在系统中有一个节点专门司职元数据管理，所有元数据都存储在该节点的存储设备上。所有客户 端对文件的请求前，都要先对该元数据管理器请求元数据。分布式管理是指将元数据存放在系统的任意节点并且能动态的迁移。对元数据管理的职责也分布到各个不 同的节点上。大多数集群文件系统都采用集中式的元数据管理。因为集中式管理实现简单，一致性维护容易，在一定的操作频繁度内可以提供较满意的性能。缺点是 单一失效点问题，若该服务器失效，整个系统将无法正常工作。而且，当对元数据的操作过于频繁时，集中的元数据管理成为整个系统的性能瓶颈。
         分布式元数据管理的好处是解决了集中式管理的单一失效点问题， 而且性能不会随着操作频繁而出现瓶颈。其缺点是，实现复杂，一致性维护复杂，对性能有一定影响。


###############################################
@@@关闭SELinux
sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config

#####################################
修改sysctl.conf配置
--关闭swap内容
swapoff -a      （打开 swapon -a）
echo 0 > /proc/sys/vm/swappiness
cat >>/etc/sysctl.conf << EOF	
vm.swappiness = 0
EOF
--生效配置
sysctl –p


#############配置打开文件数
cat >> /etc/security/limits.conf << EOF	
* soft nofile 65535
* hard nofile 65535
* - nofile 51200
EOF


############################
配置NTP：
服务器配置：
---配置namenode的ntp

配置namenode的ntp为向本地同步
cat >> /etc/ntp.conf << EOF
server 127.127.1.0 
fudge 127.127.1.0 stratum 8 
EOF


配置datanode的ntp
配置向namenode的ntp服务同步
cat >> /etc/ntp.conf << EOF
server namenode 
EOF


启动时钟同步
所有节点上执行如下命令
service ntpd start 
chkconfig ntpd on 
ntpdate -u namenode
cat >> /etc/crontab << EOF
*/5 * * * * root /usr/sbin/ntpdate -u namenode ;/sbin/hwclock -w
EOF


#################设置SSH无密码登陆
--设置namenode ssh访问权限
mkdir -p /root/.ssh
chmod 700 /root/.ssh
cd /root/.ssh
# remove/save any contents so the directory is empty
ssh-keygen -t rsa -q
# hit return for any prompts
cp id_rsa.pub authorized_keys
echo "StrictHostKeyChecking=no" >config


---设置datanode ssh
root用户ssh登录到每个datanode上依次执行如下命令
mkdir -p /root/.ssh
chmod 700 /root/.ssh
cd /root/.ssh
# remove/save any contents so the directory is empty
rm -rf *
scp namenode:/root/.ssh/* ./


#######################配置本地yum源：
cd /etc/yum.repos.d/
rm -rf *

--上传安装包到：/home/CDH
--配置yum源文件：
cat >> /etc/yum.repos.d/acloudera-manager.repo << EOF
[cloudera-manager]
name = Cloudera Manager, Version 5.3.2
enabled = 1
baseurl = file:///home/CDH/cloudera-manager/RPMS/x86_64
gpgkey = http://archive.cloudera.com/redhat/cdh/RPM-GPG-KEY-cloudera
gpgcheck = 0
EOF


---所有服务器上创建REPO
所有服务器上创建REPO
cd  /home/CDH/cloudera-manager/RPMS/x86_64/
createrepo .
yum repolist      #可以查看repo包的情况


#######################################################################
@@@@@@cpu超频追加说明：
系统命令cpufreq-info   隶属于的安装包为：cpufrequtils
使用yum 安装cpufrequtils 包时提示如下错误：
[root@localhost yum.repos.d]# yum install cpufrequtils*
。。。。。。。。。。
warning: rpmts_HdrFromFdno: Header V3 RSA/SHA256 Signature, key ID fd431d51: NOKEY


Public key for cpufrequtils-007-6.el6.x86_64.rpm is not installed

网上搜索的解决办法如下：
在网上找到了解决方法：
此时要导入rpm的签名信息即可
以root登录，执行下面命令
# rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

根据我的Linux版本是CentOS 5.4
于是我执行下面命令
#rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-5

问题终于得到解决！

==》 在redhat 系统下执行rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
后，再执行安装命令，则功能正常了；

@@执行cpu频率查询命令：
[root@localhost yum.repos.d]# cpufreq-info | grep "The governor"
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
                  The governor "ondemand" may decide which speed to use
[root@localhost yum.repos.d]# cpufreq-info | grep "The governor" | wc -l
32

The governor "ondemand" 表示CPU频率的策略。CPU有三种策略，onemand（表示系统可以通过动态调整频率，降低功耗，具体的调整策略和内核的功耗管理算法有关），userspace（表示用户可以自己设定cpu的频率），performance（表示CPU总是在最高主频下工作）。


@@@@命令解析：
 awk  '/^processor/ {system("echo performance > /sys/devices/system/cpu/cpu" $3 "/cpufreq/scaling_governor")}' /proc/cpuinfo 

[root@localhost yum.repos.d]# cat /proc/cpuinfo | grep "^processor"
processor	: 0
processor	: 1
processor	: 2
processor	: 3
processor	: 4
processor	: 5
processor	: 6
processor	: 7
processor	: 8
processor	: 9
processor	: 10
processor	: 11
processor	: 12
processor	: 13
processor	: 14
processor	: 15
processor	: 16
processor	: 17
processor	: 18
processor	: 19
processor	: 20
processor	: 21
processor	: 22
processor	: 23
processor	: 24
processor	: 25
processor	: 26
processor	: 27
processor	: 28
processor	: 29
processor	: 30
processor	: 31

对每个逻辑核，配置为performance的模式：
echo performance > /sys/devices/system/cpu/cpu" $3 "/cpufreq/scaling_governor

－－－－－－－－－－－
[root@localhost yum.repos.d]# ll /sys/devices/system/cpu/
cpu0/                    cpu17/                   cpu25/                   cpu5/                    online
cpu1/                    cpu18/                   cpu26/                   cpu6/                    possible
cpu10/                   cpu19/                   cpu27/                   cpu7/                    present
cpu11/                   cpu2/                    cpu28/                   cpu8/                    sched_mc_power_savings
cpu12/                   cpu20/                   cpu29/                   cpu9/                    sched_smt_power_savings
cpu13/                   cpu21/                   cpu3/                    cpufreq/                 
cpu14/                   cpu22/                   cpu30/                   cpuidle/                 
cpu15/                   cpu23/                   cpu31/                   kernel_max               
cpu16/                   cpu24/                   cpu4/                    offline                  
[root@localhost yum.repos.d]# ll /sys/devices/system/cpu/
－－－－－－－－－－－－－－－－－－－
[root@localhost yum.repos.d]# cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor 
userspace
[root@localhost yum.repos.d]# 

#####################################################

基于源码包安装编译网卡驱动的方法（以下为intel 40G网卡的驱动安装readme）:
Building and Installation
-------------------------

To build a binary RPM* package of this driver, run 'rpmbuild -tb
i40e-<x.x.x>.tar.gz', where <x.x.x> is the version number for the driver tar file.

NOTES:

- For the build to work properly, the currently running kernel MUST match
  the version and configuration of the installed kernel sources. If you have
  just recompiled the kernel reboot the system before building.
- RPM functionality has only been tested in Red Hat distributions.

1. Move the base driver tar file to the directory of your choice. For
   example, use '/home/username/i40e' or '/usr/local/src/i40e'.

2. Untar/unzip the archive, where <x.x.x> is the version number for the
   driver tar file:
   tar zxf i40e-<x.x.x>.tar.gz

3. Change to the driver src directory, where <x.x.x> is the version number
   for the driver tar:
   cd i40e-<x.x.x>/src/

4. Compile the driver module:
   # make install
   The binary will be installed as:
   /lib/modules/<KERNEL VERSION>/updates/drivers/net/ethernet/intel/i40e/i40e.ko

   The install location listed above is the default location. This may differ
   for various Linux distributions.

5. Load the module using the modprobe command:
   modprobe <i40e> [parameter=port1_value,port2_value]

   Make sure that any older i40e drivers are removed from the kernel before
   loading the new module:
   rmmod i40e; modprobe i40e


###########################################################################################
excel 问题解答：
Excel单元格中输入文本，但是却显示为一排＃
 在编辑excel的单元格时，将单元格格式设置成文本，在其中填写文字 用Alt＋Enter做为换行 前6行编辑都没有问题 单元格也能正常显示为文本内容 但是当想再添加1行内容的时候，回车之后，单元格的文字就全部不显示了，变成了一行＃，而且单元格的行告也自动缩...
展开

同志们，我的整列，都已经是自动换行＋文本格式了

还有其他的方案么？
==》答案：
选中你要显示多行的单元格--右键--设置单元格格式--数字--常规
选中你要显示多行的单元格--右键--设置单元格格式--对齐--自动换行--确定--OK!

############################################################################################### 82599 网卡插入别的厂家的光模块无法识别的问题对应：

[root@R5300G4 ~]# modinfo ixgbe
filename:       /lib/modules/2.6.32-431.el6.x86_64/kernel/drivers/net/ixgbe/ixgbe.ko
version:        3.15.1-k
license:        GPL
description:    Intel(R) 10 Gigabit PCI Express Network Driver
author:         Intel Corporation, <linux.nics@intel.com>
srcversion:     B390E9D9904338B52C2E361
alias:          pci:v00008086d00001560sv*sd*bc*sc*i*
alias:          pci:v00008086d0000154Asv*sd*bc*sc*i*
alias:          pci:v00008086d00001557sv*sd*bc*sc*i*
alias:          pci:v00008086d00001558sv*sd*bc*sc*i*
alias:          pci:v00008086d0000154Fsv*sd*bc*sc*i*
alias:          pci:v00008086d0000154Dsv*sd*bc*sc*i*
alias:          pci:v00008086d00001528sv*sd*bc*sc*i*
alias:          pci:v00008086d000010F8sv*sd*bc*sc*i*
alias:          pci:v00008086d0000151Csv*sd*bc*sc*i*
alias:          pci:v00008086d00001529sv*sd*bc*sc*i*
alias:          pci:v00008086d0000152Asv*sd*bc*sc*i*
alias:          pci:v00008086d000010F9sv*sd*bc*sc*i*
alias:          pci:v00008086d00001514sv*sd*bc*sc*i*
alias:          pci:v00008086d00001507sv*sd*bc*sc*i*
alias:          pci:v00008086d000010FBsv*sd*bc*sc*i*
alias:          pci:v00008086d00001517sv*sd*bc*sc*i*
alias:          pci:v00008086d000010FCsv*sd*bc*sc*i*
alias:          pci:v00008086d000010F7sv*sd*bc*sc*i*
alias:          pci:v00008086d00001508sv*sd*bc*sc*i*
alias:          pci:v00008086d000010DBsv*sd*bc*sc*i*
alias:          pci:v00008086d000010F4sv*sd*bc*sc*i*
alias:          pci:v00008086d000010E1sv*sd*bc*sc*i*
alias:          pci:v00008086d000010F1sv*sd*bc*sc*i*
alias:          pci:v00008086d000010ECsv*sd*bc*sc*i*
alias:          pci:v00008086d000010DDsv*sd*bc*sc*i*
alias:          pci:v00008086d0000150Bsv*sd*bc*sc*i*
alias:          pci:v00008086d000010C8sv*sd*bc*sc*i*
alias:          pci:v00008086d000010C7sv*sd*bc*sc*i*
alias:          pci:v00008086d000010C6sv*sd*bc*sc*i*
alias:          pci:v00008086d000010B6sv*sd*bc*sc*i*
depends:        mdio,ptp,dca
vermagic:       2.6.32-431.el6.x86_64 SMP mod_unload modversions 
parm:           IntMode:Change Interrupt Mode (0=Legacy, 1=MSI, 2=MSI-X), default 2 (array of int)
parm:           FdirMode:Flow Director filtering modes (0=Off, 1=On) default 1 (array of int)
parm:           max_vfs:Maximum number of virtual functions to allocate per physical function - default is zero and maximum value is 63 (uint)
parm:           allow_unsupported_sfp:Allow unsupported and untested SFP+ modules on 82599-based adapters (uint)
parm:           debug:Debug level (0=none,...,16=all) (int)

[root@R5300G4 ~]# cat /etc/grub.conf 
# grub.conf generated by anaconda
#
# Note that you do not have to rerun grub after making changes to this file
# NOTICE:  You have a /boot partition.  This means that
#          all kernel and initrd paths are relative to /boot/, eg.
#          root (hd0,0)
#          kernel /vmlinuz-version ro root=/dev/mapper/vg_r5300g4-lv_root
#          initrd /initrd-[generic-]version.img
#boot=/dev/sda
default=0
timeout=5
splashimage=(hd0,0)/grub/splash.xpm.gz
hiddenmenu
title Red Hat Enterprise Linux (2.6.32-431.el6.x86_64)
        root (hd0,0)
        kernel /vmlinuz-2.6.32-431.el6.x86_64 ro root=/dev/mapper/vg_r5300g4-lv_root rd_LVM_LV=vg_r5300g4/lv_root rd_NO_LUKS LANG=en_US.UTF-8 rd_NO_MD SYSFONT=latarcyrheb-sun16 crashkernel=128M rd_LVM_LV=vg_r5300g4/lv_swap  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM rhgb quiet ixgbe.allow_unsupported_sfp=1
        initrd /initramfs-2.6.32-431.el6.x86_64.img


#############################################################
环境：OS：Linux SUSE 11 sp2 64bit

           硬件：IBM x3650 M3服务器(带82599EB网卡)

问题现象：当插上10G光模块的时候，ifconfig无法显示接口，或者导致接口消失。

定位过程：dmesg发现“failed to load because an unsupported SFP+ module type was detected.”信息，以此信息google发现如下帖子，

http://discussions.citrix.com/topic/306986-xenserver-60-issues-with-intel-82598eb-10-gigabit-af-dual-port-nic/

结论：82599EB只支持与intel自家的光模块对接。而我的光模块是finisar的。

解决办法：卸载驱动并以allow_unsupported_sfp=1参数重新加载

                 modprobe -r ixgbe;modprobe ixgbe allow_unsupported_sfp=1



###############################################################

问题描述：
7805的控制器，使用的系统盘是之前在6805 下安装的suse 11sp3,
启动系统时，会挂住，提示找不到控制器 **-part2,

改善方法：按y 后等待一段时间进入shell命令行后，进入提示的目录下后，
将***part2 重命名为找不到的控制器 **-part2，然后输入exit后，继续进行正常的引导进入系统；



########################################################################
