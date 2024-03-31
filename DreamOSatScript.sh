#!/bin/sh
#

wget -O /tmp/DreamOSatScript.tar.gz "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/DreamOSatScript.tar.gz"

tar -xzf /tmp/*.tar.gz -C /

rm -r /tmp/DreamOSatScript.tar.gz


killall -9 enigma2

sleep 2;
