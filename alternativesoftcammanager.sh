#!/bin/sh
#

wget -O /tmp/alternativesoftcammanager_4.0_all.tar.gz "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/alternativesoftcammanager_4.0_all.tar.gz"

tar -xzf /tmp/*.tar.gz -C /

rm -r /tmp/alternativesoftcammanager_4.0_all.tar.gz


killall -9 enigma2

sleep 2;

