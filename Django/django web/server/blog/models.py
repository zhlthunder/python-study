from django.db import models


class Publisher(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	city=models.CharField(max_length=60)
	state_province=models.CharField(max_length=30)
	country=models.CharField(max_length=50)
	website=models.URLField()
	
	def __unicode__(self):
		return self.name

class Author(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=40)
	email=models.EmailField()
	
	def __unicode__(self):
		return self.first_name

class Book(models.Model):
	title=models.CharField(max_length=100)
	author=models.ManyToManyField(Author)
	publisher=models.ForeignKey(Publisher)
	publication_date=models.DateField()
	
	
	def __unicode__(self):
		return self.title


class Server_db(models.Model):
	name=models.CharField(max_length=30)
	ip_addr=models.CharField(max_length=30)
	user=models.CharField(max_length=30)
        passwd=models.CharField(max_length=30)
	cpu=models.CharField(max_length=30,null=True,blank=True)
	memory=models.CharField(max_length=400,null=True,blank=True)
	ethernet=models.CharField(max_length=80,null=True,blank=True)
	disk=models.CharField(max_length=400,null=True,blank=True)
	raid=models.CharField(max_length=30,null=True,blank=True)

	def __unicode__(self):
		return self.name


class Disk_info(models.Model):
	bw_num_r=models.CharField(max_length=30,null=True,blank=True)
	bw_idp_r=models.CharField(max_length=30,null=True,blank=True)
	bw_r_spec=models.CharField(max_length=30,null=True,blank=True)
	bw_num_w=models.CharField(max_length=30,null=True,blank=True)
	bw_idp_w=models.CharField(max_length=30,null=True,blank=True)
	bw_w_spec=models.CharField(max_length=30,null=True,blank=True)
	io_num_r=models.CharField(max_length=30,null=True,blank=True)
	io_idp_r=models.CharField(max_length=30,null=True,blank=True)
	iops_r_spec=models.CharField(max_length=30,null=True,blank=True)
	io_num_w=models.CharField(max_length=30,null=True,blank=True)
	io_idp_w=models.CharField(max_length=30,null=True,blank=True)
	iops_w_spec=models.CharField(max_length=30,null=True,blank=True)
	disk_cache=models.CharField(max_length=30,null=True,blank=True)
	t_date=models.CharField(max_length=30,null=True,blank=True)
	d_model=models.CharField(max_length=30,null=True,blank=True)
	d_vendor=models.CharField(max_length=30,null=True,blank=True)
	d_capacity=models.CharField(max_length=30,null=True,blank=True)
	d_firmware=models.CharField(max_length=30,null=True,blank=True)
	d_inch=models.CharField(max_length=30,null=True,blank=True)
	d_interface=models.CharField(max_length=30,null=True,blank=True)
	d_medium=models.CharField(max_length=30,null=True,blank=True)
	d_sector=models.CharField(max_length=30,null=True,blank=True)
	d_rotarate=models.CharField(max_length=30,null=True,blank=True)
	d_speed=models.CharField(max_length=30,null=True,blank=True)
	rd_model=models.CharField(max_length=30,null=True,blank=True)
	rd_firmware=models.CharField(max_length=30,null=True,blank=True)
	vol_type=models.CharField(max_length=30,null=True,blank=True)
	seq_r_bw=models.CharField(max_length=30,null=True,blank=True)
	seq_w_bw=models.CharField(max_length=30,null=True,blank=True)
	rand_r_iops=models.CharField(max_length=30,null=True,blank=True)
	rand_w_iops=models.CharField(max_length=30,null=True,blank=True)

	def __unicode__(self):
		return self.d_model

