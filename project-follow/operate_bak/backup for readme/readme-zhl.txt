#I8350 ���ȵ���  ��BMC shell(root/root)--ushell(zte/zte)--sh 1��
BSP_DbgFanTest(1)    //�رշ��ȵ��ٲ���
BSP_SetFanPwm(0xff)  //�ֶ����÷���ռ�ձȣ�����01-ff
BSP_GetFanRpm()             //��ȡ���ת��

###�����л�(BMC)
BSP_SetPanelUart(1)   //HOST UArt
BSP_SetPanelUart(0)   //BMC UArt
BSP_SetPanelUart(3)   //expander UArt --����л��������ȷ��expander�İ汾��Ϣ

###ipmitool �����з��ʣ�
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

####��ipmitool��ʹ��sol activate ��sol���ܺ�linuxϵͳ�£�����ֱ��ӳ�������еķ���(ǰ���Ǵ��ڹ���Ҫ�򿪲ſ���)
####linuxϵͳ���úô��ں󣬿����ô��ڵ�½�������£�������ص�shell����
####ֻ���ӹ���ڵ�����£�hostΪlistʱ��������sol ���ܣ�ֱ�ӵ�¼host��������


0xff--5700rpm

0xe9--5000rpm
0xd1--4500rpm
0xc1--4100~4200rpm
0xbb--4000rpm
0xa1--3500rpm  
0x8c--3000rpm  

#linux raid����ͼ�ι����ߵ�������
./startupui.sh


#LSI mega �����в���
./storcli.exe    /c0    show    all  ����ѯ��ǰ�������µ�����Ϣ �����ע EID:Slt  ���ں���������
./storcli.exe /c0 /exxx /sxx    set    good ��������תΪ Unconfig Good ��
./storcli.exe /c0    /f    all    del ������¼����̵� RAID ������Ϣ ��
./storcli.exe    /c0    /exxx    /sxx    add    hotsparedrive ����תΪ�ȱ��� ��

#PMC raid���������ã�
ARCCONF GETCONFIG <Controller#> [AD|LD [LD#]|PD|MC|AL]

#bashĬ������
/usr/local/bin/
/bin/ 

#������������
ln -s /home/thunder/storcli-linux  /bin/storcli_lnk

#fio 2.1.14 ����gfioģ�飬�����ģ��ķ���
cd��fioĿ¼����
./configure --enable-gfio
make fio
make gfio
./fio -S (fio serverģʽ)
����һ���ն�����./gfio����clientģʽ


#gfio ���ýű��У�directory�ǽ���IO���Ե�Ŀ��·��
�ڵ�һ�δ���ʱ�����Կ�����̬�Ĳ���ͼ���ڶ��β���ʱ�����������ļ���ɾ��

#linux�����̸�ʽ��
mkfs /dev/sdb, ����ʽ������ʱ�����޷����ж�д
mkdir /mnt/vfat
mount -t ext2 /dev/sdb /mnt/vfat


#���ý�ѹ���
�ܽ� 
1��*.tar �� tar �Cxvf ��ѹ 
2��*.gz �� gzip -d����gunzip ��ѹ 
3��*.tar.gz��*.tgz �� tar �Cxzf ��ѹ 
4��*.bz2 �� bzip2 -d������bunzip2 ��ѹ 
5��*.tar.bz2��tar �Cxjf ��ѹ 
6��*.Z �� uncompress ��ѹ 
7��*.tar.Z ��tar �CxZf ��ѹ 
8��*.rar �� unrar e��ѹ 
9��*.zip �� unzip ��ѹ


01-.tar��ʽ
�����[��������������]$ tar xvf FileName.tar
�����[��������������]$ tar cvf FileName.tar DirName��ע��tar�Ǵ��������ѹ������

02-.gz��ʽ
��ѹ1��[��������������]$ gunzip FileName.gz
��ѹ2��[��������������]$ gzip -d FileName.gz
ѹ ����[��������������]$ gzip FileName

03-.tar.gz��ʽ
��ѹ��[��������������]$ tar zxvf FileName.tar.gz
ѹ����[��������������]$ tar zcvf FileName.tar.gz DirName

04-.bz2��ʽ
��ѹ1��[��������������]$ bzip2 -d FileName.bz2
��ѹ2��[��������������]$ bunzip2 FileName.bz2
ѹ ���� [��������������]$ bzip2 -z FileName

