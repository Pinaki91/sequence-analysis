#!/bin/bash
FILES=ecoli/input/*
for f in $FILES
do
  echo "Processing $f file..."
  cat $f | tr -d "[:space:]" > temp
  echo 
  sed 's/MG1655/\n/g' temp > temp1
  sed 's/*//g' temp1 > temp2
  sed 's/U//g' temp2 > $f
done

