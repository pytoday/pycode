#!/usr/bin/env bash
# implement of run cmd or return custom error message.

function run_or_fail()
{
    explanation="$1"
    shift 1
    "$@" &>/dev/null
    if [ "$?" != 0 ]; then
        echo "$1" 1>&2
        exit 1
    fi
}