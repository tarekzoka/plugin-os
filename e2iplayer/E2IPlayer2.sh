#!/bin/s
#

wget -O /tmp/e2iplayer.tar.gz "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/e2iplayer/e2iplayer.tar.gz"

tar -xzf /tmp/*.tar.gz -C /

rm -r /tmp/e2iplayer.tar.gz

killall -9 enigma2

sleep 2;

