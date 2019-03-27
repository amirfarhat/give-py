#!/bin/bash
python3 interpret.py $1
[[ $? -eq 0 ]] && python3 _temp.py