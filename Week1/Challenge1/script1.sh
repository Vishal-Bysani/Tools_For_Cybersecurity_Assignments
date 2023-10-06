#!/bin/bash

n=0
while [ 0 ]
    do
        zip7=`ls | grep *.7z`
        zip=`ls | grep *.zip`
        if [  $zip7 ]
            then

            if [ $zip7 = "chall1.7z" ]
                then
                7za e $zip7
                rm $zip7

            else
                file=`ls | sed -e "/script1.sh/d" -e "/$zip7/d"`

               #if [ $file = "xPfPGoeZ2p" ]
                #    then
                 #   break
                #fi

                p1=`cat $file`
                p2=`cat $file | base64`
                p3=`cat $file | base32`
                p4=`cat $file | hex`

                7z x -p$p1 $zip7 > /dev/null
                7z x -p$p2 $zip7> /dev/null
                7z x -p$p3 $zip7> /dev/null
                7z x -p$p4 $zip7> /dev/null

                rm $zip7 $file

            fi
        elif [  $zip ]
        then
               file=`ls | sed -e "/script1.sh/d" -e "/$zip/d"`
                
                #if [ $file = "xPfPGoeZ2p" ]
                 #   then
                  #  break
               # fi
                p1=`cat $file`
                p2=`cat $file | base64`
                p3=`cat $file | base32`
                p4=`cat $file | hex`

                unzip -P $p1 $zip > /dev/null
                unzip -P $p2 $zip > /dev/null
                unzip -P $p3 $zip > /dev/null
                unzip -P $p4 $zip > /dev/null

                rm $zip $file
         
         else
             break
         fi
         n=$((n+1))
         echo $n
      done
flag=`cat flag`

echo $flag
