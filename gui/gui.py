#!/usr/bin/env python3

import tkinter as tk, threading
import imageio
import time
import sys, os
from PIL import Image, ImageTk
from playsound import playsound

class VideoPlayer(object):
    def __init__(self):
        self.video_thread = None
        self.audio_thread = None
        self.stop_threads = threading.Event()

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
        time.sleep(0.002)

def play():
    playsound('rickroll.mp3')

def reset():
    sys.stdout.flush()
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)


video_name = "rickroll.mp4" #This is your video file path
video = imageio.get_reader(video_name)

root = tk.Tk()
root.geometry('1200x800')

header = tk.Frame(root, bg='#8ecae6') #8ecae6
content = tk.Frame(root, bg='white')
footer = tk.Frame(root, bg='white')

root.columnconfigure(0, weight=1) # 100% 

root.rowconfigure(0, weight=1) # 20%
root.rowconfigure(1, weight=8) # 70%
root.rowconfigure(2, weight=1) # 10%

header.grid(row=0, sticky='news')
content.grid(row=1, sticky='news')
footer.grid(row=2, sticky='news')

text = tk.Label(root, text="AirController", bg='#8ecae6', font=("Helvetica", 18)).place(relx=0.5,rely=0.05,anchor='center')

video_player = VideoPlayer()

tutorial_button = tk.Button(root, text="Show Tutorial",
        activebackground='#517687', activeforeground='black', bg='#8ecae6',
        width=25, font=("Helvetica", 14), command=start_threads).place(x=30, rely=0.2, anchor='w')

customize_button = tk.Button(root, text="Customize Gestures", activebackground='#517687', activeforeground='black', bg='#8ecae6', width=25, font=("Helvetica", 14)).place(x=770, rely=0.2, anchor='e')

display_gestures_button = tk.Button(root, text="Display Gestures", activebackground='#517687', activeforeground='black', bg='#8ecae6', width=25, font=("Helvetica", 14)).place(x=30, rely=0.35, anchor='w')

#add in buttons to play videos

root.mainloop()
