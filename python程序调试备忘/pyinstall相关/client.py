#!/usr/bin/env python
import os,sys,commands,re,math

def collect(dict):
	##signal collecting dictory

	if 'linux' in sys.platform:  ##for linux platform processing
		##tool init:
		os.system('sh /root/client_collect/config.sh &>/dev/null')

		##collectiing hostname info
		(status,output)=commands.getstatusoutput('hostname')
		dict['serverno']=output


		##collecting cpu infor
		try:
			#cpu_num
			(status, output) = commands.getstatusoutput("cat /proc/cpuinfo | grep 'physical id' | sort |uniq -c | awk '{print $5}'")
			cpu_num=output.strip().split('\n')
			#print(cpu_num)



			#threads
			(status, output) = commands.getstatusoutput("cat /proc/cpuinfo | grep 'physical id' | sort |uniq -c | awk '{print $1}'")
			threads=output.strip().split('\n')

			#serialnumber
			(status, output) = commands.getstatusoutput("dmidecode -t processor | grep 'Serial Number:' | sort | uniq -c | cut -d: -f2")
			serial=output.strip().split('\n')


			#model
			model=[]
			(status, output) = commands.getstatusoutput("cat /proc/cpuinfo | grep 'model name' | uniq | cut -d: -f2")
			ret=output.strip()
			pat='\s([E,0-9].*?)@'
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

			cpu_info=zip(model,maker,frequency,cores,threads,serial)
			#print(model)
			#print(maker)
			#print(frequency)
			#print(cores)
			#print(threads)
			#print(serial)

			dict['cpu_info']=cpu_info
		except Exception as err:
			pass


		##collecting memory infor
		try:
			#slots
			(status, output) = commands.getstatusoutput("dmidecode -t memory  | grep 'Locator:' | grep 'DIMM10' | wc -l")
			div=int(output)
			if not div:
				div=1

			(status, output) = commands.getstatusoutput("dmidecode -t memory | grep 'Part Number' | grep -v NO | grep -v Unknown |wc -l")
			slots=int(output)/div
			#print(slots)


			#model
			model=[]
			(status, output) = commands.getstatusoutput("dmidecode -t memory | grep 'Part Number:' | grep -v NO | grep -v Unknown| cut -d: -f2")
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
			(status, output) = commands.getstatusoutput("dmidecode -t memory | grep 'Serial Number:' | grep -v NO | grep -v Unknown| cut -d: -f2")
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
				(status, output) = commands.getstatusoutput("dmidecode -t memory | grep "+i+" -B 10 | grep -i locator| grep -v Bank | uniq | cut -d: -f2")
				dimm.append(output)
			#print(dimm)

			mem_info=zip(model,serial,frequency,capacity,maker,dimm)
			#print(model)
			#print(serial)
			#print(frequency)
			#print(capacity)
			#print(maker)
			#print(dimm)

			#print(mem_info)
			dict['mem_info']=mem_info
		except Exception as err:
			pass


		##collecting ethernet info
		try:
			(status,output)=commands.getstatusoutput("lspci | grep -i eth | grep -v Xilinx| awk '{print $1}' | cut -d. -f1 | uniq -c | awk '{print $2}'")
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
				if status==0: ## for intel nic
					maker.append('Intel')
				else:   ## for broadcom nic
					(status,output)=commands.getstatusoutput("lspci | grep -i "+i+" | sed -n '1p' | grep -i broadcom")
					if status==0:
						maker.append('Broadcom')

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
			pat2='\s(BCM\d+)\s'
			temp=[]
			for i in model:
				ret=re.search('Intel',i,re.I)
				if ret: # for intel nic
					ret=re.compile(pat).findall(i)[0]
					temp.append("".join(ret))
				else: # for broadcom nic

					ret=re.compile(pat2).findall(i)[0]
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


			driver=[]
			for i in dev:
				(status,output)=commands.getstatusoutput("ethtool -i "+i+"|grep '^version:' | cut -d: -f2")
				#print(i)
				output=output.strip()
				if output and output != 'N/A' and 'Operation not supported' not in output:
					driver.append(output)
			#print(driver)


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


			##driver for sending
			driver_final=[]
			for i in index:
				driver_final.append(driver[i])
			#print(driver_final)

			nic_info=zip(model,maker,fw_final,qty,type,driver_final)
			#print(model)
			#print(maker)
			#print(fw_final)
			#print(qty)
			#print(type)
			#print(nic_info)
			dict['nic_info']=nic_info
			#print(dict)
		except Exception as err:
			pass


        ##for raid card & disk
		#(status,output)=commands.getstatusoutput("storcli /c0 /pall show | grep -i 'end device'")
		(status,output)=commands.getstatusoutput("storcli /c0 show bootdrive | grep -i bootdrive")

		if not status: ##for lsi raid card: such as 9361,9271
			try:
				#collecting raid card info
				raid=[]
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep -i ^model | grep [0-9]| cut -d= -f2")
				raid.append(output.strip())
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep -i 'Firmware Version' | cut -d= -f2")
				raid.append(output.strip())
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep -i 'Serial Number' | cut -d= -f2")
				raid.append(output.strip())
				raid.append('LSI')
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep -i 'On Board Memory' | cut -d= -f2")
				raid.append(output.strip())
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep 'BBU Status' | cut -d= -f2")
				raid.append(output.strip())
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep 'Driver Version' | cut -d= -f2")
				raid.append(output.strip())
				#print(raid)
				dict['raidcard']=raid

				##collecting disk info
				##disk model
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep '^[1-9]\{1,3\}' |grep -v RAID | awk '{print $(NF-1)}'")
				model=output.strip().split('\n')
				#disk interface type
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep '^[1-9]\{1,3\}' |grep -v RAID| awk '{print $7}'")
				type=output.strip().split('\n')
				#disk  maker
				maker=[]
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep '^[1-9]\{1,3\}' |grep -v RAID| awk '{print $12}'")
				maker1=output.strip().split('\n')
				(status,output)=commands.getstatusoutput("storcli /c0 /eall /sall show all | grep 'Manufacturer Id' | cut -d= -f2")
				maker2=output.strip().split('\n')
				tem=zip(maker2,maker1)
				#print(tem)
				for i in tem:
					if 'ATA' in i[0]:
						maker.append(i[1])
					else:
						maker.append(i[0])

				#print(maker)	
				#disk  media
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep '^[1-9]\{1,3\}' |grep -v RAID| awk '{print $8}'")
				media=output.strip().split('\n')
				#disk  fw
				(status,output)=commands.getstatusoutput("storcli /c0 /eall /sall show all | grep -i firm | cut -d= -f2")
				fw=output.strip().split('\n')
				#disk  slot
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep '^[1-9]\{1,3\}'|grep -v RAID|cut -d: -f2 | awk '{print $1}'")
				slot=output.strip().split('\n')
				#disk  sn
				(status,output)=commands.getstatusoutput("storcli /c0 /eall /sall show all | grep ^SN | cut -d= -f2")
				sn=output.strip().split('\n')
				#disk  capacity
				cap=[]
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep '^[1-9]\{1,3\}' |grep -v RAID| awk '{print $5}'")
				cap1=output.strip().split('\n')
				(status,output)=commands.getstatusoutput("storcli /c0 show all | grep '^[1-9]\{1,3\}' |grep -v RAID| awk '{print $6}'")
				cap2=output.strip().split('\n')
				capp=zip(cap1,cap2)
				
				for i in capp:
					if 'TB' in i[1]:
						#print i[1]
						b=float(i[0])
						#print(b)
						a=b*1024*1024*1024*1024/1000000000000
						a=round(a,1)	
				       		cap.append(str(a)+'TB')
					else:
						#print i[1]
						b=float(i[0])
						a=b*1024*1024*1024/1000000000
						a=round(a)
						cap.append(str(a)+'GB')
				
				disk=zip(model,type,maker,media,fw,slot,sn,cap)
				#print(disk)
				dict['disk']=disk
			except Exception as err:
				pass

		else:
			(status,output)=commands.getstatusoutput("sas3ircu 0 display | grep 'Model Number'")
			if not status:# for sas3008
				try:
					#collecting raid card info
					raid=[]
					(status,output)=commands.getstatusoutput("sas3ircu 0 display | grep 'Controller type' | cut -d: -f 2")
					raid.append(output.strip())
					(status,output)=commands.getstatusoutput("sas3ircu 0 display | grep 'Firmware version' | cut -d: -f 2")
					raid.append(output.strip())
					sn='NO'
					raid.append(sn.strip())
					raid.append('LSI')
					#for cache
					raid.append('N/A')
					##for bbut
					raid.append('N/A')
					##for driver
					(status,output)=commands.getstatusoutput("modinfo mpt3sas | grep  '^version' | cut -d: -f2")
					raid.append(output.strip())
					#print(raid)
					dict['raidcard']=raid


					##collecting disk info
					##disk model
					(status,output)=commands.getstatusoutput("sas3ircu 0 display | grep 'Model Number' | cut -d: -f2")
					model=output.strip().split('\n')
					#disk interface type
					(status,output)=commands.getstatusoutput("sas3ircu 0 display | grep 'Protocol' | cut -d: -f2")
					type=output.strip().split('\n')
					#disk  maker
					(status,output)=commands.getstatusoutput("sas3ircu 0 display | grep 'Manufacturer' | cut -d: -f2")
					maker=output.strip().split('\n')
					#disk  media
					(status,output)=commands.getstatusoutput("sas3ircu 0 display | grep 'Drive Type' | cut -d: -f2")
					media=output.strip().split('\n')
					#disk  fw
					(status,output)=commands.getstatusoutput("sas3ircu 0 display | grep 'Firmware Revision' | cut -d: -f2")
					fw=output.strip().split('\n')
					#disk  slot
					(status,output)=commands.getstatusoutput("sas3ircu 0 display | grep 'Slot #' | cut -d: -f2")
					slot=output.strip().split('\n')
					#disk  sn
					(status,output)=commands.getstatusoutput("sas3ircu 0 display | grep 'Serial No' | cut -d: -f2")
					sn=output.strip().split('\n')
					#disk  capacity
					capp=[]
					(status,output)=commands.getstatusoutput("sas3ircu 0 display | grep 'Size' | cut -d: -f2 | cut -d/ -f1")
					cap=output.strip().split('\n')
					for i in cap:
						a=int(i)
						b=a*1024*1024/1000000000
						capp.append(str(b)+'GB')
					disk=zip(model,type,maker,media,fw,slot,sn,capp)
					#print(disk)
					dict['disk']=disk
				except Exception as err:
					pass

			else: # for pmc7805
				try:
					#collecting raid card info
					raid=[]
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 ad | grep 'Controller Model' | cut -d: -f2")
					raid.append(output.strip())
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 ad | grep 'Firmware' | cut -d: -f2")
					raid.append(output.strip())
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 ad | grep 'Controller Serial Number' | cut -d: -f2")
					raid.append(output.strip())
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 ad | grep 'Controller Model' | awk '{print $4}'")
					raid.append(output.strip())

					#for cache
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 ad | grep -i memory | cut -d: -f2")
					raid.append(output.strip())

					##for bbut
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 Ad | grep ' Overall Backup' | cut -d: -f2")
					raid.append(output.strip())
					##for driver
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 Ad | grep -i driver | cut -d: -f2")
					raid.append(output.strip())
					#print(raid)
					dict['raidcard']=raid



					##collecting disk info
					##disk model
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 pd | grep -i model | grep -v SXP |cut -d: -f2 ")
					model=output.strip().split('\n')

					#disk interface type
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 pd | grep ' Transfer Speed' | cut -d: -f2")
					type=output.strip().split('\n')

					#disk  maker
					maker=[]
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 pd  | grep 'Vendor' | cut -d: -f2")
					maker1=output.strip().split('\n')
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 pd | grep -i model | grep -v SXP | cut -d: -f2 | awk '{print $1}'")
					maker2=output.strip().split('\n')
					makk=zip(maker1,maker2)
					for i in makk:
						if 'ATA' in i[0]:
							maker.append(i[1])
						else:
							maker.append(i[0])

					#disk  media
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 pd | grep -i ssd | cut -d: -f2")
					media=output.strip().split('\n')
					temp=[]
					for i in media:
						if i.strip()=='Yes':
							temp.append('SSD')
						else:
							temp.append('HDD')
					media=temp

					#disk  fw
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 pd | grep -i Firmware | cut -d: -f2")
					fw=output.strip().split('\n')

					#disk  slot
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 pd | grep 'Reported Location' | cut -d: -f 2 | cut -d, -f2")
					slot=output.strip().split('\n')

					#disk  sn
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 pd | grep 'Serial number' | cut -d: -f 2")
					sn=output.strip().split('\n')

					#disk  capacity
					cap=[]
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 pd | grep 'Total Size' | cut -d: -f2 |awk '{print $1}'")
					cap1=output.strip().split('\n')
					(status,output)=commands.getstatusoutput("arcconf getconfig 1 pd | grep 'Total Size' | cut -d: -f2 |awk '{print $2}'")
					cap2=output.strip().split('\n')
					capp=zip(cap1,cap2)

					
					for i in capp:
                                        	if 'TB' in i[1]:
                                                	#print i[1]
                                                	b=float(i[0])
                                                	#print(b)
                                                	a=b*1024*1024*1024*1024/1000000000000
                                                	a=round(a)
                                                	cap.append(str(a)+'TB')
                                        	else: ##for MB 
                                                	#print i[1]
                                                	b=float(i[0])
                                                	a=b*1024*1024/1000000000
                                                	a=round(a)
                                                	cap.append(str(a)+'GB')



					
						
					disk=zip(model,type,maker,media,fw,slot,sn,cap)
					#print(disk)
					dict['disk']=disk
				except Exception as err:
					pass
	else:  #for windows platform
		##config winrm
		COMMDIR=os.path.join(os.path.dirname(__file__),'config.bat').replace('\\','/')
		os.system(COMMDIR)

		##cpu
		try:
			##name
			fp=os.popen("wmic cpu get 'name'")
			output=fp.read()
			# print(output)
			pat='\s([E,0-9].*?)\s@'
			name=re.compile(pat).findall(str(output).strip())
			# print(name)

			#maker
			maker=[]
			fp=os.popen("wmic cpu get 'Manufacturer' |findstr -v Manu")
			output=fp.read()
			# print(output)
			temp=output.strip().split('\n')
			for i in temp:
				maker.append(i.strip())
			# print(maker)

			#frequency
			frequency=[]
			fp=os.popen("wmic cpu get 'MaxClockSpeed' |findstr -v Max")
			output=fp.read()
			# print(output)
			temp=output.strip().split('\n')
			for i in temp:
				frequency.append(i.strip())
			# print(frequency)

			#cores
			cores=[]
			fp=os.popen("wmic cpu get 'NumberOfCores' |findstr -v Num")
			output=fp.read()
			# print(output)
			temp=output.strip().split('\n')
			for i in temp:
				cores.append(i.strip())
			# print(cores)

			#NumberOfLogicalProcessors
			threads=[]
			fp=os.popen("wmic cpu get 'NumberOfLogicalProcessors' |findstr -v Num")
			output=fp.read()
			# print(output)
			temp=output.strip().split('\n')
			for i in temp:
				threads.append(i.strip())
			# print(threads)

			##serial:
			serial=[]
			for i in range(0,len(name)):
				serial.append('N/A')

			cpu_info=zip(name,maker,frequency,cores,threads,serial)
			# print cpu_info
			dict['cpu_info']=cpu_info
		except Exception as err:
			pass

		##memory
		try:
			#partnumber
			partnumber=[]
			fp=os.popen("wmic MEMORYCHIP get 'PartNumber' | findstr -v Part")
			output=fp.read()
			# print(output)
			temp=output.strip().split('\n')
			for i in temp:
				partnumber.append(i.strip())
			# print(partnumber)

			#serial
			serial=[]
			fp=os.popen("wmic MEMORYCHIP get 'SerialNumber' | findstr -v Serial")
			output=fp.read()
			# print(output)
			temp=output.strip().split('\n')
			for i in temp:
				serial.append(i.strip())
			# print(serial)


			#speed
			speed=[]
			fp=os.popen("wmic MEMORYCHIP get 'Speed' | findstr -v Speed")
			output=fp.read()
			# print(output)
			temp=output.strip().split('\n')
			for i in temp:
				speed.append(i.strip())
			# print(speed)

			#capacity
			cap=[]
			fp=os.popen("wmic MEMORYCHIP get 'Capacity' | findstr -v Cap")
			output=fp.read()
			# print(output)
			temp=output.strip().split('\n')
			for i in temp:
				ttt=float(i.strip())
				cap.append(str(math.ceil(ttt/1024/1024/1024))+'GB')
			# print(cap)

			#Manufacturer
			maker=[]
			fp=os.popen("wmic MEMORYCHIP get 'Manufacturer' | findstr -v Manu")
			output=fp.read()
			# print(output)
			temp=output.strip().split('\n')
			for i in temp:
				maker.append(i.strip())
			# print(maker)

			#DIMM
			dimm=[]
			fp=os.popen("wmic MEMORYCHIP get 'DeviceLocator' | findstr -v Device")
			output=fp.read()
			# print(output)
			temp=output.strip().split('\n')
			for i in temp:
				dimm.append(i.strip())
			# print(dimm)
			mem_info=zip(partnumber,serial,speed,cap,maker,dimm)
			dict['mem_info']=mem_info
			# print(mem_info)
		except Exception as err:
			pass


		##network card
		try:
			#model
			fp=os.popen('wmic NIC get "Caption" | findstr "Intel"')
			output=fp.read()
			pat='\s\w?\d+\s'
			ret=re.compile(pat).findall(output)
			#print(ret)
			model=ret

			#maker
			maker=[]
			fp=os.popen('wmic NIC get "Manufacturer" | findstr "Intel"')
			output=fp.read()
			for i in output.strip().split('\n'):
				maker.append(i.strip())
			#print(maker)

			##fw
			fw=[]
			for i in range(0,len(maker)):
				fw.append('NA')

			##port
			port=[]
			for i in range(0,len(maker)):
				port.append('1')

			#type
			fp=os.popen('wmic NIC get "Caption" | findstr "Intel"')
			output=fp.read()
			pat='\s(\d{1,3}\s?G[i,b].*?)\s'
			ret=re.compile(pat).findall(output)
			#print(ret)
			type=ret
			nic_info=zip(model,maker,fw,port,type)
			#print(model)
			#print(maker)
			#print(fw)
			#print(port)
			#print(type)
			dict['nic_info']=nic_info
		except Exception as err:
			pass
		
		
		try:
			##raid & disk
			COMMDIR=os.path.dirname(os.path.abspath(__file__))
			##config environment path
			# print(COMMDIR)
			temp="setx PATH '%PATH%;C:\client_collect'"
			#print(temp)
			fp=os.popen(temp)

			fp=os.popen("storcli64.exe /c0 /pall show | findstr -i 'end'")
			output=fp.read()
			if not output: #for sas3008
				try:
					# print("11111111111111111")
					#collecting raid card info
					raid=[]
					fp=os.popen("sas3ircu-win.exe 0 display  | findstr  Controller | findstr -v info")
					output=fp.read()
					#print(output)
					pat='\sSAS\d+\s'
					ret=re.compile(pat).findall(output)
					raid.append(ret[0].strip())


					fp=os.popen("sas3ircu-win.exe 0 display  | findstr  Firmware  | findstr -v Rev")
					output=fp.read()
					pat='\s(\d.*?)\s'
					ret=re.compile(pat).findall(output)
					raid.append(ret[0].strip())

					sn='N/A'
					raid.append(sn.strip())
					raid.append('LSI')
					#for cache
					raid.append('NO')
					##for bbut
					raid.append('NO')
					#print(raid)
					dict['raidcard']=raid

					##collecting disk info
					##disk model
					fp=os.popen("sas3ircu-win.exe 0 display | findstr Model")
					output=fp.read()
					pat=':(\s{1,}.*?)\s'
					ret=re.compile(pat).findall(output)
					# print(ret)
					model=ret


					#disk interface type
					fp=os.popen("sas3ircu-win.exe 0 display | findstr Protocol")
					output=fp.read()
					pat=':(\s{1,}.*?)\s'
					ret=re.compile(pat).findall(output)
					# print(ret)
					type=ret

					#disk  maker
					fp=os.popen("sas3ircu-win.exe 0 display | findstr Manufacturer")
					output=fp.read()
					pat=':(\s{1,}.*?)\s'
					ret=re.compile(pat).findall(output)
					# print(ret)
					maker=ret

					#disk  media
					fp=os.popen('sas3ircu-win.exe 0 display | findstr /c:"Drive Type"')
					output=fp.read()
					pat=':(\s{1,}.*?)\s'
					ret=re.compile(pat).findall(output)
					# print(ret)
					media=ret

					#disk  fw
					fp=os.popen('sas3ircu-win.exe 0 display | findstr /c:"Firmware Revision"')
					output=fp.read()
					pat=':(\s{1,}.*?)\s'
					ret=re.compile(pat).findall(output)
					# print(ret)
					fw=ret

					#disk  slot
					fp=os.popen('sas3ircu-win.exe 0 display | findstr /c:"Slot #"')
					output=fp.read()
					pat=':(\s{1,}.*?)\s'
					ret=re.compile(pat).findall(output)
					# print(ret)
					slot=ret

					#disk  sn
					fp=os.popen('sas3ircu-win.exe 0 display | findstr /c:"Serial No"')
					output=fp.read()
					pat=':(\s{1,}.*?)\s'
					ret=re.compile(pat).findall(output)
					# print(ret)
					sn=ret

					#disk  capacity
					capp=[]
					fp=os.popen('sas3ircu-win.exe 0 display | findstr -i size"')
					output=fp.read()
					pat=':\s{1,}(\d+)/'
					cap=re.compile(pat).findall(output)
					for i in cap:
						a=int(i)
						b=a*1024*1024/1000000000
						capp.append(str(b)+'GB')


					disk=zip(model,type,maker,media,fw,slot,sn,capp)

					
					

					#print(disk)
					dict['disk']=disk
				except Exception as err:
					pass
					
		except Exception as err:
			pass
	# print(dict)

if __name__ == '__main__':
	result={}
	collect(result)
	print(result)





"""
dict format
{'nic_info': [('X722', 'Intel', '3.1d 0x800008bb 255.65535.255', '4', 'SFI/SFP+')],
'mem_info': [('M393A4K40BB1-CRC', '32AB6217', '2400 MHz', '32 GB', 'Samsung', ' DIMM3')],
'cpu_info': [(' 5118 ', 'Intel', '2.30GHz', '12', '24','sn2324')],
'raidcard': ['AVAGO MegaRAID SAS 9361-16i', '4.740.00-8288', 'SK72771059', 'LSI','2048MB',],
'disk': [('HUS726060ALE610', 'SATA', 'HGST', 'HDD', 'T907', '1', 'K1JJPGZD            ')]
}
"""
