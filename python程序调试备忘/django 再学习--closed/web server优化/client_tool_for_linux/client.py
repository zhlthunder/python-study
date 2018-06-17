#!/usr/bin/env python
import os,sys,commands,re


##tool init:
os.system('sh client.sh &>/dev/null')


##signal collecting dictory
dict={}

##collectiing hostname info
(status,output)=commands.getstatusoutput('hostname')
dict['serverno']=output


##collecting cpu infor
#cpu_num
(status, output) = commands.getstatusoutput("cat /proc/cpuinfo | grep 'physical id' | sort |uniq -c | awk '{print $5}'")
cpu_num=output.strip().split('\n')
#print(cpu_num)



#threads
(status, output) = commands.getstatusoutput("cat /proc/cpuinfo | grep 'physical id' | sort |uniq -c | awk '{print $1}'")
threads=output.strip().split('\n')

#model
model=[]
(status, output) = commands.getstatusoutput("cat /proc/cpuinfo | grep 'model name' | uniq | cut -d: -f2")
ret=output.strip()
pat='\s\d+\s'
ret=re.compile(pat).findall(ret)
if len(ret)==1:
	for i in range(0,len(threads)):
		model.append(ret[0])
#print(model)


#cores
cores=[]
(status, output) = commands.getstatusoutput("cat /proc/cpuinfo | grep 'cpu cores' |uniq | cut -d: -f2")
ret=output.strip().split('\n')
if len(ret)==1:
	for i in range(0,len(threads)):
		cores.append(ret[0])
#print(cores)


#maker
maker=[]
(status, output) = commands.getstatusoutput("cat /proc/cpuinfo | grep 'model name' | uniq | cut -d: -f2|grep -i intel")
ret=output.strip().split('\n')
if len(ret)==1:
	for i in range(0,len(threads)):
		maker.append('Intel')
#print(maker)


#frequency
frequency=[]
(status, output) = commands.getstatusoutput("cat /proc/cpuinfo | grep 'model name' | uniq | cut -d: -f2| awk '{print $NF}'")
ret=output.strip().split('\n')
if len(ret)==1:
	for i in range(0,len(threads)):
		frequency.append(ret[0])
#print(frequency)

cpu_info=zip(model,maker,frequency,cores,threads)

dict['cpu_info']=cpu_info


##collecting memory infor
#slots
(status, output) = commands.getstatusoutput("dmidecode -t memory | grep 'Part Number' | grep -v NO |wc -l")
slots=int(output)/2
#print(slots)


#model
model=[]
(status, output) = commands.getstatusoutput("dmidecode -t memory | grep 'Part Number:' | grep -v NO | cut -d: -f2")
output=output.strip().split('\n')
#print(output)
j=0
for i in output:
	model.append(i.strip())
	j+=1
	if j==slots:
		break
#print(model)	

	
#serial
serial=[]
(status, output) = commands.getstatusoutput("dmidecode -t memory | grep 'Serial Number:' | grep -v NO | cut -d: -f2")
output=output.strip().split('\n')
#print(output)
j=0
for i in output:
	serial.append(i.strip())
	j+=1
	if j==slots:
		break
#print(serial)	


#frequency
frequency=[]
(status, output) = commands.getstatusoutput("dmidecode -t memory | grep 'Speed:' | grep -v Configured | grep -v Unknown | cut -d: -f2")
output=output.strip().split('\n')
#print(output)
j=0
for i in output:
	frequency.append(i.strip())
	j+=1
	if j==slots:
		break
#print(frequency)	


#capacity
capacity=[]
(status, output) = commands.getstatusoutput("dmidecode -t memory | grep 'Size:' | grep -v Installed |cut -d: -f2")
output=output.strip().split('\n')
#print(output)
j=0
for i in output:
	capacity.append(i.strip())
	j+=1
	if j==slots:
		break
#print(capacity)	


#maker
maker=[]
(status, output) = commands.getstatusoutput("dmidecode -t memory | grep 'Manufacturer:' | grep -v NO | cut -d: -f2")
output=output.strip().split('\n')
#print(output)
j=0
for i in output:
	maker.append(i.strip())
	j+=1
	if j==slots:
		break
#print(maker)	

##dimm
dimm=[]
for i in serial:
	(status, output) = commands.getstatusoutput("dmidecode -t memory | grep "+i+" -B 7 | grep -i locator| grep -v Bank | uniq | cut -d: -f2")
	dimm.append(output)
#print(dimm)	

mem_info=zip(model,serial,frequency,capacity,maker,dimm)
	

#print(mem_info)
dict['mem_info']=mem_info





##collecting ethernet info
(status,output)=commands.getstatusoutput("lspci | grep -i eth | awk '{print $1}' | cut -d. -f1 | uniq -c | awk '{print $2}'")
#print(output)
busid=[]
for i in output.split('\n'):
	busid.append(i)
