#!/bin/sh
#
wget -O /tmp/vavoo_1.x_.deb "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/vavoo_1.x_.deb"

wait

apt-get update ; dpkg -i /tmp/*.deb ; apt-get -y -f install

wait

dpkg -i --force-overwrite /tmp/*.deb

wait

rm -r /tmp/vavoo_1.x_.deb

wait

sleep 2;

exit 0


