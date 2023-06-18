#libraries


import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer

# Create a GUI window
root = Tk()
root.title("Music Player")
root.geometry("920x600+290+85")
root.configure(background='#212121')
root.resizable(False, False)
mixer.init()


# Create a function to open a file
def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


music_pla=True
# Button

Button(root, text="Start", bg="#ffffff", bd=0,
       command=PlayMusic).place(x=100, y=100, width=100, height=50)



def butt():
    global music_pla
    if music_pla:
        mixer.music.pause()
    else:
        mixer.music.unpause()
    music_pla=not music_pla


Button(root, text="Play/Pause", bg="#00ff00", bd=0,
       command=butt).place(x=100, y=200,width=100, height=50)


Button(root, text="stop", bg="#ff0000", bd=0,
       command=mixer.music.stop).place(x=100, y=300,width=100, height=50)
# Label 



Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=350, y=100, width=560, height=250)


Button(root, text="Open Folder", width=15, height=2, font=("times new roman",
       12, "bold"), fg="Black", bg="#21b3de", command=AddMusic).place(x=330, y=50)


Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

des=Label(root, text="Follow these Steps:\n\t 1. Open Directory of Song\n\t   2. Select Song using Cursor\n3. Start the song",height=6,width=40,bg="#333333",anchor='w', fg="yellow",font=("Times new roman", 14)).place(x=100,y=400)

# Execute Tkinter
root.mainloop()
