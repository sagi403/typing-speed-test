from tkinter import *
from tkinter.font import Font


words = ["word1","word2","word3","word4"]
colours = ["blue","green","red","yellow"]

window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20)

for index,word in enumerate(words):
    Label(window,text = word,fg=colours[index]).grid(column=index,row=0)

mainloop()