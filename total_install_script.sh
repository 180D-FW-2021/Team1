#!/bin/sh
apt-get update
yes | pip install opencv-python
yes | pip install mediapipe
yes | pip install pyaudio
yes | pip install six
yes | pip install google-cloud-speech
yes | pip install python-tk
yes | pip install threading
yes | pip install pillow
yes | pip install imageio
yes | pip install playsound
yes | brew install portaudio --HEAD
yes | pip install paho-mqtt
yes | pip install imageio-ffmpeg
export GOOGLE_APPLICATION_CREDENTIALS="/Users/stephenchu/ECE180DA/oval-replica-340120-1d2ac5839b16.json"
