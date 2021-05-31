#Importing 

import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os 
#Creating user interface
musicplayer=tkr.Tk()

musicplayer.title("Music Player")
#SETTING THE DIMENSION
musicplayer.geometry("450x350")
#asking for music directory 
directory=askdirectory()
#sttilng music directory to the current working directory
os.chdir(directory)
#creating the playlist
songlist= os.listdir()

playlist=tkr.Listbox(musicplayer,font="GoodDog 14 bold",bg="cyan2",selectmode=tkr.SINGLE)
#adding the songs from songlist to playlist
for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos=pos+1
#intializing pygame
pygame.init()
pygame.mixer.init()

#Function  for play button 
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
 #function for stop button                               
def ExitMusicPLayer():
    pygame.mixer.music.stop()

#function for pause button
def pause():
    pygame.mixer.music.pause()
#function for resume button
def resume():
    pygame.mixer.music.unpause()
#Creating Buttons 
Button1=tkr.Button(musicplayer, width=5, height=3, font="Cambria 20 bold",text="Play Music",command=play, bg="lime green", fg="black")

Button2=tkr.Button(musicplayer, width=5, height=3, font="Cambria 20 bold",text="Stop Music",command=ExitMusicPLayer, bg="red", fg="black")

Button3=tkr.Button(musicplayer, width=5, height=3, font="Cambria 20 bold",text="Pause Music",command=pause, bg="yellow", fg="black")

Button4=tkr.Button(musicplayer, width=5, height=3, font="Cambria 20 bold",text="Resume Music",command=resume, bg="skyblue", fg="black")

var=tkr.StringVar()
songtitle = tkr.Label(musicplayer,font="Helvetic 12 bold",textvariable=var)
songtitle.pack()

Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both",expand="yes")

musicplayer.mainloop()