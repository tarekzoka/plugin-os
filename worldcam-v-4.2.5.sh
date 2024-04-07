#!/bin/sh
#

wget -O /tmp/worldcam.tar.gz "https://gitlab.com/hanfy1971/plugin/-/raw/main/worldcam/worldcam.tar.gz"

tar -xzf /tmp/worldcam.tar.gz -C /

rm -r /tmp/worldcam.tar.gz

killall -9 enigma2

sleep 2;

