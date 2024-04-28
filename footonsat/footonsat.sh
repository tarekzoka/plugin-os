#!/bin/sh
#
wget -O /tmp/footonsat_1.9-r0_all.deb "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/footonsat/enigma2-plugin-extensions-footonsat_1.9-r0_all.deb"

wait

apt-get update ; dpkg -i /tmp/*.deb ; apt-get -y -f install

wait

dpkg -i --force-overwrite /tmp/*.deb

wait

rm -r /tmp/enigma2-plugin-extensions-footonsat_1.9-r0_all.deb

wait

sleep 2;

exit 0


