#!/bin/bash

baseurl='http://www.projectmadurai.org/pm_etexts/utf8/pmuni'

for i in `seq -w 0466`
    do
    wget $baseurl$i.html
done
exit 0
