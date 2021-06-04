#!/bin/bash
base_filename=$1;
dirname_="/home/bdemirel/hackathon"
pdftotext "$1" "${dirname_}/${base_filename}.txt.tmp"
iconv -f ISO-8859-1 -t UTF-8 "${dirname_}/${base_filename}.txt.tmp" > "${dirname_}/${base_filename}.txt"
rm "${dirname_}/${base_filename}.txt.tmp"
echo "____filename___:${dirname_}/${base_filename}.txt"
