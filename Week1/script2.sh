#!/bin/bash
i=1
url="https://www.cse.iitb.ac.in/~akshatka/"
while [ 0 ]
    do
        wget $url

        file=`ls | grep *.html`

        url=`cat $file | grep -o "https://[A-Za-z0-9].*html"`

        if [ -z $url ]
            then
            url=`cat $file | grep -o "https://[A-Za-z0-9].*tar.gz"`
            wget $url 
            rm $file
            file=`ls | grep *.tar.gz`
            break
        fi

        rm $file
    done

tar -xvf $file

flag=`cat `find . -type f -size 87369c`|grep -o "flag{.*}"`
