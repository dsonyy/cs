#!/usr/bin/env bash

path=$(dirname "$0")
for arg in "$@"
do
    PYTHONPATH=$path python3 $arg
done