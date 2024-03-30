#!/bin/sh
#
wget -O /tmp/sherlockmod_1.4.2_.deb "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/sherlockmod_1.4.2_.deb"

wait

apt-get update ; dpkg -i /tmp/*.deb ; apt-get -y -f install

wait

dpkg -i --force-overwrite /tmp/*.deb

wait

rm -r /tmp/sherlockmod_1.4.2_.deb

wait

sleep 2;

exit 0


