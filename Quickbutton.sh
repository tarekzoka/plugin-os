#!/bin/sh
##
echo ""

wget "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/Quickbutton.tar.gz"


tar -xzf Quickbutton.tar.gz  -C /

wait
rm -f /tmp/Quickbutton.tar.gz
echo "   UPLOADED BY  >>>>   TAREK_TT "   
sleep 4;                                                                                                                  
echo ". >>>>         RESTARING     <<<<"
echo BY-TAREK-HANFY   "**********************************************************************************"
echo

wait

killall -9 enigma2
