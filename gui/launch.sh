#!/bin/sh

python3 ../speech_processing.py &
python ../pose.py >/dev/null &
