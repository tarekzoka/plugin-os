#!/bin/sh
#

wget -O /tmp/plugin-extensions-ansite.tar.gz "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/plugin-extensions-ansite.tar.gz"

tar -xzf /tmp/*.tar.gz -C /

rm -r /tmp/plugin-extensions-ansite.tar.gz


killall -9 enigma2

sleep 2;