05-.tar.bz2��ʽ
��ѹ��[��������������]$ tar jxvf FileName.tar.bz2
ѹ����[��������������]$ tar jcvf FileName.tar.bz2 DirName

#linux�������ѯ�Ͱ�װ����
rpm -ql | grep "***"
rpm -e ***ж�����



#����dell��������Ϣ

������dell������(9MZGY02)
root/  HardTest1
IDRAC ip: 192.168.0.120
��IDRAC:integrated dell remote access controller��

#������IPMI �����ZTE��ͬ,��ipmi�����ʽ���£�
ipmitool -H *.*.*.*������IP�� -I lanplus -U <�û���> -P <����>


#R5300 ���԰汾
ftp://10.43.166.8//2015���ƶ����ɲ��԰汾//R5300//���Ʋ����ֳ����й̼��汾

RSS RSS

BMC:BMC_SGLMA_P3_R_V02.01.62.07_201508281414.BIN
EPLD:SGLMA_01_140201_EPLD_102.vpd

#linux ���
cat /proc/cpuinfo | grep name | uniq -c | cut -d: -f2
uniq -c:���ڼ�������ʾ���ظ���������������
cut -d: -f2 (����ָ���Ϊ����ֻ����ڶ�����field)cut��һ��ѡȡ������ǽ�һ�����ݾ���������ȡ��������Ҫ�ġ�һ����˵��ѡȡ��Ϣͨ������ԡ��С������з�����
��Ҫ����
-b �����ֽ�Ϊ��λ���зָ��Щ�ֽ�λ�ý����Զ��ֽ��ַ��߽磬����Ҳָ���� -n ��־��
-c �����ַ�Ϊ��λ���зָ
-d ���Զ���ָ�����Ĭ��Ϊ�Ʊ����
-f  ����-dһ��ʹ�ã�ָ����ʾ�ĸ�����

#wc:Linuxϵͳ�е�wc(Word Count)����Ĺ���Ϊͳ��ָ���ļ��е��ֽ���������������������ͳ�ƽ����ʾ���
���������

-c ͳ���ֽ�����

-l ͳ��������

-m ͳ���ַ����������־������ -c ��־һ��ʹ�á�

-w ͳ��������һ���ֱ�����Ϊ�ɿհס���������ַ��ָ����ַ�����

### HDD �������ע��
sas1064e/sas1068e:cfggen-linux (command:cfggen-linux list;cfggen-linux 0 status��cfggen-linux 0 display)

SAS2(SAS2008/2308): (��linux,windows)
sas2ircu-linux (command:sas2ircu-linux list;sas2ircu-linux 0 status;sas2ircu-linux 0 display)
lsiutil-1.71-linux ��command:./lsiutil-1.71-linux-x64 -p1 -a 1,8,16,66,60,0;./lsiutil-1.71-linux-x64 -p1 -a 21,1,2,3,0,0,0��

SAS3008: (��linux,windows)
sas3ircu-linux (command:sas3ircu-linux list;sas3ircu-linux 0 status,sas3ircu-linux 0 display)
lsiutil-1.71-linux ��command:./lsiutil-1.71-linux-x64 -p1 -a 1,8,16,66,60,0;./lsiutil-1.71-linux-x64 -p1 -a 21,1,2,3,0,0,0��

LSI MegaRaid (SAS2208/9361-8I...)(��linux,windows)
storcli-linux (command:storcli-linux /c0 show all;storcli-linux /c0 /vall show all;storcli-linux /c0 /eall /sall show all)

PMC 6805/7805:(��linux,windows)
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

##��������ʽ��
parted /dev/sdb--mklabel--gpt--yes--p--mkpart--gpt4t--ext4--1��0--(-1)--P--Q (sdb/sdb1)
mkfs.ext4 /dev/sdb1

һ������ʵ�֣�parted /dev/sdb rm 1  ɾ������
һ������ʵ�֣� parted /dev/sdb mkpart gpt4t ext4 0 4000GB I
 parted /dev/sdb mkpart gpt4t ext4 0 1997GB I

##�����÷�������
ifconfig eth0 | grep [B,b]cast |awk -F: '{print "IP_address:" $2}' | awk '{print $1}'


