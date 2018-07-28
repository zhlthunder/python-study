#I8350 风扇调速  （BMC shell(root/root)--ushell(zte/zte)--sh 1）
BSP_DbgFanTest(1)    //关闭风扇调速策略
BSP_SetFanPwm(0xff)  //手动设置风扇占空比，参数01-ff
BSP_GetFanRpm()             //读取风机转速

###串口切换(BMC)
BSP_SetPanelUart(1)   //HOST UArt
BSP_SetPanelUart(0)   //BMC UArt
BSP_SetPanelUart(3)   //expander UArt --问下谢焕军，如确认expander的版本信息

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
dd if=/dev/zero of=/dev/sdb  快速硬盘读写确认命令
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
fsck/e2fsck -c  (Check for bad blocks and add them to the badblock list)
hdparm -t /dev/sda ( -t   评估硬盘的读取效率。)
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
1）vnc 软件安装 2）启动VNCserver 3)关闭防火墙 4）修改配置文件/root/.vnc/xstartup,(# unset SESSION_MANAGER   # exec /etc/X11/xinit/xinitrc) 去掉这两行的注释，5）vncserver -kill :1 6）vncserver :1 7）在PC端打开VNC即可使用。

#### fio测试命令：

fio -name=testc -filename=/dev/sdb -bs=64k --rw=write -iodepth=32 -runtime=80h  -direct=1 -numjobs=8 -time_based  -ioengine=libaio -thread -group_reporting=1

###对系统盘压力测试用例（******）--running版本
fio -name=testc -filename=/home/tmp_io/tmp -bs=256k -rw=randrw -rwmixread=50 -iodepth=16 -direct=1 -numjobs=8 -runtime=24h -size=5G -time_based -ioengine=libaio -thread -group_reporting

####常用压缩和解压
tar zcvf servertool~.tar.gz servertool~/
tar xzf  servertool~.tar.gz


####linux进程后台执行命令 nohup (另一个作用是让所有的命令同时并发执行)
nohup命令：如果你正在运行一个进程，而且你觉得在退出帐户时该进程还不会结束，那么可以使用nohup命令。该命令可以在你退出帐户/关闭终端之后继续运行相应的进程。nohup就是不挂起的意思( no hang up)。 　
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
zypper refresh  #update过程时间较长

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

##################################################

