#!/bin/bash

#mv nbm_cnf_template.ini nbm_cnf.ini
folder=/var/opt/nbmcom/data/site_engineer
#filename=nbm_cnf.ini 
#filename1=nbm_cnf

function select_type()
{
read -t 30 -p "please select mv filetype:ini;xml;dat. " filetype

case "$filetype" in 
	"ini")
		mv_ini
		;;
	"xml")
		mv_xml
		;;
	"dat")
		mv_dat
		;;
	*)
		echo "please input ini or xml or dat"
esac
} 		


function mv_ini()
{
echo "filename: nbi_cnf.ini nbi_common.ini nbi_socket.ini nbm_cnf.ini"  
read -t 30 -p "please input filename:" filename
echo "filename1:nbi_cnf nbi_common nbi_socket nbm_cnf"
read -t 30 -p "please input filname1:" filename1
if [ -f "$folder/$filename" ];then
	echo "$filename exist"
else
	mv $filename1_template.ini $filename
	if [ -f "$folder/$filename" ];then
		echo "the $filename mv name ok."
	fi
fi
}


function mv_xml()
{
echo "filename: Migration.xml ne_config.xml ne_specialtrans.xml"
read -t 30 -p "please input filename:" filename
echo "filename1: Migration  ne_config ne_specialtrans"
read -t 30 -p "please input filename1:" filename1
if [ -f "$folder/$filename" ];then
        echo "$filename exist"
else
        mv $filename1_template.xml $filename
        if [ -f "$folder/$filename" ];then
                echo "the $filename mv name ok."
        fi
fi
}


function mv_dat()
{
echo "filename: ne_common.dat ne_udc.dat"
read -t 30 -p "please input filename:" filename
echo "filename1: ne_common  ne_udc"
read -t 30 -p "please input filename1:" filename1
if [ -f "$folder/$filename" ];then
        echo "$filename exist"
else
        mv $filename1_template.dat $filename
        if [ -f "$folder/$filename" ];then
                echo "the $filename mv name ok."
        fi
fi
}



select_type