###linux����ʱ��ʾ����ʱ����������
fsck -y /dev/sda1, fsck -y /dev/sda2, fsck -y /dev/sda3

##ȷ��redhat �汾
cat /etc/redhat-release 

##yum����·��
baseurl=ftp://redhat:redhat@129.0.0.50/

##ϵͳ崻�ʱ���鿴��
service kdump status/start  ��¼����־Ϊ��/var/crash
���������echo c > /proc/sysrq-trigger 
����֮�����kdump��ʼ��¼��־��Ϣ

#### linux shell���ѭ��,��C������ͬ
 �˳����break
  ������continue

#linux��PMC�����ַ��
https://129.0.0.77:8443/maxview/manager/login.xhtml 
(Tomcat Service)

####
kdump��һ���Ƚ��Ļ���kexec���ں˱���ת�����ơ���ϵͳ����ʱ��kdumpʹ��kexec �������ڶ����ںˡ��ڶ����ں�ͨ�����������ںˣ��Ժ�С�ڴ������Բ���ת�����񡣵�һ���ں˱������ڴ��һ���ָ��ڶ��ں������á�����kdump����kexec���������ںˣ��ƹ��� BIOS�����Ե�һ���ں˵��ڴ���Ա����������ں˱���ת���ı��ʡ�kdump��Ҫ������ͬĿ�ĵ��ںˣ������ں˺Ͳ����ںˡ������ں��ǲ����ں˷���Ķ��񡣲����ں˻��������ں˱���ʱ��������������Ӧ��ramdiskһ���齨һ��΢���������Զ������ں��µ��ڴ�����ռ���ת�档ע�⣬������ʱ��kdump������һ����������Ҫ���ڴ棬Ϊ�˼���ϵͳ��Ҫ��������С�ڴ棬����kdumpʹ�õ��ڴ��������Ծ�����������С�ڴ������
Ϊ�˸��õ��ݴ����������û������� 

####�鿴IO��Ϣ
iostat -x -d 2 /dev/sdb
iostat -x -d 2

### scp����
scp /home/thunder/zhl_jack.txt  root@129.0.0.54:/home/
scp root@129.0.0.54:/home/zhl.txt /home/thunder

###linuxϵͳ������л�ƴ�����뷨
ctrl+�ո�

###ftp�������ã�
 1. ����rpm -qa| grep vsftpd�������Ƿ��Ѿ���װ�����ftpû�а�װ��ʹ��yum  -y  install vsftpd ��װ,(ubuntu ��ʹ��apt-get install vsftpd)

2. service vsftpd start

����Ҫ��FTPÿ�ο����Զ���������������:  chkconfig --level 35 vsftpd on

3. ����ftpȨ��

vi  /etc/vsftpd/vsftpd.conf
��anonymous_enable=YES ��Ϊ anonymous_enable=NO
ESC����,���롰:wq�����沢�Ƴ�

4. ���ftp�ʺź�Ŀ¼

useradd   -d /alidata/www/wwwroot -s /sbin/nologin pwftp
passwd   pwftp
chmod -R 755 /alidata/www/wwwroot
chown -R  pwftp /alidata/www/wwwroot
/etc/rc.d/init.d/vsftpd restart
Ȼ�����ʺ�pwftp����123456
�����¾Ϳ��Ե�½ftp�ˡ�Ŀ¼��/alidata/www/wwwroot


####linuxϵͳ��־�ļ�ȷ�ϣ�
dmesg; /var/log/messages
dmesg | tail (��ʾβ������Ϣ)
dmesg -c (�����Ϣ)

#### dd Ӳ�̲���
����Ӳ��д������time dd if=/dev/zero of=/dev/sdb bs=8k count=300000  
����Ӳ�̶�������time dd if=/dev/sda of=/dev/null bs=8k count=300000
ִ�й������� iostat -x -d 2�鿴��д�� ִ�к���dmesg�鿴�Ƿ��д���


#####iostat������ȷ�����
cpu����ֵ˵����

%user��CPU�����û�ģʽ�µ�ʱ��ٷֱȡ�

%nice��CPU���ڴ�NICEֵ���û�ģʽ�µ�ʱ��ٷֱȡ�

%system��CPU����ϵͳģʽ�µ�ʱ��ٷֱȡ�

