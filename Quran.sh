#!/bin/sh
#

wget -O /tmp/Quran.tar.gz "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/Quran.tar.gz "

tar -xzf /tmp/*.tar.gz -C /

rm -r /tmp/Quran.tar.gz 


killall -9 enigma2

sleep 2;

