
############################################################

ʹ��linuxϵͳ�µ�ipmitool�鿴������Ϣ��
��װipmitool����
modprobe ipmi_devintf
���ú�Ŀ��BMC��ַ��ͬ�����ε�IP��ַ��ȷ�Ͽ���pingͨ
��telnet��½Ŀ��BMC��ַ��port 10000,zte/zte--sh1--BSP_SetPanelUart(1)�л�Ŀ�������Ĵ��ڵ�host��
ipmitool -I lanplus -H 192.168.5.78(Ŀ��BMC��ַ) -U zteroot -P superuser sol activate



##############################################################
http://cache.baiducontent.com/c?m=9d78d513d99d1af31fa7837e7c5790274e4380122ba7d6020ca38438e7732d32506793ac56250773d5d20a6316de4848adb0687d6d4566f58cc9fb57c0fad56a6dd56772671cf11b55805cf8905125b671cd05f4f848bae5af75cff59498c204038b4e067880f68a580717dd6f874e77bcf8&p=8b2a97129e9716ff57ee947d580798&newp=8b2a970a8b9e11a05bed97275f4c9f231610db2151d6d301298ffe0cc4241a1a1a3aecbf21231701d6c57c6005a44c56eaf23277370034f1f689df08d2ecce7e60d57a&user=baidu&fm=sc&query=linux+suse+%B4%AE%BF%DA%C5%E4%D6%C3&qid=f603603f0001772b&p1=2


5300 ������������ܽ᣺
ʹ��BMC�ĵ�ַ����telnet port 10000 ����: zte/zte, 
����admin # Ŀ¼
���ֱ������host�����ߣ��ڴ��ڽ����²鿴�ĳ�ʼ״̬Ҳ�� admin # --������, �����ַ�ʽ������ͬ
ִ��sh 1, �л���bsproc# Ŀ¼��
��ִ������������д����л��� 
###�����л�(BMC)  ��ʹ��uartswi() ���� host��BMC ����֮����л�
BSP_SetPanelUart(1)   //HOST UArt
BSP_SetPanelUart(0)   //BMC UArt
BSP_SetPanelUart(3)   //expander UArt

####�������÷�����
/etc/grub.conf�У�����ı���initrd /initramfs-2.6.32-431.el6.x86_64.img��
֮ǰ���� console=ttyS0,115200   --ֻ������Ҳ����������á�

{/etc/inittab �У�����ı���id:5:initdefault:��֮������
co:2345:respawn:/sbin/agetty ttyS0 115200 vt100 init q   /for rhel
co:2345:respawn:/sbin/agetty -L 115200  ttyS0 ansi    /for SLES

/etc/securetty�У��ı��������ttyS0

����server���ڴ����ն˿��Կ���host�Ĵ�ӡ��Ϣ

��ipmitool�в鿴���ڵķ�����
ipmitool -I lanplus -H 192.168.5.78 -U zteroot -P superuser sol activate (��������)
ipmitool -I lanplus -H 192.168.5.78 -U zteroot -P superuser sol deactivate���ر����



�鿴�����豸��dmesg | grep ttyS* 
�鿴���ڸ����� dmesg |gre ttyS*
�鿴����������cat /proc/tty/driver/serial
�鿴���ڵĲ����ʵ�������Ϣ�� stty -a -F /dev/ttyS0
�鿴����Ȩ�ޣ� ls -l /dev/ttyS*
################################################
5300 ���ڴ�ӡȷ�ϣ�
5300 ���ڣ�
ʹ��BMC�ĵ�ַ����telnet port 10000 ����: zte/zte, 
����admin # Ŀ¼

���ֱ������host�����ߣ��ڴ��ڽ����²鿴�ĳ�ʼ״̬Ҳ�� admin # --������

ִ��sh 1, �л���bsproc# Ŀ¼��

��ִ������������д����л���
###�����л�(BMC)
BSP_SetPanelUart(1)   //HOST UArt
BSP_SetPanelUart(0)   //BMC UArt
BSP_SetPanelUart(3)   //expander UArt --����л��������ȷ��expander�İ汾��Ϣ

##########################################################

5300g3-12  expander�̼���Ϣֻ��ͨ�����ڶ�ȡ��
1���������Ӵ��ڣ��ڴ����£���admin-->bsproc(ʹ��sh 1)��Ȼ���������uartswi()���л���host����
2��ͨ��telnet��port 10000��zte zte--sh 1 --��¼��bmc���л�����bsproc�����̣��������������޸ļĴ�����ֵ��
[bsproc]# wrepld(0x12,3)
������ʾ��Ϣ
[bsproc]Write Offset 0x0012 : Value = 0x0003.  //1��host��2δ֪��3��expander����
[bsproc]Read  Offset 0x0012 : Value = 0x0003.
[bsproc]value = '&' = 38 = 0x26
[bsproc]ushell command finished
3���ڴ������ûس������ɲ鿴������Ϣ��--��ʱΪexpander�Ĵ�����Ϣ��
4. ִ��rssgetfwversion��ѯexpander�̼��汾��Ϣ��

##########################################################################################

#I8350 ���ȵ���  ��BMC shell-port24(root/root)--ushell(zte/zte)--sh 1--BSP_SetPanelUart(1)

��BMC shell-port10000(root/superuser)--ushell(zte/zte)--sh 1--BSP_SetPanelUart(1)


BSP_DbgFanTest(1)    //�رշ��ȵ��ٲ���
BSP_SetFanPwm(0xff)  //�ֶ����÷���ռ�ձȣ�����01-ff
BSP_GetFanRpm()             //��ȡ���ת��

###�����л�(BMC)
BSP_SetPanelUart(1)   //HOST UArt
BSP_SetPanelUart(0)   //BMC UArt
BSP_SetPanelUart(3)   //expander UArt --����л��������ȷ��expander�İ汾��Ϣ
uartswitch()

########################
admin��ʾ���£����� sh 1������bspproc���̣�uartswitch()���л�����host���ڡ�
/etc/grub.conf�У�����ı���initrd /initramfs-2.6.32-431.el6.x86_64.img��
֮ǰ���� console=ttyS0,115200

��һ��������
ֱ����BMC���������� sh 1
BSP_SetPanelUart(1) ,����ʵ�ִ����л�


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
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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

ʹ��gfio�ķ�����
Ӳ�̡�����������--����ʽ����mkfs.ext4  /dev/sdb1��-->���� 
mount -t ext4 /dev/sdb1 /home/test



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
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
####
BMC--OFF SPAN
HOST--IN SPAN

##��������ʽ��
parted /dev/sdb--mklabel--gpt--yes--p--mkpart--gpt4t--ext4--1��0--(-1)--P--Q (sdb/sdb1)
mkfs.ext4 /dev/sdb1

һ������ʵ�֣�parted /dev/sdb rm 1  ɾ������
һ������ʵ�֣� parted /dev/sdb mkpart gpt4t ext4 0 4000GB I
 parted /dev/sdb mkpart gpt4t ext4 0 1997GB I

һ������ʵ�֣� 
parted /dev/sdb mkpart gpt4t ext4 0 4000GB I   :4TB (�����ʾ�޷�ʶ���豸�ļ������Լ���mklabel gpt����)
parted /dev/sdb mkpart gpt4t ext4 0 2996GB I  ��3TB  (�����ʾ�޷�ʶ���豸�ļ������Լ���mklabel gpt����)
parted /dev/sdb mkpart gpt4t ext4 0 1997GB I  ��2TB  (�����ʾ�޷�ʶ���豸�ļ������Լ���mklabel gpt����)

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
service name: stor_agent  stor_cimserver


####
kdump��һ���Ƚ��Ļ���kexec���ں˱���ת�����ơ���ϵͳ����ʱ��kdumpʹ��kexec �������ڶ����ںˡ��ڶ����ں�ͨ�����������ںˣ��Ժ�С�ڴ������Բ���ת�����񡣵�һ���ں˱������ڴ��һ���ָ��ڶ��ں������á�����kdump����kexec���������ںˣ��ƹ��� BIOS�����Ե�һ���ں˵��ڴ���Ա����������ں˱���ת���ı��ʡ�kdump��Ҫ������ͬĿ�ĵ��ںˣ������ں˺Ͳ����ںˡ������ں��ǲ����ں˷���Ķ��񡣲����ں˻��������ں˱���ʱ��������������Ӧ��ramdiskһ���齨һ��΢���������Զ������ں��µ��ڴ�����ռ���ת�档ע�⣬������ʱ��kdump������һ����������Ҫ���ڴ棬Ϊ�˼���ϵͳ��Ҫ��������С�ڴ棬����kdumpʹ�õ��ڴ��������Ծ�����������С�ڴ������
Ϊ�˸��õ��ݴ����������û������� 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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
dd if=/dev/zero of=/dev/sdb  ����Ӳ�̶�дȷ������
����Ӳ��д������time dd if=/dev/zero of=/dev/sdb bs=8k count=300000  
����Ӳ�̶�������time dd if=/dev/sda of=/dev/null bs=8k count=300000
ִ�й������� iostat -x -d 2�鿴��д�� ִ�к���dmesg�鿴�Ƿ��д���


#####iostat������ȷ�����
cpu����ֵ˵����

%user��CPU�����û�ģʽ�µ�ʱ��ٷֱȡ�

%nice��CPU���ڴ�NICEֵ���û�ģʽ�µ�ʱ��ٷֱȡ�
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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
fsck/e2fsck -c  (Check for bad blocks and add them to the badblock list)
hdparm -t /dev/sda ( -t   ����Ӳ�̵Ķ�ȡЧ�ʡ�)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
hdparm -tT /dev/sda


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
1����rpm�� ����vnc �����װ 2������VNCserver, ����vncserver������������룬���ú������ļ��� /root/.vnc/xstartup  3)�رշ���ǽ 4���޸������ļ�/root/.vnc/xstartup,(# unset SESSION_MANAGER   # exec /etc/X11/xinit/xinitrc) ȥ�������е�ע�ͣ�5��vncserver -kill :1 6��vncserver :1 7����PC�˴�VNC����ʹ�á�

#### fio�������

fio -name=testc -filename=/dev/sdb -bs=64k --rw=write -iodepth=32 -runtime=80h  -direct=1 -numjobs=8 -time_based  -ioengine=libaio -thread -group_reporting=1

###��ϵͳ��ѹ������������******��--running�汾
fio -name=testc -filename=/home/tmp_io/tmp -bs=256k -rw=randrw -rwmixread=50 -iodepth=16 -direct=1 -numjobs=8 -runtime=24h -size=5G -time_based -ioengine=libaio -thread -group_reporting

####����ѹ���ͽ�ѹ
tar zcvf servertool~.tar.gz servertool~/
tar xzf  servertool~.tar.gz


####linux���̺�ִ̨������ nohup (��һ�������������е�����ͬʱ����ִ��)
nohup����������������һ�����̣�������������˳��ʻ�ʱ�ý��̻������������ô����ʹ��nohup�����������������˳��ʻ�/�ر��ն�֮�����������Ӧ�Ľ��̡�nohup���ǲ��������˼( no hang up)�� ��
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
�������һ����ʽΪ��nohup command & ����ʹ��nohup�����ύ��ҵ
 ���ʹ��nohup�����ύ��ҵ����ô��ȱʡ����¸���ҵ��������������ض���һ����Ϊnohup.out���ļ��У���������ָ��������ļ��� ����
nohup command > myout.file 2>&1 & ����
������������У�������ض���myout.file�ļ��С� ����
ʹ�� jobs �鿴���� ����
ʹ�� fg %n���رա� ����
�������������õ�ftp����ncftpget��ncftpput������ʵ�ֺ�̨��ftp�ϴ������أ������ҾͿ���������Щ�����ں�̨�ϴ��������ļ��ˡ� 

nohup *.sh &
һ�����û��ǳ���ͬʱ�������ִ�еĳ����´�ָֹͣ����� nohup ������󣬻Ὣ������������û���


####linux�����������ͻ��˲����������£�
��������mpt2sas��������
������/lib/modules/2.6.32-431.el6.x86_64/extra/·���´���mpt2sasĿ¼��pmc��Ϊ����aacraid��Ŀ¼��
Ȼ�󽫱������ɵ�mpt2sas.ko��������һ��������Ŀ¼
��3����ִ��depmod -a��
��4����ִ��modprobe mpt2sas
��5��������/bootĿ¼��ִ��mkinitrd initramfs-2.6.32-431.el6.x86_64.img 2.6.32-431.el6.x86_64 --force����ɺ�ִ��lsinitrd  initramfs-2.6.32-431.el6.x86_64.img | grep mpt2sasȷ������·����Ԥ��һ�£�Ҳ����ͨ��modinfo mpt2sas���鿴�汾��Ϣ��ȷ���������³ɹ���
��6���裬������ȷ�������汾��Ϣ����չ���ԡ�

���˷�����
1.rm -rf extra/   ɾ��extraĿ¼��
2.depmod -a
3.ִ��modinfo aacraid ���鿴����ģ���Լ����£�

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
######################igb ixgbe��������ʹ��rpm -Uvh����ʧ�ܵ�Ӧ�Բ��ԣ������²��������������������
1���鿴ϵͳ�Դ�����ģ��汾
    # modinfo ixgbe | grep version
    2����װ����������
    # rpm -Uvh ixgbe-4.2.1-1.rhel7.0.x86_64.rpm
    3��ȷ��ixgbe����ģ��汾�Ѹ���
    # modinfo ixgbe | grep version
	4. modprobe -r ixgbe
	5. modprobe -v ixgbe
	6. mkinitrd initramfs-3.10.0-123.el7.x86_64.img 3.10.0-123.el7.x86_64 --force �����ں�ӳ���ļ�
	7.ȷ���ں��������İ汾��
	   lsinitrd initramfs-3.10.0-123.el7.x86_64.img | grep -i ixgbe.ko

####�����з��֣�����������ں�ӳ���ļ�����������ethtool -i ��ѯ�����������������ϵ���������ʹ���ϵ������ļ�������Ҳû�ã���������ں�ӳ���ļ���



==>���е������У�ֻ��raid/sas�������¹������Զ�����mkinitrd �Ĳ���������Ϊ
raid/sas���������ϵ�ʱ�ͼ��أ��������޷�����raid/sas���������������������������ϵͳ������
�ټ��ظ��£�

���ۣ������ƶ���������������ں�ӳ�������������Ļ���������Ͳ����Զ�����/lib�µ��µ������汾��
�����ں�ӳ����û�е���������������Զ�����/lib�¶�Ӧ�������汾

centos7.0���ں�ӳ���ļ��У�
��igb ,ixgbe,aacraid��������
��lpfc, megaraid_sas, mpt3sas, 

redhat6.5���ں�ӳ���ļ��У�
��igb ,ixgbe������Ҳû�г���reboot�� ����������ԭΪ�����������⣬

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



####
modprobe -l| grep ���� ���鿴��ǰ���Լ��ص�ģ�飨�������Ѿ���װ��
lsmod | grep �������鿴��ǰ�Ѿ����ص�ģ��
modprobe ������    ��������
modprobe -r ������  ж������

������������ܽ�˵����
1��ʹ��modprobe -l | grep *** �鿴ϵͳ�д��ڵ�����ģ��
2��modinfo **  �鿴�����汾���������Ƿ����û��ϵ���鿴���ǵ�ǰĬ��·������������Ϣ����depmod -a ʶ���·����
2��lsmod | grep ** �鿴���ݼ��ص�����ģ��
3��modprobe -r ***  ж������
4���ӹ�������������Դ�ļ���������ixgbe-4.1.2.tar.gz
5��tar -xzf ixgbe-4.1.2.tar.gz;  cd ./src; make ,��ʱ�ڵ�ǰ·���¾���ixgbe.ko����ģ�飬��modinfo +����·�����Բ鿴�������İ汾��Ϣ��
6����������copy��/lib/modules/2.6.32-431.el6.x86_64/extra/�½���dir/�£�
7��ִ��depmod -a  ���޸������ļ�Ĭ��ʶ�������·��,����ʶ��㼶�Ƚ�ǳ������ģ�飻
8��modprobe ixgbe.ko ����������modinfo ixgbe.ko �鿴������·���Ͱ汾��Ϣ
9�����±����ں��ļ�mkinitrd initramfs-2.6.32-431.el6.x86_64.img 2.6.32-431.el6.x86_64 --force������������·�����ĵ�����������Լ��޸���һ���豸������������������Ҫ������ļ���Ļ�������Ҫ�Ժ��Ľ������·�������¼ӵ����ñ��뵽�����ڲ�ȥ��

###����rpm����ʽ���µķ�����
rpm -Uvh *.rpm


Linux��.c�ļ�����Ϊ.ko�ļ�
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 1st time
д��my.c��һ��Makefile�ļ���Ȼ��make����һ�£��ͳɹ��ˣ�����my.ko

�ټ���һ��insmod my.ko     dmesg|grep module ����ģ���ʼ��ʱ��Ĵ�ӡ

ж��ģ��rmmod my.ko  dmesg|grep module  ��ģ��ж��ʱ��Ĵ�ӡ

####grep ����˵��
 grep -v **** ���������������������ؼ��ʵ�����line
 grep -i *** ��ʾ���Դ�Сд
 grep ***ֱ�Ӱ��ؼ��ֹ���

###�رս�������
kill  PID
pkill command

###linux ���̷����������baobab

##rpm����װ��أ�
�����-i ��װ��������ʾ�������ļ���ͻ������Ҫ����һЩ�������ļ��ȵȣ�����ֹ��װ,����ʹ��
rpm -i --force --nodeps ���Ժ�������������ϵ���ļ����⣬ʲô�� 
���ܰ�װ�ϣ�������ǿ�ư�װ����������ܱ�֤��ȫ���ӹ���

##ж��rpm����rpm -e �������������԰����汾�ŵ���Ϣ�����Բ�����ȫ���������ǲ������к�׺.rpm 
���ж�ع�������ʾ���������������������Ҫ���������ж�ء���������rpm -e --nodepsǿ��ж��

##�Ѱ�װ�İ���ѯ rpm -qa | grep ***
##�Ѱ�װ�İ��İ�װ·����ѯ rpm -ql ** ����.rpm�İ�����

###������ѯ���
uname -a
lspci | grep -i lsi
rpm -qa | grep -i mpt2sas
modinfo mpt2sas
rpm -e  ***ж������
rpm -Uvh ** ��������

####Ӳ�̸�ʽ������˵��
mk2fs -t ext4 �� mkfs.ext4  ����������ͬ����


###��Կ������أ�
ssh-keygen
ssh-copy-id -i /root/.ssh/id_rsa.pub 129.0.0.77��Ҫ��½��Ŀ��������IP��
��η���error,�����������Խ��
rm -rf /root/.ssh/known_hosts


###linuxϵͳʱ��ͬ���������������
 ntpdate -u 129.0.0.50
 date -s 10:18:00


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

####PMC 6805�̼����·�������BIOS ,����ͬʱ�����ġ�
./arcconf romupdate 1 xxxx.ufi   reboot����Ч

E9000��
����129.5.101.143
��Ƭip:192.168.12.181  root/123456
E9000���п���
raid�� --S600 S620 S610
FC��--N500
����--N720


######gfio���
./confiture --enasble-gfio
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
֮ǰ���� console=ttyS0,115200   --ֻ������Ҳ����������á�

{/etc/inittab �У�����ı���id:5:initdefault:��֮������
co:2345:respawn:/sbin/agetty ttyS0 115200 vt100 init q   /for rhel
co:2345:respawn:/sbin/agetty -L 115200  ttyS0 ansi    /for SLES

/etc/securetty�У��ı��������ttyS0}

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


remark:ִ��ʱ��ʾ�����error��ע��رշ���ǽ������������ʱ�����ȼ�����ǽ��selinux�Ƿ�ر�
[root@localhost netperf-2.6.0]# netperf -H 126.0.0.61 -l 60 -t TCP_STREAM -p 10000
establish control: are you sure there is a netserver listening on 126.0.0.61 at port 10000?
establish_control could not establish the control connection from 0.0.0.0 port 0 address family AF_UNSPEC to 126.0.0.61 port 10000 address family AF_INET



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

fio -name=testc -filename=/dev/sdb1 -bs=256k --rw=write -iodepth=32 -runtime=8h  -direct=1 -numjobs=30 -time_based  -ioengine=libaio -thread -group_reporting

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
rpm -ivh **.rpm (install)
vi /etc/hardwaremonitor.conf  (����)
rpm -qa | grep hardwaremon* ����ѯ��
rpm -e linux-hardwaremon-v00.02.01-2.x86_64 ��ж�أ�
/etc/init.d/hwmd status ��ִ�У�


###dmesg:
kernel�Ὣ������Ϣ�洢��ring buffer�С����ǿ���ʱ�������鿴��Ϣ��������dmesg���鿴��������Ϣ�ౣ����/var/logĿ¼�У�����Ϊdmesg���ļ��
��򵥵ľ��ǰ�����Ľű��ŵ�crontab��ȥ��������:

cat /var/log/dmesg >>/Ŀ¼/dmesg.txt  #��dmesg����Ϣ�ض���dmesg.txt


####linux��־�ļ���
 ���½��ܵ���20��λ��/var/log/ Ŀ¼֮�µ���־�ļ�������һЩֻ���ض��汾���ã���dpkg.logֻ���ڻ���Debian��ϵͳ�п�����

/var/log/messages �� ��������ϵͳ��Ϣ������Ҳ����ϵͳ�����ڼ����־�����⣬mail��cron��daemon��kern��auth������Ҳ��¼��var/log/messages��־�С�
/var/log/dmesg �� �����ں˻�����Ϣ��kernel ring buffer������ϵͳ����ʱ��������Ļ����ʾ�����Ӳ���йص���Ϣ��������dmesg�鿴���ǡ�
/var/log/auth.log �� ����ϵͳ��Ȩ��Ϣ�������û���¼��ʹ�õ�Ȩ�޻��Ƶȡ�
/var/log/boot.log �� ����ϵͳ����ʱ����־��
/var/log/daemon.log �� ��������ϵͳ��̨�ػ�������־��Ϣ��
/var/log/dpkg.log �C ������װ��dpkg����������������־��
/var/log/kern.log �C �����ں˲�������־���������ڶ����ں�ʱ������⡣
/var/log/lastlog �� ��¼�����û��������Ϣ���ⲻ��һ��ASCII�ļ��������Ҫ��lastlog����鿴���ݡ�
/var/log/maillog /var/log/mail.log �� ��������ϵͳ���е����ʼ�����������־��Ϣ�����磬sendmail��־��Ϣ��ȫ���͵�����ļ��С�
/var/log/user.log �� ��¼���еȼ��û���Ϣ����־��
/var/log/Xorg.x.log �� ����X����־��Ϣ��
/var/log/alternatives.log �C ���������Ϣ����¼������ļ��С�
/var/log/btmp �C ��¼����ʧ�ܵ�¼��Ϣ��ʹ��last������Բ鿴btmp�ļ������磬��last -f /var/log/btmp | more����
/var/log/cups �� �漰���д�ӡ��Ϣ����־��
/var/log/anaconda.log �� �ڰ�װLinuxʱ�����а�װ��Ϣ������������ļ��С�
/var/log/yum.log �� ����ʹ��yum��װ���������Ϣ��
/var/log/cron �� ÿ��cron���̿�ʼһ������ʱ���ͻὫ�����Ϣ��¼������ļ��С�
/var/log/secure �� ������֤����Ȩ������Ϣ�����磬sshd�Ὣ������Ϣ��¼�����а���ʧ�ܵ�¼�������
/var/log/wtmp��/var/log/utmp �� ������¼��Ϣ��ʹ��wtmp�����ҳ�˭���ڵ�½����ϵͳ��˭ʹ��������ʾ����ļ�����Ϣ�ȡ�
/var/log/faillog �C �����û���¼ʧ����Ϣ�����⣬�����¼����Ҳ���¼�ڱ��ļ��С�
 ��������Log�ļ����⣬ /var/log������ϵͳ�ľ���Ӧ�ð�������һЩ��Ŀ¼��

    /var/log/httpd/��/var/log/apache2 �� ����������access_log��error_log��Ϣ��
    /var/log/lighttpd/ �� ����light HTTPD��access_log��error_log��
    /var/log/mail/ �C  �����Ŀ¼�����ʼ��������Ķ�����־��
    /var/log/prelink/ �� ����.so�ļ���prelink�޸ĵ���Ϣ��
    /var/log/audit/ �� ������ Linux audit daemon�������Ϣ��
    /var/log/samba/ �C ������samba�洢����Ϣ��
    /var/log/sa/ �� ����ÿ����sysstat������ռ���sar�ļ���
    /var/log/sssd/ �C �����ػ����̰�ȫ����

�����ֶ��浵�������Щ��־�ļ����⣬������ʹ��logrotate���ļ��ﵽһ����С���Զ�ɾ�������Գ�����vi��tail��grep��less������鿴��Щ��־�ļ��� 

##############
####����������IP ��Ϊ��ͬ�����ε�IP ��ַ��ֻ��һ�����ڣ�ȱ����pingͨ����IP��ַ��
==�����ǣ���Ҫ��һ̨������������������������ͬ���ε�IP��Ҫ�����ģ��ذ���ַ����������
{������ϵͳradhat 5.5
eth0 10.0.135.1
eth1  10.0.135.2
�������߲�����1��ȴ��PINGͨ��2��IP
��������ͨ���������л�IP�����ĸ�����ʹ���ĸ�IP
==����Ҫ��һ̨������������������������ͬ���ε�IP��Ҫ�����ģ��ذ���ַ���������
==��лл~~~���ڵ�Ŀ�ľ�����Ҫ��һ�������������л�IP��һ�����ڶ�Ӧһ��IP�����ڳ��ֵ�������ǲ����һ�����ڣ��ڶ���IPҲ��PINGͨ����ڶ�������2��IP������PING��ͨ����û�а취��������ĸ����ھͼ����ĸ�IP��
==��1�����ڳ��ֵ�������ǲ����һ�����ڣ��ڶ���IPҲ��PINGͨ�������Ҫ����Linux��arp��Ӧ�����ˣ���arp_ignore��arp_filter�Ȳ����йأ������ֻ��Ҫ����ͨ���Եģ��򵥵�ֻҪ����net.ipv4.conf.all.arp_ignore=1Ӧ�þͿ��ԡ�


2����ڶ�������2��IP������PING��ͨ����û�а취��������ĸ����ھͼ����ĸ�IP

����㿴�»�����route table�������ˣ�������Ϊ���г�ȥ�İ������˵�һ�����ڣ�eth0��������������ڵ����ߣ����а�������ȥ�ˣ����Ҫ�������ĸ�����ͨ�ĸ���Ҫ���eth0��eth1�ֹ�����·�ɡ�}

############�������ù���
����������裺
�鿴�����̣������̱�ʾ�Ѿ���ӵ��������У������̱�ʾ���Դ��������̣�
-->�ÿ����̴��������̣������ƣ����𣬳�Ա�̣�
-->�������������̻���Ϊ��ͬ�Ĵ洢������Щ�洢�����Ϊ��
         ����������״̬������������������������ʣ������Ϊ0ʱ��������������
          ��������ʱ��ѡ�������̣������þ�������������Ϣ��
-->����ӳ���ϵ(������������뵽ӳ���飬��ӳ��������������;�Ķ�Ӧ��ϵ���������Ϸ��ʾ���
�����Ͽ���һ����ӳ��Ϊһ��������������)
                (����ӳ����ľ��ΪLUN��)

��λ����ķ�����
��ϵͳ����-->ping �У��ṩ�ӿ������˿�����������Ping���ĵĹ���

############# PMC 7805 �������´���raid:
./arcconf-linux create 1 logicaldrive name raid1_test max 1 0 2 0 3
                   Ctrl-ID Create-RAID               RAID-Size RAID-Level    [Channel-device ID]
Reported Channel,Device(T:L)       : 0,28(28:0)
./arcconf-linux delete 1 logicaldrive 1
                     Ctrl-ID    Delete-RAID        LogicalDrive ID
Logical device number 0

############windows ��IOMETERʹ��˵����
1.�����ļ���������·���£���ѹ���޸��ļ������֣�ɾ�����Ĳ��֣�
2.���Բ��裺
a)Disk targets�£�ÿһ��worker��ѡ��Ҫ���Ե������̣���sda,  Ȼ��ѡ�ж���manager,����maximum disk size  (�������ļ��㣺16G=16*1024*1024*2sectors)   1sector=512Byte
b) �趨���Գ���(IO��дҪ�� ���ݿ��СΪ4K��256K��1024K���ֱ����100%˳��� 100%˳��д 100%����� 100%���д)
c)Test setup �����ò���ʱ�䣬����ȴ�ʱ��(ex:RunTime ʱ�����5����;Ramp Up Time 15s)
d)display ѡ���£�ѡ��1s ��ˢ��Ƶ��
--���Ϳ����ˣ����⣬���԰Ѳ��Ե����ݱ���Ϊ�����ļ����´ξͲ�������������ˡ�

remark:
��windows��ֱ�Ӵ�IOmeterʱ��ϵͳ����ʾΪ��ɫ��C��+ϵͳԤ�����֣��� ��ɫ��Ϊ�����̣���ʱ��windows����Դ�����У��������̴����߼��̺���ɫ��������תΪΪ��ɫ���߼��̣��Ϳ��Զ������ж�д�����ˡ�
����ǶԷ������˵�linuxϵͳʹ��iometerʱ����ע��Ҫ����ɫ�������̽��ж�д���������Ǻ�windows��ͬ�Ĳ��֡�

��һ����Ҫ׼��ʱ��ȥ����16G���ļ���֮��Ͳ���Ҫ��


#############remote execute:
ssh 129.0.0.55 "lsblk;ifconfig"
ssh 129.0.0.55 lsblk;ifconfig

##############
ESX��vSphere��ESXI������

��������vSphere����ESXI��ֻ�����ֽз����ѣ�����������VMware���������⻯��Ʒ�����̡�
Vmware ���������⻯��һ����Ʒ��ESX���ò�Ʒֻ��60����ԣ�û�йٷ��Ͽɵ���Ѱ档����Vmware��4�汾��ʱ���Ƴ���ESXI��ESXI��ESX�İ汾���ļ����������ں˵ı仯��ESXI��С������ȫ��������������˵ESXI��������������������ѵ�license�����������汾���շѰ湦������ȫһ���ġ�
��4�汾��ʼVMware��ESX��ESXi��Ʒͳ��ΪvSphere������VMware��5�汾��ʼ�Ժ�ȡ����ԭ����ESX�汾���������������Ļ�vSphere����ESXI��ֻ�����ֽз����ѡ�һ��ٷ��ĵ����Գƺ�vSphereΪ����
 
�Ƴ�                                         ESX��ESXI����ʱ��                     ESXIʱ��
Vmware ESX��60�����,û���Ͽɵ���Ѱ棩------��Vmware version 4  ESXI-----------��  version 4 vSphere-------->version 5��ȡ����ESX�汾��ֻʣESXI)     �ٷ���ESXIΪvSphere

ESX��ESXI����������� ���ں˵ı仯��  ESXI��С������ȫ����������������ѵ�licence


###############
���϶�λ��
mcelog(ֱ��ִ�У������ʾû�������yum��װ)
dmesg(ֱ��ִ��)
messages
serial
==mcelog
������Ӳ����⣨����mcelog��
mcelog �� x86 �� Linux ϵͳ���������Ӳ�������ر����ڴ��CPU����Ĺ��ߡ� ��װ��ʽ yum install mcelog ���� mcelog �鿴��־��ʽ /var/log/mcelog

##########################
PCI �豸�������
lspci | grep -i emulex
lspci -vvv -s  84:00.0
lspci -vvv -s  84:00.0

#####################emulex FC����״̬��ע��
FC����δ������ʱ��һ���̵���˸
�������ӹ��˺�һ���̵���˸
��ȷ���ӹ��˺��̵Ƴ������Ƶ���˸

#############������Ϊ�ļ��֣���̫������FC������ISCSI����
HBA����FC-HBA�����׳ƣ�����ͨ��HBA������iSCSI-HBA����RJ45�ӿڣ�
��̫���������˽ӿڵ���̫�������׳ƣ�������̫������

�Ҷ�iSCSIЭ�������ǣ�ԭ�˷�����iSCSIЭ�齫SCSI�豸����������ݷ�װ���˱�׼��TCP/IP����Ȼ��ͨ��TCP/IPЭ����д��䣬Ŀ��˴洢ͨ��iSCSIЭ�齫��׼TCP/IP�������SCSI�豸����������ݡ� 
    ���ڷ�����������˵����������ֻ��ʶ��ʹ���TCP/IP����Ҫ��SCSI�豸����������ݴ���ɱ�׼TCP/IP��������Ҫһ�������ʵ�֣��� ������������ǿ�����initiator������ڽ��ϵĲ���ϵͳ����׼��������ﲻ����initator���������Ҫ�������ذ�װ�� �磺windows2003ϵͳҪ��ͨ����֧��iSCSIЭ�飬����Ҫ��װInitiator-2.08-build3825-x86fre.exe�� ���� 
    initator�����װ����Ҫռ�÷�����CPU������SCSIЭ���װΪTCP/IPЭ�飬�����������ͷ������ļ��������� 
    ʹ��iSCSI HBA���󣬶�SCSIЭ��ķ�װ���ɶ�����iSCSI HBA��Ӳ����������ռ�÷�����CPU�����ٶԷ��������ܵ�Ӱ�졣 
    ��ˣ���׼������Ҫ����iSCSIЭ���TCP/IP������Ҫ��װinitator�����iSCSI HBA���Ĺ��ܾ����ͷŷ�����������Դ���ṩ������Ӳ������SCSIЭ���װΪTCP/IPЭ�顣
linux:scsi-target-utils-1.0.24-10.el6.x86_64.cpio
win:Initiator-2.08-build3825-x86fre.exe

############# windows2012����˯�߹��ܣ�
 powercfg /H on

#####################################
��7805Ϊ�У�˵���������·�����
windows: ϵͳ��װ�����У���U�̼��������� ϵͳ�Ѿ���װ����ϵͳ�£��豸��������ѡ��7805����������
linux��ϵͳ��װ�����У���U�����������̣�ϵͳ�Ѿ���װ����ϵͳ�£�ʹ��rpm��ʹ��rpm -Uvh�����£�

#############################suse���
suse �رշ���ǽ��
SuSEfirewall2 stop   ������Ч����

chkconfig --list | grep fire
��������������ر�setup ��init��������Ŀ���ɣ�
chkconfig --level 3 SuSEfirewall2_setup off �������ѯ���ĸ�level on �͹ر��ĸ�level��
chkconfig --level 3 SuSEfirewall2_init  off 

############################suse ��أ�
service network restart  ������������
���������ļ�Ŀ¼��/etc/sysconfig/network



###############suse zypper ��������
1�����ع���
2��mkdir /mnt/iso
   mount -o loop /dev/sr0 /mnt/iso/
3��cd /etc/zypp/repos.d/
   mv SUSE-Linux-Enterprise-Server-11-SP1\ 11.1.1-1.152.repo SUSE-Linux-Enterprise-Server-11-SP1\ 11.1.1-1.152.repobak      #��������
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
zypper refresh  #update����ʱ��ϳ� ����ʱ��ʹzypper refresh �����쳣��Ҳ���Խ��а�װ������

8)zypper install gcc*


��������������������������
#######################
BMC �ں˹���ģ�����
sh 6 -->oam
����ִ�У�uptiime  :top��ϵͳ����



bios-->shell �����У�
pci -i 84 00 00 -b
pci -b

##########################Ӳ��IO��д�������£�2015/11/28��
raid ����
write through --���ÿ���cache
write back--�ÿ���cache
һ������ʱ����Ҫ����write back�����ܣ�

һ��ֻҪ��Ӳ�����ݱȽ϶ࣨ20������ϣ�ʱ�����ſ��ܳ�Ϊƿ��

ramp time: ֻ����Ӳ���е�cache, һ������Ϊ30s����

����Ӳ�̵�cacheΪ128M

128M/ 250MB/s * 60= 30s����

�������ݿ�Ĵ�С��Ҫ������ ��fio����ʱ��ʱ�価����30min���ϣ���ΪӲ��д��ʱ�����ܻ���д����ŵ�������ŵ���ת�ٿ죬����д��ȽϿ죻�����˵�ڵ����ٶȻرȽ�����

�����Ȳⵥ�̵����ܣ��Ա�Ӳ�̵Ĺ�����ϵĲ�����

��raid�����ܣ����Բο����£�
raid 0: ��д���ǵ���*N
raid 5: ��д���ǵ���*N-1
raid 1: д���ڵ��̣� ��Ϊ���̵�*2

raid10(��0��1)��д���ܵ���0�Ĳ���


˵����
direct=1 ָ����ϵͳ���棬������ָ�ڴ�Ĳ��֣�IO��дʱ����д�뵽�ڴ��У�
ramp_time ָ����Ӳ�̵�cache���棬��Ӳ���ϴ��Ļ��棻
raid ����
write through --���ÿ���cache
write back--�ÿ���cache

####����������һЩ��Ϣ��������
5400ת�ıʼǱ�Ӳ�̣�50-90MBÿ��

7200ת��̨ʽ��Ӳ�̣�90-190MBÿ��

��еӲ�̣�һ���7200ת��̨ʽ��Ӳ����˵��ȡ110Mд��90M����ȡʱ��14ms��1ms=100000ns
ϣ���¿���3TBӲ�̵ĳ�����д�ٶȷֱ�Ϊ155.2MB/���152.3MB/��

������7200ת�Ļ�еӲ�̣�һ����170M��200M���ҡ���д�ٶ���һ���ġ�


����Ӳ��IOPS�ο�ֵ(���ݽ����ο�)��
����2,5" 10.000 rpm  SAS 113  IOPS
����2,5" 15.000 rpm SAS 156 IOPS
����3,5" 15.000 rpm SAS 146  IOPS
����
����2,5" 5.400 rpm SATA 71 IOPS
����3,5" 7.200 rpm SATA 65 IOPS
����
����3,5" 10.000 rpm U320 104 IOPS
����3,5" 15.000 rpm U320 141 IOPS
����
����3,5" 10.000 rpm FC 125 IOPS
����3,5" 15.000 rpm FC 150 IOPS
����
����3,5" 10.000 rpm FATA 119 IOPS


��д���ܣ�
RAID 0����ã������Զ���ߣ�
RAID 1�� 	

���͵�������������

д��Ҫд����

RAID 5��
����RAID 5��RAID 0

������Ƶ����ݶ�ȡ�ٶȣ�

д��RAID 5<�Ե���

���̽���д�����

������һ����żУ����Ϣд��

RAID 10��

 	

����RAID 10��RAID 0

д��RAID 10��RAID 1




######################################
############################
initrd.img��vmlinux�� vmlinuz

initrd.img��һ��С��ӳ�󣬰���һ����С��linuxϵͳ��ͨ���Ĳ������������ںˣ�Ȼ���ں˹���initrd.img����ִ������Ľű�����һ�����ظ��ָ�����ģ�飬Ȼ����������root���������ز�ִ��/sbin/init...

initrd.img��Ȼ�ǿ�ѡ���ˣ����û��initrd.img,�ں˾���ͼֱ�ӹ���root������

˵initrd.img�ļ������ᵽ����һ������---vmlinuz��vmlinuz�ǿ������ġ�ѹ�����ںˡ���vm������ ��Virtual Memory����Linux ֧�������ڴ棬�����ϵĲ���ϵͳ����DOS��640KB�ڴ�����ơ�Linux�ܹ�ʹ��Ӳ�̿ռ���Ϊ�����ڴ棬��˵�����vm�������⣺vmlinux��δѹ�����ںˣ�vmlinuz��vmlinux��ѹ���ļ���

ΪʲôҪinitrd.img

ϵͳ�ں�vmlinuz�����ص��ڴ��ʼ�ṩ�ײ�֧�֣����ں˵�֧���¸���ģ�飬����ȱ��������С�������Ȼ�Ǵ�������׽��ܵķ�ʽ��������linux�������������еġ��������Ӳ����scsi �ӿڶ�����ں��ֲ�֧�����ֽӿ�ʱ������ں˾�û�а취����Ӳ�̣���ȻҲû������Ӳ���ϵ��ļ�ϵͳ����ô�죿���ں˼���scsi����Դ��Ȼ�����±����һ���µ��ں��ļ��滻ԭ��vmlinuz��

��Ҫ�ı��׼�ں�Ĭ���ṩ֧�ֵ����ӻ��кܶ࣬���ÿ�ζ���Ҫ�����ں˾�̫�鷳�ˡ����Ժ�����linux���ṩ��һ�����ķ����������Щ����---initrd.img��initrd.img�ļ����Ǹ�ram disk��ӳ���ļ���ramdisk����һ�����ڴ�ģ��ɴ��̣��ò���ϵͳ���ʡ�ram disk�Ǳ�׼�ں��ļ���ʶ���豸(/dev/ram0)�ļ�ϵͳҲ�Ǳ�׼�ں���ʶ���ļ�ϵͳ���ں˼������ram disk��Ϊ���ļ�ϵͳ����ʼִ�����е�"ĳ���ļ�"��2.6�ں��� init�ļ��������ظ���ģ�飬����ȡ�����һЩ���ú����к󣬾Ϳ���ȥ������̼���������root�����ˣ�Ȼ������һЩ���õȣ���������ɹ���Ҳ������ֻ��Ҫ�����ʺ��Լ��� initrd.img �ļ��Ϳ����ˡ���Ҫ���ر��ں˼򵥶��ˣ�ʡʱʡ�µͷ��ա�

#############rhel ���ñ��ع���Ϊyum��װԴ�ķ�����
1�����ع�����2�� ls /dev/sr0 ȷ�Ϲ����豸���ţ�3�� mkdir /mnt/iso��4�� mount -o loop /dev/sr0 /mnt/iso��
��cd /etc/yum.repos.d/�� cp rhel-source.repo rhel-source.repobak����
5��vi rhel-source.repo��
[baseurl=file:///mnt/iso
enabled=1]

##############����ϵͳ�¿��Կ���7805�µ������̵�����
1��PMC BIOS��Ҫ����Controller mode Ϊraid:expose raw
2) ��arcconf getconfig 1 PD��ѯ�����̵�״̬��������Raw (Pass Through)�ſ��ԣ�
�����ready, ��Ҫ������arcconf uninit 1 0 1 ��״̬��ready-->raw��
����sd*�豸�оͿ��Կ����������ˡ�

 Usage: SETCONTROLLERMODE <Controller#> <Controller Mode> [nologs]
 ===================================================================================

 Change a controller's mode.

    Controller Modes  : 0  - RAID: Expose RAW
                      : 1  - Auto Volume Mode
                      : 2  - HBA Mode
                      : 3  - RAID: Hide RAW
                      : 4  - Simple Volume Mode



############################ϵͳ����������أ�
1�������������
LSI9207-8i\9217-8i   mpt2sas
LSI 1064E\1068E      mptsas
LSI SAS2008\SAS2308  mpt2sas
LSI SAS3008          mpt3sas

SAS2008      megaraid sas
LSI 9260-8i\9271-8i\9361-8i  megaraid sas
PMC6805\7805    aacraid

---����
intel 82571   e1000e
intel i350\82576\82580   igb
realtek RTL8111F   r8168
broadcom 5718   tg3

intel 82599  ixgbe
broadcom 57810s   bnx2x
intel XL710   i40e

---FC ��
emulex IOC540  lpfc

emulex lpe1250\lpe12000  lpfc
qlogic QLE2560\QLE2563   qla2***

2)rpm ����أ�

-ivh ��װ
-Uvh ����
-q �г�ָ���Ѱ�װrpm�������
-qa �г������Ѱ�װrpm�������
-qi �г�ָ���Ѱ�װrpm �������Ϣ
-qpl �г�rpm��������ļ���Ϣ
-qpi �г�rpm�������������Ϣ
-qf ��ѯָ���ļ������ĸ�rpm�����
-eɾ����

3��rpm���ݿ���أ����rpmϵͳ�������⣬���ܰ�װ�Ͳ�ѯʱ��ʹ���������������ʼ��rpm���ݿ�
rpm --initdb
rpm --rebuilddb (rebuild���̱Ƚ���)

������װ��ɺ󣬿��������������������µ�������Ҳ�����ֶ������µ�������������Ϊ����
modprobe -r igb (ж��ԭ���ں�����)
modprobe -v igb (�����°�װ������)
ethtool -i eth1 ��ѯ�µ������Ƿ���سɹ�


###############################################
/bootĿ¼��
vmlinuz*** ����kernel �ļ���kernel��Ҫ������Ǳ��š����š�CPU���ڴ棬�ɼ����Ƕ���������������Ҫ��Ӳ�����Ĳ��֣�kernel 
����������⣬ϵͳ�϶��޷���������

initrd**�� initrd��ȫ����initial ram disk����������ϵͳ������ص�������̣�

��ϵͳ���������У�kernel��initrd��system module�����μ��صġ�initrd����һ�����ں�ģ�飬��Ҫ��һЩ�ؼ����ⲿӲ������ 
SATA��SCSI��USB�����衣�����ʧ�ܵ�ȻҲ��Ӱ��ϵͳ������
��system module��Щϵͳ�е�ģ�飬����֧�ֺ������޺ܴ��ϵ��Ӳ���йأ����û����ЩӲ���豸��֧�֣�ϵͳҲ����������ɣ� 
ֻ�Ǵ��ڹ����ϵ�ȱʧ�����������������Կ��ȡ���Щϵͳģ��Ҳ��������������modprobe�ķ�ʽ����ģ��ʹ�ã�

.vmlinuz �ں��ļ�
 linux�ں������ļ���ָ/boot/vmlinuxz-* �ļ�������һ���ɽ���ϵͳ������ѹ�����ں��ļ���/boot/vmlinux ����һ����ѹ��������ں������ļ��������ļ����е�vm���������ڴ棬���ǽ�Ӳ�����⻯���ڴ���ʹ�á����ǣ�����ϵͳʹ�������ڴ�ʱ��һ���Ŀռ����ƣ����磬dos����640kb�������ڴ��С���ơ�������file�������鿴�ں��ļ�  
   file /boot/vmlinuz-*

.initrd.img ӳ���ļ�
  linux���ں�ӳ���ļ�ʱinitrd.img. ��vmlinuz�ں��ļ���ѹ֮���������ĸ��ļ�ϵͳ��/������֮ǰ��initrd.img�ļ��ᱻ���ص��ڴ��С���Ȼ�ˣ�initrd.img �ļ���ҪӦ����livecd�������Լ�ϵͳ��ʼ��������������ں�ģ��͹��ظ��ļ�ϵͳ�ȵȡ�
  ��Ϊlinux���豸������˵�Ƕ�Ӯһ���ļ���linux����Ҫʹ���Ŀ�洢�̣��Ϳ���ʹ��mount /mnt/cdrom����Ȼ�˷�ʽ�ǲ��þ�����أ������й��ء�
��ʱ���ǿ���ʹ��mkinitrd����������initrd.imgӳ���ļ�������ͨ��file.


�����ں��� Linux �ĺ��ģ����ļ�ȴ���û������ϵͳ���������õ���Ҫ���ߡ���� Linux ��˵������ˣ�������Ϊ�� UNIX ��ͳ�У���ʹ���ļ� I/O ���ƹ���Ӳ���豸�������ļ���


/bootĿ¼���ļ����ܣ�
config-2.6.22.6-1  �ǵ�ǰ�ں˵������ļ� �����ں˱���ʹ��
initrd-2.6.22.6-1.img  ��ǰ�ں˵�initrd ,����ʼ��ramdisk�ļ� �������һЩ����ʱ��Ҫ���ص������ȵ�
system.map-2.6.22.6-1 ϵͳ�豸ӳ��
vmlinzu-2.6.22.6-1 ��ǰ�ں��ļ�
memtest86+-1.65 �ڴ�������
message ����ʱ����Լ��ص�һЩ˵�� ��Ϣ֮��� û����

grubĿ¼ ������grub����������������������ļ��������ļ�ϵͳ�������ļ�

##################################################nmon ��Ϣ�ɼ��������
linux�汾�£�ʹ��nmon_linux_14i.tar.gz ��Ӧredhat�İ汾����ֱ��ʹ��nmon_x86_64_rhel6��ʹ�ò��裺
1������ִ��Ȩ�ޣ�
2���������./ nmon_x86_fedora5 �CfT �Cs 10 �Cc 120
��������ĺ����ǣ�-f����ļ���-T��������Դ�Ľ��̣�-s�ռ����ݵ�ʱ������-c�ռ�����

������ں�̨����nmon������ã�
nohup ./ nmon_x86_fedora5 �CfT �Cs 10 �Cc 120

���������ý��̣���ʹ�ã�
ps �Caef|grep *nmon*
�������ý���ID��Ȼ��ʹ�ã�
kill -9 ����ID

3��������Խ����󣬿ɵõ�*.nmon���ļ�������SSH���߻���FTP���߽����ļ����ص����ء�
4����nmon analyser v334.xls�����analysis nmon data���ļ����ɣ���ʱ��Ҫ���ú�İ�ȫ����ſ��ԣ�

###############################Ӳ��fio���ܲ��Ժ�nmon���ʹ�þ�����
./nmon_x86_64_rhel6 -fT -s 10 -c 180

write:
fio -name=testc -filename=/dev/sdb1 -ioengine=libaio -numjobs=8 -iodepth=32 --rw=write -bs=2m -time_based -runtime=30m  -direct=1 -group_reporting=1

read:
fio -name=testc -filename=/dev/sdb1 -ioengine=libaio -numjobs=8 -iodepth=32 --rw=read -bs=2m -time_based -runtime=30m  -direct=1 -group_reporting=1

randrw:
fio -name=testc -filename=/dev/sdb1 -ioengine=libaio -numjobs=8 -iodepth=32 --rw=randrw -rwmixread=50 -bs=2m -time_based -runtime=30m  -direct=1 -group_reporting=1


###################################PMC �ڲ�EPLD���ò�ѯ��أ�
�ϵ��Ҳ���7805��---����˵����
- Resolved an issue where the Adaptec by PMC RAID controller would not be discovered during boot on some 
motherboard vendors. This fix also requires additional flashing of the CPLD (version 10) through the use 
of ARCCONF command "arcconf cpld 1 flashupdate", where "1" represents the controller number that the CPLD 
will be upgraded on. Be aware that a system reboot or power off may be required after performing the CPLD 
update procedure.


����������
  1)�鿴��ǰcpld�汾(���°汾ΪVersion 10)
   ./arcconf cpld  1   version  
          //load version��ʹ�ð汾��flash version�Ǳ���İ汾��

  2������7805��cpld�汾
   ������7805�Ĺ̼���������cpld����Ϊ�̼��а��������µ�cpld�汾��

   ./arcconf  romupdate 1  xxx.UFI  

   ./arcconf cpld  1   flashupdate     //������������ȴ�CPLD���£����ܶϵ磡���������Զ��ٴ�������
                                                                        //�ϵ������1���ٲ鿴�£�load version��flash version�汾Ҫһ�£��Ҿ�Ϊ10��

###################################
####################
������ͨѶģ��PCIE��ָʾ��˵��
dell 57810  
 û���ӹ���ʱ�������ƶ�����
 �ջ���һ���̵Ƴ���
 ͨѶʱ��һ���̵Ƴ�����һ���̵ƿ�����˸
 
 LPE12000 FC����
 û���ӹ���ʱ��һ���̵Ƴ���
 ͨѶʱ��һ���̵Ƴ�����һ���Ƶƿ�����˸������˸Ƶ�ʺ��ٶ��й�
 
 ############################�����������޸�linux�������Ƶķ�����
 ������˵��Linux��ʶ������ʱ��һ�Ż���eth0���ڶ��Ų���eth1����ʱ������ʹ���������¡��������������Ϣ�ͻ�ı䣬�¿�¡���������������������ֿ��ܱ�Ϊeth1.����������ô�޸Ķ��޷��ı䣬��Ͷ�����ʹ��N̨���������HA-heartbeatʵ��ʱ��������š�

���������������Ϊ����ϵͳ�Ĺ����и��Ƶ��ļ��Ѿ���һ��������/etc/udev/rules.d/70-persistent-net.rules��ʶ�����eth0����������е�ʶ�����eth1��

���������

1.�༭/etc/udev/rules.d/70-persistent-net.rules,�ҵ���ifconfig -a�ó���MAC��ͬ��һ�У�NAME='eth1'��һ�У���������Ϊ"NAME=eth0 "��Ȼ�������һ�У�NAME='eth0'��ɾ������

vim /etc/udev/rules.d/70-persistent-net.rules

SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:0c:29:bb:41:2b", ATTR{type}=="1", KERNEL=="eth*", NAME="eth0"
�������ʱ����ִ��

==��ֱ��reboot�����������ƾ��Զ�����ˡ�

2.�༭/etc/sysconfig/network-script/ifcfg-eth0,��MAC��Ϊ��ȷ�ģ���UUIDɾ����
==���޸����������MAC�� ɾ��UUID
==��������������



########################################################
����ping��ͨ������£����ȼ��IP�� MAC
##################################################

###########################iscsi�������
���÷������ʹ���IP�� pingͨ
ȷ��iscsi�����Ѿ���װ
iscsiadm -m discovery -t sendtargets -p 126.0.0.11
iscsiadm -m node -T iqn.2099-01.cn.com.zte:usp.spr11-4c:09:b4:b0:39:fe -p 126.0.0.11:3260 �Cl
�ڴ����ȷ��initiation��iqn,Ӧ���������أ����ڴ��������ӳ���ϵ
/etc/iscsi/initiatorname.iscsi  ȷ��host��iqn name
service *** restart ���������Ϳ��Կ���ӳ��Ĵ洢�豸�ˡ�

#################### Ӳ��smart��Ϣ�鿴����
yum install sg3*
sg3_utils-1.28-5.el6.x86_64
sg�ٰ�tab���Կ����ܶ����������������о�

sg_inq /dev/sg3 --page=0xb1 ��ȡת����Ϣ
Ŀǰ������ 9000~12000:ʶ���10000
sg_map

##########################################

#########################iperfʹ��
���Ե��߳�TCP

server�ˣ�
iperf -s -p 12345 ��-i 1 -M��

client�ˣ�
iperf -c server_ip -p 12345 -i 1 -t 10  (-w 20k)

-c���ͻ���ģʽ����ӷ�����ip

-p����ӷ���˼����Ķ˿�

-i�����ô������ʱ��������λΪ��

-t�����ò��Ե�ʱ������λΪ��

-w������tcp���ڴ�С��һ����Բ������ã�Ĭ�ϼ��� 

���Զ��߳�TCP:

iperf -c server_ip -p 12345 -i 1 -t 3 -P 2 
(�����̲߳��ԣ�server�˲���)


#############################################
###megaraid 9361-8i ��������
storcli /c0 add vd type=r1 drives=14:0-1
storcli /c0 add vd type=r5 drives=10:0,1,9,10
storcli /c0/v1 del
storcli /cx set alarm=<on|off|silence> 
storcli set help | grep alarm
###unconfig bad �������
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
Linuxϵͳ�޸� 
type1:
Fsck �Cy /dev/sda1
Fsck �Cy /dev/sda2
e2fsck /dev/mapper/VolGroup-lv_root
e2fsck /dev/mapper/VolGroup-lv_swap
e2fsck /dev/mapper/VolGroup-lv_home

type 2:
error: 
fsck.ext4:Unable to resolve 'UUID-25b5bc3d-****' /dev/mapper/VolGroup-lv_home:clean,599/32997376 files,2451565/131989504 blocks  ��FAILED��

����취��
mount -o remount,rw /�س�
�༭/etc/fstab�����޷����صķ�������������ʾ���Ǹ���������һ��������#ע�͵�����һ��ֱ��ɾ����������������OK��

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
step1������root���룬Ȼ��ȷ��
step2�����롰mount -o ro /������õ�һЩ����mount����Ϣ��������ɶ�������ڻ������ף�
step3�����롰fsck -c /�������Ļ�ϻ����һЩchecking����Ϣ�������Fix<y>������ʾ��ֱ������y��ȷ�ϡ������������reboot����ʾ��
step4������reboot��س���

################################################################
#####�����̷���IO errorʱ,�Ὣͬһ�������µ�ϵͳ��Ҳ���¹���Ϊֻ�������ڶ����ݱ�������ʱֻ��ͨ��reboot������� ������ϵͳ�̷���IO error,�����ڶ������̽���fio��дʱ������γ�raid1��һ����Ա�̺�Ҳ���ܷ���ϵͳ�̵�IO error,��ʱҲ�����¹���Ϊread only��Ҳ��Ҫ����reboot;
[root@localhost ~]# dmesg |grep -i only
Write protecting the kernel read-only data: 10240k
EXT4-fs (dm-0): Remounting filesystem read-only


###########################################################

####9361
StorCLI /c0 download file=mr3108fw.rom  �̼���������
StorCLI /c0 download file=mr3108fw.rom noverchk (����Ӹ߰汾���˵��Ͱ汾����Ҫ����noverchk)
storcli /c0 add vd type=r1 drives=14:0-1
storcli /c0/v1 del
storcli /cx set alarm=<on|off|silence> 
storcli set help | grep alarm
###unconfig bad �������
��ɾ��foreign��raid����Ӧ�û��Զ����UG,���û�У�����set good����
storcli /c0 /fall show (��ʾforeign��raid��
storcli /c0 /fall del(ɾ��foreign��raid��
storcli /c0 /e14 /s4 set good 
˵������ʱֱ�Ӳ�ѯfall show,û�������̣�������set good�������ʾ������
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

strocli��ѯ������Э������
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
��������Ϣ��ȡ���
arcconf SAVESUPPORTARCHIVE


mount -o remount,rw /




#######
��ν��linux�ļ�ϵͳread-only��״���� 
�����һ����Ŀ¼���ص���ķ����ϵ�ʱ�����������umount����������ļ�ϵͳ�ܿ��ܳ�Ϊһ��read-onlyϵͳ�����ܽ����κε�д�Ͷ��Ķ�������ʾΪRead-only file system,����ʹ�����µ�������������⡣
mount -o remount,rw /

#################################################
centos7/rhel7 ����������أ�
ifconfig -a
nmcli dev show
nmcli dev status
ip addr add 129.0.0.13/8 dev ens46f0
#############################################
# ip link show                # ��ʾ����ӿ���Ϣ
# ip link set eth0 upi           # ��������
# ip link set eth0 down          # �ر�����
# ip link set eth0 promisc on      # ���������Ļ��ģʽ
# ip link set eth0 promisc offi     # �ر������Ļ��ģʽ
# ip link set eth0 txqueuelen 1200   # �����������г���
# ip link set eth0 mtu 1400        # ������������䵥Ԫ
# ip addr show                # ��ʾ����IP��Ϣ
# ip addr add 192.168.0.1/24 dev eth0 # ����eth0����IP��ַ192.168.0.1
# ip addr del 192.168.0.1/24 dev eth0 # ɾ��eth0����IP��ַ

# ip route list                 # �鿴·����Ϣ
# ip route add 192.168.4.0/24  via  192.168.0.254 dev eth0 # ����192.168.4.0���ε�����Ϊ192.168.0.254,������eth0�ӿ�
# ip route add default via  192.168.0.254  dev eth0    # ����Ĭ������Ϊ192.168.0.254
# ip route del 192.168.4.0/24      # ɾ��192.168.4.0���ε�����
# ip route del default          # ɾ��Ĭ��·��


####################################################
###############################################

������Ŀ¼��	--������������
Emulex FC		--Emulex��׼FC����������������Emulex LPe12000ϵ��FC HBA���� lpfc
Intel IGB		--Intelǧ��������������������Intel i350ǧ�������� igb
Intel IXGBE		--Intel����������������������Intel 82599���������� ixgbe
LSI RAID		--LSI RAID����������������LSI 9361 RAID����          megaraid_sas
LSI SAS3		--LSI SAS������������������������LSI SAS3008��������   mpt3sas
MGA G200		--Matrox MGA G200�Կ���������������Pilot3�����Կ���
NetXtreme II	--Broadcom NetXtreme II����������������������BCM57810����������
PMC RAID		--Adaptec RAID����������������PMC 6805\7805 RAID����    aacraid


����˵����
    kmod-elx-lpfc-10.6.144.21-1.rhel7u0.x86_64.rpm	
    --Emulex��׼FC������
    elx-lpfc-vector-map-1-1.rhel7.noarch.rpm		
    --��ѡ��������LPFC���������Ż�I/Oͨ��CPU���ؾ��⣬������Ҫѡ���Ƿ�װ

RPM����װ���裺
    ��default�ں�Ϊ������װ�������£�
    1���鿴ϵͳ�Դ�����ģ��汾
    # modinfo lpfc | grep version
    2����װ����������
    # rpm -Uvh kmod-elx-lpfc-10.6.144.21-1.rhel7u0.x86_64.rpm
    3��ȷ������ģ��汾�Ѹ���
# modinfo lpfc | grep version


����˵����
    igb-5.3.3.2-1.el7.0.x86_64.rpm	
    --Intel i350 ǧ����������������

RPM����װ���裺
    1���鿴ϵͳ�Դ�����ģ��汾
    # modinfo igb | grep version
    2����װ����������
    # rpm -Uvh igb-5.3.3.2-1.el7.0.x86_64.rpm
    3��ȷ��igb����ģ��汾�Ѹ���
    # modinfo igb | grep version


����˵����
    ixgbe-4.2.1-1.rhel7.0.x86_64.rpm	
    --Intel 82599 ������������������

RPM����װ���裺
    1���鿴ϵͳ�Դ�����ģ��汾
    # modinfo ixgbe | grep version
    2����װ����������
    # rpm -Uvh ixgbe-4.2.1-1.rhel7.0.x86_64.rpm
    3��ȷ��ixgbe����ģ��汾�Ѹ���
    # modinfo ixgbe | grep version

����˵����
    kmod-megaraid_sas-06.705.06.00_el7.0-1.x86_64.rpm	
    --LSI SAS2208 RAID����
    
RPM����װ���裺 
    ��default�ں�Ϊ������װ�������£�
    1���鿴ϵͳ�Դ�����ģ��汾
    # modinfo megaraid_sas | grep version
    2����װ����������
    # rpm -Uvh kmod-megaraid_sas-06.705.06.00_el7.0-1.x86_64.rpm
    3��ȷ������ģ��汾�Ѹ���
    # modinfo megaraid_sas | grep version

����˵����
    kmod-mpt3sas-11.00.00.00_el7.0-1.x86_64.rpm	
    --LSI SAS3008 ����������

RPM����װ���裺 
    ��default�ں�Ϊ�������£�
    1���鿴ϵͳ�Դ�����ģ��汾
    # modinfo mpt3sas | grep version
    2����װ����������
    # rpm -Uvh kmod-mpt3sas-11.00.00.00_el7.0-1.x86_64.rpm	
    3��ȷ������ģ��汾�Ѹ���
    # modinfo mpt3sas | grep version

����˵����
	xorg-x11-drv-mga-1.6.3-6.el7.x86_64.rpm
	--MGA G200�Կ���������

RPM����װ���裺
	1����װmga������
		#rpm -ivh xorg-x11-drv-mga-1.6.3-6.el7.x86_64.rpm
	
	2���޸�grub�ļ�
		#vi /etc/default/grub
	��GRUB_CMDLINE_LINUX�������mgag200.modeset=0�������ļ���ִ�����
		# grub2-mkconfig -o /boot/grub2/grub.cfg
	����ϵͳ����Ч
	
	3��ȷ�������Ƿ���سɹ����鿴xorg��־��
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

	���ִ����������󣬲鿴����LoadModule: "mga"�������ʾmga�������سɹ���������Ҫ��ִ�����²��裺
	4������xorg�����ļ�
		#Xorg -configure :1
	5���޸�xorg�����ļ�
		#vi /root/xorg.conf.new
		ȷ�� Section "Device" �е� ����Ϊmga��������ǣ��޸�Ϊmga��
		Section "Device"
		        ### Available Driver options are:-
		        ### Values: <i>: integer, <f>: float, <bool>: "True"/"False",
		        ### <string>: "String", <freq>: "<f> Hz/kHz/MHz",
		        ### <percent>: "<f>%"
		        ### [arg]: arg optional
		        #Option     "SWcursor"                  # [<bool>]
		        ��������
		        Identifier  "Card0"
		        Driver      "mga"
		        BusID       "PCI:10:0:0"
		EndSection
	
	6��ʹ���޸ĺ��xorg����
		# mv /root/xorg.conf.new /etc/X11/
	
	7����������ͼ�ν���
		#init 3
		��ִ�� 
		#init 5
	8���鿴��־ȷ��mga�������سɹ���
		# cat /var/log/Xorg.0.log | grep mga

������װ˵��
no need extra driver, use the bnx2x driver of CentOS7u0 kernel.

# modinfo bnx2x | grep version
version:        1.78.19-0
srcversion:     494067C7E7547631B3C209F
vermagic:       3.10.0-123.el7.x86_64 SMP mod_unload modversions

����˵����
    kmod-aacraid-RHEL7.0-1.2.1-41024.x86_64.rpm	
    --Adaptec RAID����������

RPM����װ���裺 
    1���鿴ϵͳ�Դ�����ģ��汾
    # modinfo aacraid | grep version
    2����װ����������
    # rpm -Uvh kmod-aacraid-RHEL7.0-1.2.1-41024.x86_64.rpm
    3��ȷ������ģ��汾�Ѹ���
    # modinfo aacraid | grep version


#########################################################
###################
centos7 yum ����˵����
��һ�����ݵ�Ŀ¼����/etc/yum.repos.d·���µ���������Դ�ļ����ŵ�����Ŀ¼�£�������Ŀ¼�ļ���CentOS-Media.repo
#CentOS-Media.repo
#
[c6-media]
name=CentOS-$releaseber - Media
baseurl=file:///mnt
gpgcheck=0
enabled=1

######################################################
linux ��ݷ�ʽ������أ�

1.�����ն�������whereis zend studio,�ҵ���ִ���ļ���
2.Ȼ����ln��������ӵ�����Ϳ����ˡ�

ͨ��ln����ʵ��
ln -s /mnt/hgfs/share/ /home/liup/����/share

linux���ҿ�ִ���ļ��ķ���
�鿴��ǰĿ¼���ļ������ͣ���ls -F
��������ls -F�����ã�
######################################################
-F���ضԿ�ִ���ļ����һ��*�ţ�ΪĿ¼���һ��/�ţ�Ϊ�����������һ��@�š�


1.�����ն�������whereis zend studio,�ҵ���ִ���ļ���
2.Ȼ����ln��������ӵ�����Ϳ����ˡ�

ͨ��ln����ʵ��
ln -s /mnt/hgfs/share/ /home/liup/����/share

linux���ҿ�ִ���ļ��ķ���
�鿴��ǰĿ¼���ļ������ͣ���ls -F
��������ls -F�����ã�

-F���ضԿ�ִ���ļ����һ��*�ţ�ΪĿ¼���һ��/�ţ�Ϊ�����������һ��@�š�



##################################7805���������ò�����
###7805:
./arcconf-linux create 1 logicaldrive max 1 0 2 0 3
./arcconf-linux delete 1 logicaldrive 1
 arcconf task start 1 device 0 7 initialize (raw-->ready
arcconf uninit 1 0 2    (ready-->raw)
arconf setstate 1 device 0 7 HSP logicaldrive 0


###################################linux Usb�������������
1. 	Write driver diskette image on USB(For example: RHEL 6.6 x86_64 iso image: aacraid-driverdisk-1.2.1-XXXXX-RHEL6.6-x86_64.iso)
2. 	Start installing the RHEL 6.x or CentOS 6.x
3. 	When the first installation screen appears, insert the USB driver disk.
4. 	Type this command at the Boot: prompt and press Enter:
		linux dd
5. 	Select Yes to indicate that you have a driver disk, then select the driver image from the USB drive
   	(typically, /dev/sda).

##########################################
SSD����Ԥ��������
######################
To zero out and condition a drive sequentially for performance testing, use the following command twice: 
Preparing the Drive 
dd if=/dev/zero of=/dev/nvme0n1 bs=1M oflag=direct  
��SSD����nand flash��ɣ�д���ط������Ȳ���������д����Щ����ʹ��û��д���������ܸܺߣ���д��һ��ʱ��������кܴ�ĵ��䣬���ڲ���SSD��д�ȶ���ʱ��Ҫ�ȶ��̽��д��˳��дһ�����飨��Ϊpre-condition��bs=1m, rw=write����
������Diskio�����е�batch.sh�ű���ָ�����pre-conditionд������
��
Ӳ�̷�������
#parted   /dev/sdx    mklabel  gpt  
һ���ȶ�����Ӳ���ȷ������ҷ�������ʼ��ַһ��Ҫ4K���룬����Ӱ������
# parted /dev/sdx  unit  kib  mkpart  primary 1024 100%  
//����ʱӲ�����пռ���һ�������£��ҷ�����ʼ��ַҪ4k����
#parted   /dev/sdx  unit  kib  print 

#####################################################
PCIE ssd������أ�
intel 400G&800G
  hgst  1.6TB&3.2TB

hgst:
ж��ԭ������
sudo rpm -qa | grep nvme-hgst
rpm --erase "name of rpm"

��װ��
rpm -ivh **.rpm
modprobe nvme-hgst
#######intel
isdct.exe show �Ca �Cintelssd 
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
���������쳣˵������
  �����󣬷���Slot 4 = KMGNP110 ΪPending״̬��������������/dev/���Ҳ���nvme0��
  ���磬���ϵ磬�տ�ʼ�Ҳ���������һ�ᣬlspci�鿴���ҵ���nvme������/dev/Ҳ�ҵ��˶�Ӧ���豸��





######################
To zero out and condition a drive sequentially for performance testing, use the following command twice: 
Preparing the Drive 
dd if=/dev/zero of=/dev/nvme0n1 bs=1M oflag=direct  
��SSD����nand flash��ɣ�д���ط������Ȳ���������д����Щ����ʹ��û��д���������ܸܺߣ���д��һ��ʱ��������кܴ�ĵ��䣬���ڲ���SSD��д�ȶ���ʱ��Ҫ�ȶ��̽��д��˳��дһ�����飨��Ϊpre-condition��bs=1m, rw=write����
������Diskio�����е�batch.sh�ű���ָ�����pre-conditionд������
��
Ӳ�̷�������
#parted   /dev/sdx    mklabel  gpt  
һ���ȶ�����Ӳ���ȷ������ҷ�������ʼ��ַһ��Ҫ4K���룬����Ӱ������
# parted /dev/sdx  unit  kib  mkpart  primary 1024 100%  
//����ʱӲ�����пռ���һ�������£��ҷ�����ʼ��ַҪ4k����
#parted   /dev/sdx  unit  kib  print 


#################################################
############################���ⱸ�ݣ�
##############linux grub�˵�֮��һֱ�����޷���������###
����������
linux ϵͳ�����󣬿��Խ���grub�˵��������������󣬻����,���Ͻ�һ�����һֱ��˸��
��������grub�˵������õ��û�ģʽ������Ҳ��һ��������

�����ж�����������ļ�ϵͳ�𻵣������������쳣�ػ���ɵģ�
����ʶ��Ӳ�̣�����MBR������
���Խ���grub�˵�������grub����������������

����Բߣ�
��BMC ��������������Ĵ����л���host�ˣ�
��1����BMC shell-port24(root/root)--ushell(zte/zte)--sh 1--BSP_SetPanelUart(1)
��2����BMC shell-port10000(root/superuser)--ushell(zte/zte)--sh 1--BSP_SetPanelUart(1)
��3��ֱ����BMC���������� sh 1 �ҵ�[BMCMGR] ������BSP_SetPanelUart(1) ,����ʵ�ִ����л�

ǰ����host��Ҳ�����˴��ڹ��ܣ����֮ǰû�п������������������grub,�༭���ò˵�����console=ttyS0,115200����������
Give root password for maintenance
(or type Control-D to continue): 

1)�������/boot����ʱ�յģ�
ʹ�����������޸�����û�ã�
Fsck �Cy /dev/sda1
Fsck �Cy /dev/sda2
e2fsck /dev/mapper/VolGroup-lv_root
e2fsck /dev/mapper/VolGroup-lv_swap
e2fsck /dev/mapper/VolGroup-lv_home

2)��ִ����������󣬸�Ϊ������������
mount -o remount,rw /�س�

3)ʹ�ù����޸��������´���/boot��������ϸ��ο��ٶ�

ʹ������3�ӷ�����û�������ظ�������һ��ʱ���������������̣��������н����ˡ�
==������ԭ���д������о����ָ��ľ���ԭ����̫�����
#################################################################
########################################
�������ʽ��ʱ��ʾ���� (ext4�ķ�������16T���޷�֧����)
[root@localhost zhl]# mkfs.ext4 /dev/sdl1
mke2fs 1.41.12 (17-May-2010)
mkfs.ext4: Size of device /dev/sdl1 too big to be expressed in 32 bits
	using a blocksize of 4096.

��/etc/mke2fs.conf�ļ���ext4������ȥ����64λ����

ext4 = {
features = has_journal,extent,huge_file,flex_bg,uninit_bg,dir_nlink,extra_isize
auto_64-bit_support = 1      ###�������У�����ϵͳʹ��64λ��ʽ���и�ʽ��������mkfs.ext4ֱ�ӱ���
inode_size = 256
}

########################################
CentOSʹ��mkfs.ext4���ٸ�ʽ��������Ӳ�̣����ٸ�ʽ�����
mkfs.ext4  -T largefile /dev/xxx

######################################
��:1 ��β鿴��ǰ��Linux�����������м���

��: ��who -r�� �� ��runlevel�� ������������鿴��ǰ��Linux�����������м���

��:2 ��β鿴Linux��Ĭ�����أ�

��: �� ��route -n�� �� ��netstat -nr�� ������ǿ��Բ鿴Ĭ�����ء�����Ĭ�ϵ�������Ϣ�����������������ʾ��ǰ��·�ɱ�

��:3 �����Linux���ؽ���ʼ���ڴ��̾����ļ���

��: ��CentOS 5.X / RHEL 5.X�У�������mkinitrd������������ʼ���ڴ����ļ����������£�

    # mkinitrd -f -v /boot/initrd-$(uname -r).img $(uname -r)

�������Ҫ���ض����ں˰汾������ʼ���ڴ��̣������������ں����滻�� ��uname -r�� ��

��CentOS 6.X / RHEL 6.X�У�����dracut������������ʼ���ڴ����ļ����������£�

    # dracut -f

���������ܸ���ǰ��ϵͳ�汾������ʼ���ڴ��̣����ض����ں˰汾�ؽ���ʼ���ڴ����ļ���ʹ���������

    # dracut -f initramfs-2.x.xx-xx.el6.x86_64.img 2.x.xx-xx.el6.x86_64

��:4 cpio������ʲô��

��: cpio���Ǹ�����͸��Ƴ�����˼��cpio������һ���鵵�ļ����򵥸��ļ��������ļ����б������Դ�����ȡ�ļ���

��:5 patch������ʲô�����ʹ�ã�

��: ����˼�壬patch��������������޸ģ��򲹶���д���ı��ļ��patch����ͨ���ǽ���diff����������ļ��ľɰ汾ת��Ϊ�°汾���ٸ����ӣ�Linux�ں�Դ�����ɰ����д����ļ����ɣ��������ۺ�ʱ���κδ��빱���߹��׳����룬ֻ�跢�͸Ķ��Ĳ��ֶ���������Դ���룬Ȼ���������patch����Ķ�д��ԭʼ��Դ�����

����һ��diff�ļ���patchʹ�ã�

    # diff -Naur old_file new_file > diff_file

���ļ������ļ�Ҫô���ǵ������ļ�Ҫô���ǰ����ļ���Ŀ¼��-r����֧��Ŀ¼���ݹ顣

һ��diff�ļ������ã����Ǿ����ھɵ��ļ��ϴ��ϲ���������������ļ���

    # patch < diff_file

��:6 aspell��ʲô�� ?

��: ����˼�壬aspell����Linux����ϵͳ�ϵ�һ���ʽƴд�������aspell��������˸����һ����Ϊispell�ĳ��򣬲�����Ϊһ��������Ʒ ������Ҫ�������ǳ����á���aspell������Ҫ������һЩ��Ҫƴд��������ĳ�����ʹ�õ�ʱ��������������Ϊһ���������еĹ��ߵ���Ҳ��ʮ����Ч��

��:7 ��δ������в鿴��SPF��¼��

��: ���ǿ�����dig�������鿴��SPF��¼���������£�

    linuxtechi@localhost:~$ dig -t TXT google.com

��:8 ���ʶ��Linuxϵͳ��ָ���ļ�(/etc/fstab)�Ĺ�������

��: 

    # rpm -qf /etc/fstab

�����������г��ṩ��/etc/fstab������ļ��İ���

��:9 �������������鿴bond0��״̬��

��: 

    cat /proc/net/bonding/bond0

��:10 Linuxϵͳ�е�/proc�ļ�ϵͳ��ʲô�ã�

��: /proc�ļ�ϵͳ��һ�������ڴ���ļ�ϵͳ����ά���Ź��ڵ�ǰ�������е��ں�״̬��Ϣ�����а���CPU���ڴ桢�������֡�I/O��ַ��ֱ���ڴ����ͨ�����������еĽ��̡�����ļ�ϵͳ������Ĳ����Ǹ���ʵ�ʴ洢��Ϣ���ļ�������ָ������ڴ������Ϣ��/proc�ļ�ϵͳ����ϵͳ�Զ�ά���ġ�

��:11 �����/usrĿ¼���ҳ���С����10MB���ļ���

��: 

    # find /usr -size +10M

��:12 �����/homeĿ¼���ҳ�120��֮ǰ���޸Ĺ����ļ���

��: 

    # find /home -mtime +120

��:13 �����/varĿ¼���ҳ�90��֮��δ�����ʹ����ļ���

��: 

    # find /var \! -atime -90

��:14 ������Ŀ¼���²����ļ���core�����緢����������ʾֱ��ɾ�����ǡ�

��:

    # find / -name core -exec rm {} \;

��:15 strings������ʲô���ã�

��: strings����������ȡ����ʾ���ı��ļ��е��ı��ַ�������LCTT ��ע��������������ϵͳ��Ī��������ֵĶ����Ƴ���ʱ�����Դ����ҵ����ɵ��ļ����ʣ�����׷���������ô���

��:16 tee ��������ʲô���� ?

��: tee ��������������Ŀ�귢��������ݡ�������ڹܵ��Ļ��������Խ��������һ�ݵ�һ���ļ�������������һ�ݵ���Ļ�ϣ���һЩ�������򣩡�

    linuxtechi@localhost:~$ ll /etc | nl | tee /tmp/ll.out

�����������У���ll������Բ��� /tmp/ll.out �ļ��У�����ͬ������Ļ����ʾ�˳�����

��:17 export PS1 = ��$LOGNAME@hostname:\$PWD: ��������������ʲô��

��: ����export�������ĵ�¼��ʾ������ʾ�û������������͵�ǰ����Ŀ¼��

��:18 ll | awk ��{print $3,��owns��,$9}�� ��������������ʲô��

��: ����ll�������ʾ��Щ�ļ����ļ��������ǵ�ӵ���ߡ�

��:19 :Linux�е�at������ʲô�ã�

��: at������������һ��������δ������һ��һ����ִ�С������ύ�����񶼱����� /var/spool/at Ŀ¼�²��ҵ���ִ��ʱ���ʱ��ͨ��atd�ػ�������ִ�С�

��:20 linux��lspci�����������ʲô��

��: lspci����������ʾ���ϵͳ��PCI���ߺ͸����豸����Ϣ��ָ��-v��-vv��-vvv����ȡԽ��Խ��ϸ�����������-r�����Ļ��������������������׶��ԡ�

###########################################################################
########################at ���
ntpdate -s 129.0.0.150

ָ�at
��ʱ����ָ��һ��ʱ��ִ��һ������ֻ��ִ��һ�Ρ�
# yum -y install at

# ps -ef | grep atd ##�鿴�Ƿ���atd
# /etc/init.d/atd start ##����atd
# chkconfig --level 2345 atd on ##����atd��������
service atd status
����ִ�н���ڣ�/var/spool/at/spool

�﷨��# at [����] [ʱ��]
at> ִ�е�ָ��
�˳�at���� ctrl+d

��ѯ��ǰ�ĵȴ����񣬱�ִ��֮��Ͳ�����ʾ
# atq

ɾ��ϵͳ����at���������ڵȴ���ִ�е�����
# atrm ����Ĺ�����
���磺# atrm 17

����������
-m ����ָ�����������֮�󣬽����û������ʼ�����ʹû�б�׼���
-I ��atq�ı���
-d ��atrm�ı���
-v ����ʾ���񽫱�ִ�е�ʱ��
-c ����ӡ��������ݵ���׼���
-V ����ʾ�汾��Ϣ
-q �������<�ж�> ʹ��ָ�����ж�
-f �������<�ļ�> ��ָ���ļ�������������Ǵӱ�׼�������
-t ������<ʱ�����> ��ʱ���������ʽ�ύҪ���е�����

ʱ�䣺�����ʲôʱ��Ҫ����at�����񣬸�ʽ�У�
1��HH:MM
˵�����ڽ��յ� HH:MM ʱ�̽��У�����ʱ���ѳ������������ HH:MM ���д�����
ex> 04:00

2��HH:MM YYYY-MM-DD
˵�����涨��ĳ��ĳ�µ�ĳһ�������ʱ�̽��и�������
ex> 04:00 2009-03-17

3��HH:MM[am|pm] [Month] [Date]
˵�����涨��ĳ��ĳ��ĳ�յ�ĳʱ�̽��и�������
ex> 04pm March 17

4��HH:MM[am|pm] + number [minutes|hours|days|weeks]
˵�����涨��ĳ��ʱ����ټӶ���ʱ���Ž��и�������
ex> now + 5 minutes
ex> 04pm + 3 days

ʱ���ʽ��չ��
at����ʹ��һ���൱���ӵ�ָ��ʱ��ķ�����
1���ܹ������ڵ����hh:mm��Сʱ:���ӣ�ʽ��ʱ��ָ���������ʱ���ѹ�ȥ����ô�ͷ��ڵڶ���ִ�С�
2���ܹ�ʹ��midnight����ҹ����noon�����磩��teatime������ʱ�䣬һ��������4�㣩�ȱȽ�ģ���Ĵ�����ָ��ʱ�䡣
3���ܹ�����12Сʱ��ʱ�ƣ�����ʱ��������AM�����磩��PM�����磩��˵�������绹�����硣
4���ܹ�ָ������ִ�еľ������ڣ�ָ����ʽΪmonth day���� �գ���mm/dd/yy����/��/�꣩��dd.mm.yy����.��.�꣩��ָ�������ڱ������ָ��ʱ��ĺ��档
5���ܹ�ʹ����Լ�ʱ����ָ����ʽΪ��now + count time-units ��now���ǵ�ǰʱ�䣬time-units��ʱ�䵥λ�������ܹ���minutes�����ӣ���hours��Сʱ����days���죩��weeks�����ڣ���count��ʱ������������죬��Сʱ��
6���ܹ�ֱ��ʹ��today�����죩��tomorrow�����죩��ָ����������ʱ�䡣

�����û���ʹ��Ȩ��
ǰ�᣺�ܶ���������ν�Ĺ����ƽ������ֵľ������ǵ�ϵͳ���ж��˺ܶ�ĺڿͳ�����Щ����ǳ���������һЩ�ƻ����������л��Ѽ����ϵͳ������Ϣ������ʱ�ķ��͸��ڿ͡����ԣ����������Ͽɵ��ʺţ������Ȳ�Ҫ������ʹ�� at ����
at����ʹ�õĿ����ļ��������û���ʹ�ÿ���
�����ļ�Ŀ¼��/etc/at.allow��/etc/at.deny
�����ļ�ʹ�ù���
1������Ѱ /etc/at.allow ����ļ���д������ļ��е�ʹ���߲���ʹ�� at ��û��������ļ��е�ʹ��������ʹ�� at (��ʹû��д�� at.deny ����);
2����� /etc/at.allow �����ڣ���Ѱ�� /etc/at.deny ����ļ�����д����� at.deny ��ʹ��������ʹ�� at ����û������� at.deny �ļ��е�ʹ���߾Ϳ���ʹ�� at ���
3����������ļ��������ڣ���ôֻ�� root ����ʹ�� at ������
4����һ��� distributions ���У����ڼ���ϵͳ�ϵ������û����ǿ����εģ� ���ϵͳͨ���ᱣ��һ���յ� /etc/at.deny �ļ�����˼������������ʹ�� at �������˼��
5�������ϣ����ĳЩʹ����ʹ�� at �Ļ������Ǹ�ʹ���ߵ��ʺ�д�� /etc/at.deny ���ɣ� һ���ʺ�дһ�С�
# vi /etc/at.allow

ע������
1�����at��ָ�������·������ ���ѽ�����ʼ�����ʽ���͸��û�
2����һ�����񴴽��˻ᱻ���䵽һ������ţ����һ���/var/spool/at�����Ŷӡ�������ʹ��vi�༭��ȥ�޸ģ����׳���

���ӣ�
ʵ��1������������ 5 ����ִ�� /bin/ls
# at 5pm + 3 days
at> /bin/ls
at> <EOT>
job 7 at 2013-01-08 17:00

ʵ��2������17���ӣ����ʱ�䵽ָ���ļ���
# at 17:20 tomorrow
at> date > /root/doiido.log
at> <EOT>
job 8 at 2013-01-06 17:20

ʵ��3���ƻ������趨����û��ִ��֮ǰ��atq�������鿴ϵͳû��ִ�й�������
# atq
8 2013-01-06 17:20 a root
7 2013-01-08 17:00 a root

ʵ��4��ɾ���Ѿ����õ�����
# atq
8 2013-01-06 17:20 a root
7 2013-01-08 17:00 a root
# atrm 7
# atq
8 2013-01-06 17:20 a root

ʵ��5����ʾ�Ѿ����õ���������
# at -c 8
#!/bin/sh
# atrun uid=0 gid=0
# mail root 0
echo "hello"
date > doiido.log

��չָ��batch
batchΪ��at���������汾����ִ�е������ռ�ô�����Դ��ʱ���ã�ֻ��cpu�������cpu����80%��ʱ��ʹ��
# batch
at> echo "hi" > /dev/tty2
batch����������Ҳ��ͨ��atq�鿴��atrmɾ�� 

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
�ֶ���������ķ������£�
����ǰ��׼����������1��װ��windows AIK��2��peimg
1�����������������
2���ҵ�����ӳ��boot..wim,���Դ�ϵͳ��װ�������ҵ����wds�������е�����D�̸�Ŀ¼��
3����BOOT.WIM���ڵ�Ŀ¼���½�һ���ļ��У�boot
4���ڰ�װWindows AIK�ļ������ִ�����imagex /mountrw d:\boot.wim 2 d:\boot
5���ɹ���ִ�����peimg /inf=x:\netdrivers\chipset.inf d:\boot\windows�����ǰ��������ص�WIM�ļ��ͷŵ�Ŀ¼�У�/inf=x:\netdrivers\chipset.inf,�Ⱥź��Ϊ����������inf�ļ����ڵ�·������
  www.2cto.com  
6���ɹ���ִ�д�����imagex /unmount /commit d:\boot��
���Ѹ��º��WIM�ļ����뵽WDS�����оͿ����ˣ�ֱ�Ӹ���ճ������ԭ����boot.wimҲ���ԣ���

#####################################################################
BMC ���ļ���������

DTF ������ftp server��·�����û���������

BMC-->HOST
ftpput -u -p ip parsesel parsesel

host --> bmc
ftpget -u -p ip parsesel parsesel

#####################################################################
###############################
iperfʹ��˵����
tar xvfz iperf-xxx.tar.gz
cd /iperf-xxx
./configure
make
make install

iperf -s

iperf -c 126.0.0.11 -i 2 -t 60 -p 5001 -P5

�ڱ����������ִ������iperf -s���ͻ��˷�����ִ��iperf -c x.x.x.x -i n1 -t n2 -p �˿ں� -P �߳�����
����x.x.x.x�������˶Խ����ڵ�IP��ַ��n1����ֵ��ʾÿ��n1���ӡһ�Σ�n2��ʾ����ʱ������Ϊ��λ��
###################################################################
################################��Ҫ����ȷ�ϣ�
suse11.3 �Ӵ����޷�ʶ���豸�����⣬
���е����ö�������Ҳ�鿴���豸�Ѿ����ӣ�����ϵͳ�¾��ǿ������豸��
���ȷ��Ϊ���˵����⣬ ��Ȼ���˵ĵ���˸������������ȷ�ϻ���������
#######################################################

SATA���ʣ�

SATA 1.0/1.0a (1.5Gb/s)      150MB/s
SATA 2.0         (3.0Gb/s)      375MB/s
SATA 3.0         (6.0Gb/s)      750MB/s

SAS���ʣ�
 SAS (V2.0/3.0: 6Gbps/12Gbps)

########################################################
linux wget���
wget ftp://192.167.5.241/BMC_SGLMA_P3_R_V01.03.63.04_201511250330.BIN --ftp-user=zte --ftp-password=zte

#######################################################
###########################################�����󶨣�
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

�󶨺��ѯ��Ϣ��
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

remark: Ĭ������£� ������Ա�����������ļ������������ü��ɣ�

���ú��ѯ��
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
�������ܲ��ԣ�MTU���
��ubuntu���޸�mtuΪ����1500��ֵ�������
sudo ifconfig eth0 mtu 9000
��ʾ��
SIOCSIFMTU: Invalid argument
�����������������⣬
�ն�������
lspci
��֪ʹ�õ�����оƬ��Intel 82573L

��intel��վ�������°�������http://downloadcenter.intel.com/ ... e&DwnldId=15817  

��ѹ���л���srcĿ¼�£�ִ��
make install
�±������ɵ�e1000e.ko����װ�� /lib/modules/'uname -r'/kernel/drivers/net/e1000e/e1000e.ko
�����±���������ɣ���ж�ص�ǰʹ�õ�����
sudo rmmod e1000e
Ȼ��װ�����ɵ�����
sudo modprobe e1000e
��������
sudo ifconfig eth0 up
����mtu
sudo ifconfig eth0 mtu 9000
����ifconfig eth0�鿴��mtu�Ѿ����óɹ���

���ˣ����Ѿ����һ���ˡ�
ubuntuϵͳ���������ں��Ѿ���õ�e1000e.ko��Ҫ��ʹϵͳ�����Զ������±�����������޸�/etc/modules��
����������������У�
-r e1000e
e1000e
��һ������ж���ں��Ѿ����ص�ģ�飬
�ڶ����Ǽ��������ɵ�ģ�顣


MTU=1500������������MAC֡����䵥λ��С��

MTU : 1500-->9000
���Ե�BW: 940Mbit/s -->990Mbit/s

########################################################################
Ϊ vsftp����vsftp: 500 oops:missing value in config file for :Allow anonymous FTP

Vsftp.conf�ļ����ô���
ע�����������ǰ�治Ҫ�ո�=��ǰ��Ҫ�пո�
=����һ��Ҫ�����ݡ�
����ע�͵���

######################################################
vsftp������أ�
�رշ���ǽ��
[root@localhost vsftpd]# iptables -L -n
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination   

�ر�selinux:
[root@localhost vsftpd]# sestatus
SELinux status:                 disabled
[root@localhost vsftpd]# getenforce
Disabled
[root@localhost vsftpd]# setenforce 0
setenforce: SELinux is disabled
[root@localhost vsftpd]# 

�޸������ļ���
�����û�������ã�
anonymous_enable=YES
anon_upload_enable=YES
anon_mkdir_write_enable=YES
#anon_other_write_enable=YES

ϵͳ�û�������ã�
local_enable=YES
write_enable=YES

��½ȷ�ϣ�
��dos������ftp ip
��ssh ������ ftp ip������

�����û��ã� ftp��anonymous ,��Ӧ��Ŀ¼Ϊ/var/ftp
�����Ŀ¼ֻ�������أ�û���޸Ļ��ϴ���Ȩ�ޣ������û����Ҫ�ϴ������Զ�pubĿ¼�����޸ģ�
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
֮��������û��Ϳ��Զ�pubĿ¼�����ϴ����޸��ˣ�

#######################################################################
######################################
��������Ӳ�̳�ʱ��ʹ��ʱ�����spindown��״̬������standby״̬�� 3������

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
�鿴���������־��
cat /var/log/secure

###################################################################

cp -n  ����negelect������Ϣ�ģ�

############################################################swap��أ�
free�鿴�ڴ��swap��Ϣ
fdisk /dev/sd* ����һ���µķ�����
ʹ��-l�鿴�������ͣ�����-t ���������������Ϊswap
mkswap /dev/sd** ���´����ķ�����ʽ��Ϊswap���ļ�ϵͳ
swapon /dev/sd** �����´�����swap����
free�鿴swap������Ϣ��

###################################################################
	1.���߼�������أ�
	����޷����ߣ���ʾnot enough free swap
	������ж�����ڵ�swap ����  swapoff -a
	�ٴ���һ�����swap �������ؼ��ɣ�
	ֱ�Ӳ��ô�����swap����׷�ӵ����е�swap�����ϣ�ȷ�ϻ����޷����ߣ�
	
	����������ã�
	��Supports wake-on: pumbg�������֧��wake on lan����wake-on: g��������˹����Ѿ��򿪣���wake-on: d�������˹��ܹرգ�����ʹ������ ��ethtool -s eth* wol g�������
	
	 Ŀǰ����I350 �������ڣ�ֻ��һ�������������ô�wol���ܣ� �������õģ�Ĭ���ǲ�֧�����绽�ѹ��ܣ�
	 
	 ���ѷ�����
	 ʹ��MAGPAC.EXE�� ѡ����ָ����������㲥��ַ����Ĭ�ϡ�255.255.255.255��������ָ��������MAC��ַ���ɣ�

############################################################################################

readme for zxusp:

1.zxusp ��������˵����
 SATAӲ��ֱ�����ӵ������ϣ���web��ȷ������Ӳ�̣��޷�ʶ�𵽣�SATA������ҪDSPAM�ӿ����ӿ�Ҳ�ǰ�װ��Ӳ�̺���
�ģ����ڴ�SATAת����SAS�ģ� ��Ϊһ�������Ĭ�Ͻ���˫ͨ�����ʵģ�
 SAS�̿���ֱ�����ӣ����Ӻ���web��ȷ��Ϊ��ʶ��Ϊ�Ǽ����̣� ��Ҫ����ushell ����ؼ��ݻ�����ſ��Ա�ɼ����̣�

������tcpmapping ����Զ��ӳ�䣺telnet ���ʣ� 10.43.167.90  port 121 ���ô洢���˰�æ����

����Ĳ������£�


 1������ ushell�� ��telnet ��������IP 10000  zte/zte, ������port23���ʺ��л���ushell��
 2������ dm ����  sh 11 ������dm��
 3������ dmDebugListAllPdIndex() �����鿴�����б�
 4��Ϊÿ�����̵��� dmDebugClearPdMda() �������Ԫ���ݣ������� Serial Number
   ���� dmDebugClearPdMda("6SJ41W950000B219B10A") ...
 5����λ���dm���̣��ٴ��ؽ�ÿ������ dmDebugInitPdMda()����ʱÿ���̶��ǿ�����

Ӧ�ò���Ҫ����
##############################################################################################

parted gpt����ѧϰ
���̹��ع��̣�
1. ����
����������
��������
sudo parted /dev/sdb mklabel gpt
sudo parted -s �� /dev/sdb mkpart primary 0 -1s
sudo parted -s �� /dev/sdb mkpart primary 0 100% 

2. mkfs
sudo blkid |grep c1d|awk -F\�� ��{print $2,$1}��|awk -F: ��{print ��sudo mkfs.ext3 -U��,$1,��&��}�� 

sudo mkfs.ext3 -u 886dfecd-478c-4520-831f-b211ad5b3247 /dev/sdb1 &
sudo mkfs.ext3 -u 1da4342e-ee15-41d4-820f-754e7c67e1b4 /dev/sdc1 &
3. fstab
vim /etc/fstab
4. mount
mount -a
һ��parted�����ʽ
Parted �����Ϊ����ģʽ��������ģʽ�ͽ���ģʽ��
1��������ģʽ�� parted [option] device [command] ,��ģʽ����ֱ�����������¶Դ��̽��з����������Ƚ��ʺϱ��Ӧ�á��磺
# parted /dev/sdb print �C��ʾ����/dev/sdb������
2������ģʽ��parted [option] device
# parted /dev/sdb      �C���뽻��ģʽ������ʹ�ý���ģʽ�������Ƕ�parted����Ǻ���Ϥ������¡�
�������õ�2�ַ�����MBR��GPT����
MBR��MBR������(����������¼)��Ҷ�����Ϥ���ǹ�ȥ����ʹ��windowsʱ���õġ�
��֧�ֵ�����2T�����ҶԷ��������ƣ����4����������3����������һ����չ����
GPT�� GPT����GUID����������Դ��EFI��׼��һ�ֽ��µĴ��̷�����ṹ�ı�׼����δ�����̷�������Ҫ��ʽ����MBR������ʽ��ȣ����������ŵ㡣
ͻ��MBR 4�����������ƣ�ÿ���������֧��128��������֧�ִ���2T�ķ���������ɴ�18EB��
����parted����ù��ܡ�
��������������parted�󣬽���parted����Ľ���ģʽ������help����ʾ������Ϣ������ͼ򵥽���һ�³��õĹ���
1��Check �򵥼���ļ�ϵͳ�������������������ļ�ϵͳ������fsck
2��Help ��ʾ������Ϣ
3��mklabel ���������� ����ʹ��msdos��MBR������ʹ��gpt��������������ʽ������
4�� mkfs �����ļ�ϵͳ�������֧��ext3 ��ʽ����˽��鲻ʹ�ã��������parted�ֺ�����Ȼ���˳�parted����ģʽ��������������з��������磺mkfs.ext3
5��mkpart �����·�����
��ʽ��mkpart PART-TYPE  [FS-TYPE]  START  END
PART-TYPE ������Ҫ��primary����������, extended����չ������, logical���߼�����. ��չ�������߼�����ֻ��msdos��
fs-type   �ļ�ϵͳ���ͣ���Ҫ��fs32��NTFS��ext2��ext3��
start end ��������ʼ�ͽ���λ�á�
6��mkpartfs �������������ļ�ϵͳ��Ŀǰ����֧��ext3�ļ�ϵͳ����˲�����ʹ�øù��ܡ�����Ƿֺ������˳�parted��Ȼ��������������ļ�ϵͳ��
7��print ���������Ϣ���ù�����3��ѡ�
free ��ʾ���̵�������Ϣ������ʾ����ʣ��ռ�
number ��ʾָ���ķ�������Ϣ
all ��ʾ���д�����Ϣ
8��resize ����ָ���ķ����Ĵ�С��Ŀǰ��ext3��ʽ֧�ֲ��Ǻܺã����Բ�����ʹ�øù��ܡ�
9��rescue �ָ���С��ɾ���ķ����������С����parted��rm����ɾ����һ����������ô����ͨ��rescue���ܽ��лָ����ָ�ʱ��Ҫ������������ʼ�ͽ�����λ�á�Ȼ��parted�ͻ��ڸ����ķ�Χ��ȥѰ�ң�����ʾ�ָ�������
10��rm ɾ�������������ʽ rm  number ���磺rm 3 ���ǽ����Ϊ3�ķ���ɾ��
11��select ѡ���豸��������parted�����ֱ�ӻس����뽻��ģʽ�ǣ�����ж��Ӳ�̣���Ҫ��select ѡ��Ҫ������Ӳ�̡��磺select /dev/sdb
12��set ���ñ�ǡ�����ָ��������ŵı�־����־ͨ�������¼��֣�boot  hidden   raid   lvm �ȡ�
boot Ϊ����������hidden Ϊ���ط�����raid ��raid��lvm Ϊ�߼�������
�磺set 3  boot  on   ���÷�����3 Ϊ��������
ע����������Ϊparted���õĹ��ܣ����ڸù���Ŀǰ��ext3֧�ֵò��Ǻܺã������Щ�����޷�Ӧ�ã�����move���ƶ���������resize�ȡ�
�ġ�parted��������������
1��������ģʽ Ϊ/dev/sdb����gpt�����ļ�������,����500G������Ȼ��Ϊ�÷�������ext3�ļ�ϵͳ�������÷���������/test�ļ����¡�
#  parted  /dev/sdb  mklabel     ������������
#  parted  /dev/sdb  mkpart  ext3  0  500000    ������500G����/dev/sdb1
# mkfs.ext3  /dev/sdb1      ��-������/dev/sdb1��ʽ����ext3��ʽ�ļ�ϵͳ
# mount  /dev/sdb1 /test   ����/dev/sdb1 ������/test��
�����ϵͳ�Զ�����/dev/sdb1 ���ֹ��༭/etc/fstab�ļ��������ļ�ĩβ����������ݣ�
/dev/sdb1             /test                ext3    defaults        0 0
2��������СΪ4G�Ľ��������������Ѿ�������500G��/dev/sdb1 ,����ٴ����ķ���Ϊ/dev/sdb2
# parted /dev/sdb mkpart swap 500000 504000  ������4G����/dev/sdb2
# mkswap  /dev/sdb2   ��-��/dev/sdb2����Ϊ��������
# swapon /dev/sdb2   ��-����/dev/sdb2
�����ϵͳ�Զ�����/dev/sdb2����������������ֹ��༭/etc/fstab�ļ��������ļ�ĩβ����������ݣ�
/dev/sdb2             swap                swap    defaults        0 0
3���ָ�����ɾ���ķ���(Ҳ���Բο�testdisk����)������partedֱ��д���̣����һ����С��ɾ����ĳһ����������������rescue�ָ�������ͨ�����������ָ����̡�
# parted /dev/sdb mkpart ext3 504000 514000 ��-����10G����/dev/sdb3
# mkfs.ext3 /dev/sdb3  ����/dev/sdb3��ʽ����ext3�ļ�ϵͳ��
# parted /dev/sdb rm 3 ��-ɾ��/dev/sdb3
# parted /dev/sdb rescue 504000 514000    ��������Ļ��ʾ������yes���ɻָ�����ɾ������
�й�Linux GPT ������һЩ������
# parted /dev/sdb
GNU Parted 1.8.1
Using /dev/sdb
Welcome to GNU Parted! Type ��help�� to view a list of commands.
(parted) select /dev/sdb
ѡ���������sdb
(parted) mklabel gpt
��MBR���̸�ʽ��ΪGPT
(parted) mkpart primary 0 100
����һ����ʼλ��Ϊ0��СΪ100M��������
(parted) mkpart primary 100 200
����һ����ʼλ��Ϊ100M��СΪ100M��������
(parted) mkpart primary 0 -1
�������пռ䵽һ������
(parted) print
��ӡ��ǰ����
(parted) quit
���ܻ����õ���һЩ����
(parted) mklable msdos
���Ҫ������.��GPT����ת��ΪMBR����
���������������,��Ҫʹ��mkfs.ext3�����и�ʽ��
#partprobe
#mkfs.ext3 -F /dev/sdb1
�ǵ�Ŷ����Ϊfdisk�ǲ�֧��GPT���̣�����ʹ��fdisk -l���鿴���̸ղŵķ�����û���õ�. ����֮�������df-h�鿴����ʹ�������
###########################################################################################################

ʹ��parted�������������Ի���������:

��Linuxϵͳ�ϵĴ��ʹ洢�����ϴ�������(����ע��ʵ�����ǶԴ������ϻ��ָ�ϵͳ��LUN������ϵͳ��ÿ��LUNʶ��Ϊһ������)�����������󳣼����⡣��һ����������ף�ʹ��fdisk����õ��Ĵ�����Ϣ�Ѿ���ʾ�˽������İ취��

    WARNING: The size of this disk is 8.0 TB (7970004230144 bytes).
    DOS partition table format can not be used on drives for volumes
    larger than (2199023255040 bytes) for 512-byte sectors. Use parted(1) and GUID 
    partition table format (GPT).

����ע�����̴�С��8TB��DOS�������ʽ�����ڳ���2TB��512���ֽڵ��������ľ���ʹ�á���ʹ��parted�����GUID�������ʽ��GPT��
���ǣ�ʹ��parted���������ϵͳ��û��parted���밲װ���ɣ�

�ڶ�������������parted�ľ��棺
    (parted) mklabel gpt
    (parted) mkpart primary 0 100%
    Warning: The resulting partition is not properly aligned for best performance.
    Ignore/Cancel?
����ע�����ɵķ���û����ȷ�ض�����ʵ��������ܡ�����/ȡ����

������ʹ��������������ϣ�����������Ϣ�����ϵس��֡��㳢��ѡ���˺��ԣ����������û�����ԡ�

������һЩ���������������ӣ����չٷ�������̳�ϵ�һ��������������������ĺ��ġ�������ע�������ᵽ�Ļ�����̳���������޷����ʣ�

��������ȷ��������Ŀ��ٷֲ�ָ�ϡ������Ǹ��������ӵ������ܽᣬϣ������ܿ������֡���������Դ����������֮��Ч��ʵ�����������������������������У����ڻ��յ������л��ᵽ�˸�����е�����ѡ���������ֻ�г���õ����á�

1.��������е�alignment�������ǵ�Ҫ��sdb�滻Ϊϵͳ�ں˿������豸���ƣ�

    # cat /sys/block/sdb/queue/optimal_io_size
    1048576
    # cat /sys/block/sdb/queue/minimum_io_size
    262144
    # cat /sys/block/sdb/alignment_offset
    0
    # cat /sys/block/sdb/queue/physical_block_size
    512

2.��optimal_io_size��ֵ��alignment_offset��ֵ��ӣ�֮�����physical_block_size��ֵ�����ҵ��������ǣ�(1048576 + 0) / 512 = 2048��

3.�����ֵ�Ƿ�����ʼ���������µ�parted����Ӧ��д��������������

mkpart primary 2048s 100%

2048s�е���ĸs�Ǻ�������ģ�������parted�����������2048������������2048�ֽڣ�Ҳ����2048���ֽڡ�

4.���һ��˳�����������ᱻ�ɹ�������û���κξ�����Ϣ��Ȼ����Ϳ��Լ������Ƿ�����ˣ����б�Ҫ���뽫���������е�1�滻Ϊ���ʵķ����ţ���

    (parted) align-check optimal 1                                            
    1 aligned

������֮ǰ��ʾ�ģ�����һЩ�������������������Щ����������Ч�����磬���optimal_io_size��0


###################################################################################################

FCIP,FCoE,iSCSI֮�������


�����������ĸ������FC, FCP, FCIP, FCoE�ȣ���Щ�������ݽ�������׻������սӴ���ʱ����ѷ����֮�����ϵ������
��SAN���統�У�Ŀǰ�Ƚ����е�����Э���Ϊ���֣�һ����FC����һ����ISCSI��������Э��������ס�FC���ȶ��Ժ����ܸߣ����ǰ�����չ����� �ϲISCSI���ˣ������Ժá���ʵ�ʵĻ�������ʱ����Ҫ�����ܺ͸���չ�ԡ����ʱ��ͺ���ȡ�ᡣ������Ʋ��ɼ���
�����������Ĵ�Ҳ������PoP��Э���е�Э�飩��Ҳ���ǽ�һ��Э����������һ��Э���С����������Ǿ�����FCIP��FCoE��������Э�鶼�ǽ�FC����Э������IP�������С��������ڣ�FCIP��FC�����Ĳ�TCP/IP����������FCoE�ڶ�������
Ҳ����FCIP�����ݽ���TCP/IP����FCoE����ֱ�ӷ�װ��֡�
���ǿ������������ڣ�FCIP����·�ɣ���FCoE���С�ֻ��ͨ��MAC��ַ���ж�λ����Զ�������ݴ����ʱ��FCIP�ǿ���ʵ�ֵģ�����FCIP�Ŀ��� Ҳ�Ǻܴ�ġ�Ч�ʲ���ܸߡ�FCoE��Ȼ����Զ�������ӣ������ڱ���LAN�п���ʵ�ֺܸߵ��ٶȡ�����ڷ�����Ӧ�������Ǻ���Ҫ�ġ����ǿ���ʹ��FCIP �������֣���FCoE�ṩ���ݷ��ʡ�
����10G�ĸ�����̫���ĳ���FCoE�����ܻ����к���������ߡ�δ����SAN�����ǲ��ǻ��LAN�����ںϣ�������Ŀ�Դ�

##########################################################################################

linux�����绽����������(wol)  

1.Ҫʹ�õĹ��߰�װ��
yum install wol
2.�÷���
wol Ŀ��mac ��ַ
3.˵����
Ŀ�����Ҫ����wol����
 linux��ʹ��ethtool�������鿴��

ethtool eth* �鿴������Ϣ


����ͼ��ʾ��eth0Ĭ��û�п���wol����
    Supports Wake-on: pumbg  //�Ƿ�֧��wol
    Wake-on: g                          //�Ƿ���wol�Լ��Ǻ���ģʽ��d ��ʾ���ã�g��ʾ��Ӧmagic packet�Ļ��ѣ�

����������eth0��wol����
ethtool -s eth0 wol g   //s��ʾ�ı��������˼


��󣬾Ϳ�����ͬһ���������ϵ����������Ϸ���magic packet����������̨�����ˡ�
��һ�㶼��дһ���򵥵Ľű������������ķ��������Ͼ�mac��ַ�ļ����ÿ�ε�������鷳��
#!/bin/bash
wol Ŀ��mac��ַ

ע�⣺���������Ĳ���Ҫʹ��root�û���

#########################################################################################

LVM related:
fdisk /dev/sdb --n--p--1--+5G--L--t (8e:linux LVM)-w
�ȴ���PV:pvcreate /dev/sdb1 /dev/sdb2
���� VG:  vgcreate myvg /dev/sdb{1,2} [--physicalextentsize PhysicalExtentSize]
vgdisplay
����LV: 
lvcreate -L 500M -n mydata myvg   ����Ҫָ����С��LV_name �����õ�VG��
lvcreate -l 100%VG -n lvdata -m0 datavg  //ʹ��vg��ȫ���ռ䴴��lv�����

lvdisplay
lvs
lsblk
�´�����LV�ķ���Ŀ¼ ll /dev/myvg/mydata  --��/dev/mapper/myvg-mydata
����������Ĳ�������������һ�������и�ʽ���͹��ؼ��ɣ�
mkfs.ext2 /dev/myvg/mydata
mount /dev/myvg/mydata /mnt
pvdisplay �����Բ鿴��ÿ��PV��ʹ�����������û��ʹ�õ�PV�����Խ����Ƴ����������£�



[root@TJC-R5300G4-12-002 myvg]# lvremove /dev/myvg/lvdata 
Do you really want to remove active logical volume myvg/lvdata? [y/n]: y
  Logical volume "lvdata" successfully removed

[root@TJC-R5300G4-12-002 myvg]# vgreduce myvg /dev/sdc1
  Removed "/dev/sdc1" from volume group "myvg"

[root@TJC-R5300G4-12-002 myvg]# vgremove myvg
  Volume group "myvg" successfully removed

[root@TJC-R5300G4-12-002 myvg]# pvs
  PV         VG     Fmt  Attr PSize   PFree
  /dev/sda2  rhel00 lvm2 a--  836.84g    0 
  /dev/sdc1         lvm2 ---    5.00g 5.00g
  /dev/sdc2         lvm2 ---    5.00g 5.00g
[root@TJC-R5300G4-12-002 myvg]# pvremove /dev/sdc1
  Labels on physical volume "/dev/sdc1" successfully wiped.
[root@TJC-R5300G4-12-002 myvg]# pvremove /dev/sdc2
  Labels on physical volume "/dev/sdc2" successfully wiped.
[root@TJC-R5300G4-12-002 myvg]# pvs
  PV         VG     Fmt  Attr PSize   PFree
  /dev/sda2  rhel00 lvm2 a--  836.84g    0 
[root@TJC-R5300G4-12-002 myvg]# 

�ȱ������ݣ�
[root@zte mnt]# pvmove /dev/sdb2
  No data to move for myvg
��VG��ɾ��PV��
[root@zte mnt]# vgreduce myvg /dev/sdb2
  Removed "/dev/sdb2" from volume group "myvg"

�����ɾ��PV
[root@zte mnt]# pvremove /dev/sdb2
  Labels on physical volume "/dev/sdb2" successfully wiped
VG��չ��
vgextend myvg /dev/sdb3  (���Զ�ƥ��PE�Ĵ�С)
LV��չ��
lvextend -L 1G /dev/myvg/mydata  ��չ�߼���1G
�ļ�ϵͳ�߽���չ ��df -lhp�鿴��
resize2fs /dev/myvg/mydata ��չ�ɺ�����ռ�һ���󣬿����ڲ�ж�ص�����½�����չ��
�ļ�ϵͳ�߽���С������Ҫ��ж�أ��������ļ�ϵͳ�ļ�⣻

����ļ�ϵͳ���

fsck:����Ԫ���ݺ����ݵ�ƥ���⣬Ҳ������ext2�ļ�ϵͳ
e2fsck:���ext2�ļ�ϵͳ����ʹ����������ܸ�ǿ��

-f ǰ�ü��  -p �Զ��޸� -y ������ѡ��ش�yes
-a == -p 

umount /mnt
e2fsck -f /dev/myvg/mydata
�߼��߽�������resize2s /dev/myvg/mydata 200M
����߽�����  lvreduce -L 200M /dev/myvg/mydata
lvs ���в鿴ȷ��
mount /dev/myvg/mydata /mnt �鿴�ڲ������Ƿ������⣻

remark:--ɾ��lv vg pv�Ĺ��̣�
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
@@@@@md�������÷�����
mdadm -C /dev/md0 -a yes -l 0 -n 2 /dev/nvme0n1 /dev/nvme1n1
�鿴��
lsblk
mdadm -D /dev/md0
cat /proc/mdstat

ɾ��raid:
mdadm -S /dev/md0    // ֹͣraid
mdadm --zero-superblock /dev/sdb5,��������������ʽҲһ����   //ɾ��Ԫ����

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
#####MD ��أ�
mdadm -S /dev/md0   //ֹͣ��raid
mdadm --assemble --scan //������֯raid


###MD with imsm
mdadm -S /dev/md0   //ֹͣ��raid
mdadm --assemble --scan //������֯raid
mdadm -I /dev/md/imsm0  //ȷ�ϲ����ã�



@@@����
mdadm --assemble --scan

mdadm --examine /dev/md/imsm0

mdadm --create --verbose --level=5 --raid-devices=3 --chunk=64 --auto=mdp /dev/md0 /dev/sd[bcd]

mdadm -C /dev/md/imsm /dev/nvme0n1 /dev/nvme1n1 -n2 -e imsm 
mdadm -C /dev/md0 /dev/md/imsm -n 2 -l 0 -c 128
@@

###MD with imsm������أ�
��Ҫ��װmdadm-3.3.2-5�����ϰ汾��mdadm, �ſ���ʹ��imsmѡ��

//����container:
mdadm -C /dev/md/imsm /dev/nvme0n1 /dev/nvme1n1 -n 2 -e imsm   
(��ʱ/dev/md/imsm -->/dev/md127, ��ʱ��imsm��md127��ֻ��container,�������յ�raid�豸����Ҫִ������Ĵ���raid���������container����һ��raid�豸���ſ�������ʹ��)
//ʹ��һ���µ�md���ƴ���raid0
mdadm -C /dev/md0 /dev/md/imsm -n 2 -l 0 -c 128

//���RSTe raid��Ϣ��
step1 : ֹͣ���е�raid containers and  volumes
mdadm --stop /dev/md0
mdadm --stop /dev/md127

step2:���superblock
mdadm --zero-superblock /dev/nvme0n1
mdadm --zero-superblock /dev/nvme1n1

step3: ȷ�� cat /proc/mdstat��û���κ���Ϣ�˼��ɣ�

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

//��ʱ���ɵ�md127ֻ��һ��container�������Խ��ж�д��
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



[root@localhost home]# mdadm -C /dev/md127 /dev/md/imsm -n 2 -l 0 -c 128   //������ʹ��md127��������raid0����Ҫʹ��һ���µ��豸����
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

//��Ϊmd127�������յ�md�豸�������޷����ж�д��
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


@@@˵�� imsm md127 md0֮��Ĺ�ϵ��
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

������ı����У�����mdadm �Ƿ��-e�����Ĳ��죺
	[root@localhost data]# mdadm -C /dev/md/imsm /dev/nvme0n1 /dev/nvme1n1 -n 2 - e imsm
mdadm: a RAID level is needed to create an array.
[root@localhost data]# rpm -qa | grep -i mdadm
mdadm-3.3.2-5.el6.x86_64
[root@localhost data]# mdadm -C /dev/md/imsm /dev/nvme0n1 /dev/nvme1n1 -n 2 -e imsm
mdadm: container /dev/md/imsm prepared.

######################################################################################

9361����raid�ռ���չ��أ�
storcli /cx/vx expand size=<value> [expandarray]  storcli /c0 /v0 expand size=100GB expandarray  (100GΪ����)
storcli /cx/vx|vall show expansion      storcli /c0 /v0 show expansion  ��ѯ��Ϣ�У�ֻ��OCE ΪYESʱ�ſ���ִ����չ
raid��С��������Ҫ���¹��غ�ϵͳ�²ſ���ʶ�𵽵������raid������
#######################################################################################

�����ϱ���� partprobe �� partx ���ִ�к��� cat /proc/parttion��ѯ�����
[root@localhost ~]# partprobe /dev/sdb
Warning: WARNING: the kernel failed to re-read the partition table on /dev/sdb (Device or resource busy).  As a result, it may not reflect all of your changes until after reboot.
[root@localhost ~]# partx /dev/sdb
# 1:        63- 10506509 ( 10506447 sectors,   5379 MB)
# 2:  10506510- 21013019 ( 10506510 sectors,   5379 MB)
# 3:         0-       -1 (        0 sectors,      0 MB)
# 4:         0-       -1 (        0 sectors,      0 MB)

##########################################################################################
SAS3008 -R5300 12 ���¹�Ӳ�̵�ʶ�𷽷���
�ܽ᣺
SAS�̵�WWN�ž���SAS��ַ����ȫ��Ψһ�ı�ʶ��
SATA�̽���ϵͳ�У���ѯ����SAS��ַ��expander���пڵĵ�ַ������SATA����ĵ�ַ,һ��Ϊ**01��**02..��
��SAS��ַ�����һλ�Ͳ�λ����ͬ����SASЭ���SATA�̵�Э�������⣻
8�̵Ļ�����SATA�̣���Ҫ��ȷ����

SATA �̣�
[root@localhost bin]# diskman -i /dev/sdb
WWN(ata address)       : 5000cca243c4169b
Sas3ircu 0 display:
SAS Address                             : 50019c6-0-0000-0001
GUID                                    : 5000cca243c4169b
[root@localhost bin]# sudo ls -l /dev/disk/by-id
lrwxrwxrwx. 1 root root  9 Oct 21 14:19 wwn-0x5000cca243c4169b -> ../../sdb

SAS�̣�
[root@localhost ~]# diskman -i /dev/sdd
WWN(sas address)          : 5000039678026872
SAS3ircu 0 display:
SAS Address                             : 5000039-6-7802-6872
  GUID                                    : 5000039678026871
Ls �Cls  /dev/disk/by-id
lrwxrwxrwx 1 root root  9 Apr 20  2016 wwn-0x5000039678026871 -> ../../sdd

SAS3008������raid�������
  Volume wwid                             : 0825cbe1673b777f
lrwxrwxrwx 1 root root  9 Apr 20 07:45 wwn-0x600508e0000000007f773b67e1cb2508 -> ../../sde

###############################################################################################
#############################################AL13SXB60EN ����һ�����ȡʱ�ᷢ������
Ӳ�����ⱸע��
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

[root@localhost bin]# diskman -s /dev/sdd    �����������
Permanent defect  (p-list): 572
Grown defect list (g-list): 0

Smart Status(ASC/ASCQ)    : 0x0/0x0 

UncorrectedWriteErr       : 0
UncorrectedReadErr        : 6    (��6�����ɻָ��Ķ����󣬿�������дһ����Щ�������������ָܻ�)
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
��ѯrpm ���İ�װ·����
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
rpm ������ܣ�
rpm -ql | grep "***"
rpm -e ***ж�����

����rpm����ʽ���µķ�����
rpm -Uvh *.rpm

##rpm����װ��أ�
�����-i ��װ��������ʾ�������ļ���ͻ������Ҫ����һЩ�������ļ��ȵȣ�����ֹ��װ,����ʹ��
rpm -i --force --nodeps ���Ժ�������������ϵ���ļ����⣬ʲô�� 
���ܰ�װ�ϣ�������ǿ�ư�װ����������ܱ�֤��ȫ���ӹ���

rpm -qa | grep hardwaremon* ����ѯ��

2)rpm ����أ�

-ivh ��װ
-Uvh ����
-q �г�ָ���Ѱ�װrpm�������
-qa �г������Ѱ�װrpm�������
-qi �г�ָ���Ѱ�װrpm �������Ϣ
-qpl �г�rpm��������ļ���Ϣ
-qpi �г�rpm�������������Ϣ
-qf ��ѯָ���ļ������ĸ�rpm�����
-eɾ����

��ѯ��װ·����
scli-1.7.2-7.i386.rpm 
rpm -ql scli
###########################################################
######lspci ��ѯ����Ϣȷ�ϣ�
		LnkCap:	Port #2, Speed 5GT/s, Width x4, ASPM L0s L1, Exit Latency L0s <4us, L1 <32us  --�豸֧�ֵ�����---��ʾ���ǵ�ǰ�豸֧�ֵ�����
		LnkSta:	Speed 5GT/s, Width x4, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-      --Э�̺������-----��ʾ���ǵ�ǰ�豸link��״̬
		LnkCtl2: Target Link Speed: 5GT/s, EnterCompliance- SpeedDis-                               --pcie slot֧�ֵ�����---LCTL2��Link Control 2 Register  ���Ƶ�ǰ��·״̬�ļĴ���
  
LnkCap--�豸��link�����Ĵ���--��ʾ�豸��link����
LnkCtl--�豸��link���ƼĴ���--���ڿ����豸������һ��link״̬
LnkSta--�豸��link״̬�Ĵ���--��ʾ��ǰ�豸link����ʲô��·״̬

##############################################################
 �鿴 SELinux״̬���ر�SELinux 

�鿴SELinux״̬��

1��/usr/sbin/sestatus -v      ##���SELinux status����Ϊenabled��Ϊ����״̬

SELinux status:                 enabled

2��getenforce                 ##Ҳ���������������

�ر�SELinux��

1����ʱ�رգ�����������������

setenforce 0                  ##����SELinux ��Ϊpermissiveģʽ

                              ##setenforce 1 ����SELinux ��Ϊenforcingģʽ

2���޸������ļ���Ҫ����������

�޸�/etc/selinux/config �ļ�

��SELINUX=enforcing��ΪSELINUX=disabled

������������
###############################################################

SATA HDD���ܲο���
����֧���ᵽ�ģ�2.5   110~130����  3.5 180~200����

#################################################################
################alias ��أ�
alias
vi /etc/profile
���ĵ������ϣ� alias ss='service network restart'
. /etc/profile   ���������ļ��б���
��ִ��alias���Բ鿴���ն���ı�����

�������¿�ݼ���
ctrl +a �л�������
ctrt+e �л�����β
ctrl+k ɾ�����������
ctrt+u ɾ�����ǰ������

##########################vi�༭���
ɾ����ǰ�е���β��
  ����ģʽ��dG
ĩ��ģʽ��:.,$d

������ģʽ�£�
��o�ڵ�ǰ�����½�һ��
��O �ڵ�ǰ����һ���½�һ��
��u����������
��h:����һλ  j:����һλ k:����һλ l:����һλ
1.���������ƶ���꣺

    h����    l����    k����    j����

2.ɾ��һ�У�dd

3.ɾ��һ���ַ���x

4.ɾ��һ�����з���J

5.�ڹ���·��½�һ�У����ҽ������ģʽ��o��Сд��ĸo��

6.�ڹ���Ϸ��½�һ�У����ҽ������ģʽ��O����д��ĸO��

7.����ƶ�����һ���ʵĴ��ף�w

8.����ƶ���ǰһ���ʵĴ��ף�b

9.����ƶ�����һ���ʵĴ�β��e

10.����ƶ���ǰһ���ʵĴ�β��ge

11.�ƶ�����ǰ�е�һ���ַ���0������0��

12.�ƶ�����ǰ�еĵ�һ���ǿ��ַ���^

13.�ƶ�����ǰ�е���β��$

14.�ƶ��������е�ָ���ַ���fc��c����Ҫ�ҵ�������ַ���

15.�����ƶ��������е�ָ���ַ���Fc��c����Ҫ�ҵ�������ַ���

16.�����ƶ��������е�ָ���ַ���tc��c����Ҫ�ҵ�������ַ���

17.����ƥ�䣺%    

    �����Ҫ����һ�£�����������һ�У���a + b�� �� c�����赱ǰ����������ţ��ϣ�����ͨģʽ������%����ͻ�ʹ����Զ���ת�������ţ��ϡ�

18.�ƶ���ָ���У�30G��30�����кţ�

19.�ƶ����ļ�ĩβ��G

20.�ƶ����ļ�ͷ��gg����1G

21.��λ���ļ���λ�õİٷ�֮���٣�30%��30����Ҫ��λ�ı�����

22.�ƶ�����ǰ��һ��Ļ�Ŀ�ͷ��H��H����Head����˼��

23.�ƶ�����ǰ��һ��Ļ���м䣺M��M����Middle����˼��

24.�ƶ�����ǰ��һ��Ļ��ĩβ��L��L����Last����˼��

25.����Ļ�����ƶ�����Ļ��ctrl+U

26.����Ļ�����ƶ�����Ļ��ctrl+D

27.��ǰ����һ��Ļ��ctrl+F

28.�������һ��Ļ��ctrl+B

29.����������й�������ǰ��Ļ������zt

30.����������й�������ǰ��Ļ�ײ���zb

31.����������й�������ǰ��Ļ�в���zz

32.����undo�ϴβ�����u

33.����redo�ϴβ�����ctrl+R
############################################################
######viĩ��ģʽ��
��set nu   :set nonu
u#������һ������
/Fedora#����Fedora�ַ�
:s /Fedora/Redhat #��Fedora�ַ��滻ΪRedhat(ֻ�滻�ڹ�����ڵ���)
:1,.s/redhat/fedora
#.�ű�ʾ��ǰ��,�����������
#����1�е���ǰ��(.)��һ�γ��ֵ�redhat�ַ�����Ϊfedora
:1,.s/redhat/fedora/g
#����1�е���ǰ��(.)���г��ֵ�redhat�ַ�����Ϊfedora,gȫ�ֱ�־
:1,$s/redhat/fedora/g
#$��ʾ���һ��
#����1�е����һ�����г��ֵ�redhat�ַ�����Ϊfedora
:%s/redhat/fedora/g
#ͬ��һ������

##########################################################
##################Ӳ�����˵����
����ȫ��洢����(HGST)
1: WD 2: SEAGATE 3: HGST    WD��HGST 2011��ϲ����ϲ��������ռ��ȫ��HDD�г���48%.

HDD:��WD��hgst��seagate��toshiba
ssd: intel��hgst������

toshiba: 
2.5INCH---AL13SEB(10K,512n,64MB,SAS2)/AL13SXB(15K,512n,64MB,SAS2)
          /AL14SEB(10K,(512n/512e/4kn),128MB,SAS3)
3.5INCH--MG03ACA(SATA,7.2K,512n,64MB)/MG03SCA(SAS,7.2K,512n,64MB)
     /MG04ACA(SATA,7.2K,512e,128MB)/MG04SCA(SAS,7.2K,(512e,4kn),128MB)

wd:WD****
hgst:HUC**/HUA**/HTE**/HUS**
seagate:ST**
####################################################
#######################kick start install�������########
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
#########dd����ʵ��ϵͳ����ȫcopy������#####
dd if=/dev/sdb of=/dev/sdc �������̵ķ�����Ϣ���£�
��ʹ��sdc��Ϊϵͳ��ʱ����Ҫ����2308 BIOS���ò˵�������sdcΪ�������̿��Գɹ�������


   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1   *           1          64      512000   83  Linux
Partition 1 does not end on cylinder boundary.
/dev/sdb2              64       72841   584582144   8e  Linux LVM




   Device Boot      Start         End      Blocks   Id  System
/dev/sdc1   *           1          64      512000   83  Linux
Partition 1 does not end on cylinder boundary.
/dev/sdc2              64       72841   584582144   8e  Linux LVM

######################################################################################
#########dd����ʵ��ϵͳ����ȫcopy������#####
dd if=/dev/sdb of=/dev/sdc �������̵ķ�����Ϣ���£�
��ʹ��sdc��Ϊϵͳ��ʱ����Ҫ����2308 BIOS���ò˵�������sdcΪ�������̿��Գɹ�������
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

type2: 600G��ϵͳ��--��300G���ϣ��鵽�������̵ķ�������Ϣ��ȫһ����
����300G�������ļ�ϵͳ�����޷�����������
time dd if=/dev/sdb of=/dev/sdc bs=256k iflag=direct
dd: writing `/dev/sdc': No space left on device
300000000000 bytes (300 GB) copied, 2015.96 s, 149 MB/s

type3:600G��ϵͳ��--��900G����,���ƺ������̵ķ�������Ϣ��ȫһ��
time dd if=/dev/sdd of=/dev/sdb bs=256k iflag=direct
600127266816 bytes (600 GB) copied, 3682.71 s, 163 MB/s

##########################################################

#####################������ع��ߣ�
[root@localhost home]# mii-tool eth2
eth2: negotiated 100baseTx-FD, link ok
[root@localhost home]# ethtool eth2  �����Բ鵽���ʼ�����״̬������û��Э�̵����ʣ�
	Link detected: yes
#############################Linux netstat�������
Netstat ����������ʾ�������������Ϣ�����������ӣ�·�ɱ��ӿ�״̬ (Interface Statistics)��masquerade ���ӣ��ಥ��Ա (Multicast Memberships) �ȵȣ�
�г����ж˿� (����������δ������)��
�г����ж˿� netstat -a      �г����� tcp �˿� netstat -at     �г����� udp �˿� netstat -au
�г����д��ڼ���״̬�� Sockets��
  ֻ��ʾ�����˿� netstat -l   ֻ�г����м��� tcp �˿� netstat -lt ֻ�г����м��� udp �˿� netstat -lu

��ʾÿ��Э���ͳ����Ϣ��
��ʾ���ж˿ڵ�ͳ����Ϣ netstat -s    ��ʾ TCP �� UDP �˿ڵ�ͳ����Ϣ netstat -st �� -su

�� netstat �������ʾ PID �ͽ������� netstat -p
netstat -p ��������������һ��ʹ�ã��Ϳ������ ��PID/�������ơ� �� netstat ����У����� debugging ��ʱ����Ժܷ���ķ����ض��˿����еĳ���

�� netstat ����в���ʾ�������˿ں��û��� (host, port or user)
���㲻�����������˿ں��û�����ʾ��ʹ�� netstat -n������ʹ�����ִ�����Щ���ơ�
������� netstat ��Ϣ   netstat -c
��ʾ����·����Ϣ netstat -r
 �ҳ��������еĶ˿� netstat -ap | grep ssh
�ҳ�������ָ���˿ڵĽ���  netstat -an | grep ����80��
��ʾ����ӿ��б� netstat -i
��ʾ��ϸ��Ϣ������ ifconfig ʹ�� netstat -ie:
IP��TCP����:
�鿴����ĳ����˿����ĵ�IP��ַ
netstat -nat | grep "192.168.1.15:22" |awk '{print $5}'|awk -F: '{print $1}'|sort|uniq -c|sort -nr|head -20
TCP����״̬�б�:
netstat -nat |awk '{print $6}'
�Ȱ�״̬ȫ��ȡ����,Ȼ��ʹ��uniq -cͳ�ƣ�֮���ٽ�������
netstat -nat |awk '{print $6}'|sort|uniq -c
netstat -nat |awk '{print $6}'|sort|uniq -c|sort -rn
####################################lsof
lsof(list open files)��һ���г���ǰϵͳ���ļ��Ĺ��ߡ���linux�����£��κ����ﶼ���ļ�����ʽ���ڣ�ͨ���ļ����������Է��ʳ������ݣ������Է����������Ӻ�Ӳ���������紫�����Э�� (TCP) ���û����ݱ�Э�� (UDP) �׽��ֵȣ�ϵͳ�ں�̨��Ϊ��Ӧ�ó��������һ���ļ�����������������ļ��ı�����Σ����ļ�������ΪӦ�ó������������ϵͳ֮��Ľ����ṩ��ͨ�ýӿڡ���ΪӦ�ó�����ļ����������б��ṩ�˴����������Ӧ�ó��������Ϣ�����ͨ��lsof�����ܹ��鿴����б��ϵͳ����Լ��Ŵ��Ǻ��а����ġ�


##################################################################################tee����

ifconfig | tee /home/aa.out

###############################################################################
fio��д����˵����
fio -name=testc -directory=/home/test -ioengine=sync -numjobs=8 -iodepth=32 --rw=read -bs=256k -size=500M -runtime=30m -direct=1 -group_reporting=1

fio -name=testc -filename=/dev/sdb -ioengine=libaio -numjobs=8 -iodepth=32 --rw=read -bs=4k -time_based -runtime=30m  -direct=1 -group_reporting=1


˵����
-directory=/home/test ��Ŀ¼��д�� Ҫ�ȴ��� testĿ¼���������ļ���
-filename=/dev/sdb  ���豸���ж�д��

 -size=500M -runtime=30m ����������ͬʱ����ʱ����С��Ϊ׼�����������500M��ʱ��С��30m,�Զ���500M��ʱ��Ϊ׼��


fio -name=testc -directory=/home/test -ioengine=sync -numjobs=8 -iodepth=32 --rw=read -bs=256k -size=500M -time_based -runtime=30m -direct=1 -group_reporting=1


-size=500M -time_based -runtime=30m �� ���������������ͬʱ���ڣ���д�Ĵ�С����500M������ʱ��Ϊ׼����500M��д���ˣ���û��30m,��Ҫ�ظ���ȡ���500M�Ŀռ䣻
###################################################################################
########################��׼���������
�������Ĭ��ָ��ǰ�Ĳ����նˣ�

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

ls -l > aa  ��������ض���
ls -l >> aa  ׷������ض���

###ȷ�ϱ�׼�������
tail -f /var/log/messages > aa
ctrl+z //��������𵽺�̨
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

###stdin�ض�����������Щ��֧��ִ�в����ļ������
[root@localhost ~]# tr 'a-z' 'A-Z' /etc/passwd   //NG
tr: extra operand `/etc/passwd'
Try `tr --help' for more information.

tr 'a-z' 'A-Z' < /etc/passwd  // ok


mail -s 'root to hello'  root < /etc/passwd �����ʼ�
ִ��mail ����ҵ�ָ�����ʼ�����������Ӧ�����־Ϳ��Բ鿴��


ls -l /etc/passwd /etc/sadfaf 1>aa 2>bb  //��������ֱ�λ����ͬ���ļ��У�
ls -l /etc/passwd /etc/sadfaf &>aa  //ʹ��&&���Ž�stdout ��stderrout��λ����ͬ���ļ��У�
ls -l /etc/passwd /etc/sadfaf &>>aa  //ʹ��&&���Ž�stdout ��stderrout��λ����ͬ���ļ���(׷�Ӳ�����)

##### <<���������ֹ���������Ҫ�ֶ���ctrl+D ��������

[root@localhost ~]# cat << END    //ʹ�������ֹ��������������򵽱�׼���
> 1111111111
> 22222222222
> END
1111111111
22222222222


[root@localhost ~]# cat << END >aa  //ʹ�������ֹ����������������ļ���
> 1111111111111
> 222222222222
> END
[root@localhost ~]# cat aa
1111111111111
222222222222


###�ܵ���� �Ὣǰһ�������stdout(������stderrout) ��Ϊ�ڶ��������stdin��
�����һ��������stderrout,Ϊ��ֹ���ţ��������� 2>/dev/null�� stderrout���˵�
ls -l /etc/passwd /etc/aaa | grep a

##�������֧�ֹܵ�������Ҫ����xargs���

[root@localhost ~]# which find | rpm -qf
rpm: no arguments given for query
[root@localhost ~]# which find | xargs rpm -qf
findutils-4.4.2-6.el6.x86_64
[root@localhost ~]# 


##ʹ�ùܵ�ʱ���ļ���λ����Ĳ鿴��
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
###############7805 �²鿴expander ��Ϣ����phy ��Ϣ��
ִ��arcconf getconfig 1 pd ����ѯexpander��Ϣ��
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

##arcconf smp  1  0 DR 0 //12�̻���Ϊ��0-11
##arcconf smp  1  0 rpelr 0  //12�̻���Ϊ��0-11

################################################################
#############################linux �����������÷�����
redhat : ������׷�ӵ� /etc/rc.local �ļ������
suse: ������׷�ӵ� /etc/rc.d/after.local�ļ������
 ��������ļ������ڣ����Լ�����һ��
###################################################

#######################################################################################################
windows �´���������������̵�ϵͳ�¿�ʶ����̣�diskpart���߽���˵������
DISKPART> list disk

  ���� ###  ״̬           ��С     ����     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  ���� 0    ����              279 GB      0 B
* ���� 1    �ѻ�              557 GB   557 GB

DISKPART> select disk 1

���� 1 ��������ѡ���̡�

DISKPART> online disk

DiskPart �ɹ�ʹ��ѡ����������

DISKPART> list disk

  ���� ###  ״̬           ��С     ����     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  ���� 0    ����              279 GB      0 B
* ���� 1    ����              557 GB   557 GB

DISKPART> clean

DiskPart �ɹ�������˴��̡�

DISKPART> create volume simple

ָ���Ĵ��̲��Ƕ�̬�ġ�
��ָ��һ����̬���̣�Ȼ������һ�Ρ�


DISKPART> convert dynamic                    // ��һ��ȷ��ʱ������߿�ס�ˣ����˼��ζ�û�гɹ�������ȷ���ǵ�ǰ�Ĳ����̷����˱������list diskȷ���µ�ǰ�����̵���Ϣ���ɣ�

DiskPart �ѽ���ѡ���̳ɹ���ת����Ϊ��̬��ʽ��


DISKPART> create volume simple

DiskPart �ɹ��ش����˾�


DISKPART> assign letter=E

DiskPart �ɹ��ط������������Ż�װ�ص㡣

DISKPART> format fs=ntfs label="new volume" quick

  100 �ٷֱ������

DiskPart �ɹ���ʽ���þ�

��ʱ��ϵͳ�¾Ϳ��Կ��������豸�ˣ�

ִ��list volume,�鿴���´����ľ�Ϊ ��new volume��
DISKPART> list volume

  �� ###      LTR  ��ǩ         FS     ����        ��С     ״̬       ��Ϣ
  ----------  ---  -----------  -----  ----------  -------  ---------  --------
  ��     0         ϵͳ����         NTFS   ���̷���         350 MB  ����
 ϵͳ
  ��     1     C                NTFS   ���̷���         279 GB  ����         ��
��
* ��     2     E   new volume   NTFS   ��           557 GB  ����

ִ��list disk,��ѯ����Ϣ���ص��豸����

DISKPART> list disk

  ���� ###  ״̬           ��С     ����     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  ���� 0    ����              279 GB      0 B
* ���� 1    ����              557 GB      0 B   *

############################################################################################

dos�µ��ַ�����������
ipconfig /all | findstr "DNS "

##########################################################
pcie ssd��ȡ�¶ȣ�
isdct dump -intelssd 0 datatype=nvmelog logid=197 | grep -i current
hdm generate-report --path=/dev/nvme1 | grep -i tempe


########################################################burnin test ʹ��˵����
��Ҫ�������� cpu, ram, disk, network

�����װ��Ϻ���system information�����£����Բ鿴������������ϸ������Ϣ��

�ֶ�����������˵���
configuraton -test selection& duty cycles and test perferences

1) cpu 
 ��Ҫ�������ֲ������ͣ�
ָ����ԣ���ѡmaximum heat,������ѡ�Ķ�ѡ�ϣ�
���Ȳ��ԣ�ֻѡmaximum heat��
����ѡ���Ĭ�ϣ�����Ҫ���ü��ɣ�

test selection& duty cycles :
�����趨ʱ���cycles, �ĸ�����ʱ�䳤���ĸ�Ϊ׼��
ĳ����������ռ�ı��ʣ������趨Ϊ100%

����ֻѡcpu, ��Ϊ100%
���Է���ʱ�����Կ� temperature ���ߵı仯���鿴��ѹ�������
����ָ��ʱ��һ��ѡ2~3 cycles���ɣ�

2)RAM
ģʽ��Ϊ��
standardѡ�����ڴ�ռ䶼���ꣻ
multi-process torture test�� ѡ�����ѡ��ʱ�������multi-process torture test setting �ſ��Խ������ã�
     number of processes �� �����߼�CPU����Ŀ
     % of RAM  : �趨ÿ���߼�cpu��ռ�õ��ڴ���ʣ�
	  Ԥ��ֵ���߼�cpu��Ŀ* ÿ��ռ���ñ��ʡ�=���е��ڴ�ٷֱȣ�����ϵͳ�ᷢ��������
  	  �������ϣ�����100% ���õ� �����ڴ棬���������ϴ���100%Ҳû�й�ϵ��
	  
	  
remark: �ڴ���Ե����̣��Ƚ��ڴ�д����Ȼ���ȡ��У�飻 

test pattern: ����ѡ��������ͣ�����ֱ����Ĭ�ϵļ��ɣ�

ram����׼����ֻ�в���cpu�ڼ�ѹ��
ram(multi-process):ÿ��cpu���ڼ�ѹ	 
��ʹ���Զ����ű����в���ʱ��ֻ��ʹ�ñ�׼ģʽ��
�ڴ���ԣ�һ������cycle��


3��disk
Ϊ��ֹ�����ƻ�������һ�㲻ѡ�����̣�ѡ�߼���
���ȷ��Ӳ���е�����û�ã�Ҳ����ֱ��ѡ�������̣�

ѡ��c�̣� ��ѡ�� test this drive
test mode: ����ѡ��ͬ�Ĳ����㷨��Ĭ�ϼ��ɣ�
file size: д���ļ��Ĵ�Сռ����Ӳ�̿ռ�İٷֱȣ�
block size: ���С
slow drive threshold: ��С�������ޣ����Բ����ã�
�������̣���д�룬Ȼ���ȡ�ٽ���У�飬�����к�ʹ��iometer�ȹ��߲�ͬ��iometerֻ�������ݵ�д����ȡ����
ͳ��BW��iops�������������ݵ�У�飻 ���У������ֲ��ԵĲ��Է�����ͬ��

��������
����ģʽ��
 standard network test 
  ��������֤��������BW��ֻ������·�Ƿ�ɿ��� ��loop ���ԣ�
 advanced network test
 ѡ��Ҫ���Ե�������Զ��Ҫ��endpoint ���,��display endpoint�����Կ����Զ˵�������Ϣ��ѡ���Ӧ��
 ���ں�Ϳ��Խ���ping�������ˣ� ��������֤��������BW��ֻ������·�Ƿ�ɿ�
  ��ע�� 
  1.�����������һ�����������˶��IP��ַ����endpoint��ֻ����ʾһ��IP��ַ������ҪΪ��������ú�
  ���������IP��ͬ��IP��ַ����ѡ�����IP��ַ�ſ��ԣ�
  2.�ɹ���ʼ���Ժ���endpoint�Ĵ����£����Կ�����̨������IP��ַ��Ϣ�������Դ������Ϣ�ȣ�
  
 
 
 ���������
 1)error���ã���Ҫ���÷��ִ���ʱ�Ƿ�ֹͣ��
  reported whea hardware errorҪѡ�У�
  
 2��logging:  max file size��lines�������£�
 
 �Զ�������ִ�з����� test --execute file ,ѡ��ű���
 
 �ű���ƿ�ܣ� loop N {cpu�� ram, disk network}

 
 
 ���Խű�sample1��
 
 ��װ����ķ������ֶ��������ò�����ѡ��file-save test config as�� �������õ������ļ���
 
 Ȼ��༭�ű��ļ���MyScript-�Զ����Խű�.bits�����£�
 
 LOAD "C:\Users\Administrator\Documents\PassMark\BurnInTest\LastUsed.bitcfg"  
 RUN CONFIG   

 ���Խű�sample2��
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


���ط����� test-excute scripts, ѡ��ű�����
 
 #########################################################################################
#################rpm related
which perl

[root@localhost VMC]# which perl
/usr/bin/perl
[root@localhost VMC]# rpm -qf /usr/bin/perl
perl-5.16.3-283.el7.x86_64

[root@localhost VMC]# rpm -qa | grep -i perl

��ѯperl�İ�װ���·��
[root@localhost VMC]# rpm -ql perl




##################zxve���˵����

1.�����Ѿ���װ��vnc����
rpm -ql tigervnc-server
����û��������������Ҫ�������ú������ſ���;
ֱ��ִ��vnc������������뼴�ɣ�

[root@localhost VMC]# service vncserver status
Redirecting to /bin/systemctl status  vncserver.service
vncserver.service
   Loaded: not-found (Reason: No such file or directory)
   Active: inactive (dead)

   2. ֱ��ִ�� virsh��ѯ���� ID�ſ����Ǵ����
   [root@localhost VMC]# virsh list
 Id    Name                           State
----------------------------------------------------
 2     vmc                            running

 ��Ϊ��vnc����ip��2������ host�������������������棬
 �ĳɷ���ip:1 ����������������棬���Ѿ��ڰ�װϵͳ��ͣ�ڹ����豸���Ľ����ˣ�
 
 3. ��vnc�����������ʱ����һ�δ�����ʾ��ȫ����Ҫ�رպ󣬵ڶ����ٴ��ǣ���ʾ�����ˣ�

##############################################################
#####################cpu ,�ڴ棬io����������
���ܳ���CPUƿ����Ӧ�����ʼ�����������̬web��������
���ܳ����ڴ�ƿ�����д�ӡ�����������ݿ����������̬web��������
i) load average������ֵ��������ֵ�Ĵ�Сһ�㲻�ܴ���ϵͳCPU�ĸ���
ii) cpu��������
vmstat:
r�б�ʾ���к͵ȴ�cpuʱ��Ƭ�Ľ����������ֵ������ڴ���ϵͳCPU�ĸ�����˵��CPU���㣬��Ҫ����CPU�� 
b�б�ʾ�ڵȴ���Դ�Ľ��������������ڵȴ�I/O�������ڴ潻���ȡ�
 ���ݾ��飬us+sy�Ĳο�ֵΪ80%�����us+sy���� 80%˵�����ܴ���CPU��Դ���㡣 
iii)�ڴ棺
free �Cm   Ӧ�ó�������ڴ�/ϵͳ�����ڴ�>70%ʱ����ʾϵͳ�ڴ���Դ�ǳ����㣬��Ӱ��ϵͳ����
Vmstat:   һ������£�si��so��ֵ��Ϊ0, ���si��so��ֵ���ڲ�Ϊ0�����ʾϵͳ�ڴ治�㡣��Ҫ����ϵͳ�ڴ档
Iiii)���̣�
Sar �Cd ��iostat �Cx �Cd
svctm��ֵ��await�ܽӽ�����ʾ����û��I/O�ȴ����������ܺܺã����await��ֵԶ����svctm��ֵ�����ʾI/O����
�ȴ�̫����ϵͳ�����е�Ӧ�ó��򽫱�������ʱ����ͨ�����������Ӳ����������⡣ 
%util���ֵҲ�Ǻ�������I/O��һ����Ҫָ�꣬���%util�ӽ�100%����ʾ���̲�����I/O����̫�࣬I/Oϵͳ�Ѿ���
���ɵ��ڹ������ô��̿��ܴ���ƿ����������ȥ���Ʊ�Ӱ��ϵͳ�����ܣ�����ͨ���Ż��������ͨ���������ߡ�
����Ĵ�������������⡣

LOAD:
ָ�꣺< CPU���� * ������ * 0.7   ����Ҳ��ָ�꣺< CPU���� * ������ * 0.5
α�ĺˡ� intel��i3����i5��˫�����̵߳�cpu��Ҳ����ÿ�����Ŀ��Լ���ͬʱ���������̡߳����ĺ��á�
���ĺˡ� intel��amd���еģ������ĺ����̡߳�
�������൱�ڴ����������߳����൱��һ��������ͬʱ������ټ����飨������ͬʱ�����ͻ�Բ֪��������

###################################################################

 Linux��yum�������
��Ҫ�����Ǹ���������/ɾ��/����RPM��.
�����Զ������������������.
���ܱ��ڹ������ϵͳ�ĸ�������
һ��yum list|more               �г����а��ļ����ɴ���grep��ѯ���������yum list |grep kernel
����yum info xxx                 ��ʾ��xxx��ϸ��Ϣ����ʹxxxû�а�װ
����yum update kernel       ��yum�����ں�
�ġ�yum update                 ȫ������ϵͳ
�塢yum list available         �г�����Դ�����п��԰�װ�İ�(List all packages in the yum repositories available to be installed.)
����yum list updates           �г�����Դ�����п��Ը��µİ�(List all packages with updates available in the yum repositories.)
�ߡ�yum list installed          �г��Ѿ���װ�İ�
�ˡ�yum install xxx              ��װxxx��
�š�yum update xxx            ����xxx��
ʮ��yum remove xxx            ɾ��xxx��

#####################################################################
linux�� cpu �߼��˵Ĳ鿴������
cat /proc/cpuinfo  | grep -i processor | wc -l    ���Բ�����е��߼��˵���Ŀ�����߳���Ŀ��
 

8/9#########linuxϵͳ����raid�������� mdadm
multidisk --md
/dev/md*
man mdadm

Options :
-l: raid level
-n: numbers of disks to make raid
-c: chunk size ��һ����bs����������
-a: automatic make md disk
-x: numbers of disks for spare

##������raid:mdadm -C /dev/md0 -a yes -l 0 -n 2 /dev/sdc{1,2}
   Device Boot      Start         End      Blocks   Id  System
/dev/sdc1               1         523     4200966   fd  Linux raid autodetect
/dev/sdc2             524        1046     4200997+  fd  Linux raid autodetect

mdadm -C /dev/md0 -a yes -l 0 -n 2 /dev/sdc{1,2}

##�鿴��cat /proc/mdstat 
##�鿴��ϸ��Ϣ��mdadm -D /dev/md0

mkfs.ext /dev/md0
mkdir /test1
mount /dev/md0 /test1
[root@localhost bin]# cd /test1
[root@localhost test1]# ls
lost+found


watch -n 1 'cat /proc/mdstat'


##����ģʽ��
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

mkfs.ext3 -b 4096 -E stride=16 /dev/md0  //ָ����չѡ��stride �ĸ�ʽ������


###������raid��ִ�У�mdadm  -D --scan ɨ��������raid����Ϣ����д�������ļ���
mdadm -D --scan >> /etc/mdadm.conf

[root@localhost ~]# mdadm  -D --scan
ARRAY /dev/md/localhost.localdomain:0 metadata=1.2 name=localhost.localdomain:0 UUID=d3d489f3:373b6f4a:b9622d54:fc8f0f31
ARRAY /dev/md/localhost.localdomain:0_0 metadata=1.2 name=localhost.localdomain:0 UUID=f212a10d:93791182:6c4b4e58:08ee11c0
ARRAY /dev/md0 metadata=1.2 name=localhost.localdomain:0 UUID=2dd4a619:d2f01b6c:f25cfce7:a151e7fc
[root@localhost ~]# mdadm -D --scan >> /etc/mdadm.conf

##stop ��raid���
mdadm -S /dev/md0
stop ��raid ���stop֮��Ϳ��������raid��Ϣ�ˣ�

##�༭�������ļ���ִ��mdadm -A /dev/md0 --scan ���Զ�����raid����װ����
[root@localhost ~]# mdadm -A /dev/md0 --scan
mdadm: /dev/md0 has been started with 2 drives.

############################################################################
8.9###linux mysql ���֪ʶ�ܽ᣺
yum install mysql* -y
�漰��������Ҫ�İ���
mysql-server.x86_64 
mysql-test.x86_64 ���� mysql-client��

service mysqld start
netstat -ntpl | grep -i 3306(MysqlĬ�ϵĶ˿���3306)

#��½mysql
������� mysql
mysql [-u username] [-h host] [-p[password]] [dbname] 
username �� password �ֱ��� MySQL ���û��������룬mysql�ĳ�ʼ�����ʺ���root��û�����룬ע�⣺���root�û�����Linux��ϵͳ�û���
MySQLĬ���û���root������ ��ʼû�����룬��һ�ν�ʱֻ�����mysql���ɡ� 

##MySQL�ļ�����ҪĿ¼
�������ݿ��ļ��������ļ��������ļ��ֱ��ڲ�ͬ��Ŀ¼
--���ݿ�Ŀ¼
/var/lib/mysql/ 
--�����ļ� 
/usr/share /mysql��mysql.server��������ļ���
--������� 
/usr/bin(mysqladmin mysqldump������)
--�����ű�
/etc/rc.d/init.d/�������ű��ļ�mysql��Ŀ¼


##�޸ĵ�¼����
�����������usr/bin/mysqladmin -u root password 'new-password'  ����Ϊ��ʼʱrootû�����룬 ����-p������һ��Ϳ���ʡ���ˣ�

�޸������ʽ��mysqladmin -u�û��� -p������ password ������  (���������Q&A����취)


## ��������
service mysqld start/stop/restart
chkconfig mysqld on 
chkconfig --list | grep -i mysql

##����mysql���ݿ��ļ��洢Ŀ¼
�����Ĭ�ϵ�/var/lib/mysql -->/home/data
1��service mysqld stop
2��mv /var/lib/mysql��/home/data/  �����ܵĲ��裺 chown -R mysql:mysql /home/data��
3)�޸������ļ���
mv /etc/my.cnf /etc/my.cnf.bak
cp /usr/share/mysql/my-medium.cnf��/etc/my.cnf
vi /etc/my.cnf
���������γ��ֵġ�socket=�� ���޸�Ϊ��
socket  = /home/data/mysql/mysql.sock
4��vi /etc/rc.d/init.d/mysqld
�����ж�Ӧ��λ���޸�Ϊ��
get_mysql_option mysqld datadir "/home/data/mysql"
5��
service mysqld restart
�����������������ʾOK


##���ݿⳣ�ò������
show databases;
use mysql;
show tables;

���⣺create database zhl;
����
use zhl;
//�ڸմ�����aaa���н�����name,������id(��ţ��Զ��� ��)��xm��������,xb���Ա�,csny���������£��ĸ��ֶ� 
create table student (id int(3) auto_increment not null primary key,xm char(8),xb char(2),csny date);
//�ڸմ�����aaa���н�����name,������id(��ţ��Զ��� ��)��xm��������,xb���Ա�,csny���������£��ĸ��ֶ� 
//��������Ӽ�¼��
insert into student values('','jack','male','1999-11-11');
//��select��������֤���
select * from student;
//�޸ļ�¼��
update student set csny='1000-1-1' where xm='tom';
//ɾ����¼��
delete from student where xm='tom';
//ɾ���ɾ��
drop database ����; 
drop table ������


##����mysql�û�
//����һ���û�user_1����Ϊ123�������������κ������ϵ�¼�������������ݿ��в�ѯ�����롢�޸ġ�ɾ����Ȩ�ޡ���������root�û�����MySQL��Ȼ�������������
mysql> grant select,insert,update,delete on *.* to user_1@"%" Identified by "123";

[root@localhost test1]# mysql -u root -p
Enter password: 
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)

Q&A����취��
# /etc/init.d/mysql stop
# mysqld_safe --user=mysql --skip-grant-tables --skip-networking &
# mysql -u root mysql
mysql> UPDATE user SET Password=PASSWORD(��newpassword��) where USER=��root��;
mysql> FLUSH PRIVILEGES;
mysql> quit
# /etc/init.d/mysql restart 
# mysql -uroot -p
Enter password: <�������������newpassword>
mysql> 
��ע��ʹ�����ַ����󣬲���֧��������½�ˣ���ֱ��ʹ��mysql ���޷���½�ˣ�


####�������û���������û��޷���½����
----������û��޷���½���⣺
������ͨ�û�����root�û��ȵ�½��Ȼ��ִ�У�
mysql> use mysql
mysql> delete from user where user='';
mysql> flush privileges;
��˼��ɾ�������û��� 

---<<<<�û�����>>>>>>
1�������û���
����:CREATE USER 'username'@'host' IDENTIFIED BY 'password'; 
˵��:username - �㽫�������û���, host - ָ�����û����ĸ������Ͽ��Ե�½,����Ǳ����û�����localhost, ������ø��û����Դ�����Զ��������½,����ʹ��ͨ���%. password - ���û��ĵ�½����,�������Ϊ��,���Ϊ������û����Բ���Ҫ�����½������. 

������create user 'test'@'%' identified by '123';

2����Ȩ��
����:GRANT privileges ON databasename.tablename TO 'username'@'host
˵��: privileges - �û��Ĳ���Ȩ��,��SELECT , INSERT , UPDATE ��(��ϸ�б�����������).���Ҫ��������Ȩ����ʹ��ALL.;databasename - ���ݿ���,tablename-����,���Ҫ������û����������ݿ�ͱ����Ӧ����Ȩ�������*��ʾ, ��*.*. 
grant all on *.* to 'test'@'%';

remark: ��ʱ��֤������һ̨�����ϣ�ʹ��mysql -u test -p -h 128.0.0.201 �����Է���Ŀ�������ϵ����ݿ��ļ���

ע��:������������Ȩ���û����ܸ������û���Ȩ,������ø��û�������Ȩ,����������:
GRANT privileges ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION; 

3������������û�����
����:SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');����ǵ�ǰ��½�û���SET PASSWORD = PASSWORD("newpassword"); 

4�������û�Ȩ�� 
����: REVOKE privilege ON databasename.tablename FROM 'username'@'host'; 
˵��: privilege, databasename, tablename - ͬ��Ȩ����. 
����: REVOKE SELECT ON *.* FROM 'pig'@'%';

ע��: �������ڸ��û�'pig'@'%'��Ȩ��ʱ����������(�����Ƶ�):GRANT SELECT ON test.user TO 'pig'@'%', ����ʹ��REVOKE SELECT ON *.* FROM 'pig'@'%';������ܳ������û���test���ݿ���user���SELECT ����.�෴,�����Ȩʹ�õ���GRANT SELECT ON *.* TO 'pig'@'%';��REVOKE SELECT ON test.user FROM 'pig'@'%';����Ҳ���ܳ������û���test���ݿ���user���Select Ȩ��. 

5��ɾ���û� 
����: DROP USER 'username'@'host';
####################################################################
##apache ��������ĵ�
����ֱ�ӷ��ʣ� /www/apache/orge
Ҳ���Բ������·�����
yum -y install httpd-manual
Ȼ����ʱ���web��ַ���ɣ�
��װ���manual�ļ��� /var/wwwĿ¼�£�ʹ������������IP���з��ʼ��ɣ�
http://128.0.0.66/manual/

Ҳ�����������������������׷��manual�����з������ɣ�
http://hello.b.com/manual/

###Ĭ�����������Ķ���
<VirtualHost 128.0.0.66:80>
   ServerName _default
   DocumentRoot "/www/default"
</VirtualHost>

###location��ʹ��
<Location /status>
    SetHandler server-status    //server-status��apache���õ�handler
	Order Deny,Allow
	Deny from all
	Allow from .foo.com
</Location>

directory ������Ǳ����ļ�ϵͳ·��
location�������һ��URL·��

����ʵ����vi /etc/httpd/conf/httpd.conf�У���������handler:
 <Location /server-status>
    SetHandler server-status
    Order allow,deny
    Allow from all
</Location>

httpd -t �����﷨��飻
service httpd restart��������
Ȼ��ʹ��IP/server-status ���handler���з��ʣ�
http://128.0.0.66/server-status
����鿴�ǵ��Ƿ�������״̬��Ϣ������һ��ֻ�����ض����û����в鿴��


##httpsʵ����
http�����ĵ�Э�飻
https�Ǽ��ܴ���Э�飻������443�˿ڣ�

client �� server�˵�ͨ�����̣�

��client�ȷ������3��TCP/IPͨ��������TCP/IP�ĻỰ��
Ȼ����ssl�Ự��Э����Ҫʹ�õļ����㷨--server�˽��Լ���֤�鷢�͸���������--�ͻ�����֤֤�飬�����֤ͨ����
����һ������ĶԳ���Կ���͸���������--�ͻ��˷���URL��Դ����--�������˽��ͻ�����������ݣ��ÿͻ��˷��͹�����
�Գ���Կ���ܺ���͸��ͻ��ˣ�

���ԣ����еĹؼ����ڣ�severҪ�����Լ���֤����ͻ��ˣ��ҿͻ��˿�����֤ͨ����������Ҫ��������һ�����õ�֤�飻
��������Ҫ��һ����������֤��䷢���������ҵķ�������֤���ҿͻ�����Ҫ�����֤���ŵ������ϣ�������֤�����˵�
֤�飻
 

�������̣�
1��ʹ��openssl ����һ��CA�� һ��CA��������ǩ��֤�飻
2������������Ҫ������Կ��Ȼ�󽫹�Կ���͸�CA,��CA����ǩ������֤�飬Ȼ���͸���������
3������������Ҫ����ʹ�Լ��ܹ�ʹ�����֤�飬���ڿͻ�������ʱ�����Խ�֤�鷢�͸��ͻ��ˣ�
4�� �ͻ���ʹ���Լ������CA��֤������֤���֤��

CA��server����ͬһ̨������Ҳ�ǿ��Եģ�
����������̨������һ����CA��һ����http server;

SSL�ĻỰ���޷����������������ֵģ�ֻ�ܻ���IP���У�
�����ζ�ţ�����ҵ�����ֻ��һ��IP��ַ��������ֻ��Ϊһ�������ṩssl�Ự���ܣ�

###���ù��̣�
ʹ��httpd -M �鿴����û�� ��Ӧ��SSLģ�飬��Ҫ��װ��
yum install mod_ssl
�鿴��װ�ļ���
rpm -ql mod_ssl
[root@localhost default]# rpm -ql mod_ssl
/etc/httpd/conf.d/ssl.conf
/usr/lib64/httpd/modules/mod_ssl.so
/var/cache/mod_ssl
/var/cache/mod_ssl/scache.dir
/var/cache/mod_ssl/scache.pag
/var/cache/mod_ssl/scache.sem


#����CA ������Ҫ������ǩ֤��
1��cd /etc/pki/CA

��ִ��(umask 077;openssl genrsa -out private/cakey.pem 2048) ����˽Կ
[root@localhost CA]# (umask 077;openssl genrsa -out private/cakey.pem 2048)
Generating RSA private key, 2048 bit long modulus
...........................................+++
....................................+++
e is 65537 (0x10001)
[root@localhost CA]# ls -l private/
total 4
-rw-------. 1 root root 1675 Aug 14 15:38 cakey.pem
2��������ǩ֤�飻
�ȱ༭�����ļ���
[root@localhost pki]# pwd
/etc/pki
[root@localhost pki]# vi tls/openssl.cnf 
��λ����[ req_distinguished_name ]���޸�������Ϣ��
 countryName_default             = CN
stateOrProvinceName_default     = Henan
localityName_default    = Zhengzhou
0.organizationName_default      = MageEdu
organizationalUnitName_default  =Tech

�ٴ� cd /etc/pki/CA
ִ�У�openssl req -new -x509 -key private/cakey.pem -out cacert.pem -days 3655 ������ǩ֤��
-days ��֤�����Ч��
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
Common Name (eg, your name or your server's hostname) []:ca.magedu.com   //Ҫ�䷢�����������˴��Ǹ��Լ���
Email Address []:admin@magedu.com
[root@localhost CA]# ls
cacert.pem  certs  crl  newcerts  private
[root@localhost CA]# 

Ҫ�����֤����Ϊ��ǩ֤����ʹ�ã���Ҫ�޸�openssl�еĲ���������Ϣ��
cd /etc/pki
vi tls/openssl.conf�ļ���
��λ�� [ CA_default ]���������޸ģ�
dir             = /etc/pki/CA           # Where everything is kept
certs           = $dir/certs            # Where the issued certs are kept
crl_dir         = $dir/crl              # Where the issued crl are kept
database        = $dir/index.txt        # database index file.

certificate     = $dir/cacert.pem       # The CA certificate
serial          = $dir/serial           # The current serial number

�� cd  /etc/pki/CA �£����������漰���ļ���Ŀ¼��
 mkdir certs crl newcerts
 �ٴ��������ļ���
 [root@localhost CA]# touch index.txt
[root@localhost CA]# echo 01 > serial
[root@localhost CA]# ls
cacert.pem  certs  crl  index.txt  newcerts  private  serial

##Ȼ���httpd ����������ã�
cd /etc/httpd/
mkdir ssl
cd ssl
 ִ��  (umask 077; openssl genrsa 1024 > httpd.key) ������Կ  //�˴���>,�����������-out,��������
 [root@localhost ssl]# ll
total 4
-rw-------. 1 root root 887 Aug 14 16:15 httpd.key

������֤��䷢����
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
��ʱ�Ѿ�����֤��ǩ������
Ȼ��ʹ�ñ���CAǩ��֤�飺 ִ��openssl ca -in /etc/httpd/ssl/httpd.csr -out /httpd.crt -days 3650ǩ��֤�飺

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

�Ҵ�ʱ��CAĿ¼�¿��Կ�����Ӧ��֤��ǩ����Ϣ��

[root@localhost ssl]# cd /etc/pki/CA/
[root@localhost CA]# ls
cacert.pem  crl        index.txt.attr  newcerts  serial
certs       index.txt  index.txt.old   private   serial.old
[root@localhost CA]# cat index.txt
V	260812082712Z		01	unknown	/C=CN/ST=Henan/O=MageEdu/OU=Tech/CN=hello.zhl.com/emailAddress=hello@zhl.com
[root@localhost CA]# cat serial
02
��֤�鸴�Ƶ� sslĿ¼�£�
[root@localhost CA]# cd /etc/httpd/ssl/
[root@localhost ssl]# ls
httpd.csr  httpd.key
[root@localhost ssl]# cp /httpd.crt .
[root@localhost ssl]# ls
httpd.crt  httpd.csr  httpd.key


Ȼ�������÷���������ʹ�ð䷢��֤�飺
 cd /etc/httpd/conf.d/
  vi ssl.conf ���б༭
  <VirtualHost 128.0.0.66:443>
  ServerName hello.zhl.com
  DocumentRoot "/www/zhl.com"
  ErrorLog logs/ssl_error_log
TransferLog logs/ssl_access_log    //��Ӧhttp�� customlog
LogLevel warn
  SSLEngine on
 SSLProtocol all -SSLv2   //��֧��sslv2
 
 SSLCertificateFile /etc/httpd/ssl/httpd.crt  //ǩ����֤���λ��
 SSLCertificateKeyFile /etc/httpd/ssl/httpd.key //˽Կ
 
 
 ����﷨�� httpd -t
  ������������ service httpd restart��������
  ȷ��443�˿��Ѿ���ʼ������
  [root@localhost conf.d]# netstat -ntpl | grep 443
tcp        0      0 :::443                      :::*                        LISTEN      419/httpd 

ֱ����https://hello.zhl.com/ ����ʱ����ʾ�����Ӳ������Σ�
������PC���������֤�飻���������£�
��Ҫ��CA��֤�鵼�뵽���أ�
cd cd /etc/pki/CA/
��cacert.pem ֤�鴫�䵽���أ�
�ڱ���PC�ϣ����ļ�����Ϊ cacert.crt�� �޸ĺ��ļ�ͼ�����֤���ͼ�꣬������Ӧ��ʹ�������չ����
ֱ��˫������ļ������ ����װ֤�顱��ѡ��֤��洢λ�� �������εĸ�֤��䷢������������ѡĬ�ϼ������֤��ĵ��룻
��ʱ����ttps://hello.zhl.com/  ������ʾͿ�������������
###############################################################

//9361 ��ʹ�������У����Բ鿴��MSM tool����ʾ����־����Ϣ����4��������raid5��
��ִ��storcli /c0 delete termlog ɾ����ʷlog
��ִ��storcli /c0 show termlog
�Ȱγ���һ���̣���־����ʾ���γ��̵�sas address�� raid��������Ϣ
08/17/16  0:35:41: C0:EVT#67035-08/17/16  0:35:41: 112=Removed: PD 0c(e0x0a/s1)
08/17/16  0:35:41: C0:EVT#67036-08/17/16  0:35:41: 248=Removed: PD 0c(e0x0a/s1) Info: enclPd=0a, scsiType=0, portMap=00, sasAddr=50019c6000000041,0000000000000000
08/17/16  0:35:41: C0:EVT#67037-08/17/16  0:35:41: 114=State change on PD 0c(e0x0a/s1) from ONLINE(18) to FAILED(11)
08/17/16  0:35:41: C0:EVT#67038-08/17/16  0:35:41:  81=State change on VD 00/1 from OPTIMAL(3) to DEGRADED(2)
08/17/16  0:35:41: C0:EVT#67039-08/17/16  0:35:41: 251=VD 00/1 is now DEGRADED
08/17/16  0:35:41: C0:LoadBalance 0
�ٰγ�һ���̣���־����ʾ���γ��̵�sas address�� raid offline����Ϣ
08/17/16  0:43:05: C0:EVT#67042-08/17/16  0:43:05: 112=Removed: PD 0b(e0x0a/s0)
08/17/16  0:43:05: C0:EVT#67043-08/17/16  0:43:05: 248=Removed: PD 0b(e0x0a/s0) Info: enclPd=0a, scsiType=0, portMap=00, sasAddr=50019c6000000040,0000000000000000
08/17/16  0:43:05: C0:EVT#67044-08/17/16  0:43:05: 114=State change on PD 0b(e0x0a/s0) from ONLINE(18) to FAILED(11)
08/17/16  0:43:05: C0:EVT#67045-08/17/16  0:43:05:  81=State change on VD 00/1 from DEGRADED(2) to OFFLINE(0)

��Ӧ

   0 Active 6.0Gb/s   0x50019c6000000040 
   0 Active 6.0Gb/s   0x50019c6000000049 
   0 Active 6.0Gb/s   0x50019c600000004a 
   0 Active 6.0Gb/s   0x50000396083ae336 


9361 �漰log�����
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
�����������
��¼�����telnet������¼�û������룺zte/zte�����룺tcs_debug.sh 128  4321 100��������;
����رգ�������:tcs_debug.sh 128  0,���������󼴿ɡ�

#######zte �������÷�����
--ӳ�䷽����
��FCЭ�鴦��ѯFC����WWPN����WWPN����һ��������
�鿴�����̣������̱�ʾ�Ѿ���ӵ��������У������̱�ʾ���Դ��������̣�
-->�ÿ����̴��������̣������ƣ����𣬳�Ա�̣�
-->�������������̻���Ϊ��ͬ�Ĵ洢������Щ�洢�����Ϊ��
         ����������״̬������ʱ����������ʣ������Ϊ0ʱ��������������
          ��������ʱ��ѡ�������̣������þ�������������Ϣ��
-->����ӳ���ϵ(������������뵽ӳ���飬��ӳ��������������;�Ķ�Ӧ��ϵ���������Ϸ��ʾ��������Ͽ���һ����ӳ��Ϊһ��������������)

---ʹ�������ڴ�ķ�����

��¼�����telnet������¼�û������룺zte/zte��;su �л���root �û��� 
���������ڴ�����tcs_debug.sh 128  4321 100;  �����ú���ϵͳ��fdisk -l�ܿ���100G���Ҵ�С���̣���
�ر������ڴ������:tcs_debug.sh 128  0, ��ʱ��Ҫ��������ſ�����Ч
#############################################################################################

#####vmware ����������������
����2��tab���鿴ϵͳ֧�ֵ�����
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

###vmware�鿴HBA��������������firmware�汾��Ϣ
�� ESXi 5.x �У�swfw.sh ������ vm-support ֧�ְ��ռ�����һ���ṩ��swfw.sh ���������ʶ�����ӵ�������Ӳ���Ĺ̼�����������汾��Ҫ���д������ʹ�ø�·����

# /usr/lib/vmware/vm-support/bin/swfw.sh

/tmp # find / -name "swfw.sh"
/usr/lib/vmware/vm-support/bin/swfw.sh


###Identifying the firmware of a Qlogic or Emulex FC HBA��
/usr/lib/vmware/vmkmgmt_keyval/vmkmgmt_keyval -a   //��ѯemulex HBA����Ϣ��

###��ȡ����������������ǰʹ�õ�������������
/usr/lib/vmware/vmkmod # esxcfg-scsidevs -a
vmhba0  ahci              link-n/a  sata.vmhba0                             (0:0:31.2) Intel Corporation Patsburg 6 Port SATA AHCI Controller
vmhba1  mpt2sas           link-n/a  sas.50015ebe0012973f                    (0:1:0.0) LSI Logic / Symbios Logic LSI2008
vmhba2  lpfc              link-up   fc.20000090fa61b583:10000090fa61b583    (0:4:0.0) Emulex Corporation LPe1250 8Gb Fibre Channel Host Adapter
vmhba32 ahci              link-n/a  sata.vmhba32                            (0:0:31.2) Intel Corporation Patsburg 6 Port SATA AHCI Controller
vmhba33 ahci              link-n/a  sata.vmhba33                            (0:0:31.2) Intel Corporation Patsburg 6 Port SATA AHCI Controller
vmhba34 ahci              link-n/a  sata.vmhba34                            (0:0:31.2) Intel Corporation Patsburg 6 Port SATA AHCI Controller
vmhba35 ahci              link-n/a  sata.vmhba35                            (0:0:31.2) Intel Corporation Patsburg 6 Port SATA AHCI Controller
vmhba36 ahci              link-n/a  sata.vmhba36                            (0:0:31.2) Intel Corporation Patsburg 6 Port SATA AHCI Controller
ע�⣺�ڶ�����ʾ��� HBA ���õ���������

###Ҫ�鿴����ʹ�õ���������İ汾����������������
esxcli software vib list   �鿴��������ģ�鼰�汾��Ϣ
/usr/lib/vmware/vmkmod # esxcli software vib list | grep -i lpfc
lpfc                           10.0.100.1-1vmw.550.0.0.1331820       VMware  VMwareCertified   2014-05-02  
scsi-lpfc820                   8.2.3.1-129vmw.550.0.0.1331820        VMware  VMwareCertified   2014-05-02

####������������esxcli software vib

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

###�鿴������ϸ��Ϣ��  vmkload_mod -s mpt2sas
/usr/lib/vmware/vmkmod # vmkload_mod -s mpt2sas |grep Version
 Version: Version 14.00.00.00.3vmw, Build: 1623387, Interface: 9.2 Built on: Feb 21 2014
  
  #### vmkload_mod �����鿴������
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


###����ʹ������ ������ ESXi/ESX �����汾��

# vmware -v


###Ҫȷ���Ƽ������������������򣬱���ʹ�� vmkchdev �����ȡ��Ӧ�� ID (VID)���豸 ID (DID)���ӹ�Ӧ�� ID (SVID) �����豸 ID (SDID)��

# vmkchdev -l |grep vmhba1

000:16.0 1000:0030 15ad:1976 vmkernel vmhba1


###Ҫʹ��һ�������ȡϵͳ������ HBA �Ĺ�Ӧ����Ϣ����ʹ���������

# for a in $(esxcfg-scsidevs -a |awk '{print $1}') ;do vmkchdev -l |grep $a ;done

###��ȡ������������͹̼���Ϣ
//��ȡ����ӿڿ��������б�
ESXi/ESX 4.x �� ��esxcfg-nics -l �� �� ESXi 5.x ����esxcli network nic list��
/usr/lib/vmware/vmkmod # esxcfg-nics -l  �� esxcli network nic list
Name    PCI           Driver      Link Speed     Duplex MAC Address       MTU    Description                   
vmnic0  0000:07:00.00 r8168       Up   100Mbps   Full   4c:09:b4:b0:bc:ac 1500   Realtek Realtek 8168 Gigabit Ethernet
vmnic1  0000:08:00.00 r8168       Up   100Mbps   Full   4c:09:b4:b0:bc:ad 1500   Realtek Realtek 8168 Gigabit Ethernet
vmnic2  0000:81:00.00 ixgbe       Down 0Mbps     Full   90:e2:ba:c0:c1:24 9000   Intel Corporation 82599EB 10-Gigabit SFI/SFP+ Network Connection
vmnic3  0000:81:00.01 ixgbe       Down 0Mbps     Half   90:e2:ba:c0:c1:25 1500   Intel Corporation 82599EB 10-Gigabit SFI/SFP+ Network Connection

//ʹ�� ethtool -i ������ʾһ������ӿڵĿ�����Ϣ
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


###Ҫͨ�� ethtool -i ͬʱ��ȡ������������������Ϣ���������������

for a in $(esxcfg-nics -l|awk '{print $1}'|grep [0-9]) ;do ethtool -i $a;done

�� ESXi 5.x �У�������ʹ����������:
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

    Ҫȷ���Ƽ������������������򣬱���ʹ�� vmkchdev �����ȡ��Ӧ�� ID (VID)���豸 ID (DID)���ӹ�Ӧ�� ID (SVID) �����豸 ID (SDID)

    # vmkchdev -l |grep vmnic0

    002:01.0 8086:100f 15ad:0750 vmkernel vmnic0

    �ڱ����У�ֵ�ֱ�Ϊ��


    Ҫʹ��һ�������ȡϵͳ�����������Ĺ�Ӧ����Ϣ����ʹ�ã�

    # for a in $(esxcfg-nics -l |awk '{print $1}' |grep [0-9]) ;do vmkchdev -l |grep $a ;done
     

    VID = 8086

    DID = 100f

    SVID = 15ad

    SDID = 0750

���ڿ����� VMware Compatibility Guide ��������Ӧ�� ID (VID)���豸 ID (DID)���ӹ�Ӧ�� ID (SVID) �����豸 ID (SDID)����ĳЩ����£�
������Ҫִ���ı��������Խ���Χ��С�����⿨��ע�⣺����ʹ������ ������ ESXi/ESX �����汾��# vmware -vͨ�� ESXi/ESX �汾���������ͣ�
�����˽�Ҫʹ�õ���������İ汾��VMware downloads page �ṩ�����������������


####Additional Information

��Щ�ű���Ϣ�������� ESXi 5.x��
Ҫ�� esxi5.x ��ʹ��һ�������ȡϵͳ������ HBA ����������汾����ʹ�ã�	
esxcli storage core adapter list|awk '{print $1}'|
grep [0-9]|while read a;do vmkload_mod -s $a|grep -i version;done
Ҫ�� esxi5.x ��ʹ��һ�������ȡϵͳ������ HBA �Ĺ�Ӧ����Ϣ����ʹ�ã�
esxcli storage core adapter list|awk '{print $1}'
|grep [0-9]|while read a;do vmkchdev -l |grep $a ;done
Ҫ�� esxi5.x ��ͨ�� ethtool -i һ�λ�ȡ������������������Ϣ���������������
esxcli network nic list | awk '{print $1}'|grep [0-9]|while read a;do ethtool -i $a;done
Ҫ�� esxi5.x ��ʹ��һ�������ȡϵͳ�����������Ĺ�Ӧ����Ϣ����ʹ�ã�
esxcli network nic list | awk '{print $1}'|grep [0-9]|while read a;do vmkchdev -l|grep $a;done

####vm-support tool��  ���ص��ע��nicinfo.sh    swfw.sh��
/usr/lib/vmware/vm-support/bin # ls
altlocaltgz.sh               dump-vmdk-rdm-info.sh        hostd.sh                     partedUtil.sh                vFlash.sh
cat-newest-vmkernel-core.sh  dump-vmfs-traces.sh          localtgz.sh                  smartinfo.sh
debug-hung-vm                dump-vxlan-stats-info.sh     nicinfo.sh                   swfw.sh


####����������
/usr/lib/vmware # esxcli software vib list | grep aacraid
scsi-aacraid                   1.1.5.1-9vmw.550.0.0.1331820          VMware  VMwareCertified   2014-05-02  

�������裺��.vib���ļ��ϴ���/var/log/vmware Ŀ¼�£���ס���������Ŀ¼�ſ��ԣ��������������Ŀ¼������ʱ�ᱨ��

/var/log/vmware # esxcli software vib install -v vmware-esxi-drivers-scsi-aacraid-550.5.2.1.41024.-1.5.5.1331820.x86_64.vib -f --maintenance-mode
Installation Result
   Message: The update completed successfully, but the system needs to be rebooted for the changes to be effective.
   Reboot Required: true
   VIBs Installed: Adaptec_Inc_bootbank_scsi-aacraid_5.5.5.2.1.41024-1OEM.550.0.0.1331820
   VIBs Removed: VMware_bootbank_scsi-aacraid_1.1.5.1-9vmw.550.0.0.1331820
   VIBs Skipped: 
   //��ʾ��Ҫ���� �ſ�����Ч,��������֤��Ч
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
Ӳ��smart��Ϣȷ�ϣ�
 ����SMART
# smartctl --smart=on --offlineauto=on --saveauto=on /dev/sda
smartctl -a /dev/sda
SMART Health Status: OK   #�汾�Ĳ�ͨ������ʾ��Ҳ��һ����
Elements in grown defect list: 0  #���ǳ��������׳Ƴɳ�������
 Non-medium errorcount:       51  #�ǽ��ʴ�����˼��˵�����̵����⣬һ���ǵ��¡����䡢У�����⣬���Ժ��Եġ�

����������ֱ�Ӳ鿴Ӳ�̵ĺû�:
 smartctl -H /dev/sda

Badblocks���߲����������޻�����Ϣ��
 badblocks������Լ�����װ�����𻵵����顣ִ�и�ָ��ʱ��ָ����Ҫ���Ĵ���װ�ã�����װ�õĴ�����������
badblocks -s//��ʾ����  -v//��ʾִ����ϸ���   /dev/sda1
badblocks -s//��ʾ���� -w//��дȥ��� -v//��ʾִ����ϸ��� /dev/sda2
ע�⣬������д�ķ�ʽ����Ѿ����ص�Ӳ��

badblocks -s -v /dev/sda
���ǣ����������������ĳһ������ͣ�Ͳ�ǰ�����󱨸�����ʾ�л��飬��ô�����ˡ������Ĵ����л����ˡ�
������ʲô���͵Ļ����������������Ƚ������ݱ��ݣ�����Ҫ���ݽ��б���Ȼ���ٳ����޸������������Ҫ����ȴ�޷���ȡ�����̳����쳣������ô������ֹͣʹ�ô˴��̲���רҵ��Ա�����޸���


 ʹ��hdparm����   ����Ӳ�̶�д�ٶ�
# hdparm -Tt /dev/sda
 �﷨��

hdparm [-CfghiIqtTvyYZ][-a <��ȡ����>][-A <0��1>][-c <I/Oģʽ>][-d <0��1>][-k <0��1>][-K <0��1>][-m <������>][-n <0��1>][-p <PIOģʽ>][-P <������>][-r <0��1>][-S <ʱ��>][-u <0��1>][-W <0��1>][-X <����ģʽ>] [�豸]

-a<��ȡ����> �趨��ȡ�ļ�ʱ��Ԥ�ȴ�������ķ���������������<��ȡ����>ѡ�����ʾĿǰ���趨�� -A<0��1> ������رն�ȡ�ļ�ʱ�Ŀ�ȡ���ܡ�-c<I/Oģʽ> �趨IDE32λI/Oģʽ�� -C ���IDEӲ�̵ĵ�Դ����ģʽ��-d<0��1> �趨���̵�DMAģʽ��-f ���ڴ滺����������д��Ӳ�̣�������������� -g ��ʾӲ�̵ĴŹ죬��ͷ�������Ȳ�����-h ��ʾ������-i ��ʾӲ�̵�Ӳ�������Ϣ����Щ��Ϣ���ڿ���ʱ��Ӳ�̱������ṩ�� -I ֱ�Ӷ�ȡӲ�����ṩ��Ӳ�������Ϣ��-k<0��1> ����Ӳ��ʱ������-dmu�������趨�� -K<0��1> ����Ӳ��ʱ������-APSWXZ�������趨��-m<������> �趨Ӳ�̶��ط�����ȡ�ķ������� -n<0��1> ����Ӳ��д��ʱ�������Ĵ���-p<PIOģʽ> �趨Ӳ�̵�PIOģʽ�� -P<������> �趨Ӳ���ڲ���ȡ�ķ�������-q ��ִ�к����Ĳ���ʱ��������Ļ����ʾ�κ���Ϣ�� -r<0��1> �趨Ӳ�̵Ķ�дģʽ��-S<ʱ��> �趨Ӳ�̽���ʡ��ģʽǰ�ĵȴ�ʱ�䡣-t ����Ӳ�̵Ķ�ȡЧ�ʡ� -T ƽ��Ӳ�̿�ȡ�Ķ�ȡЧ�ʡ�-u<0��1> ��Ӳ�̴�ȡʱ�����������ж�Ҫ��ͬʱִ�С�-v ��ʾӲ�̵�����趨�� -W<0��1> �趨Ӳ�̵�д���ȡ��-X<����ģʽ>  �趨Ӳ�̵Ĵ���ģʽ��-y ʹIDEӲ�̽���ʡ��ģʽ�� -Y ʹIDEӲ�̽���˯��ģʽ��-Z �ر�ĳЩSeagateӲ�̵��Զ�ʡ�繦�ܡ�


����ʹ��sg_vpd����鿴Ӳ��ת�٣�sg_vpd������sg3_utils����һ������.
sg_vpd /dev/sda

 ����smart���Ӳ�������:

smartctl -a <device> �����豸�Ƿ��Ѿ���SMART������ smartctl -s on <device> ���û�д�SMART������ʹ�ø������SMART������ smartctl -t short <device> ��̨���Ӳ�̣�����ʱ��̣� smartctl -t long <device> ��̨���Ӳ�̣�����ʱ�䳤�� smartctl -C -t short <device> ǰ̨���Ӳ�̣�����ʱ��̣� smartctl -C -t long <device> ǰ̨���Ӳ�̣�����ʱ�䳤����ʵ��������Ӳ��SMART���Լ���� smartctl -X <device> �жϺ�̨���Ӳ�̡� smartctl -l selftest <device> ��ʾӲ�̼����־�� smartctl -l error <device> ��ʾӲ�̴�����ܡ�

����ͨ��dmesg���ߣ�ȷ��һ��Ӳ�̵��豸���š������ʾΪsdb�������SATA��SCSI
smartctl -i /dev/sda ȷ��Ӳ���Ƿ����SMART֧��

 SMART support is: Enabled                          //��ʾ������smart֧��

�������SMART support is: Disabled��ʾSMARTδ���ã�ִ�������������SMART

# smartctl --smart=on --offlineauto=on --saveauto=on /dev/sda

 smartctl 5.40 2010-10-16 r3189 [i386-redhat-linux-gnu] (local build)

Copyright (C) 2002-10 by Bruce Allen, http://smartmontools.sourceforge.net

=== START OF ENABLE/DISABLE COMMANDS SECTION ===

SMART Enabled.

SMART Attribute Autosave Enabled.

SMART Automatic Offline Testing Enabled every four hours.

����Ӳ�̵�SMART�����Ѿ����򿪣�ִ����������鿴Ӳ�̵Ľ���״��

smartctl -H /dev/sda
 smartctl 5.40 2010-10-16 r3189 [i386-redhat-linux-gnu] (local build)

Copyright (C) 2002-10 by Bruce Allen, http://smartmontools.sourceforge.net

=== START OF READ SMART DATA SECTION ===

SMART overall-health self-assessment test result: PASSED

��ע��result��ߵĽ����PASSED�����ʾӲ�̽���״̬���ã����������ʾFailure����ô������̸�����������Ӳ�̡�SMARTֻ�ܱ�������Ѿ����ٽ��������Ǳ������ܼ������ж���ǲ�ȷ���ġ�ͨ����SMART������������Ԥ���ģ����̱����󣬲��ᵱ��������һ���ܼ��һ��ʱ�䣬�е�Ӳ��SMART�����󻹼������˺ü��꣬�е�Ӳ��SMART�������ͻ��ˡ�����һ�����ֱ��������������������ܵġ���

 #smartctl -A   /dev/sda  �鿴Ӳ�̵���ϸ��Ϣ

#smartctl -s on  /dev/sda  ���û�д�SMART������ʹ�ø������SMART������

#smartctl -t short  /dev/sda  ��̨���Ӳ�̣�����ʱ��̣�

#smartctl -t long  /dev/sda   ��̨���Ӳ�̣�����ʱ�䳤��

#smartctl -C -t  /dev/sda   shortǰ̨���Ӳ�̣�����ʱ��̣�

#smartctl -C -t  /dev/sda   longǰ̨���Ӳ�̣�����ʱ�䳤����ʵ��������Ӳ��SMART���Լ����

#smartctl -X   /dev/sda      �жϺ�̨���Ӳ�̡�

#smartctl -l selftest  /dev/sda  ��ʾӲ�̼����־��

#smartctl -l error   /dev/sda    ��ʾӲ�̴�����ܡ�


 �����Ҫ���ڵ�¼��������������smartctl�Ƚ��鷳ʱ��linux���ṩ��ϵͳ����smartd���༭�����ļ���1    vi  /etc/smartd.conf

��������ļ��д󲿷ֿ�����ע�͵���˵����ֻ��Ҫд��͵�ǰӲ����ص����ü��ɣ�

/dev/sda -H  -m  test@test123123.com  //��ش��̵Ľ���״̬,��SMART�б���PASSED��ʱ����ǡ�һ������Failure���������ʼ�֪ͨ�û�ָ��������

 /dev/sda -a -m  admin@example.com,root@localhost  //��ش��̵���������,��SMART�б���PASSED��ʱ����ǡ�һ������Failure���������ʼ�֪ͨ�û�ָ�������� 

 /dev/twa0 -d 3ware,0 -a -s L/../../7/00 //���3ware 9000�������ϵĵ�һ��ATA���̵���������,��ÿ��������00:00--01:00���г���ʽ�����Ҽ��

 /dev/sg2 -d areca,1 -a  -s L/../(01|15)/./22 //���Areca Raid�������ϵĵ�һ��SATA���̵���������,��ÿ������µĵ�1��͵�15���22:00--23:00���г���ʽ�����Ҽ��

 -s (O/../.././(00|06|12|18)|S/../.././01|L/../../6/03) //��ÿ���00:00,06:00,12:00,18:00�������ߵ��Լ죬����ÿ���01:00-02:00���ж̸�ʽ���Լ죬����ÿ�����6��03:00-04:00���г���ʽ���Լ� 

���ú�smartd.conf����ִ��

/etc/init.d/smartd restart ������Ч

������smartd.conf��ص����ÿɲμ�:


Ӳ�̴��������
1. UncorrectedReadErr--��ӦΪӲ�̴��󣻴�ʱ��dd��д�ᷢ��error;

[root@localhost bin]# diskman -s /dev/sdc
Permanent defect  (p-list): 859
Grown defect list (g-list): 0

Smart Status(ASC/ASCQ)    : 0x0/0x0 

UncorrectedWriteErr       : 0
UncorrectedReadErr        : 0
UncorrectedvVerifyErr     : 0
NonMediumErr              : 4

[root@localhost bin]# diskman -s /dev/sdd    �����������
Permanent defect  (p-list): 572
Grown defect list (g-list): 0

Smart Status(ASC/ASCQ)    : 0x0/0x0 

UncorrectedWriteErr       : 0
UncorrectedReadErr        : 6
UncorrectedvVerifyErr     : 0
NonMediumErr              : 2

2.smartctl ��Ϣ�еĳɳ�����
Elements in grown defect list: 0  #���ǳ��������׳Ƴɳ�������
����Non-medium errorcount:       51  #�ǽ��ʴ�����˼��˵�����̵����⣬һ���ǵ��¡����䡢У�����⣬���Ժ��Եġ�


 ʹ��smartctl��dell����������ʵ¼ 


һ��ִ�����

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

 

�����鿴Ӳ�̷���

#fdisk �Clu

Disk/dev/sda: 300.0 GB, 300000000000 bytes

255heads, 63 sectors/track, 36472 cylinders, total 585937500 sectors

Units = sectors of 1 * 512 = 512 bytes

 

   Device Boot      Start         End      Blocks  Id  System

/dev/sda1   *         63      208844      104391  83  Linux

/dev/sda2         208845   585922679   292856917+ 8e  Linux LVM

����ȷ�ϻ���λ��

# echo 'scale=5;(435567298 - 208845) * 512/4096'|bc    *512��1��Units512�ֽڣ�/4096��ÿ�����豸��4096�ֽ�

54419806.62500 ���ڵ����������8������1���飬0.125*5=0.625

˵����54419806�����ĵ�5�����������⣬�������鿴�³�����ĵط��Ƿ����ļ�ʹ����

 

�ġ��鿴�Ƿ����ļ���ʹ�û���

# debugfs

debugfs 1.39 (29-May-2006)

debugfs: open /dev/mapper/VolGroup00-LogVol02 #��/dev/mapper/VolGroup00-LogVol02

debugfs:  icheck 54419806                  # Print a listing of the inodes which use the one or more blocks specified on the command line

Block  Inode number

54419806        50659332

debugfs:  ncheck 50659332               # Take the requested list of inode numbers, and print alisting of pathnames to those inodes.

Inode  Pathname

50659332        /database/jhl_2918_x5/mysql/ibdata1  #�ҵ������ļ����ڻ���λ��

debugfs:  


#############################raid��Ա����Ϣ��ȡ˵����
SAS3008/PMC7805 :ʹ��sg�豸��
LSI9361 :ʹ��megacli������ķ������У�

����raid��Ա�̣�ʹ��smartctl ���߲�ѯ������smart��Ϣ�ķ�����
Ȼ��ʹ��MegaCLI64 ����ѯ���������̵�ID�š�
Virtual Drive: 0 ������ĵ�һ��RAID VD�� PD 0 �������VD����ĵ�һ��������̡�
./MegaCli64 -LdPdInfo -aALL   ��ѯ�� ��Device Id: 0��

��ִ�� smartctl -a -d megaraid,N /dev/sd*
N ��Device ID ���滻  X����RAID����ϵͳ��ʶ��ı���滻��

smartctl -a -d megaraid,0 /dev/sda    �Ϳ��Բ�ѯ����Ա�̵�smart��Ϣ�ˡ�


����ʵ����
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



LBAд��

lba���߼���ַ��pba�������ַ��

Ӳ���ϵĿռ��Ϊһ��һ����������ÿ����512�ֽڣ��ѿռ�������Ϊ��λ����0�ൽ��β���Ϳ��Ը��ݵ�ַ���з��ʣ�lbaֵ�Ͷ�Ӧ������λ�á�

��victoria�������ɨ��Ŀ�ʼ�ͽ�������������дlbaֵ����������ɨ��Ŀռ俪ʼ�ͽ������ɣ�һ��ȱʡֵ����Ӳ�̵�0�Ⱥͽ�β������

LBA��Logincal Block Addeessing ��д,��Ӳ���������ַ��һ��������

LBA 

LBA(Logical Block Address),�������ƣ��߼������ַ�����������Դ洢�豸���������������ͨ�û��ƣ�һ��������Ӳ�������ĸ��������豸��
LBA������ָĳ����������ĵ�ַ����ĳ����ַ��ָ����������顣��������νһ���߼�����ͨ����512��1024λ�顣ISO-9660��ʽ�ı�׼CD����2048λ��Ϊһ���߼������С��



fdisk -l��ʾ��Ϣ���

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

������
Disk /dev/sda: 10.7 GB, 10737418240 bytes
���豸����Ϊ/dev/sda�����豸�Ĵ�СΪ10.7GB��������ֲ����ر�ȷ����ϵͳ��10GB��10737418240 bytes����ת�����ֽں�Ĵ�С������10737418240/1024/1024/1024=10GB (ע��bytes=B����ʾ���ֽڡ���bit=b����ʾ��λ��)
255 heads, 63 sectors/track, 1305 cylinders
255 heads����ʾ��ͷ��Ϊ255
63 sectors/track����ʾÿ�ŵ�����63������
1305 cylinders����ʾ����1305�����棬�����Ƿ�������С��λ
Units = cylinders of 16065 * 512 = 8225280 bytes

16065=255*63 ��Ϊÿһ����ͷ������ͬһ������ģ�63��ʾÿ���ŵ��ϵ��������������������ĳ˻���ʾһ�������ϵ���������������16065*512��ʾһ������Ĵ�С��8225280�ֽ�
Sector size (logical/physical): 512 bytes / 512 bytes
��ʾһ�������Ĵ�С��512�ֽ�

�ܽ᣺����һ�����̵Ĵ�С=һ�������С*���������=��ͷ����*ÿ���ŵ��ϵ�������*һ��������С*��������

�������̴�С=8225280*1305=10733990400bytes=9.99GB=255*63*512*1305
��������ʾ�����ǵĴ���ֻ��1305�����棬���±ߵķ�����Ϣ�г�����1306��������������̫���⣬linux��ʾ����Щ���ݲ���ʮ�־�ȷ��



###################lsi9271,lsi9361 check with megacli
 MegaCli���ò������� 

MegaCli -adpCount ����ʾ������������

MegaCli -AdpGetTime �CaALL ����ʾ������ʱ�䡿

MegaCli -AdpAllInfo -aAll     ����ʾ������������Ϣ��

MegaCli -LDInfo -LALL -aAll    ����ʾ�����߼���������Ϣ��

MegaCli -PDList -aAll    ����ʾ���е�������Ϣ��

MegaCli -AdpBbuCmd -GetBbuStatus -aALL |grep ��Charger Status�� ���鿴���״̬��

MegaCli -AdpBbuCmd -GetBbuStatus -aALL����ʾBBU״̬��Ϣ��

MegaCli -AdpBbuCmd -GetBbuCapacityInfo -aALL����ʾBBU������Ϣ��

MegaCli -AdpBbuCmd -GetBbuDesignInfo -aALL    ����ʾBBU��Ʋ�����

MegaCli -AdpBbuCmd -GetBbuProperties -aALL    ����ʾ��ǰBBU���ԡ�

MegaCli -cfgdsply -aALL    ����ʾRaid���ͺţ�Raid���ã�Disk�����Ϣ��

�Ŵ�״̬�ı仯���Ӱ��̣������̵Ĺ����С� 

Device         |Normal|Damage|Rebuild|Normal

Virtual Drive     |Optimal|Degraded|Degraded|Optimal

Physical Drive     |Online|Failed �C> Unconfigured|Rebuild|Online

������ʾ����

MegaCli -PDList -aALL

��������������Ӳ�̵���Ϣ��

MegaCli -LDPDInfo -aall

�����������߼��豸(�Ұ�LD��֮ΪLogical Device)������Ӳ��֮��Ĺ�ϵ��

MegaCli -CfgLdAdd -r(0|1|5) [E:S, E:S, ...] -aN

�������������µ�raid 0,1,5�������豸������

MegaCli -LDBI -ProgDsply -LALL -aALL

����������raid��building���ȵ�
һ����linux����MegaCli��ά��dell������raid��Ҳ������windows���ã�
%SystemRoot%\system32\GAMSERV\megacli -adpeventlog -getevents -f d:\%computername%_nvram.log -aall  ��ҪװMylex Global Array Manager�����

############################LBA���
LBA(Logical Block Addressing)�߼���Ѱַ���� LBA ģʽ�£�����֪��Ӳ���ϵ�һ�����������������ڵĴ�ͷ�����棨Ҳ���Ǵŵ�����������Ψһȷ����
����ϵͳ����ֱ��ʹ�ô�ͷ�������������Ӳ�̽���Ѱַ�����ΪCHSѰַ��������Ҫ�ֱ�洢ÿ��������������������Ϊ3D��������
ʹ��ʱ�ٷֱ��ȡ����������Ȼ�����͵����̿�����ȥִ�С�����ϵͳ��8b���洢��ͷ��ַ����10b���洢�����ַ����6b���洢������ַ��
��һ����������512B������ʹ��CHSѰַһ��Ӳ���������Ϊ256 * 1024 * 63 * 512B = 8064 MB(1MB = 1048576B)������1MB=1000000B�������8.4GB����
����Ӳ�̼����Ľ�����Ӳ������Խ��Խ��CHSģʽ�޷�������8064 MB��Ӳ�̣���˹���ʦ�Ƿ����˸��Ӽ���LBAѰַ��ʽ����LBA��ַ�У�
��ַ���ٱ�ʾʵ��Ӳ�̵�ʵ�������ַ�����桢��ͷ����������LBA��ַ��ʽ��CHS������άѰַ��ʽת��Ϊһά������Ѱַ��
����Ӳ�����е�����������C/H/S���ͨ��һ���Ĺ���ת��Ϊһ���Եı�ţ�ϵͳЧ�ʵõ������ߣ������˷����Ĵ�ͷ/����/������Ѱַ��ʽ��
�ڷ���Ӳ��ʱ����Ӳ�̿������ٽ������߼���ַת��Ϊʵ��Ӳ�̵������ַ��
��������Ӳ��ģʽ�У����� LBA ģʽʹ����ࡣ ����
LBA��C/H/S ֮���ת��: ����
��NSΪÿ�ŵ���������NHΪ��ͷ����C��H��S�ֱ��ʾ���̵����桢��ͷ��������ţ�LBA��ʾ�߼������ţ�divΪ�������㣬modΪ������㣬�� ����
LBA=NH��NS��C+NS��H+S-1�� ����
C=(LBA div NS)div NH�� ����
H=(LBA div NS)mod NH�� ����
S=(LBA mod NS)+1 ����
���� LBA = 0 �� CHS = 0/0/1 ����
��C/H/S��LBA�ļ��㹫ʽ�� ����LBA=��C-CS��*PH*PS+��H-HS��*PS+(S-SS) 

IDE SATA SCSI SAS ��Щ��ָӲ�̵Ľӿ�������ʽ��
AHCI PATA ISCSI ��Щ��Ӳ�̵ĽӿڵĹ淶�������Բ�ͬ��������ʽ���֡�
����SATA�ӿڣ� Serial ATA��SATA, Serial Advanced Technology Attachment������ƴ���ATA���Ǵ���SCSI��SAS��Serial Attached SCSI���������ֵܣ�
���ߵ����߼��ݣ�SATAӲ�̿ɽ���SAS�ӿڡ�����һ�ֵ������ߣ���Ҫ��������������ʹ����洢�豸����Ӳ�̼�������������֮������ݴ���֮�á�
���нӿڻ����нṹ�򵥡�֧���Ȳ�ε��ŵ㡣 


################################scsi�豸ȷ�ϣ�
ϵͳ��ʶ�𵽵�scsi_Host:  /sys/class/scsi_host
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


###################################fc����˵����
ramdisk��ص����ã�
telnet manage_ip port 23  zte/zte
su
tcs_debug.sh 128  4321 100  ����100G��ramdisk
����Ҫ����ִ�����Σ���ʾ "TCs loop test is already started" ��ʾ�����Ѿ�����
ִ�к󣬿�����fdisk -l�鿴�豸�Ĵ�С����֮ǰӳ��Ĵ����������̵Ĵ�С������smartctl���߲鿴�Ѿ��޸Ĺ��ˣ�
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

�ر�ramdisk��� tcs_debug.sh  128 0 
��ʱҪ����ִ�����Σ���ʾ ��TCS loop test is already stopped��

��ע�� ������ʹ��ӳ��������̻���ram disk,������ɺ󣬶���Ҫ��ι��˾Ϳ���ʶ���ˣ�

###########################################################################################
nfs�������ã�
yum install nfs* -y

[root@localhost ~]# cat /etc/exports 
/home/vpshare *(insecure,rw,async,no_root_squash)

service nfs start

############################################################
@@@@linux��������������أ�
vi /etc/profile
������������һ�У�
export PATH=$PATH:/usr/sbin/ocmanager/
ִ��  . /etc/profile ��source /etc/profile ������Ч��

##########################################################


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@���з�����ֱ������Կ�������÷�����
��ͨSSH������ssh�������½�����нڵ�֮���������Կ���ɷ��ʣ���

1�������ڵ㣨����һ���ڵ㣩��ִ�� ssh-keygen -t rsa һ·�س����������������Կ�ԣ�

2������Կ��ӵ���֤�ļ��У� cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys ��������authorized_keys�ķ���Ȩ�ޣ� chmod 600 ~/.ssh/authorized_keys ��

3��scp  �������֤�ļ������нڵ㣺

scp ~/.ssh/authorized_keys root@*.*.*.*:~/.ssh/

==>�������нڵ�֮��Ϳ����໥�����ˣ�

####################################################################

@@@@@@@@@@@@@@@@@@@@@@@@YUMԴ�������
cd /etc/yum.repos.d/
rm -rf *
cat >> /etc/yum.repos.d/iso.repo << EOF
[server]
name=server
baseurl=file:///mnt
enabled=1
gpcheck=0
EOF

��֤yum:
yum clean all  #����ɿ���Ϣ
yum update   #yum��Դ����� 
yum list  #�����¿⣬����г������������

@@@@@@@@@@@@����CPU��Ƶ

��ϵͳ������cpu��Ƶ������BIOS�����ó�Ƶ
cat >> /etc/rc.local << EOF
modprobe acpi_cpufreq 
awk  '/^processor/ {system("echo performance > /sys/devices/system/cpu/cpu" $3 "/cpufreq/scaling_governor")}' /proc/cpuinfo 
EOF


����ʵ����
 cat /etc/rc.local 
modprobe acpi_cpufreq 
awk  '/^processor/ {system("echo performance > /sys/devices/system/cpu/cpu"$3"/cpufreq/scaling_governor")}' /proc/cpuinfo 

ִ��source /etc/rc.local��
��ѯ cat /proc/cpuinfo | grep "cpu MHz"
ȫ��cpu MHz		: 2401.000 �ˣ��Ѿ�����Ϊ��Ƶģʽ�ˣ�

��ע˵����

������ѯ������Ϣ��
E5-2630 v3
��������������Ƶ�ʣ�2.4Ghz,
����ƵƵ�ʣ�3.2Ghz,

��PTU ����в�ѯ������Ϣ��
 Max Turbo 01C:32x, 02C:32x, 03C:30x, 04C:29x, 05C:28x, 06C:27x, 07C:26x, 08C:26x
 ����Ĳ���˵��������ãУ��ܹ���8��core,��һ��core����ʱ������ƵƵ��Ϊ3.2Ghz,�Դ����ƣ�
 Ĭ���ǰ˸��˹�����Ҳ����ͨ����������һ��core������


==> ���еĺ�����Ϊondemandģʽʱ�����ٲ��ֺ˹���Ƶ��Ϊ2.4G����������2.4G�ĺ˵���Ŀ���̶����Ǳ䶯�ġ�

remark:
ʹ��cpufreq���߸�CPU��ʱ������Ƶ

ʹ��cpufreq���߸�CPU��ʱ������Ƶ
 
�ִ���CPU�����嶼�нڵ缼������CPU�͸��ɹ����Ļ��Զ���Ƶ�������Ҫ��ʱ������Ƶ�͹���ģʽ����ʹ��cpufreq�ֶ����������ģʽ����������ʧЧ�������Ҫ���ڵ������޸�/etc/sysconfig/cpuspeed��
  www.2cto.com  
lsmod | grep "acpi_cpufreq"
 
ִ��������������Ƿ����acpi_cpufreqģ�飬����û�м��������ʹ��yumȥ��װ��ģ��
 
yum install -y cpufreq-utils.x86_64
 modprobe acpi_cpufreq  #���������ģ�鲻֧��intel xeon��������ֻ��ֻ��P4-clockmod���ģ��֧��xeon������������ǰ��Ҫ�Լ����ֱ����ںˡ�����
 
�鿴��ǰCPU����Ƶ�ʺ�״̬��
  www.2cto.com  
cpufreq-info
ִ���������������½����
 
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
 
The governor "ondemand" ��ʾCPUƵ�ʵĲ��ԡ�CPU�����ֲ��ԣ�onemand����ʾϵͳ����ͨ����̬����Ƶ�ʣ����͹��ģ�����ĵ������Ժ��ں˵Ĺ��Ĺ����㷨�йأ���userspace����ʾ�û������Լ��趨cpu��Ƶ�ʣ���performance����ʾCPU�����������Ƶ�¹�������
  www.2cto.com  
current CPU frequency is 1.60 GHz ��ʾ��ǰ�������е���Ƶ��
 
����CPU����ģʽ��
1���������幤��ģʽ
 
cpufreq-set -g performance
ִ�����������ʾ��CPU�����������Ƶ�¹����������ܣ��������ܣ���ִ����Ϻ󣬿��ٴ�ִ��cpufreq-info�鿴CPU�Ĺ������Ժ͵�ǰ��Ƶ��
 
2���ֹ�0�ź��ĵ�ָ�����Ƶ�ʺ���СƵ��
 
cpufreq-set -c 0 -g userspace -d 180000 -u 240000
ִ����������趨 0�ź��� Ϊ �û��Զ��壬��������СƵ��Ϊ1.8GHz�����Ƶ��2.4GHz


################
�ļ�ϵͳ��أ�
�༭/etc/mke2fs.conf�ļ���ȥ��ext4��has_journal
���أ�mount /dev/sdb1  /data1 -o rw,noatime,barrier=0

remark:
Linux�ļ�ϵͳ��barrier�����û��ǽ��� 




�������ǰ���е�Linux�ļ�ϵͳ������EXT3��EXT4�������ļ�ϵͳbarrier��Ϊһ����ǿ�İ�ȫ���ԡ����������ݲ���д���ռǡ��� �ǣ����������£����ǲ��������Щbarrier�Ƿ����á����ľ�ΪʲôҪ�����Linuxϵͳ������barrier�����˽��͡�

Linux��־��barrier����

Ҫ���barrier����������Ҫ����ļ�ϵͳ��־���ܡ����õ��ļ�ϵͳʹ����־��������֤�ļ�ϵͳ�������ԡ��ù��ܱ����˼·�ܼ򵥣���д���µ� ���ݿ鵽����֮ǰ�����Ƚ�Ԫ����д����־��Ԥ�Ƚ�Ԫ����д����־���Ա�֤��д����ʵ����ǰ��һ������������־�����ܺ����׵ػع�������֮ǰ��״̬����� ����ȷ���˲��ᷢ���ļ�ϵͳ�����������

����ʹ����־���ܲ��ܱ�֤û���κβ�����ڵĴ��̴��д������Ļ��棬���ݲ�������д�뵽�����У�������д�뵽���̻����С�����һ�������̿����� ���ܸ��Ӹ�Ч�ؽ��临�Ƶ������С����������˵���кô��ģ����Ƕ���־������˵���෴��Ϊ�˱�֤��־�ٷ�֮�ٿɿ�����������Ա�֤Ԫ��������ʵ����д��֮ ǰ��Ԥ��д�롣���������Ҫ�����ļ�ϵͳbarrier��ԭ��

���Ǻ��������ʹ��barrier�ĸ���ԭ��barrier�����ֹ��barrier֮��д�����ݣ���ʵ�����ݿ齫��barrier��д��֮ǰ�� ȫд����̡�ʹ��barrier����ȷ���ļ�ϵͳ�������ԣ���Ϊbarrier������EXT4�ļ�ϵͳ����Ĭ�����õ�(������Ĳ���ϵͳ���������Ĭ���� ��)��

Linux�ļ�ϵͳ��barrier�����û��ǽ���?

�����ͨ��/proc/mounts�ļ�������ļ�ϵͳbarrier�ĵ�ǰ״̬;����ÿһ�����ص��ļ�ϵͳ��������ļ����ܿ������еĹ���ѡ�����㿴��barrier=1����ô����ļ�ϵͳ������ʹ��barrier���ܡ�������Ϣ��һ���ļ�ϵͳ�����ӣ�

/dev/sda1 /boot ext4 rw,seclabel,relatime,barrier=1,data=ordered 0 0/dev/mapper/luks-3e67401f-44c6-4a27-a1bf-cdf0dcf45f65 /home ext4 rw,seclabel,noatime,barrier=1,data=ordered 0 0

�ļ�ϵͳbarrier��ʱ������?

Barrier���������ڣ�������Ӧ�������������¡�����豸ӳ������Ϊ�洢������ȼ�ʹ�ã���ô�ļ�ϵͳbarrier���޷������ˣ���Ϊ�豸ӳ ������֧��barrier�����ԣ���������ļ�ϵͳĬ��֧��barrier�������޷����߼�����RAID���߶�·�����������иù���(RED HAT��������ص�Linux�汾����barrier��ΪĬ��ѡ��)��

����������ķ���֮һ���Ǳ���ʹ���豸ӳ�����������ڰ�װ������ʱ������Ҫ��ֿ�������ѡ����ȣ��㲻��ʹ��LVM��װ����������Ӧ��ѡ���ô� ͳ�ķ�����ʽ�����ţ��㲻��ʹ�ú��豸ӳ������Ϲ����Ķ�·�����̣�������SAN�ϴ����������·����ĳЩ����£�SAN��Ӧ�̻��ṩһ��ר����������Ϊ ѡ�񣬵��������й�Ӧ�̶��ṩ��ѡ���õİ취�ǲ�������Ӳ����

ʹ��barrier�����ķ���֮һ�ǣ���ϵͳ�ж�ʱ�����ݻ����ڻ����У���������д���ļ�ϵͳ��һ���򵥵ĵ�ر��ݿ��������Ա���������⡣��������ʹ�õ�����������������ˣ����̿�������Ȼ�ܱ�֤��������������ų���barrierʹ�õ���Ҫ��

ʹ��barrier����һ������֮�����ڣ�����Ҫ�����������ܵĴ��ۡ��������Ҫ���������ܣ���ô������ù���ѡ��-o barrier=0���ر�barrier���ܣ����磺mount /dev/sda2 -o barrier=0 /data��

�ļ�ϵͳbarrier���ܷǳ����ã����ǲ��ܺ��豸ӳ������Ϲ������������Ҫʹ�������豸����������Ҫ��֤�ļ�ϵͳ�����ԣ���ô������õ�ر� �ݴ��̿�������������Ӳ����֧���������ô��ֻ�ܱ���ʹ���豸ӳ����������������barrier�����������ļ�ϵͳ�����ԡ����У������ϣ���õ����õ� ϵͳ���ܣ����Ҳ��Ҫ����barrier���ܣ����ή��ϵͳ�����ٶȡ�


Ԫ����metadata ��IO�ж��Ӱ�죿
��־�ļ�ϵͳ��journaling file systems���ɷ�ֹϵͳ����ʱ���µ����ݲ�һ�����⡣���ļ�ϵͳԪ���ݣ�metadata���ĸ��Ķ���������һ�ݵ�������־������� ϵͳ����ʱ���Ը�����־��ȷ�ػָ����ݡ�����֮�⣬��־ʹϵͳ��������ʱ���ؽ����ļ�ϵͳ�ļ�飬�Ӷ������˻ָ�ʱ�䡣

����˵Ԫ���ݾ������ݵ����ݡ�
�κ��ļ�ϵͳ�е����ݷ�Ϊ���ݺ�Ԫ���ݡ�������ָ��ͨ�ļ��е�ʵ�����ݣ���Ԫ
����ָ��������һ���ļ���������ϵͳ���ݣ��������Ȩ�ޡ��ļ�ӵ�����Լ��ļ�����
��ķֲ���Ϣ(inode...)�ȵȡ��ڼ�Ⱥ�ļ�ϵͳ�У��ֲ���Ϣ�����ļ��ڴ����ϵ�λ���Լ������ڼ�Ⱥ�е�λ�á��û���Ҫ����һ���ļ��������ȵõ�����Ԫ���ݣ����ܶ�λ���ļ���λ�ò��ҵõ��ļ������ݻ�������ԡ�
2�� Ԫ���ݹ���ʽ
         Ԫ���ݹ��������ַ�ʽ������ʽ����ͷֲ�ʽ��������ʽ������ָ��ϵͳ����һ���ڵ�ר��˾ְԪ���ݹ�������Ԫ���ݶ��洢�ڸýڵ�Ĵ洢�豸�ϡ����пͻ� �˶��ļ�������ǰ����Ҫ�ȶԸ�Ԫ���ݹ���������Ԫ���ݡ��ֲ�ʽ������ָ��Ԫ���ݴ����ϵͳ������ڵ㲢���ܶ�̬��Ǩ�ơ���Ԫ���ݹ����ְ��Ҳ�ֲ��������� ͬ�Ľڵ��ϡ��������Ⱥ�ļ�ϵͳ�����ü���ʽ��Ԫ���ݹ�����Ϊ����ʽ����ʵ�ּ򵥣�һ����ά�����ף���һ���Ĳ���Ƶ�����ڿ����ṩ����������ܡ�ȱ���� ��һʧЧ�����⣬���÷�����ʧЧ������ϵͳ���޷��������������ң�����Ԫ���ݵĲ�������Ƶ��ʱ�����е�Ԫ���ݹ����Ϊ����ϵͳ������ƿ����
         �ֲ�ʽԪ���ݹ���ĺô��ǽ���˼���ʽ����ĵ�һʧЧ�����⣬ �������ܲ������Ų���Ƶ��������ƿ������ȱ���ǣ�ʵ�ָ��ӣ�һ����ά�����ӣ���������һ��Ӱ�졣


###############################################
@@@�ر�SELinux
sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config

#####################################
�޸�sysctl.conf����
--�ر�swap����
swapoff -a      ���� swapon -a��
echo 0 > /proc/sys/vm/swappiness
cat >>/etc/sysctl.conf << EOF	
vm.swappiness = 0
EOF
--��Ч����
sysctl �Cp


#############���ô��ļ���
cat >> /etc/security/limits.conf << EOF	
* soft nofile 65535
* hard nofile 65535
* - nofile 51200
EOF


############################
����NTP��
���������ã�
---����namenode��ntp

����namenode��ntpΪ�򱾵�ͬ��
cat >> /etc/ntp.conf << EOF
server 127.127.1.0 
fudge 127.127.1.0 stratum 8 
EOF


����datanode��ntp
������namenode��ntp����ͬ��
cat >> /etc/ntp.conf << EOF
server namenode 
EOF


����ʱ��ͬ��
���нڵ���ִ����������
service ntpd start 
chkconfig ntpd on 
ntpdate -u namenode
cat >> /etc/crontab << EOF
*/5 * * * * root /usr/sbin/ntpdate -u namenode ;/sbin/hwclock -w
EOF


#################����SSH�������½
--����namenode ssh����Ȩ��
mkdir -p /root/.ssh
chmod 700 /root/.ssh
cd /root/.ssh
# remove/save any contents so the directory is empty
ssh-keygen -t rsa -q
# hit return for any prompts
cp id_rsa.pub authorized_keys
echo "StrictHostKeyChecking=no" >config


---����datanode ssh
root�û�ssh��¼��ÿ��datanode������ִ����������
mkdir -p /root/.ssh
chmod 700 /root/.ssh
cd /root/.ssh
# remove/save any contents so the directory is empty
rm -rf *
scp namenode:/root/.ssh/* ./


#######################���ñ���yumԴ��
cd /etc/yum.repos.d/
rm -rf *

--�ϴ���װ������/home/CDH
--����yumԴ�ļ���
cat >> /etc/yum.repos.d/acloudera-manager.repo << EOF
[cloudera-manager]
name = Cloudera Manager, Version 5.3.2
enabled = 1
baseurl = file:///home/CDH/cloudera-manager/RPMS/x86_64
gpgkey = http://archive.cloudera.com/redhat/cdh/RPM-GPG-KEY-cloudera
gpgcheck = 0
EOF


---���з������ϴ���REPO
���з������ϴ���REPO
cd  /home/CDH/cloudera-manager/RPMS/x86_64/
createrepo .
yum repolist      #���Բ鿴repo�������


#######################################################################
@@@@@@cpu��Ƶ׷��˵����
ϵͳ����cpufreq-info   �����ڵİ�װ��Ϊ��cpufrequtils
ʹ��yum ��װcpufrequtils ��ʱ��ʾ���´���
[root@localhost yum.repos.d]# yum install cpufrequtils*
��������������������
warning: rpmts_HdrFromFdno: Header V3 RSA/SHA256 Signature, key ID fd431d51: NOKEY


Public key for cpufrequtils-007-6.el6.x86_64.rpm is not installed

���������Ľ���취���£�
�������ҵ��˽��������
��ʱҪ����rpm��ǩ����Ϣ����
��root��¼��ִ����������
# rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

�����ҵ�Linux�汾��CentOS 5.4
������ִ����������
#rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-5

�������ڵõ������

==�� ��redhat ϵͳ��ִ��rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
����ִ�а�װ������������ˣ�

@@ִ��cpuƵ�ʲ�ѯ���
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

The governor "ondemand" ��ʾCPUƵ�ʵĲ��ԡ�CPU�����ֲ��ԣ�onemand����ʾϵͳ����ͨ����̬����Ƶ�ʣ����͹��ģ�����ĵ������Ժ��ں˵Ĺ��Ĺ����㷨�йأ���userspace����ʾ�û������Լ��趨cpu��Ƶ�ʣ���performance����ʾCPU�����������Ƶ�¹�������


@@@@���������
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

��ÿ���߼��ˣ�����Ϊperformance��ģʽ��
echo performance > /sys/devices/system/cpu/cpu" $3 "/cpufreq/scaling_governor

����������������������
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
��������������������������������������
[root@localhost yum.repos.d]# cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor 
userspace
[root@localhost yum.repos.d]# 

#####################################################

����Դ�����װ�������������ķ���������Ϊintel 40G������������װreadme��:
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
excel ������
Excel��Ԫ���������ı�������ȴ��ʾΪһ�ţ�
 �ڱ༭excel�ĵ�Ԫ��ʱ������Ԫ���ʽ���ó��ı�����������д���� ��Alt��Enter��Ϊ���� ǰ6�б༭��û������ ��Ԫ��Ҳ��������ʾΪ�ı����� ���ǵ��������1�����ݵ�ʱ�򣬻س�֮�󣬵�Ԫ������־�ȫ������ʾ�ˣ������һ�У������ҵ�Ԫ����и�Ҳ�Զ���...
չ��

ͬ־�ǣ��ҵ����У����Ѿ����Զ����У��ı���ʽ��

���������ķ���ô��
==���𰸣�
ѡ����Ҫ��ʾ���еĵ�Ԫ��--�Ҽ�--���õ�Ԫ���ʽ--����--����
ѡ����Ҫ��ʾ���еĵ�Ԫ��--�Ҽ�--���õ�Ԫ���ʽ--����--�Զ�����--ȷ��--OK!

############################################################################################### 82599 ���������ĳ��ҵĹ�ģ���޷�ʶ��������Ӧ��

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
������OS��Linux SUSE 11 sp2 64bit

           Ӳ����IBM x3650 M3������(��82599EB����)

�������󣺵�����10G��ģ���ʱ��ifconfig�޷���ʾ�ӿڣ����ߵ��½ӿ���ʧ��

��λ���̣�dmesg���֡�failed to load because an unsupported SFP+ module type was detected.����Ϣ���Դ���Ϣgoogle�����������ӣ�

http://discussions.citrix.com/topic/306986-xenserver-60-issues-with-intel-82598eb-10-gigabit-af-dual-port-nic/

���ۣ�82599EBֻ֧����intel�ԼҵĹ�ģ��Խӡ����ҵĹ�ģ����finisar�ġ�

����취��ж����������allow_unsupported_sfp=1�������¼���

                 modprobe -r ixgbe;modprobe ixgbe allow_unsupported_sfp=1



###############################################################

����������
7805�Ŀ�������ʹ�õ�ϵͳ����֮ǰ��6805 �°�װ��suse 11sp3,
����ϵͳʱ�����ס����ʾ�Ҳ��������� **-part2,

���Ʒ�������y ��ȴ�һ��ʱ�����shell�����к󣬽�����ʾ��Ŀ¼�º�
��***part2 ������Ϊ�Ҳ����Ŀ����� **-part2��Ȼ������exit�󣬼���������������������ϵͳ��



########################################################################
@@@@@linux�¸�����ʹ����100%�Ľ���취��

--��ʽ1��ȷ����Ч��
һ�����linux������ʹ�����ﵽ100%���������������

    root���ܵ�¼

    ϵͳ������������

����ͨ��������Ҹ������ڵĴ��ļ�

1.du -sh /* 2>/dev/null | sort -hr | head -3

2.�����������ִ�к���/var/ռ�ռ������ô�ڲ���/var�����ڵĴ��ļ����磺

du -sh /var/* 2>/dev/null | sort -hr | head -3

3.�Դ����ƣ�����ҵ��Ǹ����ļ���ɾ�����߲�ȡ������ʩ���ɣ�


--��������
 ���췢����һ���ͻ��ķ�����/ռ��100%��
������du -sh ./*  �������һ�£�ȥ������Ŀ¼��ռ�ã�/ʵ������Ҳ��40%���ң���������������ȫ���ռ��һ�벻����

ͨ��lsof |grep delete�����ö��ļ��Ѿ�ɾ�������ǻ�û���ͷſռ䣬��Ȼ�������Խ�����⣬���Ƿ���Ҳ���ж��ˣ�
�о���һ�£�ͨ��ɾ�����̺��ǿ��԰ѿռ��ͷų����ġ�
sync && for i in `lsof |grep delete |awk '{print $2}'`; do kill -9 $i; done
��ɺ��ֿռ����ͷš�

PS. ע�⣬ִ������ǰһ��Ҫȷ�Ͻ��̺Ŷ�Ӧ�ķ����Ƿ���ʹ�ã���ѹؼ�����ͣ���ˣ���


############################################################################

####screen
screen -ls   //��ѯ�Ƿ��У�attached or deattached
screen -S name  //����
screen -r name  //����
screen -x name

##################################################################################
@@@��ѯlinux ��dhcp�������IP��ַ����Ϣ
/var/lib/dhcpd/dhcpd.leases

###################################################################################


summary:
1)Ӳ�̻���������
badblocks -s -v /dev/sdb1  �����
badblocks -s -v -w /dev/sdb1  д���


2��Ӳ�̹������ʵ����⣺

diskman��ֱ�Ӷ���Ӳ�̼Ĵ�������Ӳ�������¼��ʵ��Э�����ʣ���Ӳ����expander
lsiman��diskman��һ���ģ�ֱ�Ӷ���Ӳ���Ĵ���
������--expander  �� expander--Ӳ��
���������Э�������ǲ�һ���ģ�
������--expander��������controller��-��expander֮���ĸ������ʾ����ģ�
expander--Ӳ����������expander��disk֮�����ĸ������ʾ�����
����expander��controller����sas3������sas2.0�̣���expander--disk��sas2.0��
��controller-expander�� sas3

PMC 7805 Raid����ʹ�ó��������й���arcconf getconfig 1 pd ��ѯ����ÿ����λ�����ʣ�
==����������
==�����ۣ�
1.PMC��raid����ʹ��arcconf  getconfig  1 PD ��ѯ����ÿ����λ�����ʣ�ָ�������ж˿ڵ����ʣ��Ҷ���8������ͨ���Ķ˿ڣ�����в��ֶ˿�Э�̳�3Gbps,����ѭ���¼��ݵĲ��ԣ������пڻ�Э�̳�3Gbps, ��ʱʹ��arcconf  getconfig  1 PD �����ѯ�������ʶ���3Gb/s��




3�����ع��˵ķ�����
[root@localhost zhl]# diskman -i /dev/sdb | grep -E "Support Max|Negotiate"
Support Max Speed      : 3.0Gbps
Negotiated link Speed  : 3.0Gbps

4��
�ܽ᣺
SAS�̵�WWN�ž���SAS��ַ����ȫ��Ψһ�ı�ʶ��
SATA�̽���ϵͳ�У���ѯ����SAS��ַ��expander���пڵĵ�ַ������SATA����ĵ�ַ,һ��Ϊ**01��**02..��
��SAS��ַ�����һλ�Ͳ�λ����ͬ����SASЭ���SATA�̵�Э�������⣻
8�̵Ļ�����SATA�̣���Ҫ��ȷ����


5�� 7805 ����raid���ر�cache:
arcconf create 1 logicaldrive Method QUICK Rcache ROFF Wcache WT max 5 0 14 0 15 0 16

6)
12-disk expander:
��phy display �£�
 0-11�� Ϊ���е�12��ͨ������Ӧǰ�õ�12��Ӳ��
 12-19�� Ϊ���е�8��ͨ������Ӧ���ӵ���raid����
 21��  ��ӦΪ ϵͳ�̵�����ͨ����
 
 
 6�� 7805 ��simple volume��ϵͳ�̣�����ֱ����SAS3008 ��������
 
 7�� SAS3008 ��װϵͳʱ����ʾӲ�����б�Ŀ������raid��Ϣ��������ʱ��
 ==�� ����Բߣ� �������̣���raid1,Ȼ����ɾ�����Ͷ�����ʶ���ˣ�
 
 8��Ӳ��cache�������
 [root@localhost zhl]# diskman | grep -i cache
  -w on/off  enable/disable write cache
  
 9�� lsi raid���Ĳ�ѯ���ߣ�
  lsiman : ֻ��ִ��һ��������ò�ѯ����Ӳ�̣����̻�raid��Ա�̵�smart�������Ϣ��
  megacli  ������ϸ��������� ���ý��smartctl ��ѯraid��Ա�̵�smart��Ϣ�ȣ�
  storcli: ����ϸ�����������
  
  
 10�� awk ��أ�
 �ļ���ȡ��storcli /c0 show all | awk '$1=="TOPOLOGY",$4=="8:11"{print $0}'
 ����������
 [root@localhost zhl]# storcli /c0 show all | awk 'BEGIN{print "disk information"}$1=="TOPOLOGY",$4=="8:31"{print $0}END{print "the end of the disk information"}'
disk information
TOPOLOGY :
========

-------------------------------------------------------------------------
DG Arr Row EID:Slot DID Type  State BT      Size PDC  PI SED DS3  FSpace 
-------------------------------------------------------------------------
 0 -   -   -        -   RAID0 Optl  N  465.25 GB dflt N  N   none N      
 0 0   -   -        -   RAID0 Optl  N  465.25 GB dflt N  N   none N      
 0 0   0   8:31     9   DRIVE Onln  N  465.25 GB dflt N  N   none -      
the end of the disk information

11) awk �����÷�˵����
awk '/^processor/{system("cat /sys/devices/system/cpu/cpu"$3"/cpufreq/scaling_governor")}' /proc/cpuinfo

awk '/^processor/{system("echo performance > /sys/devices/system/cpu/cpu"$3"/cpufreq/scaling_governor")}' /proc/cpuinfo 

@@@
�ر�esxi����ǽ��
esxcli network firewall set --enabled false

~ # esxcli network firewall set --enabled false
~ # esxcli network firewall get
   Default Action: DROP
   Enabled: false
   Loaded: true
   
 12�� Ӳ��smart��Ϣ��
 �ص��ע THRESH ��Ϊ0����Ŀ��
 �����ǰֵ��THRESH�ͣ�����ʾ FAILING_NOW
 ���WORSTֵ��THRESH�ͣ�����ʾIn_the_past
 
 
  @@@@smart��Ϣѡ����ܣ�
 �����ϣ�SMART���Ա��г�����������Ӳ���ж���õ�����ֵ���Լ���Щ������صĹ�����ֵ��������������̼��Զ����ɺ͸��¡�

    ID������ID��ͨ����һ��1��255֮���ʮ���ƻ�ʮ�����Ƶ����֡�
    ATTRIBUTE_NAME��Ӳ�������̶������������
    FLAG�����Բ�����־�����Ժ��ԣ���
    VALUE�����Ǳ��������Ҫ����Ϣ֮һ������������Եı�׼��ֵ����1��253֮�䡣253��ζ����������1��ζ��������ȡ�������Ժ������̣���ʼ��VALUE���Ա����ó�100��200.
    WORST������¼����СVALUE��
    THRESH���ڱ���Ӳ��FAILED״̬ǰ��WORST�����������Сֵ��
    TYPE�����Ե����ͣ�Pre-fail��Oldage����Pre-fail���͵����Կɱ�����һ���ؼ����ԣ���ʾ������̵�����SMART����������PASSED/FAILED��������κ�Pre-fail���͵����Թ��ϣ���ô����Ϊ���̽�Ҫ�������ϡ���һ���棬Oldage���͵����Կɱ�����һ���ǹؼ������ԣ��������Ĵ���ĥ�𣩣���ʾ����ʹ���̱��������ϡ�
    UPDATED����ʾ���Եĸ���Ƶ�ʡ�Offline���������ִ�����߲��Ե�ʱ�䡣
    WHEN_FAILED�����VALUEС�ڵ���THRESH���ᱻ���óɡ�FAILING_NOW�������WORSTС�ڵ���THRESH�ᱻ���óɡ�In_the_past������������ǣ��ᱻ���óɡ�-�����ڡ�FAILING_NOW������£���Ҫ���챸����Ҫ�ļ����ر���������Pre-fail����ʱ����In_the_past�����������Ѿ������ˣ��������в��Ե�ʱ��û���⡣��-������������Դ�û���Ϲ���
    RAW_VALUE�������̶����ԭʼֵ����VALUE������

��ʱ������ܻ��룬���ǵģ�smartctl�������Ǹ�����Ĺ��ߣ����Ҹ���֪����α����ֶ����е��鷳��������ܹ���ָ���ļ�����У�ͬʱ����֪ͨ�Ҳ��Խ�����ǲ��Ǹ����𣿡�

����Ϣ�ǣ���������Ѿ����ˡ���smartd�������õ�ʱ���ˣ�


13��
 
   
@@@LinuxϵͳӲ�̳��ֹ��ϵ��޸�����

LinuxϵͳӲ����ʹ�ù����л����һЩ�������������������ϵͳ�ؼ����򣬾ͻ���ϵͳ�ļ������ָ��ִ���
���ľ�������һ�£����ľ����̴��LinuxϵͳӲ�̳��ֹ��ϵ��޸�������

14��
����io������ʱ�����޸����Ĳ���
[root@localhost ~]# cat /proc/sys/dev/scsi/logging_level
0
[root@localhost ~]# echo 1016 > /proc/sys/dev/scsi/logging_level 
[root@localhost ~]# echo 1 > /sys/module/mpt2sas/parameters/mpt2sas_fwfault_debug
[root@localhost ~]# echo 2 > /sys/module/aacraid/parameters/firmware_debug

echo 1016  > /proc/sys/dev/scsi/logging_level

15�� linxu ϵͳ����ǰ�����־�����
echo "" > /var/log/messages


16��
��Ӳ�̸�ʽ��ʱ��ÿ�ζ��Ḵ����������⣺
aacraid: Host adapter reset request. SCSI hang ?					
aacraid: Host adapter reset request. SCSI hang ?					
aacraid: Host adapter reset request. SCSI hang ?					
aacraid: Host adapter reset request. SCSI hang ?					
sd 5:1:18:0: [sdl]  Result: hostbyte=DID_ERROR driverbyte=DRIVER_SENSE					
sd 5:1:18:0: [sdl]  Sense Key : Unit Attention [current] [descriptor]					
sd 5:1:18:0: [sdl]  Add. Sense: Commands cleared by device server					
sd 5:1:18:0: [sdl] CDB: Write(10): 2a 00 00 00 26 c7 00 00 41 00					
end_request: I/O error, dev sdl, sector 9927					
Buffer I/O error on device sdl1, logical block 9893					
lost page write due to I/O error on sdl1					
Buffer I/O error on device sdl1, logical block 9894					

==��ȷ��Ӳ�̵�smart��Ϣ�У�û���κ��쳣�����ˣ�
199 UDMA_CRC_Error_Count    0x0032   154   154   000    Old_age   Always       -       168					

==���ͳ���ȷ�ϵ���Ϣ��

������ϵͳHOST��SI�Ƿ������⣿���ߡ����塢HBA������أ�
��Log��û�з���ECC��ش��󣬵����в���CRC����
��������SMART�п�����ID199�


ECC:�����߼�����
CRC:ѭ������У��

�ܽ᣺  �ص��ע������,��,����������
����C7��199��Ultra ATA����У������� Ultra ATA CRC Error Rate
�����������������ֵ�ۼ���ͨ���ӿ�ѭ������У�飨Interface Cyclic Redundancy Check��ICRC�����ֵ������ߴ������Ĵ������������ֵ��Ϊ0�ҳ�����������ʾӲ�̿������������ߡ�Ӳ�̽ӿڳ��ִ������ʵ������ߡ��ӿڽӴ����������ܵ��´�����������һ�������ֵ���Ḵ�㣬����ĳЩ��Ӳ��Ҳ�����һ������������ֻҪ���������ߺ�����ֵ���ټ�������������ʾ�����ѵõ������ 


����01��001���ײ����ݶ�ȡ������ Raw Read Error Rate
��������Ϊ0������ֵ����ǰֵӦԶ�������ٽ�ֵ�� 
�����ײ����ݶ�ȡ�������Ǵ�ͷ�Ӵ��̱����ȡ����ʱ���ֵĴ��󣬶�ĳЩӲ����˵������0�����ݱ������̱�����߶�д��ͷ�������⣬��������ˡ���ͷ��Ⱦ����ͷ����ȵȡ�������ϣ��Ӳ����˵�����Ӳ�̵���һ����кܴ�����������ⲻ�������κ����⣬��Ҫ�ǿ���ǰֵ�½��ĳ̶ȡ� 
�����ڹ�̬Ӳ���У����������ֵ�����˿�У���Ĵ����벻��У����RAISE����UECC��URAISE����

����ע��RAISE��Redundant Array of Independent Silicon Elements����Ϊ������Ԫ���������У��ǹ�̬Ӳ�����е�һ������ָ���������֤�ڲ�������RAID���е����ݰ�ȫ�ԡ�


03��003����������ʱ�� Spin Up Time
������������ʱ��������������������ﵽ�ת�����õ�ʱ�䣬����ֱֵ����ʾʱ�䣬��λΪ��������룬�������ֵԽСԽ�á�������������Ӳ����˵����һ�������һ���ο�ֵ��Ӳ��ÿ�ε�����ʱ�䶼����ͬ��ĳ������������ЩҲ����ʾ�������⡣
����Ӳ�̵����������������ﵽ�ת�ٴ�����Ҫ4�롫15�����ң�����������ʱ��˵�����������·������л��������⡣����һ����������ֵ��ĳЩ�ͺŵ�Ӳ��������Ϊ0�����Ҫ����ǰֵ�����ֵ���ж��ˡ� 
�������ڹ�̬Ӳ����˵�����е����ݶ��Ǳ����ڰ뵼�弯�ɵ�·�У�û������������������û�����壬���ݹ̶�Ϊ0����ǰֵ�̶�Ϊ100��


��05��005����ӳ���������� Reallocated Sectors Count/ ���ۿ���� Retired Block Count
��������ӦΪ0����ǰֵӦԶ�����ٽ�ֵ��
������Ӳ�̵�ĳ�����������ֶ�/д/У�����ʱ��Ӳ�̹̼�����Ὣ��������������ַ����ȱ�ݱ�(G-list)�����õ�ַ���¶���Ԥ�ȱ����ı��������������е�����һ��ת�ƣ���ͳ�Ϊ��ӳ�䡣ִ����ӳ��������Ӳ����Windows�����������޷����ֲ��������ģ������ַ�ѱ�ָ��������������������˲��������� 
�����������������ֱֵ�ӱ�ʾ�Ѿ�����ӳ����������������ǰֵ����������ֵ�����Ӷ������½��������ִ��������ֵ��Ϊ��ʱ��Ҫ����ע���䷢չ���ƣ����ܳ��ڱ����ȶ�����Ӳ�̻������������У�������ֵ����������˵�����������������ӣ�Ӳ���Ѵ��ڲ��ȶ�״̬��Ӧ�����Ǹ����ˡ������ǰֵ�ӽ����ѵ����ٽ�ֵ����ʱ������ֵ����һ���ܴ���Ϊ��ͬӲ�̱����ı���������������ͬ������ʾȱ�ݱ����������������þ����Ѿ�ʧȥ����ӳ�书�ܣ��ٳ��ֲ��������ͻ����ֳ�����ֱ�ӵ������ݶ�ʧ�� 
������һ�����Ӳ�̵������ؼ�������������ӳ������������Ҳֱ��Ӱ��Ӳ�̵����ܣ�����ĳЩӲ�̻�����������ܴ󣬵���ǰֵ�½������Ե����������Ӳ�̾��ܻ����������У���Ҳ���˼���ʹ�á���Ϊ������������λ�ڴ���β����������Ƭ���Ĵ�����������ʹ�ñ���������ʹѰ��ʱ�����ӣ�Ӳ�����������½��� 
������������ڻ�еӲ�����Ƿǳ����еģ������ڹ�̬Ӳ����˵ͬ��������Ҫ���塣�������������̬�ֲ��ģ�����˵MLC��д��һ������ϣ�ʵ����˵����д��һ���֮ǰ���ᷢ���������𻵡�����ĳЩ��Ԫ����д�뼸ʮ�ξ����ˡ�����֮����еӲ�̵���Ƭ�������д���𻵣����ֲ�����������빤��������أ�������Ķ�д�����������޵ģ�������������ġ����Թ�̬Ӳ��������ʱҲ������һ���Ŀռ䣬��ĳ���洢��Ԫ��������󼴰��𻵵Ĳ��ָ��룬�úõĲ��������档��һ�滻�����ͻ�еӲ�̵�������ӳ����һ������ֻ������еӲ������ʱ��������ӳ������������ڹ�̬Ӳ���Ǿ����Եġ� 
�����ڹ�̬Ӳ������һ������ݻ�����ʹ�ö�����������ֻҪ�������ٶȱ����ȶ��Ϳ��ԡ�ͨ������£�����ֵ��100����100�����滻��/����������������Ҳ���Թ����Ӳ�̵�ʣ�������� 
����Intel��̬Ӳ���ͺŵĵ�ʮ������ĸ��ʾ�����ֹ�񣬸���ĸΪ1��ʾ��һ����50���׼�����SSD��Ϊ2��ʾ�ڶ�����34���׼�����SSD����SSDSA2M160G2GN�ͱ�ʾ��34nm��SSD�����Բ����Ĳ鿴Ҳ����������� 
����50nm��SSD��һ����Ҫ����ǰֵ�����ֵ��ʼ��100���������滻���ʱ�����ֵ�����������仯��һֱ�����滻�ĸ���ʱ���ֵ��Ϊ1��֮��ÿ�����ĸ��鵱ǰֵ�ͣ�1��Ҳ����100��Ӧ0��3���飬1��Ӧ4��7���飬2��Ӧ8��11���顭�� 
����34nm��SSD��������ֱ�Ӳ鿴����ֵ������ֱֵ�ӱ�ʾ�ж��ٸ����滻�Ŀ顣


������

��������ʾ��

����Jul 17 00:46:34 xxxxxxxxxxxxxx kernel�� ��8384801.159283�� EXT4-fs ��sdl1���� warning�� mounting fs with errors�� running e2fsck is recommended

����Jul 17 00:50:00 xxxxxxxxxxxxxx kernel�� ��8385006.016500�� sd 6:0��6:0�� ��sdl�� Sense Key �� Medium Error ��current��

����Jul 17 00:50:00 xxxxxxxxxxxxxx kernel�� ��8385006.016508�� sd 6:0��6:0�� ��sdl�� Add. S��ense��ense�� Unrecovered read error

����Jul 17 00:50:00 xxxxxxxxxxxxxx kernel�� ��8385006.016524�� Buffer I/O error on device sdl1�� logical block 1415594116

����Jul 17 00:50:00 xxxxxxxxxxxxxx kernel�� ��8385006.095561�� Buffer I/O error on device sdl1�� logical block 1415594117

�������Ͻ����

����#e2fsck /dev/sdl1

����1��������block�޷��޸�������Ҫ��fdisk������������ʽ��Ӳ�̣���

����#fdisk /dev/sdl

����#d

����#n

����#p

����#Enter

����#Enter

����#w

����2����ext4�ļ�ϵͳ��ʽ�����̣�

����#mkfs.ext4 /dev/sdl1

����3���Ѹ�ʽ���õ�Ӳ��mount������

����#mount -L /Hadoop07 /hadoop/7 -t ext4 -o defaults��noatime��nodiratime��noauto

�������������/var/log/messages���������µ�/dev/sdl�Ĵ�����־���������Ӳ����Ҫ�����ˣ���ʱ�����Ƚ��������������Ŀ¼�Ķ�д���ܣ��ڴ�֮ǰ������Ȱ���������ݿ���������

����#chmod 0 /hadoop07

�������Ͼ���LinuxϵͳӲ�̳��ֹ��ϵ��޸������ˣ���Ȼ���������Ļ������Ǿ���Ӳ�̱�������⣬���ǲ��������ַ����޸��ġ�

==�� �ܽ᣺ e2fsck �����޸��߼��Ļ����� �������޸�Ӳ������Ļ���������Ļ���Ҫʹ�õͼ���ʽ�������޸���

@@@Linux�����޸�e2fsck����
�ͻ�������һ̨�����������ṩ���񣬾����Ų���ͻȻ�ϵ����ܲ����˴��̻������£�����ʹ��e2fsck��������˴����޸���

linux�´��̼���޸�����e2fsck
 
-a: ��� partition���緢��������Զ��޸���
-b: �趨 superblock λ�á� www.2cto.com  
-B size: ָ�� size ��Ϊ�����С��
-c: ��� partition �Ƿ��л��졣
-C file: ����������浽 file��
-d: ��� e2fsck debug �����
-f: e2fsck Ԥ��ֻ��Դ���ĵ���ϵͳ��飬���� -f ��ǿ�Ƽ�顣
-F: �ڼ��ǰ��Ӳ�̵� buffer cache ��գ����ⷢ������
-l list: ��¼�˻���������� list �С�
-d : ��ӡ e2fsck �� debug �����
-f : ǿ�Ƽ�顣
-n: �� (read-only) ��������ϵͳ
-p: �رջ���ģʽ�����������Զ��޸�����ͬ -a��
-v: ��ʾ��ϸ���档
-y: ����ʹ���߻���ģʽ��
 
ʹ������  www.2cto.com  
��� /dev/mapper/VolGroup00-LogVol02 �Ƿ������⣬�緢��������Զ��޸�:
 
e2fsck -a  /dev/mapper/VolGroup00-LogVol02
 
ִ�� e2fsck �� fsck ǰ���� umount partition�������л������ϵͳ����
 
����æ���������Ҫ�������漰�÷����Ľ���ɱ�����и����ٵķ�����ִ�� fuser -k /home ��
 
�����Ҫ�Ը�Ŀ¼ (/) ���м�鼰�޸�������Ҫ���� singal user mode ִ�С�
 
�������˽�����mount�ϡ�

@@@@@@��������޸�Ӳ�̻���
����Ӳ�̲��ôŽ������洢���ݣ��ھ�����ʱ���ʹ�û���ʹ�ò���֮������ᷢ��һЩ���⣬Ҳ��������ͨ����˵�Ĳ�������������
��Ȼ���ֻ����п���������Ĵ���Ҳ�п�����Ӳ�̱���Ӳ�����ϣ����ǲ�����˵Ӳ�����˻���֮��ͻᱨ�ϣ���ʵ�������õ���
������ȫ����������Ӳ�̡��ָ�������������Ҳ������Ӳ�̡��������١���

�����ķ���

����Ӳ�̳��ֻ�������Ӳ�̱��������Լ��ϻ���ԭ���⣬���кܴ�̶���������ƽʱʹ�ò�����ɵġ�Ӳ�̻������������ʿ��Է�Ϊ�߼����������������֣�����˵���߼�����������һЩ�������ʹ�ò�����ɵģ����ֻ�������ʹ������޸���������������Ӳ����Ƭ����ĴŽ��ʳ������⣬������Ƭ���������ˣ��������ͨ��ʹ�����Ҳ�޷��޸��Ĵ���

������Ӳ��һ������������Щ����ʱ����͸�ע��Ӳ���Ƿ��Ѿ������˻�����

������1���ڶ�ȡĳһ�ļ�������ĳһ����ʱ��Ӳ�̷��������ҳ�����ʾ�ļ��𻵵���Ϣ������Ҫ�����ܳ�ʱ����ܳɹ�����ʱ��������������ȣ�

������2��Ӳ������ͻȻ��ԭ��������Ħ��������˹�����

������3�����ų�������Ⱦ�������ϵͳ�޷��������������֡�Sectornotfound����GeneralerrorinreadingdriveC������ʾ��Ϣ��

������4��FormatӲ��ʱ����ĳһ����ֹͣ��ǰ����󱨴��޷���ɣ�

������5��ÿ��ϵͳ���������Զ�����Scandiskɨ����̴���

������6����Ӳ��ִ��FDISKʱ����ĳһ���Ȼᷴ���������ˣ�

������7������ʱ����ͨ��Ӳ������ϵͳ�����������������ת��Ӳ���̷������޷����룬��SYS�����ϵͳҲ���ܳɹ�������������п�����Ӳ�̵����������������⡣

�������޸�����

��������Ӳ���ڲ�����������Ҫ��Ϊ�ϸ�СС�Ļҳ����뵽Ӳ���ڲ�Ҳ����ɲ�����ص��𻵣����Ե�Ӳ�̳��ֻ���ʱ�����ǲ����ܲ�Ӳ�̽���ά�ޣ�ֻ�ܹ�ͨ��һЩ��������������޸����Ӷ�����޶ȵ������ʧ��������ȷ��Ӳ���л���֮�����ǲ�����ȷ����������������߼����˻����������ˣ�����ֻ�ܹ���ѭ�Ӽ򵥵����ӵĲ�������޸���һ���߼����������򵥵�����޸��Ϳ��Խ�����ϣ�����һЩ����������Ҫ��һ�����޸����ܱ�֤Ӳ�̵����ݰ�ȫ������ʹ�á�


@@�߼��������޸�
һ������£�Ӳ�̲����߼�������ԭ����һЩ�����������Ӳ����ĳЩ����д����Ϣ��������������޷����������������������£�Ӳ�̼�⹤��Ҳ������Ϊ�����������˻�����һ�����������������޸����������ڵ����Խ��Խ�ٵĲ������ּ��ܷ�ʽ�ˡ�

��������һ���������ʹ�ò�����ɵ��ˣ�����Ӳ���ڶ�ȡ����ʱ�����⵽���������п��ܲ����߼�������������ص���������������������Ǵ�ʱ����ʹ��Windows�Դ��Ĵ��̹��߶�Ӳ�̽���ɨ�裬���ҶԴ�������Զ��޸���

�������岽�����£���WindowsXPΪ���������ҵĵ�����ѡ���̷��󵥻�����Ҽ����ڵ��������������Դ���������ѡ�񡰹��ߡ���ʼ��顱


������ѡ���Զ��޸��ļ�ϵͳ���󡱺͡�ɨ�貢�ָ�����������Ȼ������ʼ


����ɨ��ʱ��������������ɨ��ѡ��Ĳ�ͬ���������졣����ֵ��ע����ǣ���Windows98�������ϵĲ���ϵͳ�У���������ʾÿ����������ϸ���������ͨ������������£�������û���ѡ��DOS�µĴ��̼�⹤��Scandisk��Scandisk����ÿ�����������һ��ǻ��������������ϵͳ��������������򡣱�֤��ϵͳ���е��ȶ������ݵİ�ȫ�ԡ�

����һ����˵��ͨ�������ķ������޸����֮��Ӳ���ϻ�����Ȼ���ڣ�ֻ�������˱�ǣ�ϵͳ������������ˣ��������Ŷ�Ӳ�̵ļ���ʹ�ã����ǿ��ܻᷢ��Ӳ�̻����п�����ɢ���������ַ��������ܴӸ����Ͻ�����⡣�Ƚ����Ƶİ취�Ƕ�Ӳ�����ݽ��б��ݣ�Ȼ�����·�����ʽ��Ӳ�̣�һ����˵�����Ӳ���ϵĹ��Ͻ������߼��������Ϳ��Գ��׵Ľ�����⡣��Ȼ�������ڽ������·����͸�ʽ��֮��ʹ��DOS��Scandisk�ٴζ�Ӳ�̽��м�⣬ȷ��Ӳ���߼���������ȫ�޸���

@@���������޸�
��������������������·�����ʽ��֮����Ȼ����Ӳ���л�������ôӲ�̺��п��ܾ������������ˡ���ʵ����������£�����Ҳ���ؼ��ڶ�Ӳ�̻����Ƿ�����޸��½��ۣ������Բ�������һ�������Ӳ�̽��е͸��ڽ������·�����ʽ������ЩӲ�̻���Ҳ�п���ͨ�����ַ�ʽ�õ������

����a���ͼ���ʽ��Ӳ��

�����͸�ķ�ʽ�����֣�һ����ͨ������BIOS�Դ��ĵ͸񹤾ߣ�һ���ǲ�������ķ�ʽ���е͸�ͨ������BIOS�Դ��ĵ͸񹤾ߵķ������ܵ���������ƣ���Щ������BIOS�в�û���䱸�����ĳ��򣬲���Ŀǰ���ͺŵ������඼û������͸�Ĺ����ˣ������Ƽ����ǲ�������ķ�ʽ������Ӳ�̵ĵͼ���ʽ����

����Maxtor��Ʒ��һ���͸񹤾�low.exe�����������Զ�MaxtorӲ�̽��е͸���ʵ���������������ڸ���Ʒ�Ƹ����ͺŵ�IDEӲ�̡�������Ĳ����൱��


��������֮�󰴡�Y�����������ֻ��ѡ����Ҫ�͸��Ӳ�̣�Ȼ��ѡ��ʼ�͸�ѡ�е�Ӳ�̾Ϳ����ˡ�


����һ��͸�Ĺ��̱Ƚϳ���������Ҫ���ĵĵȴ������⣬��Ҫ���Ѷ��ߵ�һ����ǣ������Ļ����ϻ���װ��������Ӳ�̣�������low����͸�����ʱ����ý����Ӳ��ж�£��������ݶ�ʧ��

����b������������

��������͸�֮����Ȼ�����л�������ô�������Կ϶������Ӳ�������������ˡ�����������ͨ��������Ӳ��ʹ��������ײ������ͻȻ�ϵ����������ģ�����Ƭ������תʱ����ͷ�п���ײ����Ƭ����ɴŽ������˶��γɵģ���ʹͨ�����̼�������������ǣ�����ϵͳ��Ȼ������������������������������ͨ����ʹ��һ��ʱ������ɢ������������Ȼ�������֮�󣬵���Ӳ����Ȼ���ܷ��ʵ�������Χ���������Ӷ����𻵵�����ɢ��Ϊ�˱��⻵������ɢ����������ǽ��������ε�һ��δʹ�õķ�����

�����������λ�����һ��δʹ�õķ���������ʹ�����PQMagic����������DOS��Windows�汾��������������ͨ���Ǹ�ʽ��Ӳ��֮������Ȼ�л���������ʱ��û�а�װWindowsϵͳ�������Ƽ�ʹ��DOS�汾��PQMagic�������İ汾����

�����ڲ���PQMagic���з���֮ǰ����������Ҫ�ҵ�������λ�á����ǿ�����ͨ��Scandisk���д��̱����ɨ�裬��Ӳ�̵Ļ�������λ�������˽�֮�󣬲���ȷ�������ķ���������Ӳ�̻����ڴ�Լ��C��20�����ң����ǾͿ�����PQMagic��Ӳ����C�̵�ǰ�����25����30���Ŀռ仮Ϊ���ط���������Ĳ����������£�����DOS�µ�PQMagic�������ͼ�����Ǿ���Windows�İ汾Ϊ��������ʾ��������ͬС�죩������PQMagic����ͼ�ν�������C�̵�ͼʾ�ϵ������Ҽ���ѡ�񡰵�������/�ƶ���


�����ͻ����һ�����������Ĺ�����������ֻ�轫C�̴�Ӳ�̵���ʼλ�������ƶ��Ϳ����ˡ��������Ĺ������·�Ҳ��Ӳ����ʼλ��֮��C��֮ǰ�����ɿռ��������ʾ


��������C������Ϊ10GB������ֻ�轫������ɿռ����Ϊ3GB���ҾͿ����ˣ���ʱ��C�̵������ͱ�Ϊ7GB�ˡ�����������У����齫���εĿռ�ѡ���Դ�һ�㣬�����ý��ƽ϶�ʧ��������������Ȼ������������C�̵Ŀռ���Ͼ����ڵ�Ӳ�̶���80GB��120GB����ʧ����������G���������ǾͿ������һ��Ӳ�̻���ֵ�õġ�ȷ��֮���˳����ȴ�PQMagic�ƶ�������Ȼ����������֮��Ӳ�̻������Ѿ������صķ����У�����ϵͳ���޷����ʵ��ˡ����߲������ַ����ɹ��Ľ�һ��80GBӲ�̵Ļ������Σ�ʹ��������Ȼ�ȶ�����ע�⣺��������ɻ�������֮����µķ�������һ��ɨ�裬��Ȼ�Ƽ�ʹ��Scandisk��ȷ�������Ѿ���ȫ���ε����صķ�������Ȼ�������Ŀռ��������ÿ�ϧ��Ҳ�����ڻ���֮ǰ�����µķ�������Ȼǰ���ǲ�Ҫ�ѻ����ٴλ��ֵ��µķ����У�������������ô��������������ಢ�ҹ�����ɢ����ϴ��Ӱ��������ܡ���

������Ȼ�����η��������������������Ӳ�̻����Ƚϼ��е���������Ӳ�̻����ȽϷ�ɢ�ͱȽ��鷳�ˣ��ͽ������Ӳ����ȷ��ϵͳ���ȶ������ݵİ�ȫ�ˡ�
ͨ������Ĳ��裬���ǾͿ����޸�Ӳ�̵��߼������������λ��������ط������Ӷ���֤ϵͳ���е��ȶ��Լ������ļ��İ�ȫ�����������Ĵ���֮��Ӳ�̾Ϳ������»����ഺ���߿�������޶ȵġ��������١��ˡ������ǲ���Ҳ�ܼ��أ�

@@@LINUXϵͳ�¼����̻���

Linux���Ӳ�̻���

����badblocks

��������˵����������װ�����𻵵����顣

�����﷨��badblocks [-svw][-b ][-o ][����װ��][����������][��ʼ����]

��������˵����ִ��ָ��ʱ��ָ����Ҫ���Ĵ���װ�ã�����װ�õĴ�����������

����������

����-b ָ�����̵������С����λΪ�ֽڡ�

����-o �����Ľ��д��ָ��������ļ���

����-s �ڼ��ʱ��ʾ���ȡ�

����-v ִ��ʱ��ʾ��ϸ����Ϣ��

����-w �ڼ��ʱ��ִ��д����ԡ�

����[����װ��] ָ��Ҫ���Ĵ���װ�á�

����[����������] ָ������װ�õ�����������

����[��ʼ����] ָ��Ҫ���ĸ����鿪ʼ��顣

����badblocks �����̻���

����1)$badblocks -s //��ʾ���� -v //��ʾִ����ϸ��� /dev/sda1

����2)��д��ʽ��� δ���صĴ����豸�����

����$badblocks -s //��ʾ���� -w //��дȥ��� -v //��ʾִ����ϸ��� /dev/sda2




linux��win�ǲ�ͬ�ģ��ϻ� ����win�´��̼�⹤��һץһ��ѣ����ò����õ�������Ķ��൱ţ������**��ʦ����**ר�ң����ǹ��õľͲ����ˡ��� 

linux�£���õĴ��̼�⹤����smartcontrol�ˣ�smartctl��

�����ҵ��ƶ�Ӳ�̾�Ȼ��֧��smart������ֻ���÷����������� 

����������ĳ�ߴ���ĳ���壬��������״��������320G eaget �ƶ�Ӳ���ϣ���������ˣ���Ϊ���ڽ��ж�д���������Խ��л�����⡣�����߰����� ��


����umount�Ѿ�mount���ƶ�Ӳ��

����:
umount /dev/sd*



���м�⣺

����һ��
����:
badblocks -s  -v  /dev/sd*1



��������
����:
sudo e2fsck -f -c /dev/sd*1



��Ϊ��Ҫ�Դ��̽��м�⣬�����ٶȷǳ�֮�������ڼ�������ע�ⲻҪ�ϵ磬��Ҫ��Ӳ�̽����κζ�д����Ҫ�Ƴ�Ӳ�̣���Ҫ�������ˣ���Ҫ�𶯵ȵȡ�

����Ӳ�̻�Ҫע��ɢ�ȡ�

�����̿�����;��ֹ��Ҳ����ָ���������¿�ʼ

�÷���
����:
sudo badblock /dev   last  start



����:
���ĵȴ��ɣ���320G�ƶ�Ӳ�̣�����2Сʱ��60%��Ȼ��Ϊ��д��ƪ���£����ߵİ�����ctrl+c

�Һÿ���ָ�����鿪ʼ



���㿴����
����:
Pass completed, 0 bad blocks found.



��ϲ����û�л��������>0����ô��Ҳ�����ˡ���������޸��ɣ���

����:
����
1��fsckʹ��badblocks����Ϣ
badblocksֻ������־�ļ��б�ǳ���������Ϣ������ϣ���ڼ�����ʱҲ��������Щ���鲻��⣬����ʹ��fsck��-l������

# -l /tmp/ /dev/hda1

2���ڴ����ļ�ϵͳǰ��⻵��
badblocks������e2fsck��mke2fs��-cɾ��һ�����У���ext3�ļ�ϵͳҲһ�������ڴ����ļ�ϵͳǰ���ȼ�⻵����Ϣ��


# -c /dev/hda1

�����ʾʹ��-c�ڴ����ļ�ϵͳǰ��黵����Ӳ�̡�
��������Ѿ�������ظ�֪���ǿ��Բ��á� -c��ѡ���á�read-only����ʽ���Ӳ�̡����������ڸ�ʽ��Ӳ��ʱ���Ӳ�̣�����������Ӳ�̡�block���������������ʽ��Ӳ�̣���Ҫ���൱������ģ���Ϊ�������к󣬻�һ�����ö��ķ�ʽ���Ӳ�̡�




�����Լ������Ϣ��ο���

/> />
2009-10-04 update:

���������320G�ƶ�Ӳ��read-only badblock test

���û��á�
����:
delectate@delectate-laptop:~$ umount /dev/sdc1
delectate@delectate-laptop:~$ umount /dev/sdc2
delectate@delectate-laptop:~$ sudo badblocks -s -v /dev/sdc1
[sudo] password for delectate: 
Checking blocks 0 to 304182710
Checking for bad blocks (read-only test): done 
Pass completed, 0 bad blocks found.
delectate@delectate-laptop:~$ sudo badblocks -s -v /dev/sdc2
[sudo] password for delectate: 
Checking blocks 0 to 8385929
Checking for bad blocks (read-only test): done 
Pass completed, 0 bad blocks found.
delectate@delectate-laptop:~$



����˵���ƶ�Ӳ�̣�Ӧ�ö��ע����ǡ�

ÿ�ΰ���ʱ��Ҫumount��Ȼ���ٰ��¡�

�����ҳ��Թ�����һ��umount�����ϰ��£�Ӳ�������죬Ƶ�ʺܸߵĿ�֧��������umount���10s�����ٰ���������û�У�����Ӧ���Ǵ�ͷ��landing zone��ʱ��ɣ�

�ƶ�Ӳ�̲���u�̣����С�ģ����ע�����Ŷ���� 

update : 2009-12-05

�����������Ҽ�����̷���Ȼ��ѡ��safely remove this device�����󲿷��ƶ�Ӳ�̿����Զ�ж�ز�ֹͣת����������Ҫ���л�������ͯЬ����Ҫ������ѡ�����ж�ؼ��ɡ���

�����ɺ󣬿���mount���ٵ���Ǹ���safely remove device����ʹ�ƶ�Ӳ��ֹͣת����

���󲿷��ƶ�Ӳ�̿���ֹͣת��������С���ֵĻ��ǲ����ԣ�ԭ��δ֪��Ӧ����Ӳ�̺����⡣��

 

 

==============================================================

 

 

 

���̻������������˶���ϣ�����������顭��

���̻�����������������½�������ϵͳ����ʧ�ܣ����ݶ�ʧ����������Ҫʱ�̹�ע���̽���״������ʱ������Ҫ���ݡ�

ʲô��S.M.A.R.T��

ȫ��Ϊ Self��Monitoring Analysis and Report Technology �����ڴ������Ҽ�⣬�����û��������״̬���������Ҫ����֧�֣��Ҽ������һ��׼ȷ��

linux�Ͽ���ʹ��gnome-disk-utility�鿴���̵�S.M.A.R.T�����Ϣ��

��Ҳ���԰�װ

1
	

sudo pacman -S libatasmart smartmontools gsmartcontrol

����smartͼ�λ�����(gsmartcontrol)/cli����(smartctl)���в鿴��

���³�˹�ش��̣���Ӳ��ԭ��

����ԭ����Ƿǹ���ʱ���ͷͣ����landing zone����Ҫ��ȡ����ʱ����ͷ�뿪landing zone��������Ƭ����ת����������������Ƭ�����ȡ���ݡ�

��Ϊ��Ƭ��ת�ٶȷǳ��죬�Ҵ�ͷ����Ƭ����ǳ�����ͷ��˿��ǧ��֮һ������������𶯻������������������ѹ���ȣ����п��ܵ��´�ͷ�������ת����Ƭ��������Ӵ�����ɲ����޸��������𻵡�

�����Ĵ��̣�

 

1.�ڶ�ȡĳһ�ļ�������ĳһ����ʱ��Ӳ�̷��������ҳ�����ʾ�ļ��𻵵���Ϣ������Ҫ�����ܳ�ʱ����ܳɹ�����ʱ���������������            

2.io wait �޹����߻�Ӹ߲��£�

3.Ӳ������ͻȻ��ԭ��������Ħ��������˹�����

4.ϵͳ�޷��������������֡�IO error������ʾ��Ϣ��

5.mkfsʱ����ĳһ����ֹͣ��ǰ����󱨴��޷���ɣ�

6.ÿ��ϵͳ���������Զ�����fsckɨ����̴���

7.��Ӳ��ִ��FDISKʱ����ĳһ���Ȼᷴ���������ˣ�

8.������Ĵ��̳�������״����������Ҫ��ʱ�Դ��̽��л�������Բ��Դ��̿����ԣ��������������ݡ�

 

�����̻������

����ʹ��livecd����liveusb�Ա��ش��̽��м�⡣����Ƕ��ƶ��洢�豸���м�⣬��umount���ٽ��м�⣬������������

1
	

umount /dev/sd*

�Դ��̽���read-only��⣺

 
	

sudo badblocks -s  -v  /dev/sd*

��Ϊ��Ҫ�Դ��̽��м�⣬�����ٶȷǳ��������ڼ�������ע�ⲻҪ�ϵ磬��Ҫ��Ӳ�̽����κβ�������Ҫ�Ƴ�Ӳ�̣���Ҫ�������ˣ���Ҫ�𶯵ȡ�

�����̿�����;��ֹ��Ҳ����ָ���������¿�ʼ��

1
	

sudo badblock -s -v  /dev/sd*   last  start

����������ɺ󿴵�

Pass completed, 0 bad blocks found.

��ô��ϲ���˴���ͨ�����ԣ�û�л��������飩�������Է���ʹ�á�

�������л����ˡ���

���ǣ����������������ĳһ������ͣ�Ͳ�ǰ�����󱨸�����ʾ�л��飬��ô�����ˡ������Ĵ����л����ˡ�

������ʲô���͵Ļ����������������Ƚ������ݱ��ݣ�����Ҫ���ݽ��б���Ȼ���ٳ����޸������������Ҫ����ȴ�޷���ȡ�����̳����쳣������ô������ֹͣʹ�ô˴��̲���רҵ��Ա�����޸���

���������޸�/����

����������Ϊ���¼������ͣ�

��              

o �߼�����

o 0�ŵ���

o ������

����һ���Ե������������ʽ���֡�

���߼������޸���

1
	

fsck -a /dev/sd*

����ô�򵥡�

����fsck�÷������Բ鿴������߲鿴man�ֲᡣ

��0�ŵ����޸���

ʹ��1�ŵ�������ŵ�������Σ���������

�������̾���ȫ�̸�ʽ����Ȼ�����·������༭������ʹ��1�ŵ����Ӷ�����Ӳ�̡�

�����ֲᣨ1��2��3��

��������

������û���޸������ԣ�ֻ�ܽ������Ρ�

������Ѿ������˻�����⣬��ô���϶��Ѿ�֪�����������飩����λ���Լ������С������Ҫ��

1.����Ӳ������

2.ɾ������Ӳ�̷���

3.���ݻ���λ���Լ���С���������ռ�ռ䣨���繲100�����飬���̴�СΪ100g��20-30�𻵣��򻵿���20-30g������䣩

4.���з��������ϣ�����ӦΪ 0-15|15-35|35-100���м��15-35gΪ�л����ķ�����Ҫ���л����ķ����������ݴ�����ֵ��Ҫ��С�����⻵�����ֵ�������������

5.����15-35g����������������أ�����д����������

6.���Ĵ��̿��ÿռ���٣�����ʣ��ռ�����ã������Ѿ����Σ�

����������������ɢ�ԣ����Խ��龡���ô��̡����ݡ����ǡ���

���������޸�����

������ķ������Ѿ����𻵣�����ʹ��testdisk�����޸��������Կ��ٻظ���������ķǳ����ã��޸��ҵ�Ӳ��n�Σ�����Ҳ����

��װ

1
	

sudo pacman -S testdisk

�����÷���1��2��

���䰮���̣���������

�����мۣ������޼�

��Ҫ�ȴ��̳��������˲��뵽���ݻ�û�б��ݣ����������Ķ��˲������������Ҫ������Ҫ��rm�˲�����������Ҫ�ļ�ɾ���ˡ��������ݲ����Ƕ�ô���ѣ�Ҳ����Ҫ����ʱ�䣬����������ʱ���ݣ������޼۵����ݰɣ�


@@@@
2016-10-13 09:51:01*[�Ž���10026634]˵:
diskman��ֱ�Ӷ���Ӳ�̼Ĵ�������Ӳ�������¼��ʵ��Э�����ʣ���Ӳ����expander
2016-10-13 09:51:27*[�Ž���10026634]˵:
lsiman��diskman��һ���ģ�ֱ�Ӷ���Ӳ���Ĵ���
2016-10-13 09:51:38*[�����10185097]˵:
������--expander  �� expander--Ӳ��
2016-10-13 09:51:51*[�����10185097]˵:
���������Э�����ʿ��Բ�һ����
2016-10-13 09:52:01*[�Ž���10026634]˵:
�ǵ�Ȼ��һ����
2016-10-13 09:52:47*[�����10185097]˵:
�����˼�������ʱ�� ���к����е�ͨ���������ǲ�һ�µ���
2016-10-13 09:52:49*[�Ž���10026634]˵:
������--expander��������controller��-��expander֮���Ǹ������ʾ����ģ�
2016-10-13 09:53:24*[�����10185097]˵:
��expander--disk֮���أ�
2016-10-13 09:53:53*[�����10185097]˵:
Ҳ��ȡexpander��Ӳ�̽ӿ������еĵ͵���
2016-10-13 09:56:37*[�Ž���10026634]˵:
expander--Ӳ����������expander��disk֮���Ǹ������ʾ�����
2016-10-13 09:57:42*[�Ž���10026634]˵:
����expander��controller����sas3������sas2.0�̣���expander--disk��sas2.0����controller-expander�� sas3
2016-10-13 09:58:49*[�����10185097]˵:
���к��������ʲ�һ�£�����������������


@@@@@
3.2	����SAS Controller��SAS ExpanderоƬ�ӿ�������Ϣ
SAS2 controller��6Gbps����
LSI SAS1064E��SAS2008��SAS2308��Mega2208оƬ��
PMC 8001оƬ��6805��7805 PCIe����
     
SAS3 controller��12Gbps����
LSI SAS3008��Mega3108оƬ
PMC 8068оƬ��OCSA��Ŀʹ�ã��� 
PMC8072 оƬ����֧��RAID����USPʹ�ã�
8805 PCIe����PMC������
Renegade8000-16i��smartHBA��HP������128MB���棩

     SAS2 expander��6Gbps����
          ����(Maxim)��MAX72044(44-port)��72038(38-port)��72024(24-port)��72018(18-port)
          PMC��8005
     
SAS3 expander��12Gbps����
LSI 3X36
PMC 8054



@@@@
MegaCliʹ�÷���


ѡ����Ӧ�汾�İ�װ��

����֮���ѹ��

unzip CSA1.5-MegaCli_REL80571.zip

cd MegaCLI/MegaCli_Linux

rpm -ivh MegaCli-8.05.71-1.noarch.rpm


��װ���

ln -s /opt/MegaRAID/MegaCli/MegaCli64 /usr/bin/

Ĭ�ϰ�װ��/opt���棬����������/usr/bin



MegaCli���ò������� 
MegaCli -adpCount ����ʾ������������
MegaCli -AdpGetTime �CaALL ����ʾ������ʱ�䡿
MegaCli -AdpAllInfo -aAll     ����ʾ������������Ϣ��
MegaCli -LDInfo -LALL -aAll    ����ʾ�����߼���������Ϣ��
MegaCli -PDList -aAll    ����ʾ���е�������Ϣ��
MegaCli -AdpBbuCmd -GetBbuStatus -aALL |grep ��Charger Status�� ���鿴���״̬��
MegaCli -AdpBbuCmd -GetBbuStatus -aALL����ʾBBU״̬��Ϣ��
MegaCli -AdpBbuCmd -GetBbuCapacityInfo -aALL����ʾBBU������Ϣ��
MegaCli -AdpBbuCmd -GetBbuDesignInfo -aALL    ����ʾBBU��Ʋ�����
MegaCli -AdpBbuCmd -GetBbuProperties -aALL    ����ʾ��ǰBBU���ԡ�
MegaCli -cfgdsply -aALL    ����ʾRaid���ͺţ�Raid���ã�Disk�����Ϣ��

�Ŵ�״̬�ı仯���Ӱ��̣������̵Ĺ����С� 
Device         |Normal|Damage|Rebuild|Normal
Virtual Drive     |Optimal|Degraded|Degraded|Optimal
Physical Drive     |Online|Failed �C> Unconfigured|Rebuild|Online

������ʾ����
MegaCli -PDList -aALL
��������������Ӳ�̵���Ϣ��
MegaCli -LDPDInfo -aall
�����������߼��豸(�Ұ�LD��֮ΪLogical Device)������Ӳ��֮��Ĺ�ϵ��
MegaCli -CfgLdAdd -r(0|1|5) [E:S, E:S, ...] -aN
�������������µ�raid 0,1,5�������豸������
MegaCli -LDBI -ProgDsply -LALL -aALL
����������raid��building���ȵ�

һ����linux����MegaCli��ά��dell������raid��Ҳ������windows���ã�
%SystemRoot%\system32\GAMSERV\megacli -adpeventlog -getevents -f d:\%computername%_nvram.log -aall  ��ҪװMylex Global Array Manager�����



@@@Ӳ��smart���ܣ�
 �����̵� Smart �����Ƿ�����
 smartctl -i /dev/sdb
  �����������SMART support is: Enabled��
  
  ���ô��̵� Smart ����
  smartctl -s on /dev/sdb
  
  ���ô��̵� Smart ����
  smartctl -s off  /dev/sdb
  
  ��ʾ���̵���ϸ Smart ��Ϣ
  root@linuxtechi:~# smartctl -a /dev/sdb              // For IDE drive
root@linuxtechi:~# smartctl -a -d ata /dev/sdb       // For SATA drive  �������ã�

��ʾ�������彡��״��
smartctl -H  /dev/sdb


ʹ��long��shortѡ�����Ӳ��
Long����
smartctl --test=long /dev/sdb

Short����
smartctl --test=short /dev/sdb

ע�⣺short���Խ��������2���ӣ�����long������û��ʱ�����ƣ���Ϊ�����ȡ����֤���̵�ÿ����

 �鿴���������Լ���
 
 smartctl -l selftest /dev/sdb
 
 �������ʱ���ֵ
 
 smartctl -c  /dev/sdb
 
 ��ʾ���̴�����־
 
 smartctl -l error  /dev/sdb

 
 
 
 @@@@Ӳ��smart��Ϣ��ע��
 *******************************************************
Slot                      : 0
*******************************************************

DeviceId                  : 18
Device Model              : WDC WD4000FYYZ-0
Serial Number             :      WD-WMC130F2DNV2
Firmware Version          : 01.01K04
Capacity                  : 4000GB

form factor               : not reported
sector type               : 512n
Interface Type            : SATA3.0 (V2.5/3.0: 3Gbps/6Gbps)
Support Max Speed         : 6.0Gbps
Negotiated link Speed     : 6.0Gbps
WWN(ata address)          : 50014ee606712e09
Disk Medium Type          : HDD (RotaRate=7200)
ssd support trim/unamp    : no 

Write Cache Support       : Yes
Write Cache Status        : Off

SMART Attributes Data Structure revision number: 16
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  1 Raw_Read_Error_Rate     0x002f   200   200   051    Pre-fail  Always       -       0
  3 Spin_Up_Time            0x0027   152   148   021    Pre-fail  Always       -       11383
  4 Start_Stop_Count        0x0032   100   100   000    Old_age   Always       -       32
  5 Reallocated_Sector_Ct   0x0033   200   200   140    Pre-fail  Always       -       0
  7 Seek_Error_Rate         0x002e   200   200   000    Old_age   Always       -       0
  9 Power_On_Hours          0x0032   098   098   000    Old_age   Always       -       1614
 10 Spin_Retry_Count        0x0032   100   253   000    Old_age   Always       -       0
 11 Calibration_Retry_Count 0x0032   100   253   000    Old_age   Always       -       0
 12 Power_Cycle_Count       0x0032   100   100   000    Old_age   Always       -       32
 16 Unknown_Attribute       0x0022   045   155   000    Old_age   Always       -       2456698452125
183 Unknown_Attribute       0x0032   100   100   000    Old_age   Always       -       0
192 Power-Off_Retract_Count 0x0032   200   100   000    Old_age   Always       -       29
193 Load_Cycle_Count        0x0032   200   100   000    Old_age   Always       -       1194
194 Temperature_Celsius     0x0022   131   095   000    Old_age   Always       -       21
196 Reallocated_Event_Count 0x0032   200   200   000    Old_age   Always       -       0
197 Current_Pending_Sector  0x0032   200   200   000    Old_age   Always       -       0
198 Offline_Uncorrectable   0x0030   200   200   000    Old_age   Offline      -       0
199 UDMA_CRC_Error_Count    0x0032   200   200   000    Old_age   Always       -       0
200 Multi_Zone_Error_Rate   0x0008   200   200   000    Old_age   Offline      -       0


*******************************************************
Slot                      : 1
*******************************************************

DeviceId                  : 15
Device Model              : WDC WD2000FYYZ-0
Serial Number             :      WD-WCC1P0488710
Firmware Version          : 01.x1Kx2
Capacity                  : 2000GB

form factor               : not reported
sector type               : 512n
Interface Type            : SATA3.0 (V2.5/3.0: 3Gbps/6Gbps)
Support Max Speed         : 3.0Gbps
Negotiated link Speed     : 3.0Gbps
WWN(ata address)          : 50014ee25dfaf4a4
Disk Medium Type          : HDD (RotaRate=7200)
ssd support trim/unamp    : no 

Write Cache Support       : Yes
Write Cache Status        : Off

SMART Attributes Data Structure revision number: 16
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  1 Raw_Read_Error_Rate     0x002f   198   005   051    Pre-fail  Always   In_the_past 24
  3 Spin_Up_Time            0x0027   167   160   021    Pre-fail  Always       -       6625
  4 Start_Stop_Count        0x0032   100   100   000    Old_age   Always       -       958
  5 Reallocated_Sector_Ct   0x0033   135   135   140    Pre-fail  Always   FAILING_NOW 2027
  7 Seek_Error_Rate         0x002e   100   253   000    Old_age   Always       -       0
  9 Power_On_Hours          0x0032   099   099   000    Old_age   Always       -       1435
 10 Spin_Retry_Count        0x0032   100   100   000    Old_age   Always       -       0
 11 Calibration_Retry_Count 0x0032   100   100   000    Old_age   Always       -       0
 12 Power_Cycle_Count       0x0032   100   100   000    Old_age   Always       -       957
183 Unknown_Attribute       0x0032   100   100   000    Old_age   Always       -       0
192 Power-Off_Retract_Count 0x0032   199   199   000    Old_age   Always       -       954
193 Load_Cycle_Count        0x0032   200   200   000    Old_age   Always       -       3
194 Temperature_Celsius     0x0022   129   089   000    Old_age   Always       -       21
196 Reallocated_Event_Count 0x0032   176   176   000    Old_age   Always       -       24
197 Current_Pending_Sector  0x0032   200   198   000    Old_age   Always       -       0
198 Offline_Uncorrectable   0x0030   200   200   000    Old_age   Offline      -       0
199 UDMA_CRC_Error_Count    0x0032   200   200   000    Old_age   Always       -       10
200 Multi_Zone_Error_Rate   0x0008   200   200   000    Old_age   Offline      -       0


*******************************************************
Slot                      : 2
*******************************************************

DeviceId                  : 16
Device Model              : WDC WD4000FYYZ-0
Serial Number             :      WD-WMC130F5ARAD
Firmware Version          : 01.01K04
Capacity                  : 4000GB

form factor               : not reported
sector type               : 512n
Interface Type            : SATA3.0 (V2.5/3.0: 3Gbps/6Gbps)
Support Max Speed         : 6.0Gbps
Negotiated link Speed     : 6.0Gbps
WWN(ata address)          : 50014ee65bc36ea3
Disk Medium Type          : HDD (RotaRate=7200)
ssd support trim/unamp    : no 

Write Cache Support       : Yes
Write Cache Status        : Off

SMART Attributes Data Structure revision number: 16
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  1 Raw_Read_Error_Rate     0x002f   200   195   051    Pre-fail  Always       -       36
  3 Spin_Up_Time            0x0027   150   147   021    Pre-fail  Always       -       11483
  4 Start_Stop_Count        0x0032   100   100   000    Old_age   Always       -       30
  5 Reallocated_Sector_Ct   0x0033   133   133   140    Pre-fail  Always   FAILING_NOW 2063
  7 Seek_Error_Rate         0x002e   200   200   000    Old_age   Always       -       0
  9 Power_On_Hours          0x0032   096   096   000    Old_age   Always       -       3028
 10 Spin_Retry_Count        0x0032   100   253   000    Old_age   Always       -       0
 11 Calibration_Retry_Count 0x0032   100   253   000    Old_age   Always       -       0
 12 Power_Cycle_Count       0x0032   100   100   000    Old_age   Always       -       30
 16 Unknown_Attribute       0x0022   102   098   000    Old_age   Always       -       5517221621289
183 Unknown_Attribute       0x0032   100   100   000    Old_age   Always       -       0
192 Power-Off_Retract_Count 0x0032   200   100   000    Old_age   Always       -       28
193 Load_Cycle_Count        0x0032   200   200   000    Old_age   Always       -       238
194 Temperature_Celsius     0x0022   129   080   000    Old_age   Always       -       23
196 Reallocated_Event_Count 0x0032   165   165   000    Old_age   Always       -       35
197 Current_Pending_Sector  0x0032   200   200   000    Old_age   Always       -       2
198 Offline_Uncorrectable   0x0030   200   200   000    Old_age   Offline      -       0
199 UDMA_CRC_Error_Count    0x0032   200   199   000    Old_age   Always       -       83
200 Multi_Zone_Error_Rate   0x0008   200   200   000    Old_age   Offline      -       20


*******************************************************
Slot                      : 3
*******************************************************

DeviceId                  : 17
Device Model              : WDC WD4000FYYZ-0
Serial Number             :      WD-WMC130F5V9L6
Firmware Version          : 01.x1Kx2
Capacity                  : 4000GB

form factor               : not reported
sector type               : 512n
Interface Type            : SATA3.0 (V2.5/3.0: 3Gbps/6Gbps)
Support Max Speed         : 6.0Gbps
Negotiated link Speed     : 6.0Gbps
WWN(ata address)          : 50014ee65bc41276
Disk Medium Type          : HDD (RotaRate=7200)
ssd support trim/unamp    : no 

Write Cache Support       : Yes
Write Cache Status        : Off

SMART Attributes Data Structure revision number: 16
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  1 Raw_Read_Error_Rate     0x002f   197   001   051    Pre-fail  Always   In_the_past 135
  3 Spin_Up_Time            0x0027   154   149   021    Pre-fail  Always       -       11258
  4 Start_Stop_Count        0x0032   100   100   000    Old_age   Always       -       29
  5 Reallocated_Sector_Ct   0x0033   134   134   140    Pre-fail  Always   FAILING_NOW 2052
  7 Seek_Error_Rate         0x002e   200   200   000    Old_age   Always       -       0
  9 Power_On_Hours          0x0032   098   098   000    Old_age   Always       -       1686
 10 Spin_Retry_Count        0x0032   100   253   000    Old_age   Always       -       0
 11 Calibration_Retry_Count 0x0032   100   253   000    Old_age   Always       -       0
 12 Power_Cycle_Count       0x0032   100   100   000    Old_age   Always       -       29
183 Unknown_Attribute       0x0032   100   100   000    Old_age   Always       -       0
192 Power-Off_Retract_Count 0x0032   200   100   000    Old_age   Always       -       27
193 Load_Cycle_Count        0x0032   200   200   000    Old_age   Always       -       1
194 Temperature_Celsius     0x0022   130   087   000    Old_age   Always       -       22
196 Reallocated_Event_Count 0x0032   180   180   000    Old_age   Always       -       20
197 Current_Pending_Sector  0x0032   200   200   000    Old_age   Always       -       304
198 Offline_Uncorrectable   0x0030   200   200   000    Old_age   Offline      -       0
199 UDMA_CRC_Error_Count    0x0032   200   200   000    Old_age   Always       -       0
200 Multi_Zone_Error_Rate   0x0008   191   191   000    Old_age   Offline      -       2914


*******************************************************
Slot                      : 4
*******************************************************

DeviceId                  : 19
Device Model              : WDC WD4000FYYZ-0
Serial Number             :      WD-WMC130F6X0UY
Firmware Version          : 01.x1Kx2
Capacity                  : 4000GB

form factor               : not reported
sector type               : 512n
Interface Type            : SATA3.0 (V2.5/3.0: 3Gbps/6Gbps)
Support Max Speed         : 6.0Gbps
Negotiated link Speed     : 6.0Gbps
WWN(ata address)          : 50014ee6b12b4400
Disk Medium Type          : HDD (RotaRate=7200)
ssd support trim/unamp    : no 

Write Cache Support       : Yes
Write Cache Status        : Off

SMART Attributes Data Structure revision number: 16
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  1 Raw_Read_Error_Rate     0x002f   100   253   051    Pre-fail  Always       -       0
  3 Spin_Up_Time            0x0027   164   137   021    Pre-fail  Always       -       10758
  4 Start_Stop_Count        0x0032   100   100   000    Old_age   Always       -       25
  5 Reallocated_Sector_Ct   0x0033   133   133   140    Pre-fail  Always   FAILING_NOW 2063
  7 Seek_Error_Rate         0x002e   196   195   000    Old_age   Always       -       12038
  9 Power_On_Hours          0x0032   098   098   000    Old_age   Always       -       1648
 10 Spin_Retry_Count        0x0032   100   253   000    Old_age   Always       -       0
 11 Calibration_Retry_Count 0x0032   100   253   000    Old_age   Always       -       0
 12 Power_Cycle_Count       0x0032   100   100   000    Old_age   Always       -       25
183 Unknown_Attribute       0x0032   100   100   000    Old_age   Always       -       0
192 Power-Off_Retract_Count 0x0032   200   100   000    Old_age   Always       -       23
193 Load_Cycle_Count        0x0032   200   200   000    Old_age   Always       -       1
194 Temperature_Celsius     0x0022   131   085   000    Old_age   Always       -       21
196 Reallocated_Event_Count 0x0032   001   001   000    Old_age   Always       -       2063
197 Current_Pending_Sector  0x0032   197   197   000    Old_age   Always       -       2127
198 Offline_Uncorrectable   0x0030   200   197   000    Old_age   Offline      -       0
199 UDMA_CRC_Error_Count    0x0032   200   200   000    Old_age   Always       -       0
200 Multi_Zone_Error_Rate   0x0008   001   001   000    Old_age   Offline      -       131000


*******************************************************
Slot                      : 10
*******************************************************

DeviceId                  : 13
Device Model              : HGST HUS726040AL
Serial Number             : N8GK11DY            
Firmware Version          : APGNT90A
Capacity                  : 4000GB

form factor               : 3.5inch 
sector type               : 512e
Interface Type            : SATA3.1 (V2.5/3.0: 3Gbps/6Gbps)
Support Max Speed         : 6.0Gbps
Negotiated link Speed     : 6.0Gbps
WWN(ata address)          : 5000cca244c7be3b
Disk Medium Type          : HDD (RotaRate=7200)
ssd support trim/unamp    : no 

Write Cache Support       : Yes
Write Cache Status        : Off

SMART Attributes Data Structure revision number: 16
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  1 Raw_Read_Error_Rate     0x000b   100   100   016    Pre-fail  Always       -       0
  2 Throughput_Performance  0x0005   137   137   054    Pre-fail  Offline      -       104
  3 Spin_Up_Time            0x0007   153   153   024    Pre-fail  Always       -       322 (Average 375)
  4 Start_Stop_Count        0x0012   100   100   000    Old_age   Always       -       123
  5 Reallocated_Sector_Ct   0x0033   100   100   005    Pre-fail  Always       -       0
  7 Seek_Error_Rate         0x000b   100   100   067    Pre-fail  Always       -       0
  8 Seek_Time_Performance   0x0005   128   128   020    Pre-fail  Offline      -       18
  9 Power_On_Hours          0x0012   100   100   000    Old_age   Always       -       338
 10 Spin_Retry_Count        0x0013   100   100   060    Pre-fail  Always       -       0
 12 Power_Cycle_Count       0x0032   100   100   000    Old_age   Always       -       119
192 Power-Off_Retract_Count 0x0032   100   100   000    Old_age   Always       -       134
193 Load_Cycle_Count        0x0012   100   100   000    Old_age   Always       -       134
194 Temperature_Celsius     0x0002   171   171   000    Old_age   Always       -       35 (Lifetime Min/Max 24/55)
196 Reallocated_Event_Count 0x0032   100   100   000    Old_age   Always       -       0
197 Current_Pending_Sector  0x0022   100   100   000    Old_age   Always       -       0
198 Offline_Uncorrectable   0x0008   100   100   000    Old_age   Offline      -       0
199 UDMA_CRC_Error_Count    0x000a   200   200   000    Old_age   Always       -       0


*******************************************************
Slot                      : 31
*******************************************************

DeviceId                  : 14
Device Model              : ST9500620NS     
Serial Number             :             9XF1JQSX
Firmware Version          : SN03    
Capacity                  : 500GB

form factor               : 2.5inch 
sector type               : 512n
Interface Type            : SATA3.0 (V2.5/3.0: 3Gbps/6Gbps)
Support Max Speed         : 6.0Gbps
Negotiated link Speed     : 6.0Gbps
WWN(ata address)          : 5000c5003ceb2e21
Disk Medium Type          : HDD (RotaRate=7200)
ssd support trim/unamp    : no 

Write Cache Support       : Yes
Write Cache Status        : On

SMART Attributes Data Structure revision number: 1
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  1 Raw_Read_Error_Rate     0x000f   083   065   044    Pre-fail  Always       -       228196240
  3 Spin_Up_Time            0x0003   096   096   000    Pre-fail  Always       -       0
  4 Start_Stop_Count        0x0032   100   100   020    Old_age   Always       -       563
  5 Reallocated_Sector_Ct   0x0033   100   100   036    Pre-fail  Always       -       0
  7 Seek_Error_Rate         0x000f   060   060   030    Pre-fail  Always       -       1204238
  9 Power_On_Hours          0x0032   100   100   000    Old_age   Always       -       320
 10 Spin_Retry_Count        0x0013   100   100   097    Pre-fail  Always       -       0
 12 Power_Cycle_Count       0x0032   100   100   020    Old_age   Always       -       563
184 Unknown_Attribute       0x0032   100   100   099    Old_age   Always       -       0
187 Reported_Uncorrect      0x0032   100   100   000    Old_age   Always       -       0
188 Unknown_Attribute       0x0032   100   100   000    Old_age   Always       -       0
189 High_Fly_Writes         0x003a   100   100   000    Old_age   Always       -       0
190 Airflow_Temperature_Cel 0x0022   066   060   045    Old_age   Always       -       34 (Lifetime Min/Max 30/34)
191 G-Sense_Error_Rate      0x0032   100   100   000    Old_age   Always       -       0
192 Power-Off_Retract_Count 0x0032   100   100   000    Old_age   Always       -       560
193 Load_Cycle_Count        0x0032   100   100   000    Old_age   Always       -       673
194 Temperature_Celsius     0x0022   034   040   000    Old_age   Always       -       34 (0 15 0 0)
195 Hardware_ECC_Recovered  0x001a   119   100   000    Old_age   Always       -       228196240
197 Current_Pending_Sector  0x0012   100   100   000    Old_age   Always       -       0
198 Offline_Uncorrectable   0x0010   100   100   000    Old_age   Offline      -       0
199 UDMA_CRC_Error_Count    0x003e   200   200   000    Old_age   Always       -       0
 




@@@@@@@@@@@@@ suse ϵͳ���ã�

suse ��������yast����Դ:
 ���iso�ļ������ص�/mntĿ¼��
 �������Ŀ¼���뵽Դ�б���
zypper sa file:///media local-sles 

 SuSE�����װ��� zypper��yast2 
 SuSE�����װ��� zypper��yast2 
 
 suse �� 
zypper se xxxxx �����������
zypper in xxxxx �����apt-get install xxxx�ȼ�
zypper rm xxxx  ɾ��
zypper up xxxx �������

SuSE��ʵ�ṩһ������ͼ�λ�����Ĺ���yast����ʵ�ֹ�������Ҫ���ֹ����á������ʹ�ã���ô�ҿ϶�����������ߣ����������ѧϰ����ô������ʵ�޸������ļ�����Ƚ������˽⡣
 
 --��ѯ���
 zypper search ssh
 
 --��װ���
 zypper install openssh

yast2 -i openssh

@@@@@@@@@@@@@@@@@@@@@@@@@@@@

������OS��Linux SUSE 11 sp2 64bit

           Ӳ����IBM x3650 M3������(��82599EB����)

�������󣺵�����10G��ģ���ʱ��ifconfig�޷���ʾ�ӿڣ����ߵ��½ӿ���ʧ��

��λ���̣�dmesg���֡�failed to load because an unsupported SFP+ module type was detected.����Ϣ���Դ���Ϣgoogle�����������ӣ�

http://discussions.citrix.com/topic/306986-xenserver-60-issues-with-intel-82598eb-10-gigabit-af-dual-port-nic/

���ۣ�82599EBֻ֧����intel�ԼҵĹ�ģ��Խӡ����ҵĹ�ģ����finisar�ġ�

����취��ж����������allow_unsupported_sfp=1�������¼���

                 modprobe -r ixgbe;modprobe ixgbe allow_unsupported_sfp=1
				 


@@@@running  need to check

��Ϊ cache off: 17MB  ON�� 29MB

���ǵ���ֻ��cache �Բ��Խ��û��Ӱ�죬����8MB

�������+cache + �Զ�����

lsscsi -l

http://blog.csdn.net/msdnchina/article/details/43638857

io���ȶ��� deadline ???

�Ķ�����ȵ����
[root@localhost ~]# cat /sys/block/sda/queue/nr_requests    //�������
128
[root@localhost ~]# cat /sys/block/sda/device/queue_depth 
256
[root@localhost ~]# 
				 
				 
echo 16 >/sys/block/sda/queue/nr_requests  //�������
echo 16>/sys/block/sda/device/queue_depth 


BMS flag : off   --���BMS
BMS flag: on    --û���BMS,��BMS �򿪣������Զ��������ٲ��ԣ����2h���ң�


cache �򿪣����ȸ�Ϊ16,==�� 41MB

==�� ����raid��ͬ��Ҫ������ Ӳ�̵�BMSҲҪ�Ƚ�����


./diskman-rh-suse-x86 -b bms-off /dev/sdxx
./diskman-rh-suse-x86 -p c-on /dev/sdxx
./diskman-rh-suse-x86 -p y-on /dev/sdxx
./diskman-rh-suse-x86 -p z-on /dev/sdxx

����������Լ�����óɹ����
./diskmanxxx -I /dev/sdxxx


@@@�����־���
rm -rf /var/log/*.gz

rm -rf /var/log/*.1

echo "" > /var/log/dmesg

echo "" > /var/log/kern.log

echo "" > /var/log/messages

echo "" > /var/log/syslog


@@@@
 ʹ��dd�������linux���̶�д�ٶȵķ���

1������Ϥ����������豸��
��1��/dev/null������վ���޵׶���
��2��/dev/zero�������ַ���

2�����Դ���д����

���ƴ���
��������:

time dd if=/dev/zero of=/testw.dbf bs=4k count=100000


��Ϊ/dev//zero��һ��α�豸����ֻ�������ַ����������������IO�����ԣ�IO���Ἧ����of�ļ��У�of�ļ�ֻ����д��������������൱�ڲ��Դ��̵�д�����������β���oflag=direct�������ڴ滺�棬���oflag=sync������hdd���档

 

3�����Դ��̶�����

���ƴ���
��������:

time dd if=/dev/sdb of=/dev/null bs=4k


��Ϊ/dev/sdb��һ����������������Ķ�ȡ�����IO��/dev/null��α�豸���൱�ںڶ���of�����豸�������IO�����ԣ���������IOֻ������/dev/sdb�ϣ�Ҳ�൱�ڲ��Դ��̵Ķ���������Ctrl+c��ֹ���ԣ�

 


4������ͬʱ��д����

���ƴ���
��������:

time dd if=/dev/sdb of=/testrw.dbf bs=4k


����������£�һ�������������һ����ʵ�ʵ��ļ��������ǵĶ�д�������IO����/dev/sdb�Ƕ�����/testrw.dbf��д�����������Ƕ���һ�������У����������൱�ڲ��Դ��̵�ͬʱ��д������

@@@@
[root@localhost zhl]# ar vx libqtwebkit4_2.3.2-0ubuntu7_amd64.deb 
x - debian-binary
x - control.tar.gz
x - data.tar.xz



@@@@9361 ����raid10��
storcli64.exe /c0 add vd r10 drives=43:5-10 pdperarray=2



#########################################################

#dd if=/dev/zero of=/dev/sdd bs=4k count=300000 oflag=direct
��¼��300000+0 �Ķ��� ��¼��300000+0 ��д�� 1228800000�ֽ�(1.2 GB)�Ѹ��ƣ�17.958 �룬68.4 MB/��
Ϊʲô���Ӳ�̵�MBPSֻ��68MB/s? ������Ϊ������������78%��û�е���95%���ϣ����в���ʱ���ǿ��еġ���dd��ǰһ��IO��Ӧ֮����׼��������һ��IOʱ��SATAӲ���ǿ��еġ���ô��β�����������ʣ��ô��̲������أ�ֻ��һ���취���Ǿ�������Ӳ�̵Ķ�����ȡ������CPU��˵��Ӳ�����������豸�����в���ϵͳ���и�ÿ��Ӳ�̷���һ��ר�ŵĶ������ڻ���IO����

ʲô�Ǵ��̵Ķ�����ȣ�
��ĳ��ʱ��,��N��inflight��IO����,�����ڶ����е�IO���󡢴������ڴ����IO����N���Ƕ�����ȡ�
�Ӵ�Ӳ�̶�����Ⱦ�����Ӳ�̲��Ϲ���������Ӳ�̵Ŀ���ʱ�䡣
�Ӵ������� -> ��������� -> ���IOPS��MBPS��ֵ -> ע����Ӧʱ���ڿɽ��ܵķ�Χ��

���Ӷ�����ȵİ취�кܶ�
 
    ʹ���첽IO��ͬʱ������IO�����൱�ڶ������ж��IO����
    ���̷߳���ͬ��IO�����൱�ڶ������ж��IO����
    ����Ӧ��IO��С������ײ�֮�󣬻��ɶ��IO�����൱�ڶ������ж��IO���� ������������ˡ�

������������ˣ�IO�ڶ��еĵȴ�ʱ��Ҳ�����ӣ�����IO��Ӧʱ��������ҪȨ�⡣������ͨ������IO��С������dd�Ķ�����ȣ�����û��Ч����

dd if=/dev/zero of=/dev/sdd bs=2M count=1000 oflag=direct 
��¼��1000+0 �Ķ��� ��¼��1000+0 ��д�� 2097152000�ֽ�(2.1 GB)�Ѹ��ƣ�10.6663 �룬197 MB/��

���Կ���2MB��IO����ײ�֮�󣬻��ɶ��512KB��IO��ƽ�����г���Ϊ2.39�����Ӳ�̵���������97%��MBPS�ﵽ��197MB/s��(Ϊʲô����512KB��IO�������ȥʹ��Googleȥ��һ���ں˲��� max_sectors_kb�������ʹ�÷��� )

Ҳ����˵���Ӷ�����ȣ��ǿ��Բ��Գ�Ӳ�̵ķ�ֵ�ġ�

==��max_sectors��

inux���豸�ڴ���ioʱ���ܵ�һЩ�������豸��queue limits���������¼��limits��������Ӱ�죬����һ���������������������������segment���ȡ���Щ����������/sys/block//queue/�²鿴�����豸�ڳ�ʼ��ʱ������Ĭ��ֵ��������Ҫ����max_segments��max_sectors_kb�� 

 1. ��������

1.1 �εĸ���
���Ⱦ���Ҫ�˽�һ��ʲô�ǶΣ�segment����
һ���ξ���һ���ڴ�ҳ�����ڴ�ҳ��һ���֣����ǰ����������������ڵ����ݿ顣
���̵�ÿ��io�������Ǵ�����һЩRAM��Ԫ֮���໥����һЩ�������������ݡ����������£����̿���������DMA��ʽ�������ݣ����豸��������ֻҪ����̿����������ʵ�������Ϳ��Դ���һ�����ݴ��ͣ�һ��������ݴ��ͣ����̿������ͻᷢ��һ���ж�֪ͨ���豸��������
DMA��ʽ���͵��Ǵ��������ڵ��������ݣ���ȻҲ�����Ͳ����ڵ��������ݣ���������Ƚϵ�Ч����Ϊ��ͷ�ƶ�����
�ϵĴ��̿���������֧�֡��򵥡���DMA��ʽ�����̱�����RAM���������ڴ浥Ԫ�������ݡ������µĴ��̿�����֧�ַ�ɢ�ۼ���scatter-gather��DMA��ʽ�����̿�����һЩ���������ڴ������໥�������ݡ�
Ϊ��֧�ַ�ɢ�ۼ�DMA��ʽ�����豸������������ܹ������Ϊ�ε����ݴ洢��Ԫ��һ�η�ɢ�ۼ�DMA���Դ��ͼ����Ρ�
�����ͬ�Ķ���RAM����Ӧ��ҳ�������������Ĳ����ڴ�������Ӧ������Ҳ�����ڵģ���ôͨ�ÿ��Ϳ��Խ��кϲ������ֺϲ���ʽ�����ĸ�����ڴ�����ͳ�Ϊ����Ρ�

segment

1.2 ����������
max_segments��ʾ�豸�ܹ���������ε���Ŀ��
max_sectors_kb��ʾ�豸�������������С��
max_hw_sectors_kb��ʾ�����������ܴ�������KB��ӲԼ���� 



[root@localhost ~]# cat /sys/block/sdb/queue/
add_random           max_hw_sectors_kb    physical_block_size
discard_granularity  max_sectors_kb       read_ahead_kb
discard_max_bytes    max_segments         rotational
discard_zeroes_data  max_segment_size     rq_affinity
hw_sector_size       minimum_io_size      scheduler
iosched/             nomerges             unpriv_sgio
iostats              nr_requests          
logical_block_size   optimal_io_size   

[root@localhost ~]# cat /sys/block/sdb/device/
block/                iorequest_cnt         scsi_device/
bsg/                  modalias              scsi_disk/
delete                model                 scsi_generic/
device_blocked        power/                scsi_level
dh_state              queue_depth           state
driver/               queue_ramp_up_period  subsystem/
eh_timeout            queue_type            timeout
evt_media_change      raid_devices/         type
generic/              rescan                uevent
iocounterbits         rev                   vendor
iodone_cnt            sas_address           
ioerr_cnt             sas_device_handle     

[root@localhost ~]# cat /sys/block/sdb/queue/max_sectors_kb 
512
[root@localhost ~]# cat /sys/block/sdb/queue/max_segment
max_segments      max_segment_size  
[root@localhost ~]# cat /sys/block/sdb/queue/max_segment_size 
65536
[root@localhost ~]# cat /sys/block/sdb/queue/max_segments 
128

@@@�Ķ�����ȵ����
[root@localhost ~]# cat /sys/block/sda/device/queue_depth 
256
[root@localhost ~]# 

echo 16>/sys/block/sda/device/queue_depth   //�޸Ķ������


BMS flag : off   --���BMS
BMS flag: on    --û���BMS,��BMS �򿪣������Զ��������ٲ��ԣ����2h���ң�


==�� ����raid��ͬ��Ҫ������ Ӳ�̵�BMSҲҪ�Ƚ�����


./diskman-rh-suse-x86 -b bms-off /dev/sdxx
./diskman-rh-suse-x86 -p c-on /dev/sdxx
./diskman-rh-suse-x86 -p y-on /dev/sdxx
./diskman-rh-suse-x86 -p z-on /dev/sdxx

����������Լ�����óɹ����
./diskmanxxx -I /dev/sdxxx


@@@���̳�����������
Medium Error[0x03]

Unrecove read error [0x11]
	
UNC
	
�߼��������������쳣����ȣ���������ECCУ���������������������𻵣�Ӳ�̹̼����л����滻
----------------------------------
Medium Error[0x03]
	
Record not found[0x14]
	
IDNF
	
����LBA��ַ�Ƿ�
----------------------------------
Hardware Error[0x04]
	
Internal target failure [0x44]
	
DF
	
�豸����
----------------------------------
Data Protect[0x07]
	
Write protected[0x27]
	
WP
	
д����
----------------------------------
Aborted Command[0x0B]
	
No additional sense information[0x00]
	
ABRT
	
����Ӧ�κ�ATA���SCSI���ش���
----------------------------------
Abort Command[0x0B]
	
Information unit iuCRC error detected[0x47]
	
ICRC
	
Ӳ�̳�������ᵼ��ϵͳ��·�������ȣ�I/O�������������п���ʹ�����̲�����������
----------------------------------
��д�����˵��///����ϵͳ�������///VDL�������///SmartData�������

//UNC
	
//
SLES10SP2��SCSI�в������5��SCSI���

SLES11SP1��SCSI�в㲻�����ԣ�ֱ�ӽ�SCSI����ִ�н���ύ�����豸��
	
//
�����󲻴���д������������,ͨ�����µ糢�Իָ����ָ��ɹ�����м���Ƿ���Լ���ʹ�ã����������½���ϵͳʹ�á�
	
//
��UNC���ع������ݺ󸲸�дԭ���ķ�Ƭ��дʧ�ܣ����滻�����ռ�д��

дUNC ʧ�ܣ�ֱ������ӳ�䵽����Ԥ���ռ��޸�������Ԥ���������̡�
----------------------------------
//IDNF
	
//
SLES10SP2��SCSI�в������5��SCSI���

SLES11SP1��SCSI�в㲻�����ԣ�ֱ���ύ�����豸��
	
//
����ӳ�䵽����Ԥ���ռ��޸�������Ԥ���������̡�
----------------------------------
//DF
	
//
SLES10SP2��SLES11SP1ֱ���ύ�����豸�㡣������ȷ��SAS2008�£�scsi_device->retry_hwerror��ֵΪ0
	
//
ͨ�����µ糢�Իָ����ָ��ɹ�����м���Ƿ���Լ���ʹ�ã����������½���ϵͳʹ�á�
	
//
���̣����ض�дʧ�ܣ��ļ���RAID�Զ��ع����ָ����ݡ�
----------------------------------
//WP
	
//
SLES10SP2��SLES11SP1��SCSI�в㽫ִ�н��ֱ���ύ�����豸��
----------------------------------
//ABRT
	
//
SLES10SP2��SLES11SP1��SCSI�в������5��SCSI����
	
//
�����ԣ����Բ��ɹ�ִ�����µ�ظ�
----------------------------------
//ICRC
	
//
SLES10SP2��SLES11SP1��SCSI�в������5��SCSI����
//
�����ԣ����Բ��ɹ�ִ�����µ�ظ�
	
//
����ӳ�䵽����Ԥ���ռ��޸�������Ԥ���������̡�




@@@raid�������������� 
���⣺
1.��raid 5 ��������СΪ128k�����д����ļ���С�� 2k���Ǵ�ŵķ�ʽ��ռ����������ôȷ����ʣ��������ô����
2.�����ڸ�ʽ����ʱ���и���Ԫ�����С�������������ļ���ŵ���С��λ����raid����Ŀ�����

����ͷ��
Ҫ�������������⣬�ҽ���¥�������ֵĻ������ڻ�ͼ��
������Ҫд��2k�ġ��ļ�������Ȼǣ�����ļ�����Ҫǣ�����ļ�ϵͳ�ķ��䵥Ԫ��Ҳ������ڶ������⡣

raid�����ϵͳ�ṩ���Ǿ������������������߽�LBA���ռ��ַ���������ļ�ϵͳ��չʾ���Ƿ���������ھ��������ǽ���Ƭ������ַ�ٴ��п����ļ�ϵͳ�����������ν���ء������߽�cluster�����߽з��䵥Ԫ��fs�������ֻ�Դ�Ϊ��λ����������֡��������д������ء�����io�������֮�µĸ��㶼�����Ե�������Ϊ��λ�ˣ������Ǵ洢ϵͳ��С��io��λ�������˵ײ���Щӳ���ϵ���Ϳ��������о�io��Ϊ�ˡ�

��˵��������˵Ҫд��2kbytes�ġ��ļ�������Ȼ��Ҫ�����ļ�ϵͳ����д���ˣ�����ļ�ϵͳ�Ĵش�С���趨Ϊ2k�����ļ�ϵͳ���ڷ����ڷ���2k�Ŀռ�������ļ�ʵ�����ݣ�Ҳ����4��������������ַ�����⣬����Ҫ����inode��unix������MFT��Win������ν��Ԫ����/metadata����Ҳ��Ҫռ�ö���Ŀռ䡣ֵ��һ����ǣ�inode����MFT�Ķ�Ӧĳ���ļ���metadata�����ǿ��Դ��һ���������ļ�ʵ�����ݵģ�һ����64�ֽڣ�С�������ֵ���ļ�ֱ�Ӵ����inode�У�����������ݣ�inode�лᱻ�����������������ӳ��ָ��ָ���ļ�ʵ�����ݱ���ŵ�������ַ����Ѱַ������

��������raid���ṩ�Ľ�ɫ����˵��raid�ṩһƬ����������ַ�������ļ�ϵͳѡ��������1024-1027����4��������������Ϊ���2k�ļ��Ĵ�ſռ䣬���ļ�ϵͳд������ļ���ʱ�򣬾���ܵ����ָ��֮�󣬻Ὣ����������봫�͸�raid������raid��������֮��Ὣ���봫�͸�raidоƬ���е�ַ���루Ӳraid��������ֱ��������������е�ַ���루��raid��������ַ�����������˼�ǽ���������ĵ�ַӳ�䵽ʵ�ʵ�����Ӳ�̵�ַ����Ϊraid�ṩ���ϲ�����������/lun��һ��lun���Էֲ��ڶ������Ӳ���ϡ���ַ����Ĺ���һ��Ҫ��ѯstripeҲ��������ӳ�����������ô�ֵģ���ʱ�ͻ�Ӱ�췭��֮��ʵ�ʵ�Ӳ��������ַ���ٻ���˵���raid5��128KB������128KB����=������������ÿ��������������������segment��С��Ҳ����˵һ�����������еĶ�����̺����г���һ��һ���ģ�Ӳ�̱����൱���������������������п�֮���γɵ�С���Ӿ���segment��Ҳ��������ȣ�stripedepth������8���̵�raid5ϵͳ������һ�����ڴ��parity��128KB��������8����16KB��Ҳ����˵segment=�������=16KB=ÿ�������Ϲ���һ��������ʹ�õĿռ䡣

�ٻ���˵2k���ļ�д�룬�������£���ַ����Ὣ2k�ĵ�ַ����Ϊ������m�ϵ�n������m�ϵ�n+3������������ȻҲ�����ǡ�����x�ϵ�y������a�ϵ�b������֮��ַ��������Ӳ���ϵ��ĸ�������������/������Ե/��������Ӳ��/�������Ӳ�̣��ļ�ϵͳ�ǲ�֪���ģ���raid������������ֲ�֪����Ϊ��ä�������ڴ���ļ�ϵͳ��ä������Ҳ�в�ä���߰�ä�ġ�������raid����������������ֲ��ȣ�ʵ���϶���ä������Ч������ܴ󣬰���raid5����Ĳ���io�ص㣬Ҳ��ä��������ν����������ղŵ����ӣ�ĳ��io��Ҫд��2k�����ݣ������ַ������Ϊ��4����������һ��segment������ioֻ��ռ��һ�������̣������Ҫռ��parity���������ʱ����һ��io��Ҫд��2k���ݣ�����ε�4��������������һ���������ϣ�������Ҫ��parity����ǡ����ǰһ��io��������Ҫ��parity������ͬһ�����ϣ���������io���Բ��в�����4�����ͬʱ��д���������ֲ����ǻ��ڡ�ǡ�á��ģ�����raid5�ṩ����ä������Ҫʵ�ֲ�ä�Ĳ���ֻ�ܿ��ϲ��ļ�ϵͳ��


�ļ�ϵͳ�Ĵش�С��
[root@localhost ~]# tune2fs -l /dev/sde1 | grep "Block size"
Block size:               4096

raid��strip:
[root@localhost ssdtest]# storcli /c0 /v1 show all | grep -i strip
Strip Size = 64 KB


@@@RAID����������
RAID��������������һ���Զ��Ľ� I/O �ĸ��ؾ��⵽�����������ϵļ������������������ǽ�һ�����������ݷֳɺܶ�С���ֲ������Ƿֱ�洢����ͬ������ȥ�������ʹ�������ͬʱ�������ݵĶ����ͬ���ֶ�������ɴ��̳�ͻ����������Ҫ���������ݽ���˳����ʵ�ʱ����Ի�����̶��ϵ� I/O �����������Ӷ���÷ǳ��õ����ܡ������������� I/O ���������ϵ���Խ���֣���������Ӧ��ϵͳ���ڵļ��㻷���еĶ����λ�ƽ̨���漰�����������ļ����������ϵͳ�ʹ洢ϵͳ����������ж�����ʹ��������������[1] 
�������������������ṩ���ٶȱȵ����������ṩ���ٶ�Ҫ��ܶ࣬�������ڴ洢�������죬�����ϵͳ��������������ʵ��ϵͳ��I/O���طֵ������OS��LVM�������Ӳ�������豸�������������������(stripe depth)���������(stripe width)��


@@@RAID�������
RAID�������ָ���������Ĵ�С��Ҳ��������С����ʱҲ������block size, chunk size, stripe length ���� granularity���������ָ����д��ÿ������ϵ��������ݿ�Ĵ�С��RAID�����ݿ��Сһ����2KB��512KB֮��(���߸���)������ֵ��2�Ĵη�����2KB,4KB,8KB,16KB������������С�����ܵ�Ӱ�������������������Ķࡣ
�� ��С������С: ����������С��С�ˣ����ļ����ֳ��˸��������С�����ݿ顣��Щ���ݿ�ᱻ��ɢ�������Ӳ���ϴ洢���������˴�������ܣ���������Ҫ���Ѱ�Ҳ�ͬ�����ݿ飬���̶�λ�����ܾ��½��ˡ�
�� ����������С: ���С������С�෴���ή�ʹ������ܣ���߶�λ���ܡ�
�����ϱߵ����������ǻᷢ�ָ��ݲ�ͬ��Ӧ�����ͣ���ͬ���������󣬲�ͬ�������Ĳ�ͬ�ص�(��SSDӲ��)��������һ���ձ����õ�"���������С"��������Ҳ�Ǵ洢���ң��ļ�ϵͳ��д�����������Լ�����������С��ԭ��


@@@RAID�������
RAID���������ָͬʱ���Բ�������д�����������������������RAID�е�����Ӳ������������һ�������������ģ�����4������Ӳ�̵����е�������Ⱦ���4������������ȣ������������еĶ�д���ܡ���������ԣ����Ӹ����Ӳ�̣�Ҳ�������˿���ͬʱ��������д����������������������һ����ǰ���£�һ����8��18GӲ����ɵ��������һ����4��36GӲ����ɵ����о��и��ߵĴ������ܡ�

@@@@Disk Striping

Disk striping allows you to write data across multiple drives instead of just one drive. Disk striping involves 
partitioning each drive storage space into stripes that can vary in size from 8 KB to 1024 KB. These stripes are 
interleaved in a repeated sequential manner. The combined storage space is composed of stripes from each drive. It is 
recommended that you keep stripe sizes the same across RAID drive groups.
For example, in a four-disk system using only disk striping (used in RAID level 0), segment 1 is written to disk 1, 
segment 2 is written to disk 2, and so on. Disk striping enhances performance because multiple drives are accessed 
simultaneously, but disk striping does not provide data redundancy.

Stripe Width:
Stripe width is the number of drives involved in a drive group where striping is implemented. For example, a four-disk 
drive group with disk striping has a stripe width of four.

Stripe Size:
The stripe size is the length of the interleaved data segments that the RAID controller writes across multiple drives, not 
including parity drives. For example, consider a stripe that contains 64 KB of disk space and has 16 KB of data residing 
on each disk in the stripe. In this case, the stripe size is 64 KB, and the strip size is 16 KB.

Strip Size: or segment
The strip size is the portion of a stripe that resides on a single drive.

stripe [straip] ���ƣ�������
strip [strip] :����

@@@@@

@@@9361  JBODģʽ ����RAID�ķ�����

PD LIST :
=======

------------------------------------------------------------------------------
EID:Slt DID State DG      Size Intf Med SED PI SeSz Model                  Sp 
------------------------------------------------------------------------------
8:8      13 JBOD  -   3.637 TB SATA HDD N   N  512B WDC WD4000FYYZ-01UL1B3 U  
8:9      17 JBOD  -   1.818 TB SATA HDD N   N  512B WDC WD2000FYYZ-01UL1B2 U  
8:10     28 JBOD  -   3.637 TB SATA HDD N   N  512B TOSHIBA MG04ACA400E    U  
8:30     10 Onln  0  465.25 GB SATA HDD N   N  512B ST9500620NS            U  
8:31     11 JBOD  -  465.25 GB SATA HDD N   N  512B ST9500620NS            U  
------------------------------------------------------------------------------
[root@localhost ~]# storcli /c0 /e8 /s31 set good
Controller = 0
Status = Failure
Description = Set Drive Good Failed.

Detailed Status :
===============

----------------------------------------------------------------------
Drive      Status  ErrCd ErrMsg                                       
----------------------------------------------------------------------
/c0/e8/s31 Failure   255 Drive is JBOD! Use -force option to confirm. 
----------------------------------------------------------------------


[root@localhost ~]# storcli /c0 /e8 /s31 set good force
Controller = 0
Status = Success
Description = Set Drive Good Succeeded.


PD LIST :
=======

------------------------------------------------------------------------------
EID:Slt DID State DG      Size Intf Med SED PI SeSz Model                  Sp 
------------------------------------------------------------------------------
8:8      13 JBOD  -   3.637 TB SATA HDD N   N  512B WDC WD4000FYYZ-01UL1B3 U  
8:9      17 JBOD  -   1.818 TB SATA HDD N   N  512B WDC WD2000FYYZ-01UL1B2 U  
8:10     28 JBOD  -   3.637 TB SATA HDD N   N  512B TOSHIBA MG04ACA400E    U  
8:30     10 Onln  0  465.25 GB SATA HDD N   N  512B ST9500620NS            U  
8:31     11 UGood -  465.25 GB SATA HDD N   N  512B ST9500620NS            U  
------------------------------------------------------------------------------



==��
[root@localhost ~]# storcli /c0 /e8 /s31 set jbod

==��

PD LIST :
=======

------------------------------------------------------------------------------
EID:Slt DID State DG      Size Intf Med SED PI SeSz Model                  Sp 
------------------------------------------------------------------------------
8:8      13 JBOD  -   3.637 TB SATA HDD N   N  512B WDC WD4000FYYZ-01UL1B3 U  
8:9      17 JBOD  -   1.818 TB SATA HDD N   N  512B WDC WD2000FYYZ-01UL1B2 U  
8:10     28 JBOD  -   3.637 TB SATA HDD N   N  512B TOSHIBA MG04ACA400E    U  
8:30     10 Onln  0  465.25 GB SATA HDD N   N  512B ST9500620NS            U  
8:31     11 JBOD  -  465.25 GB SATA HDD N   N  512B ST9500620NS            U  
------------------------------------------------------------------------------



#######################################################################


type 1: �����𻵵�Ӳ��---�����������𻵣�
1��Ӳ��smart��Ϣ��--���Բ鿴��failing����Ŀ
[root@localhost home]# smartctl -a /dev/sdc
smartctl 5.43 2012-06-30 r3573 [x86_64-linux-2.6.32-431.el6.x86_64] (local build)
Copyright (C) 2002-12 by Bruce Allen, http://smartmontools.sourceforge.net

=== START OF INFORMATION SECTION ===
Device Model:     WDC WD4000FYYZ-01UL1B3
Serial Number:    WD-WMC130F5V9L6
LU WWN Device Id: 5 0014ee 65bc41276
Firmware Version: 01.x1Kx2
User Capacity:    4,000,787,030,016 bytes [4.00 TB]
Sector Size:      512 bytes logical/physical
Device is:        Not in smartctl database [for details use: -P showall]
ATA Version is:   8
ATA Standard is:  Exact ATA specification draft version not indicated
Local Time is:    Tue Dec 13 17:32:30 2016 CST
SMART support is: Available - device has SMART capability.
SMART support is: Enabled

=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: FAILED!
Drive failure expected in less than 24 hours. SAVE ALL DATA.
See vendor-specific Attribute list for failed Attributes.

General SMART Values:
Offline data collection status:  (0x82)	Offline data collection activity
					was completed without error.
					Auto Offline Data Collection: Enabled.
Self-test execution status:      (   0)	The previous self-test routine completed
					without error or no self-test has ever 
					been run.
Total time to complete Offline 
data collection: 		(47880) seconds.
Offline data collection
capabilities: 			 (0x7b) SMART execute Offline immediate.
					Auto Offline data collection on/off support.
					Suspend Offline collection upon new
					command.
					Offline surface scan supported.
					Self-test supported.
					Conveyance Self-test supported.
					Selective Self-test supported.
SMART capabilities:            (0x0003)	Saves SMART data before entering
					power-saving mode.
					Supports SMART auto save timer.
Error logging capability:        (0x01)	Error logging supported.
					General Purpose Logging supported.
Short self-test routine 
recommended polling time: 	 (   2) minutes.
Extended self-test routine
recommended polling time: 	 ( 517) minutes.
Conveyance self-test routine
recommended polling time: 	 (   5) minutes.
SCT capabilities: 	       (0x70bd)	SCT Status supported.
					SCT Error Recovery Control supported.
					SCT Feature Control supported.
					SCT Data Table supported.

SMART Attributes Data Structure revision number: 16
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  1 Raw_Read_Error_Rate     0x002f   197   001   051    Pre-fail  Always   In_the_past 154
  3 Spin_Up_Time            0x0027   156   149   021    Pre-fail  Always       -       11175
  4 Start_Stop_Count        0x0032   100   100   000    Old_age   Always       -       64
  5 Reallocated_Sector_Ct   0x0033   134   134   140    Pre-fail  Always   FAILING_NOW 2052
  7 Seek_Error_Rate         0x002e   200   200   000    Old_age   Always       -       0
  9 Power_On_Hours          0x0032   098   098   000    Old_age   Always       -       2114
 10 Spin_Retry_Count        0x0032   100   253   000    Old_age   Always       -       0
 11 Calibration_Retry_Count 0x0032   100   253   000    Old_age   Always       -       0
 12 Power_Cycle_Count       0x0032   100   100   000    Old_age   Always       -       64
183 Runtime_Bad_Block       0x0032   100   100   000    Old_age   Always       -       0
192 Power-Off_Retract_Count 0x0032   200   100   000    Old_age   Always       -       62
193 Load_Cycle_Count        0x0032   200   200   000    Old_age   Always       -       1
194 Temperature_Celsius     0x0022   116   087   000    Old_age   Always       -       36
196 Reallocated_Event_Count 0x0032   173   173   000    Old_age   Always       -       27
197 Current_Pending_Sector  0x0032   200   200   000    Old_age   Always       -       304
198 Offline_Uncorrectable   0x0030   200   200   000    Old_age   Offline      -       0
199 UDMA_CRC_Error_Count    0x0032   200   200   000    Old_age   Always       -       0
200 Multi_Zone_Error_Rate   0x0008   197   191   000    Old_age   Offline      -       1162

SMART Error Log Version: 1
ATA Error Count: 12 (device log contains only the most recent five errors)
	CR = Command Register [HEX]
	FR = Features Register [HEX]
	SC = Sector Count Register [HEX]
	SN = Sector Number Register [HEX]
	CL = Cylinder Low Register [HEX]
	CH = Cylinder High Register [HEX]
	DH = Device/Head Register [HEX]
	DC = Device Command Register [HEX]
	ER = Error register [HEX]
	ST = Status register [HEX]
Powered_Up_Time is measured from power on, and printed as
DDd+hh:mm:SS.sss where DD=days, hh=hours, mm=minutes,
SS=sec, and sss=millisec. It "wraps" after 49.710 days.

Error 12 occurred at disk power-on lifetime: 2023 hours (84 days + 7 hours)
  When the command that caused the error occurred, the device was active or idle.

  After command completion occurred, registers were:
  ER ST SC SN CL CH DH
  -- -- -- -- -- -- --
  04 61 0c 00 00 00 00  Device Fault; Error: ABRT

  Commands leading to the command that caused the error were:
  CR FR SC SN CL CH DH DC   Powered_Up_Time  Command/Feature_Name
  -- -- -- -- -- -- -- --  ----------------  --------------------
  ef 03 0c 00 00 00 00 00   3d+18:12:46.258  SET FEATURES [Set transfer mode]
  e5 00 00 00 00 00 00 00   3d+18:12:46.258  CHECK POWER MODE
  ec 00 00 00 00 00 00 00   3d+18:12:46.257  IDENTIFY DEVICE
  ec 00 00 00 00 00 00 00   3d+18:11:05.420  IDENTIFY DEVICE
  ec 00 00 00 00 00 00 00   3d+18:11:05.403  IDENTIFY DEVICE

Error 11 occurred at disk power-on lifetime: 1934 hours (80 days + 14 hours)
  When the command that caused the error occurred, the device was active or idle.

  After command completion occurred, registers were:
  ER ST SC SN CL CH DH
  -- -- -- -- -- -- --
  04 61 0c 00 00 00 00  Device Fault; Error: ABRT

  Commands leading to the command that caused the error were:
  CR FR SC SN CL CH DH DC   Powered_Up_Time  Command/Feature_Name
  -- -- -- -- -- -- -- --  ----------------  --------------------
  ef 03 0c 00 00 00 00 00      00:53:40.098  SET FEATURES [Set transfer mode]
  e5 00 00 00 00 00 00 00      00:53:40.098  CHECK POWER MODE
  ec 00 00 00 00 00 00 00      00:53:40.098  IDENTIFY DEVICE

Error 10 occurred at disk power-on lifetime: 1892 hours (78 days + 20 hours)
  When the command that caused the error occurred, the device was active or idle.

  After command completion occurred, registers were:
  ER ST SC SN CL CH DH
  -- -- -- -- -- -- --
  04 61 0c 00 00 00 00  Device Fault; Error: ABRT

  Commands leading to the command that caused the error were:
  CR FR SC SN CL CH DH DC   Powered_Up_Time  Command/Feature_Name
  -- -- -- -- -- -- -- --  ----------------  --------------------
  ef 03 0c 00 00 00 00 00      00:36:12.823  SET FEATURES [Set transfer mode]
  e5 00 00 00 00 00 00 00      00:36:12.823  CHECK POWER MODE
  ec 00 00 00 00 00 00 00      00:36:12.822  IDENTIFY DEVICE

Error 9 occurred at disk power-on lifetime: 1887 hours (78 days + 15 hours)
  When the command that caused the error occurred, the device was active or idle.

  After command completion occurred, registers were:
  ER ST SC SN CL CH DH
  -- -- -- -- -- -- --
  04 61 0c 00 00 00 00  Device Fault; Error: ABRT

  Commands leading to the command that caused the error were:
  CR FR SC SN CL CH DH DC   Powered_Up_Time  Command/Feature_Name
  -- -- -- -- -- -- -- --  ----------------  --------------------
  ef 03 0c 00 00 00 00 00      17:32:53.093  SET FEATURES [Set transfer mode]
  e5 00 00 00 00 00 00 00      17:32:53.093  CHECK POWER MODE
  ec 00 00 00 00 00 00 00      17:32:53.093  IDENTIFY DEVICE
  ef 03 0c 00 00 00 00 00      16:49:07.294  SET FEATURES [Set transfer mode]
  e5 00 00 00 00 00 00 00      16:49:07.294  CHECK POWER MODE

Error 8 occurred at disk power-on lifetime: 1887 hours (78 days + 15 hours)
  When the command that caused the error occurred, the device was active or idle.

  After command completion occurred, registers were:
  ER ST SC SN CL CH DH
  -- -- -- -- -- -- --
  04 61 0c 00 00 00 00  Device Fault; Error: ABRT

  Commands leading to the command that caused the error were:
  CR FR SC SN CL CH DH DC   Powered_Up_Time  Command/Feature_Name
  -- -- -- -- -- -- -- --  ----------------  --------------------
  ef 03 0c 00 00 00 00 00      16:49:07.294  SET FEATURES [Set transfer mode]
  e5 00 00 00 00 00 00 00      16:49:07.294  CHECK POWER MODE
  ec 00 00 00 00 00 00 00      16:49:07.293  IDENTIFY DEVICE
  ef 03 0c 00 00 00 00 00      16:05:59.425  SET FEATURES [Set transfer mode]
  e5 00 00 00 00 00 00 00      16:05:59.425  CHECK POWER MODE

SMART Self-test log structure revision number 1
No self-tests have been logged.  [To run self-tests, use: smartctl -t]


SMART Selective self-test log data structure revision number 1
 SPAN  MIN_LBA  MAX_LBA  CURRENT_TEST_STATUS
    1        0        0  Not_testing
    2        0        0  Not_testing
    3        0        0  Not_testing
    4        0        0  Not_testing
    5        0        0  Not_testing
Selective self-test flags (0x0):
  After scanning selected spans, do NOT read-scan remainder of disk.
If Selective self-test is pending on power-up, resume after 0 minute delay.


2����д����ʱ��ʾinput/output error,��ʱ���Զ�д������
[root@localhost home]# dd if=/dev/sdc of=/dev/null bs=5M iflag=direct
dd: reading `/dev/sdc': Input/output error
181+0 records in
181+0 records out
948961280 bytes (949 MB) copied, 12.8175 s, 74.0 MB/s


3����־--�����淢����д����ʱ���ڶ�Ӧ����־��������Ĵ���
[root@localhost home]# dmesg
sd 0:0:31:0: [sdc] Unhandled sense code
sd 0:0:31:0: [sdc] Result: hostbyte=DID_OK driverbyte=DRIVER_SENSE
sd 0:0:31:0: [sdc] Sense Key : Medium Error [current] 
Info fld=0x1ce756
sd 0:0:31:0: [sdc] Add. Sense: Unrecovered read error
sd 0:0:31:0: [sdc] CDB: Read(10): 28 00 00 1c e4 00 00 04 00 00
sd 0:0:31:0: [sdc] Unhandled sense code
sd 0:0:31:0: [sdc] Result: hostbyte=DID_OK driverbyte=DRIVER_SENSE
sd 0:0:31:0: [sdc] Sense Key : Medium Error [current] 
Info fld=0x1c99ae
sd 0:0:31:0: [sdc] Add. Sense: Unrecovered read error
sd 0:0:31:0: [sdc] CDB: Read(10): 28 00 00 1c 98 00 00 04 00 00
sd 0:0:31:0: [sdc] Unhandled sense code
sd 0:0:31:0: [sdc] Result: hostbyte=DID_OK driverbyte=DRIVER_SENSE
sd 0:0:31:0: [sdc] Sense Key : Medium Error [current] 
Info fld=0x1c99ae
sd 0:0:31:0: [sdc] Add. Sense: Unrecovered read error
sd 0:0:31:0: [sdc] CDB: Read(10): 28 00 00 1c 98 00 00 04 00 00
sd 0:0:31:0: [sdc] Unhandled sense code
sd 0:0:31:0: [sdc] Result: hostbyte=DID_OK driverbyte=DRIVER_SENSE
sd 0:0:31:0: [sdc] Sense Key : Medium Error [current] 
Info fld=0x1c6cae
sd 0:0:31:0: [sdc] Add. Sense: Unrecovered read error
sd 0:0:31:0: [sdc] CDB: Read(10): 28 00 00 1c 6c 00 00 04 00 00


[root@localhost home]# diskman -s /dev/sdc
SMART Attributes Data Structure revision number: 16
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  1 Raw_Read_Error_Rate     0x002f   197   001   051    Pre-fail  Always   In_the_past 155
  3 Spin_Up_Time            0x0027   156   149   021    Pre-fail  Always       -       11175
  4 Start_Stop_Count        0x0032   100   100   000    Old_age   Always       -       64
  5 Reallocated_Sector_Ct   0x0033   134   134   140    Pre-fail  Always   FAILING_NOW 2052
  7 Seek_Error_Rate         0x002e   200   200   000    Old_age   Always       -       0
  9 Power_On_Hours          0x0032   098   098   000    Old_age   Always       -       2114
 10 Spin_Retry_Count        0x0032   100   253   000    Old_age   Always       -       0
 11 Calibration_Retry_Count 0x0032   100   253   000    Old_age   Always       -       0
 12 Power_Cycle_Count       0x0032   100   100   000    Old_age   Always       -       64
183 Unknown_Attribute       0x0032   100   100   000    Old_age   Always       -       0
192 Power-Off_Retract_Count 0x0032   200   100   000    Old_age   Always       -       62
193 Load_Cycle_Count        0x0032   200   200   000    Old_age   Always       -       1
194 Temperature_Celsius     0x0022   116   087   000    Old_age   Always       -       36
196 Reallocated_Event_Count 0x0032   173   173   000    Old_age   Always       -       27
197 Current_Pending_Sector  0x0032   200   200   000    Old_age   Always       -       304
198 Offline_Uncorrectable   0x0030   200   200   000    Old_age   Offline      -       0
199 UDMA_CRC_Error_Count    0x0032   200   200   000    Old_age   Always       -       0
200 Multi_Zone_Error_Rate   0x0008   197   191   000    Old_age   Offline      -       1162



###########################################################################
EC600G4��
����4�����ڣ�2����ڣ�2����ڣ�
2����ڷֱ����ӵ�3��4 ��λ�Ľ������ϣ�
2����ڷֱ����ӵ�3��4��λ�Ľ������ϣ�
ֻ����4��λ�Ľ����壬������3��λ�Ľ���������£���ѯ���ڵ���λ��Ϣ���£�

[root@EC600G4-001 ~]# ethtool eth0 | grep "Link"
	Link detected: no
[root@EC600G4-001 ~]# ethtool eth1 | grep "Link"
	Link detected: yes
[root@EC600G4-001 ~]# ethtool eth2 | grep "Link"
	Link detected: no
[root@EC600G4-001 ~]# ethtool eth3 | grep "Link"
	Link detected: no
[root@EC600G4-001 ~]# 

���������嶼���ӵ�����£�
[root@EC600G4-001 ~]# ethtool eth0 | grep "Link"
	Link detected: yes
[root@EC600G4-001 ~]# ethtool eth1 | grep "Link"
	Link detected: yes
[root@EC600G4-001 ~]# ethtool eth2 | grep "Link"
	Link detected: no
[root@EC600G4-001 ~]# ethtool eth3 | grep "Link"
	Link detected: no
[root@EC600G4-001 ~]# 

��Ϣ���£�
XH20G3:
���ص�X722 ����˵����
0000:1a:00.0 Ethernet controller: Intel Corporation Ethernet Connection X722 for 10GbE backplane (rev 03)
0000:1a:00.1 Ethernet controller: Intel Corporation Ethernet Connection X722 for 10GbE backplane (rev 03)
0000:1a:00.2 Ethernet controller: Intel Corporation Ethernet Connection X722 for 10GbE backplane (rev 03)
0000:1a:00.3 Ethernet controller: Intel Corporation Ethernet Connection X722 for 10GbE backplane (rev 03)


Ĭ�Ͽ�����������10GE�Ŀڣ������slot3/4�����ӵ���NS10�� ��Э�̳�1GE�Ŀڣ�
������ӵ���NS20����Э�̳�10GE�ڣ�
��������1GE�Ŀڣ���Ҫ�������ú�ſ���ʹ�ã�

���ӽ������û�����ӽ���������ڲ�ѯ������Ϣ������

Settings for ens3f0:
	Supported ports: [ ]
	Supported link modes:   1000baseT/Full 
	                        10000baseT/Full 
	Supported pause frame use: Symmetric
	Supports auto-negotiation: Yes
	Advertised link modes:  1000baseT/Full 
	                        10000baseT/Full 
	Advertised pause frame use: No
	Advertised auto-negotiation: Yes
	Speed: Unknown!
	Duplex: Unknown! (255)
	Port: Other
	PHYAD: 0
	Transceiver: external
	Auto-negotiation: off
	Supports Wake-on: g
	Wake-on: g
	Current message level: 0x0000000f (15)
			       drv probe link timer
	Link detected: no
[root@EC600G4-001 ~]# ethtool ens3f1
Settings for ens3f1:
	Supported ports: [ Backplane ]
	Supported link modes:   Not reported
	Supported pause frame use: Symmetric
	Supports auto-negotiation: Yes
	Advertised link modes:  Not reported
	Advertised pause frame use: No
	Advertised auto-negotiation: Yes
	Speed: 1000Mb/s
	Duplex: Full
	Port: None
	PHYAD: 0
	Transceiver: external
	Auto-negotiation: on
	Supports Wake-on: g
	Wake-on: g
	Current message level: 0x0000000f (15)
			       drv probe link timer
	Link detected: yes

##################################################################