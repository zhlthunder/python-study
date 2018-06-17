#!/bin/bash


dir=`pwd`
rpm -ivh sg3_utils-1.37-5.el7.x86_64.rpm --nodeps
chmod +x sas3ircu-linux storcli-linux 
rm -rf /usr/bin/sas3ircu
rm -rf /usr/bin/storcli
ln -s $dir/sas3ircu-linux /usr/bin/sas3ircu
ln -s $dir/storcli-linux /usr/bin/storcli


