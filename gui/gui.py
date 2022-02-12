#!/usr/bin/env python3

import tkinter as tk, threading
import imageio
import time
import sys, os
import subprocess
from PIL import Image, ImageTk
from playsound import playsound

class VideoPlayer(object):
    def __init__(self):
        self.video_thread = None
        self.audio_thread = None
        self.stop_threads = threading.Event()

def play_video(tutorial_name):
    global video_name, audio_name, video
    video_name = tutorial_name+'.mp4'
    video = imageio.get_reader(video_name)
    audio_name = tutorial_name+'.mp3'
    start_threads()

def start_threads():
    label = tk.Label(root)    
    label.place(relx = 0.5, rely = 0.7, anchor='center')
    label.grid(row=2)
    video_player.video_thread = threading.Thread(target=stream, args=(label,))
    video_player.audio_thread = threading.Thread(target=play)
    video_player.video_thread.daemon = 1 
    video_player.audio_thread.daemon = 1 
    video_player.video_thread.start()
    video_player.audio_thread.start()
    return_button = tk.Button(root, text="Back", font=("Helvetica", 14),
            command=reset).place(relx=0.9, rely=0.9)

def stream(label):
    for image in video.iter_data():
        #image = image.resize((400, 300))
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image
        #time.sleep(0.002)

def play():
    playsound(audio_name)

def reset():
    sys.stdout.flush()
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

def launch_cv():
    sys.stdout.flush()
    subprocess.call("./launch.sh")

def stop_controller():
    sys.stdout.flush()
    subprocess.call("./kill.sh")
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

root = tk.Tk()
root.geometry('1200x800')

header = tk.Frame(root, bg='#8ecae6') #8ecae6
content = tk.Frame(root, bg='white')
footer = tk.Frame(root, bg='white')

#Plan: have the GUI be able to cycle through each mode by pressing a button

root.columnconfigure(0, weight=1) # 100% 

root.rowconfigure(0, weight=1) # 20%
root.rowconfigure(1, weight=8) # 70%
root.rowconfigure(2, weight=1) # 10%

header.grid(row=0, sticky='news')
content.grid(row=1, sticky='news')
footer.grid(row=2, sticky='news')

text = tk.Label(root, text="AirController", bg='#8ecae6', font=("Helvetica", 22)).place(relx=0.5,rely=0.05,anchor='center')

demo_videos = tk.Label(root, text="Tutorial Videos", font=("Helvetica",
    18)).place(relx=0.5, rely=0.15,anchor='center')

video_player = VideoPlayer()

channel_up = tk.Button(root, text="Channel Up",
        activebackground='#517687', activeforeground='black', bg='#8ecae6',
        width=25, font=("Helvetica", 14), command=lambda:
        play_video("channel-up")).place(x=30,
                rely=0.25, anchor='w')

channel_down = tk.Button(root, text="Channel Down",
        activebackground='#517687', activeforeground='black', bg='#8ecae6',
        width=25, font=("Helvetica", 14), command=lambda:
        play_video("channel-down")).place(x=30, rely=0.40, anchor='w')

power_on = tk.Button(root, text="Power On",
        activebackground='#517687', activeforeground='black', bg='#8ecae6',
        width=25, font=("Helvetica", 14), command=lambda:
        play_video("turn-on")).place(x=717, rely=0.25, anchor='e')


power_off = tk.Button(root, text="Power Off",
        activebackground='#517687', activeforeground='black', bg='#8ecae6',
        width=25, font=("Helvetica", 14), command=lambda:
        play_video("turn-off")).place(x=717, rely=0.40, anchor='e')

volume_up = tk.Button(root, text="Volume Up",
        activebackground='#517687', activeforeground='black', bg='#8ecae6',
        width=25, font=("Helvetica", 14), command=lambda:
        play_video("vol-up")).place(x=900,
                rely=0.25, anchor='w')

volume_down = tk.Button(root, text="Volume Down",
        activebackground='#517687', activeforeground='black', bg='#8ecae6',
        width=25, font=("Helvetica", 14), command=lambda:
        play_video("vol-down")).place(x=900, rely=0.40, anchor='w')

controller = tk.Label(root, text="Controller", font=("Helvetica",
    18)).place(relx=0.5, rely=0.55,anchor='center')

start_controller = tk.Button(root, text="Start Controller",
        activebackground='#517687', activeforeground='black', bg='#8ecae6',
        width=25, font=("Helvetica", 14), command=launch_cv).place(x=417,
                rely=0.70, anchor='e')

stop_controller = tk.Button(root, text="Stop Controller",
        activebackground='#517687', activeforeground='black', bg='#8ecae6',
        width=25, font=("Helvetica", 14), command=stop_controller).place(x=717,
                rely=0.70, anchor='w')

root.mainloop()
