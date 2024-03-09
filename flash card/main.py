from tkinter import *
import random
import pandas
x = 0
# -------------------------------CSV-------------------------------------#


def french_picker():
    global x
    x = random.randint(0, len(data_list)-1)
    y = data_list[x][0]
    canvas.itemconfig(canvas_image, image=white_img)
    canvas.itemconfig(lang_word, text="French", fill="black")
    canvas.itemconfig(word_word, fill="black")
    canvas.itemconfig(word_word, text=y)
def tick():

# -------------------------------FLIP------------------------------------#
def flip():
    global is_French
    if is_French:
        canvas.itemconfig(canvas_image, image=green_img)
        canvas.itemconfig(lang_word, text="English", fill="white")
        canvas.itemconfig(word_word, text=data_list[x][1], fill="white")
        is_French = False
    else:
        french_picker()
        is_French = True

def flipper():
    window.after(3000, flipper)
    flip()
# -------------------------------UI--------------------------------------#
window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

canvas = Canvas(width=810, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
white_img = PhotoImage(file="card_front.png")
green_img = PhotoImage(file="card_back.png")
canvas_image= canvas.create_image(420, 275, image=white_img)
right = PhotoImage(file="right.png")
wrong = PhotoImage(file="wrong.png")

lang_word = canvas.create_text(410, 165, text="French", font=("Ariel", 28), fill="black")
word_word = canvas.create_text(410, 265, text=data_list[0][0], font=("Ariel", 35, "bold"), fill="black")

is_French = False
flipper()

right_button = Button(image=right, highlightthickness=0, command=tick)
wrong_button = Button(image=wrong, highlightthickness=0)






canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)
window.mainloop()

