#!/bin/sh
#

wget -O /tmp/quran.tar.gz "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/quran.tar.gz"

tar -xzf /tmp/quran.tar.gz.tar.gz -C /

rm -r /tmp/quran.tar.gz


killall -9 enigma2

sleep 2;
