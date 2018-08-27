#!/usr/bin/env bash
lsof -n | grep delete |grep "/data" | sort -nrk 7 | head -n 100 | awk '{print $2}' > /root/pid.tmp
for i in $(cat /root/pid.tmp)
do
	cd /proc/"$i"/fd && ls -lh | grep '/data/.*log\..*[0-9] (deleted)' | awk '{print $9}' > /root/fd.tmp
	for j in $(cat /root/fd.tmp)
	do
	cd /proc/"$i"/fd && echo > "$j"
	done
done