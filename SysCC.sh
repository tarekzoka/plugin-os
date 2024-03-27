#!/bin/sh
##
echo ""

wget "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/SysCC.tar.gz"


tar -xzf SysCC.tar.gz  -C /

wait
rm -f /tmp/SysCC.tar.gz
echo "   UPLOADED BY  >>>>   TAREK_TT "   
sleep 4;                                                                                                                  
echo ". >>>>         RESTARING     <<<<"
echo BY-TAREK-HANFY   "**********************************************************************************"
echo

wait

killall -9 enigma2
