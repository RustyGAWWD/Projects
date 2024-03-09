from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
import pandas
import random
z = ""
x = ""
try:
    data = pandas.read_csv("words_to_learn.csv")
    data_list = data.to_dict()

except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")
    data_list = data.to_dict()

def random_word():
    global z
    global x
    x = random.randint(1, len(data_list["French"]))
    y = data_list["French"][x]
    z = data_list["English"][x]
    canvas.itemconfig(word_word, text=y)
def flip():
    language = canvas.itemcget(lang_word, 'text')
    if language == "English":
        canvas.itemconfig(canvas_image, image=white_img)
        canvas.itemconfig(lang_word, text="French", fill="black")
        canvas.itemconfig(word_word, fill="black")
        random_word()
        window.after(3000, flip)
    else:
        canvas.itemconfig(canvas_image, image=green_img)
        canvas.itemconfig(lang_word, text="English", fill="white")
        canvas.itemconfig(word_word, text=z, fill="white")
        window.after(3000, flip)

def tick():
    del data_list["French"][x]
    del data_list["English"][x]
    df = pandas.DataFrame(data_list)
    df.to_csv("words_to_learn.csv", index=False)
    flip()

window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

canvas = Canvas(width=810, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
white_img = PhotoImage(file="card_front.png")
green_img = PhotoImage(file="card_back.png")
canvas_image = canvas.create_image(420, 275, image=white_img)
right = PhotoImage(file="right.png")
wrong = PhotoImage(file="wrong.png")
lang_word = canvas.create_text(410, 165, text="English", font=("Ariel", 28), fill="black")
word_word = canvas.create_text(410, 265, text="Word", font=("Ariel", 35, "bold"), fill="black")

right_button = Button(image=right, highlightthickness=0, command=tick)
wrong_button = Button(image=wrong, highlightthickness=0, command=flip)






canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)
window.mainloop()