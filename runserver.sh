#!/bin/bash

output=`screen -ls`
str='survival'

if [[ "$output" == *"$str"* ]]; then
	exit
else
	cd /home/playermc2003/spigotsurvival
	./start.sh
fi
