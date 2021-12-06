#!/bin/sh

python3 ../speech/speech_processing.py &
python ../pose_detection_code/together.py >/dev/null &
