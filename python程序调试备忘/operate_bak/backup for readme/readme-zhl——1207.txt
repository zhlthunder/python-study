#I8350 ���ȵ���  ��BMC shell(root/root)--ushell(zte/zte)--sh 1��
BSP_DbgFanTest(1)    //�رշ��ȵ��ٲ���
BSP_SetFanPwm(0xff)  //�ֶ����÷���ռ�ձȣ�����01-ff
BSP_GetFanRpm()             //��ȡ���ת��

###�����л�(BMC)
BSP_SetPanelUart(1)   //HOST UArt
BSP_SetPanelUart(0)   //BMC UArt
BSP_SetPanelUart(3)   //expander UArt --����л��������ȷ��expander�İ汾��Ϣ

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
dd if=/dev/zero of=/dev/sdb  ����Ӳ�̶�дȷ������
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
fsck/e2fsck -c  (Check for bad blocks and add them to the badblock list)
hdparm -t /dev/sda ( -t   ����Ӳ�̵Ķ�ȡЧ�ʡ�)
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
1��vnc �����װ 2������VNCserver 3)�رշ���ǽ 4���޸������ļ�/root/.vnc/xstartup,(# unset SESSION_MANAGER   # exec /etc/X11/xinit/xinitrc) ȥ�������е�ע�ͣ�5��vncserver -kill :1 6��vncserver :1 7����PC�˴�VNC����ʹ�á�

#### fio�������

fio -name=testc -filename=/dev/sdb -bs=64k --rw=write -iodepth=32 -runtime=80h  -direct=1 -numjobs=8 -time_based  -ioengine=libaio -thread -group_reporting=1

###��ϵͳ��ѹ������������******��--running�汾
fio -name=testc -filename=/home/tmp_io/tmp -bs=256k -rw=randrw -rwmixread=50 -iodepth=16 -direct=1 -numjobs=8 -runtime=24h -size=5G -time_based -ioengine=libaio -thread -group_reporting

####����ѹ���ͽ�ѹ
tar zcvf servertool~.tar.gz servertool~/
tar xzf  servertool~.tar.gz


####linux���̺�ִ̨������ nohup (��һ�������������е�����ͬʱ����ִ��)
nohup����������������һ�����̣�������������˳��ʻ�ʱ�ý��̻������������ô����ʹ��nohup�����������������˳��ʻ�/�ر��ն�֮�����������Ӧ�Ľ��̡�nohup���ǲ��������˼( no hang up)�� ��
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
zypper refresh  #update����ʱ��ϳ�

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

##################################################

