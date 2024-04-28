#!/bin/sh
#
wget -O /tmp/extensions-e2iplayer_2_all.deb "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/e2iplayer/enigma2-plugin-extensions-e2iplayer_2_all.deb"

wait

apt-get update ; dpkg -i /tmp/*.deb ; apt-get -y -f install

wait

dpkg -i --force-overwrite /tmp/*.deb

wait

rm -r /tmp/enigma2-plugin-extensions-e2iplayer_2_all.deb

wait

sleep 2;

exit 0


