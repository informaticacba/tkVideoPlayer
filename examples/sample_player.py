import datetime
import tkinter as tk
from tkinter import filedialog
from tkmultimedia import TkinterVideo


def update_duration(event):
    print("UPdating duration")
    end_time["text"] = str(datetime.timedelta(seconds=vid_player.duration()))
    progress_slider["to"] = vid_player.duration()


def update_scale(event):
    progress_slider.set(vid_player.current_duration())


def load_video():
    file_path = filedialog.askopenfilename()

    if file_path:
        vid_player.load(file_path)

    progress_slider.config(to=0, from_=0)
    progress_slider.set(0)


def seek(value):
    vid_player.seek(int(value))


def skip(value: int):
    vid_player.skip_sec(value)


def play_pause():
    if vid_player.is_paused():
        vid_player.play()
        play_pause_btn["text"] = "Pause"

    else:
        vid_player.pause()
        play_pause_btn["text"] = "Play"


def video_ended(event):
    progress_slider.set(progress_slider["to"])
    play_pause_btn["text"] = "Play"


root = tk.Tk()

load_btn = tk.Button(root, text="Load", command=load_video)
load_btn.pack()

vid_player = TkinterVideo(master=root, scaled=True, pre_load=False)
vid_player.pack(expand=True, fill="both")

play_pause_btn = tk.Button(root, text="Play", command=play_pause)
play_pause_btn.pack()

skip_plus_5sec = tk.Button(root, text="Skip -5 sec", command=lambda: skip(-5))
skip_plus_5sec.pack(side="left")

start_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)))
start_time.pack(side="left")

progress_slider = tk.Scale(root, from_=0, to=0, orient="horizontal", command=seek)
progress_slider.pack(side="left", fill="x", expand=True)

end_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)))
end_time.pack(side="left")

vid_player.bind("<<Duration>>", update_duration)
vid_player.bind("<<SecondChanged>>", update_scale)
vid_player.bind("<<Ended>>", video_ended )

skip_plus_5sec = tk.Button(root, text="Skip +5 sec", command=lambda: skip(5))
skip_plus_5sec.pack(side="left")

root.mainloop()
