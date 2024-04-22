#!/bin/sh
#
mkdir /usr/lib/enigma2/python/Plugins/Extensions/Quran


wget -O /usr/lib/enigma2/python/Plugins/Extensions/Quran/Quran.png "https://github.com/tarekzoka/plugin-os/blob/main/Quran/Quran.png"
wait
wget -O /usr/lib/enigma2/python/Plugins/Extensions/Quran/__init__.py"https://github.com/tarekzoka/plugin-os/blob/main/Quran/__init__.py"
wait
wget -O /usr/lib/enigma2/python/Plugins/Extensions/Quran/__init__.pyo "https://github.com/tarekzoka/plugin-os/blob/main/Quran/__init__.pyo"
wait
wget -O /usr/lib/enigma2/python/Plugins/Extensions/Quran/plugin.py "https://github.com/tarekzoka/plugin-os/blob/main/Quran/plugin.py"
wait
wget -O /usr/lib/enigma2/python/Plugins/Extensions/Quran/plugin.pyo "https://github.com/tarekzoka/plugin-os/blob/main/Quran/plugin.pyo"
wait
wget -O /usr/lib/enigma2/python/Plugins/Extensions/Quran/tilawat/kuraas.xml"https://github.com/tarekzoka/plugin-os/blob/main/Quran/tilawat/kuraas.xml"
wait
wget -O /usr/lib/enigma2/python/Plugins/Extensions/Quran/tilawat/rtmpdump"https://github.com/tarekzoka/plugin-os/blob/main/Quran/tilawat/rtmpdump"
wait
wget -O /usr/lib/enigma2/python/Plugins/Extensions/Quran/tilawat/soura.xml"https://github.com/tarekzoka/plugin-os/blob/main/Quran/tilawat/soura.xml"
wait

#!/bin/sh

#

wget -O /tmp/icon.tar.gz "https://raw.githubusercontent.com/tarekzoka/plugin-os/main/Quran/icon.tar.gz"

tar -xzf /tmp/icon.tar.gz -C /

rm -r /tmp/Quran.tar.gz


killall -9 enigma2

sleep 2;

