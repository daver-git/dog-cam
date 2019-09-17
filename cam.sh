#!/bin/bash
#
# dog-cam
# Pre & Post processing
#
#echo sh+ `date +"%F %T"` `df -h / --output=avail | tr -d '\n'` >> cam.log
echo sh+ `date +"%F %T"` `df -h / --output=avail | tail -1` Free  >> cam.log
python3 cam.py
echo sh- `date +"%F %T"` `df -h / --output=avail | tail -1` Free  >> cam.log
exit 0
