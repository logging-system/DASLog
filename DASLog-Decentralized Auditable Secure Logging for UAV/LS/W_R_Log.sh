#!/bin/bash
python3 Get-new-1.py &
python3 RDS-read-rootGen1.py &
python3 fetch-Block-inf.py &
echo "--------------------------------------------------------"
