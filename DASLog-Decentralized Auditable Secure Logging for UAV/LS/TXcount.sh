#!/bin/bash
#s=$(($(date +%s%N)/1000000))
node writeRootAdd2RDS.js

#e=$(($(date +%s%N)/1000000))
#echo "Completed in"
#echo  $(($e - $s))
#echo "milliseconds"
echo "Root inf. is stored to the RDS ..."
echo "--------------------------------------------------------"
