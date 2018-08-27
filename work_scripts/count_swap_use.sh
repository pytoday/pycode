#!/usr/bin/env bash
total=$(free |tail -1|awk '{print $2}')
if [ "$total" -eq 0 ];then
    per=0
    /data/services/op_agent_d/tools/send_value 3429 $per
else
    per=$(free |tail -1|awk '{printf "%.2f",$3*100/$2}')
    if [ $per -gt 50 ];then
        /data/services/op_agent_d/tools/send_value "fid=3429&value=$per&info=交换空间使用率过高"
    else
         /data/services/op_agent_d/tools/send_value 3429 $per
    fi
fi
exit