%iowait��CPU�ȴ�����������ʱ��İٷֱȡ�

%steal���������ά����һ�����⴦����ʱ������CPU������ʶ�ȴ�ʱ��ٷֱȡ�

%idle��CPU����ʱ��ٷֱȡ�

��ע�����%iowait��ֵ���ߣ���ʾӲ�̴���I/Oƿ����%idleֵ�ߣ���ʾCPU�Ͽ��У����%idleֵ�ߵ�ϵͳ��Ӧ��ʱ���п�����CPU�ȴ������ڴ棬��ʱӦ�Ӵ��ڴ�������%idleֵ�����������10����ôϵͳ��CPU����������Խϵͣ�����ϵͳ������Ҫ�������Դ��CPU��

disk����ֵ˵����

rrqm/s:  ÿ����� merge �Ķ�������Ŀ���� rmerge/s

wrqm/s:  ÿ����� merge ��д������Ŀ���� wmerge/s

r/s:  ÿ����ɵĶ� I/O �豸�������� rio/s

w/s:  ÿ����ɵ�д I/O �豸�������� wio/s

rsec/s:  ÿ������������� rsect/s

wsec/s:  ÿ��д���������� wsect/s

rkB/s:  ÿ���K�ֽ������� rsect/s ��һ�룬��Ϊÿ������СΪ512�ֽڡ�

wkB/s:  ÿ��дK�ֽ������� wsect/s ��һ�롣

avgrq-sz:  ƽ��ÿ���豸I/O���������ݴ�С (����)��

avgqu-sz:  ƽ��I/O���г��ȡ�

await:  ƽ��ÿ���豸I/O�����ĵȴ�ʱ�� (����)��

svctm: ƽ��ÿ���豸I/O�����ķ���ʱ�� (����)��

%util:  һ�����аٷ�֮���ٵ�ʱ������ I/O ����������io���ĵ�cpu�ٷֱ�

��ע����� %util �ӽ� 100%��˵��������I/O����̫�࣬I/Oϵͳ�Ѿ������ɣ��ô��̿��ܴ���ƿ������� svctm �ȽϽӽ� await��˵�� I/O ����û�еȴ�ʱ�䣻��� await Զ���� svctm��˵��I/O ����̫����io��Ӧ̫��������Ҫ���б�Ҫ�Ż������avgqu-sz�Ƚϴ�Ҳ��ʾ�е���io�ڵȴ���




#### txt�ļ�ת��Ϊcsv�ļ�����
sort *.txt > *.csv

###Ӳ����죺fsck, e2fsck
fsck/e2fsck -c  (Check for bad blocks and add them to the badblock list)
hdparm -t /dev/sda ( -t   ����Ӳ�̵Ķ�ȡЧ�ʡ�)


###�꿨�̼����·�����
1������dos�����̣���������DOS��ִ��eeupdate�س�����ʾ�����nic��
2���ս������Ĺ̼�ʹ���������£�eeupdate -nic=x  -data=xxxx.txt

���䣺
ͨ��DOS�������ս�����MAC����
1������DOS����U�̣���ײ˵������
2����Eeupdate.exe���ߺ͹̼�ӳ������1G��ӳ��i350_KX_NO-MNG_1_52.txt������U��s
3����Ƭ��������DOS��ִ��eeupdate�س�����ʾ�����nic�ţ�ĸ�����0��1
4���ս������Ĺ̼�ʹ����������
eeupdate -nic=x  -data=xxxx.txt
5���ս�������MACʹ����������
eeupdate -nic=x -mac=001122334455


####lsi 2308 �̼���bios���·���
1�����̼���bios ��lsiutil���߷ŵ���ͬ��Ŀ¼
2��1--�鿴bios�͹̼��İ汾
   2--�����̼�
   4--����bios

####������ѯ��
lspci | grep "Ethernet"
ifconfig -a
ethtool ethx
ethtool -i ethx

