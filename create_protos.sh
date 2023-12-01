#!/bin/zsh
if [ $# -lt 2 ]; then
    echo "Must give year and day positional arguments"
    exit 1
fi
for i in {1..$2}
do
    DAY=$(printf "%02d" $i)
    mkdir -p $1/$DAY
    cp -n proto/* $1/$DAY/
    cd $1/$DAY
    aoc download --year $1 --day $i
    cd ../..
done
