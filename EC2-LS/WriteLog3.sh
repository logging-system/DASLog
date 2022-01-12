#!/bin/bash
s=$(($(date +%s%N)/1000000))
truffle exec --network besuWallet ./scripts/index-write.js
e=$(($(date +%s%N)/1000000))
echo "Completed in"
echo  $(($e - $s))
echo "milliseconds"
python3 metaread6.py
echo "End . . ."
echo "--------------------------------------------------------"