#print(busid)

##qty for sending
(status,output)=commands.getstatusoutput("lspci | grep -i eth | awk '{print $1}' | cut -d. -f1 | uniq -c | awk '{print $1}'")
qty=[]
for i in output.split('\n'):
        qty.append(i)
#print(qty)

##maker for sending
maker=[]
for i in busid:
	(status,output)=commands.getstatusoutput("lspci | grep -i "+i+" | sed -n '1p' | grep -i intel")
	if status==0:
		maker.append('Intel')
#print(maker)

##porttype for sending
type=[]
for i in busid:
        (status,output)=commands.getstatusoutput("lspci | grep -i "+i+" | grep 'SFP'")
        if status==0:
                type.append('SFI/SFP+')
	else:
		type.append('Twisted Pair')
#print(type)





#model for sending
model=[]
for i in busid:
	(status,output)=commands.getstatusoutput("lspci | grep -i eth | grep -i "+i+" | sed -n '1p' | cut -d: -f3")
	if status==0:
		model.append(output)
#print(model)
pat='\s(\w?\d+\w*)\s'
temp=[]
for i in model:
	ret=re.compile(pat).findall(i)[0]	
	temp.append("".join(ret))
model=temp
#print(model)



(status,output)=commands.getstatusoutput("ifconfig -a  | grep '^[a-z]' | cut -d: -f1")
dev=[]
for i in output.split('\n'):
        dev.append(i)
#print(dev)

fw=[]
for i in dev:
	(status,output)=commands.getstatusoutput("ethtool -i "+i+"|grep 'firmware' | cut -d: -f2")
	#print(i)
	output=output.strip()
	if output and output != 'N/A' and 'Operation not supported' not in output:
		fw.append(output)
#print(fw)


	
bussid=[]
for i in dev:
	(status,output)=commands.getstatusoutput("ethtool -i "+i+"|grep 'bus' | awk  '{print $2}'")
	#print(status)
	output=output.strip()
	if output and output != 'N/A' and 'Operation not supported' not in output and output !='tap':
		bussid.append(output)
#print(bussid)

index=[]
for i in busid:
	nn=bussid.index("0000:"+i+".0")
	index.append(nn)
#print(index)

##fw for sending
fw_final=[]
for i in index:
	fw_final.append(fw[i])
#print(fw_final)



nic_info=zip(model,maker,fw_final,qty,type)
#print(nic_info)
dict['nic_info']=nic_info
#print(dict)



(status,output)=commands.getstatusoutput("storcli /c0 /pall show | grep -i 'end device'")
##for lsi raid card: such as 9361,9271
if not status:
	#collecting raid card info
	raid=[]
	(status,output)=commands.getstatusoutput("storcli /c0 show all | grep -i ^model | grep [0-9]| cut -d= -f2")
	raid.append(output.strip())
	(status,output)=commands.getstatusoutput("storcli /c0 show all | grep -i 'Firmware Version' | cut -d= -f2")
	raid.append(output.strip())
	(status,output)=commands.getstatusoutput("storcli /c0 show all | grep -i 'Serial Number' | cut -d= -f2")
	raid.append(output.strip())
	raid.append('LSI')
	#print(raid)
	dict['raidcard']=raid

	##collecting disk info
	##disk model
	(status,output)=commands.getstatusoutput("storcli /c0 show all | grep '^[1-9]\{1,3\}' | awk '{print $(NF-1)}'")
	model=output.strip().split('\n')
	#disk interface type
	(status,output)=commands.getstatusoutput("storcli /c0 show all | grep '^[1-9]\{1,3\}' | awk '{print $7}'")
	type=output.strip().split('\n')
	#disk  maker
	(status,output)=commands.getstatusoutput("storcli /c0 show all | grep '^[1-9]\{1,3\}' | awk '{print $12}'")
	maker=output.strip().split('\n')
	#disk  media
	(status,output)=commands.getstatusoutput("storcli /c0 show all | grep '^[1-9]\{1,3\}' | awk '{print $8}'")
	media=output.strip().split('\n')
	#disk  fw
	(status,output)=commands.getstatusoutput("storcli /c0 /eall /sall show all | grep -i firm | cut -d= -f2")
	fw=output.strip().split('\n')
	#disk  slot
	(status,output)=commands.getstatusoutput("storcli /c0 show all | grep '^[1-9]\{1,3\}'|cut -d: -f2 | awk '{print $1}'")
	slot=output.strip().split('\n')
	#disk  sn
	(status,output)=commands.getstatusoutput("storcli /c0 /eall /sall show all | grep ^SN | cut -d= -f2")
	sn=output.strip().split('\n')
	disk=zip(model,type,maker,media,fw,slot,sn)
	#print(disk)
	dict['disk']=disk
print(dict)

