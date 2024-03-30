#!/bin/sh
#

wget -O /tmp/extensions-sherlockmod_1.4.2.tar.gz "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/extensions-sherlockmod_1.4.2.tar.gz"

tar -xzf /tmp/*.tar.gz -C /

rm -r /tmp/extensions-sherlockmod_1.4.2.tar.gz


killall -9 enigma2

sleep 2;