#####linux��VNCʹ�ò�����ɣ�
1��vnc �����װ 2������VNCserver 3)�رշ���ǽ 4���޸������ļ�/root/.vnc/xstartup,(# unset SESSION_MANAGER   # exec /etc/X11/xinit/xinitrc) ȥ�������е�ע�ͣ�5��vncserver -kill :1 6��vncserver :1 7����PC�˴�VNC����ʹ�á�

#### fio�������

fio -name=testc -filename=/dev/sda -bs=256k --rw=write -iodepth=32 -runtime=4h  -direct=1 -numjobs=30 -time_based  -ioengine=psync -thread -group_reporting

####����ѹ���ͽ�ѹ
tar zcvf servertool~.tar.gz servertool~/
tar xzf  servertool~.tar.gz

#### linuxϵͳ�����صĳ���
bin�ļ�������ֱ������ִ��Ȩ�޺�ִ��
Դ���ļ�����Ҫ���밲װ

###centos 7��
systemctl stop firewalld.service #ֹͣ
systemctl disable firewalld.service #����
֮ǰ�İ汾��
service iptables stop #ֹͣ
chkconfig iptables off #����

#####netstat | grep ssh

####PMC 6805�̼����·�����
./arcconf romupdate 1 xxxx.ufi

E9000��
����129.5.101.143
��Ƭip:192.168.12.181  root/123456
E9000���п���
raid�� --S600 S620 S610
FC��--N500
����--N720


######gfio���
./confiture --enable-gfio
make fio
make gfio
./fio -S
./gfio
ÿ��ʹ��ǰ��ɾ���ϴζ�д���ļ������β���ÿ�ζ����Գ�����������iostat -x -d 2 ���鿴Ӳ���Ƿ��ڽ��ж�д����ʱ��һ���޷�������ʼ�����ڶ��ξͿ�����

####libaio
yum install libaio-devel ���ӱ��صĹ���ftp�����أ�
-- Make clean��make��make install 


#####mcelog:
yum install -y mcelog* 
��װ��ɺ���/etc������mcelog��Ŀ¼����Ŀ¼����mcelog.conf �ļ��� ��װ֮ǰ��û��/etc/mcelogĿ¼

service kdump status --ȷ��kdump�Ƿ��

��װϵͳ��ʱ��װkdump


###�鿴���ڣ�
dmesg | grep ttyS* 

####�������÷�����
/etc/grub.conf�У�����ı���initrd /initramfs-2.6.32-431.el6.x86_64.img��
֮ǰ���� console=ttyS0,115200

/etc/inittab �У�����ı���id:5:initdefault:��֮������
co:2345:respawn:/sbin/agetty ttyS0 115200 vt100 init q   /for rhel
co:2345:respawn:/sbin/agetty -L 115200  ttyS0 ansi    /for SLES

/etc/securetty�У��ı��������ttyS0

����server���ڴ����ն˿��Կ���host�Ĵ�ӡ��Ϣ


####�������ܣ�netperf��
1)ʹ�������netperf-2.6.0.tar.bz2 ��tar �Cjxvf, ./configure; make; make installl��,֮����whereis netperf ��whereis netserver��ѯ�������Ϣȷ������Ѿ���װ�ɹ�
2)��������У�netserver -p 10000���˿ڵ�ַ�������⣩
3)�ͻ������У� netperf -H 128.0.0.62�������IP��ַ�� -l 72000������ʱ�䣬��λs�� -t TCP_STREAM -p 10000��Ҳ���Բ�ָ����
4)ʹ������������ѯ������̵���Ϣ
ps aux | grep netperf
ps aux | grep netserver
5)��ifconfig ��ѯÿ���������շ�������Ϣ
6)��Ҫ��127.*.*.*��IP��ַ�������ַ��ϵͳԤ�����Լ���IP��ַ��
7)��pkill netperf ,pkill netserver ���رս���
remark:
��̨�������໥����Ĳ���ģʽ��
��̨�������϶�����netserver 
ÿ���������ֱ���Է�����������ִ��netperf�������ѹ��ģʽ


####�������ܲ��ԣ�ixchariot��
1)ʹ�������6endpoint.tar.gz��tar -zxvf/xzf; ./endpoint.install,һֱ���ո�������룺accept_license����װ��ϣ�
2�����Ի��ϰ�װwindows�汾�Ŀͻ��ˣ�
3������ʱ��ֻ���ڿͻ��˽������ü��ɣ��������˲����κ�����
�ͻ��˴򿪣����ͼ�꣨�����������ߣ�--����д���Ե�����������endpoint��IP��ַ��select script,ѡ��֮���޸Ĳ����漴������Զ������ԣ�

�������ʵ����
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


