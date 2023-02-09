import tkinter
from actions import *
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')
timer = None

# Get words


def get_words():
    words = choose_random_words()
    canvas.itemconfig(french_word, text=words[0])
    canvas.itemconfig(english_word, text=words[1])


# Flip the card

def flip_card():
    # If title is French, go to English
    if canvas.itemcget(title, 'text') == 'French':
        canvas.itemconfig(canvas_image, image=back_card)
        canvas.itemconfig(title, text='English')
        canvas.itemconfig(english_word, state='normal')
        canvas.itemconfig(french_word, state='hidden')
    # if title is English, go to French
    elif canvas.itemcget(title, 'text') == 'English':
        canvas.itemconfig(canvas_image, image=front_card)
        canvas.itemconfig(title, text='French')
        canvas.itemconfig(english_word, state='hidden')
        canvas.itemconfig(french_word, state='normal')


def reset_cards():
    get_words()
    flip_card()

    cancel_timer()
    set_timer()


def update_list():
    cancel_timer()
    i_know_this_word(canvas.itemcget(french_word, 'text'), canvas.itemcget(english_word, 'text'))

    if canvas.itemcget(title, 'text') == 'English':
        reset_cards()
    else:
        get_words()
        set_timer()


def set_timer():
    global timer
    timer = window.after(3000, flip_card)


def cancel_timer():
    global timer
    window.after_cancel(timer)

# UI

window = tkinter.Tk()
window.title('Flashcard Game')
window.config(width=900, height=600, bg=BACKGROUND_COLOR, pady=50, padx=50)

# Create photo images
front_card = tkinter.PhotoImage(file='./images/card_front.png')
back_card = tkinter.PhotoImage(file='./images/card_back.png')
right_btn_img = tkinter.PhotoImage(file='./images/right.png')
wrong_btn_img = tkinter.PhotoImage(file='./images/wrong.png')

# Game layout
canvas = tkinter.Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)

# Text

title = canvas.create_text(400, 150, text='French', font=TITLE_FONT)
french_word = canvas.create_text(400, 263, text='French Word', font=WORD_FONT, state='normal')
english_word = canvas.create_text(400, 263, text='English Word', font=WORD_FONT, state='hidden')

# Call to set the words

get_words()

# Buttons

right_button = tkinter.Button(image=right_btn_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=update_list)
wrong_button = tkinter.Button(image=wrong_btn_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=reset_cards)

right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

# Timer will flip cards after 3 seconds

set_timer()

# Keeps window open
window.mainloop()
