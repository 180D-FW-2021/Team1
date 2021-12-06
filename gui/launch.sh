#!/bin/sh

python3 ../speech_processing.py &
python ../pose_detection_code/together.py >/dev/null &