####Ӳ��IO���ԣ���fio��
1)ʹ�������fio-2.1.14.tar.bz2
2�����ڰ�װfio(tar -xjf; ./configure; make; make install)
2)��װgfio (./configure --enable-gfio;make fio; make gfio;)
3)ִ�У�
./fio -S  ./gfio

����ǰ�ᣨӲ�̡�����������--����ʽ����mkfs.ext4  /dev/sdb1��-->���� 
mount -t ext4 /dev/sdb1 /home/test��

fio -name=testc -filename=/dev/sdb1 -bs=4k --rw=randread -iodepth=32 -size=512m  -direct=1  -ioengine=libaio

����֤��fio��gfio���Խ���൱

###libaio
yum install libaio-devel ���ӱ��صĹ���ftp�����أ�
-- Make clean��make��make install   ==>��ʱ�Ϳ�������ʹ��libaio��


#####Linux �в鿴�������������� -- sar 
sar -n DEV 2

### �����������Ų�������裺
1��ȷ�Ϸ������Ƿ��ܹ��ϵ磬�����ȫ���ܼӵ磬���Ǽ��cpu���ڴ桢Ӳ���Լ��忨�İ�װ�����
2������ܼӵ磬����������������������Ϣ��
3�������װ��ϵͳ�޷���������ȷ��������ѡ������ȷ��

#### ����˿�ȷ�ϣ�
netstat -ntl

####
���⣺�������쳣�ػ��� ������ѹ������С�İ�����Դ�����¹ػ���󣬿����޷�����ͼ��ģʽ��
   �ڴ����£����Խ���������ģʽ�� ����ʾ��ʱ��ĳ����Ҳ���Խ���������ģʽ

�Բߣ���fsck�޸����з����������Ϳ��Խ���ͼ�ν����ˡ�

####��������ftp�����
1�� useradd  username, passwd username
2) vi /etc/vsftpd/vsftpd.conf
anonymous_enable=no
ascii_upload_enable=YES
3)�����������ر����ذ�ȫ����

#####BMC busyBOx��ftp �ϴ��������
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


####windows�Դ�DNS ·����
C:\Windows\System32\drivers\etc\hosts

#####specpower ����˵����
1�����Ի��ͷ������϶�Ҫ��װ����java��specpower�����
32bin windows���Ի�����װ��Ӧ��java(jdk-6u10-rc2-bin-b32-windows-i586-p-12_sep_2008.zip)
64bin windows��������ֱ�Ӱ�ibm_sdk70.zip copy��ĳ��·���½�ѹ�󼴿ɣ����ð�װ��java���ڵ�Ŀ¼����\ibm_sdk70\jre\bin\java.exe�� 
2��copy SPECpower_2008��װ�ļ���ϵͳ����Ŀ¼
3����SUT �ˣ���cmd���ڣ�����javaĿ¼·��������java���java �Cjar E:\SPEC_2008\setup.jar����֮��һ·next��װ��ɣ�
4���ڵ��Ի��ϣ�ֱ��˫��setup.jar��װ���ɣ�

5���������¶Ⱥ͹��ʵ�����µĻ����������£�
SUT�ˣ� �����ص�runssj_yd.bat�Ŀ������滻��SPECpower_2008��װĿ¼��ssjĿ¼�µ�runssj.bat�ű������������޸ģ�
a)?
:: Set the number of JVMs to run
set JVMS=8
(�趨JVM�߳������趨ԭ����JVMS����һ�������߼�cpu��������4����2�ó���Ҫ�ܱ�����)
b)set DIRECTOR_HOST=129.1.6.100(Ϊʵ�ʵĵ��Ի���IP)
c)set JAVA=C:\eclipseDevelopmentPackage\ibm_sdk70\bin\java (Ϊʵ�ʵ�java�������ڵ�·��)

���ƶ����ã�
a)set NUM_HOSTS=1   ///(���ô������豸������)
b)
:: Properties file to be passed to Director
::set PROPFILE=SPECpower_ssj_EXPERT.props
set PROPFILE=SPECpower_ssj.props
3)	����director���������ļ�������ʽ����ʱһ��Ҫѡ��Ĭ�ϵ�SPECpower_ssj.props�����ڵ��Թ����У�����ΪSPECpower_ssj_EXPERT.props�󣬿�����SPECpower_ssj_EXPERT.props���޸Ĳ��Ե�ʱ�����������еȵ�

