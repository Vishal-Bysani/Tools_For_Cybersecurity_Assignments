#!/bin/bash


while [ 0 ]
    do
        zip7=`ls | grep "*.7z"`
        zip=`ls | grep "*.zip"`
        if [ -n $zip7 ]
            then

            if [ $zip7 == "chall1.7z" ]
                then
                7za e $zip7
                rm $zip7

            else
                file=`ls | sed -e "/script1.sh/d" -e "/$zip7/d"`
                p1=`cat $file`
                p2=`cat $file | base64`
                p3=`cat $file | base32`
                p4=`cat $file | hex`

                7za e $zip7 -p $p1 > /dev/null
                7za e $zip7 -p $p2 > /dev/null
                7za e $zip7 -p $p3 > /dev/null
                7za e $zip7 -p $p4 > /dev/null

                rm $zip7 $file

            fi
        elif [ -n $zip ]
        then
               file=`ls | sed -e "/script1.sh/d" -e "/$zip/d"`
                p1=`cat $file`
                p2=`cat $file | base64`
                p3=`cat $file | base32`
                p4=`cat $file | hex`

                unzip -P $p1 $zip > /dev/null
                unzip -P $p2 $zip > /dev/null
                unzip -P $p3 $zip > /dev/null
                unzip -P $p4 $zip > /dev/null

                rm $zip $file
         fi

         sleep 200000
      done

