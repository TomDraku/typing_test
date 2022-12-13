from tkinter import *
from helper import random_text, orginal_text
import time


# I get the first string from the list of words that the user needs to write
number = 0
text_towrite = random_text(orginal_text)[number] + " "


# This function is responsible for compering typed text with displayed text
# If a user makes mistake he will be informed about import
# If a user typed the word correctly displayed text will be changed after pressing space
# This function is bind with space button
def key_press(event):
    global number, text_towrite
    user_text = name.get()
    if user_text != text_towrite:
        word.config(bg="#FF0000")
    else:
        gettext.delete(0, 'end')
        number += 1
        text_towrite = random_text(orginal_text)[number] + " "
        word.config(bg="#7a7873", text=text_towrite)
        
# This function creates a popup window to display the score and button to quite game or restart it again
def show_score():  
    global top
    next_win = Toplevel(top)
    next_win.geometry("300x250")
    score = Label(next_win, text=f"You wrote {number} words in a minute", font=("Helvetica", 12, "bold")) 
    score.place(x=30, y=50)
    try_again = Label(next_win, text="Do you want to try again?")
    try_again.place(x=65, y=90)
    gettext.config(state="disabled")
    yes = Button(next_win, text="Yes", command=lambda:[top.destroy(), game()])
    no = Button(next_win, text="No", command=top.destroy)
    yes.place(x=100, y=150)
    no.place(x=150, y=150)
    
# This function countdown
def countdown():
    t=60
    while t>0:
        t-=1
        timer.config(text=t)
        time.sleep(1)
        top.update()
    show_score()
        
                
        


    
# This function creates a window with the game 
def game():
    global name, word, gettext, timer, top
    top = Tk()
    top.geometry("450x300")

    title = Label(top, text="Welcome to the game!")
    subtitle = Label(top, text="You can see how fast you can type on your keyboard")
    empty= Label(top, text=" ")
    title.grid(row=0, column=1, padx=10)
    subtitle.grid(row=1, column=1, padx=10, pady=20)
    empty.grid(row=0, column=0)

    watch = Label(top, text="Write this text: ")
    word = Label(top, text=text_towrite, bg="#7a7873")
    watch.grid(row=2, column=0, padx=5)
    word.grid(row=2, column=1, pady=10)

    write = Label(top, text="Write here: ")

    name = StringVar()
    gettext = Entry(top, textvariable = name, cursor="arrow")
    write.grid(row=3, column=0, padx=5)
    gettext.grid(row=3, column=1, pady=20)
    gettext.focus_set()

    t_label = Label(top, text="Time left: ")
    t_label.grid(row=4, column=0)


    timer = Label(top, text=60)
    timer.grid(row=4, column=1)


    top.bind('<space>', key_press)
    countdown()



    top.mainloop()
    

    

game()