c)C:\SPECpower_ssj2008\PTDaemonĿ¼���༭runpower.bat�ļ�
set DEVICE=0 ��Ĭ�����˼��û�нӹ��������Ĳ���

d)��SPECpower_2008Ŀ¼������ccsĿ¼,���û���¶ȴ����������߹��ʲ����ǣ�������ccs.props�����Ӧ��temp1��pwr1ע�͵���
#ccs.ptd = pwr1, temp1

6)ִ��˳��
�ڿ��ƶˣ�����SPECpower_2008��װĿ¼������ssj��Ŀ¼������rundirector.bat�ű�
�л���SUT�ˣ�����SPECpower_2008��װĿ¼������ssj��Ŀ¼������runssj.bat �ű�
�л������ƶˣ�����SPECpower_2008��װĿ¼������ccs��Ŀ¼������runCCS.bat�ű�

7��SPECpower_2008��������һ�Σ���Ҫ73�������ң����ʹ��SPECpower_ssj_EXPERT.props��������������ƣ���ʱ�����Լ�����

8��������ɣ���SPECpower_2008��װĿ¼���Զ�����result��Ŀ¼�������Ŀ¼�����Բ鿴������Զ����ɵ�ssj.0036-main.html�ļ�����û�����ɱ�����ο����ĵ��鿴ԭ����result��Ŀ¼������power��ssj_ops����Ӧ�Ľ��

ע�����
1��IP Ҫ��ȷ������ǽҪ�رգ�
2��SUT����������á��ڴ�����ҳ��������administator�ӵ��ڴ������У��ᵼ��SUT����runssj.bat���Զ��رգ���������һ��Ҫ���òſ����������в���
3)�����power������£�specpowerֻ����Ϊһ��ѹ��������������Խ��û���κ�����


####
  windows����ϵͳ�У�������2�ַ����鿴ϵͳ��־��

         һ����ʼ---�������---������---�¼��鿴��---ϵͳ��־��

         ������ʼ---����---cmd---eventvwr---���ɲ鿴ϵͳ��־

##### sed���

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
sed '1s/^/& zhuhonglei/g' /etc/sysconfig/iptables  �ڵ�һ�еĿ�ͷ׷��
sed 's/lo/& zhuhonglei/g' /etc/sysconfig/iptables  ��λ��lo֮��׷��
sed '/lo/a zhuhonglei' /etc/sysconfig/iptables  ƥ����lo����֮��׷��

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

####�������������ݣ�
tar -g /home/jack/snapshort -czvf /home/jack/system_full_backup.tar.gz /home/thunder
tar -g /home/jack/snapshort -czvf /home/jack/system_add_backup.tar.gz /home/thunder/

####��ִ̨���Ҳ��������
nohup ./cron_test.sh (check with aux (cron*))
ʹ����������ӡ��ϢҲ��������ն���ʾ

�رգ� kill processID


#######crontab���
ʱ��ȷ�Ϻ�ͬ����أ�
date
date -s
ntpdate 129.0.0.50

��CRONTAB��ÿ10��������һ��ָ�� */10  * * * *

�༭��crontab -e 

�鿴��crontab -l
*/10 * * * * /bin/bash /home/thunder/cron_test.sh >> /home/thunder/log.txt
�����Խ�crontab�������ֱ����������ִ�У�����Ч�����������ִ���ټ���crontab�м��ɣ�

linux��ʱ����鿴��־�������кͶ�ʱ������صĶ�������¼�����棩
/var/log/cron*��crontab��ִ����־


cat /var/log/secure | grep -i password | egrep -o "([0-9]{1,3}\.){3}[0-9]{1,3}" | sort -nr | uniq -c | awk '$1>=4{print $2}'

#######ͬ�����
rsync -av /home/jack/ /home/jack1/    ����Ŀ��·���µĲ���
rsync -aP --delete /home/jack/ /home/jack1/  ��ȫͬ��


#######linux �¼���������˵����
rpm -ivh 
vi /etc/hardwaremonitor.conf 
rpm -qa | grep hardwaremon*
rpm -e linux-hardwaremon-v00.02.01-2.x86_64
/etc/init.d/hwmd status