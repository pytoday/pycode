#!/usr/bin/env bash
TMP_PID=/dev/shm/pid.tmp
FD=/dev/shm/fd.tmp
lsof -n | grep delete |grep "/data" | sort -nrk 7 | head -n 100 | awk '{print $2}' > "${TMP_PID}"
for i in $(cat ${TMP_PID})
do
	cd /proc/"$i"/fd && ls -lh | grep '/data/.*log\..*[0-9] (deleted)' | awk '{print $9}' > "$FD"
	for j in $(cat $FD)
	do
	cd /proc/"$i"/fd && echo > "$j"
	done
done
