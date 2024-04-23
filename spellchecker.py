from tkinter import *
import customtkinter
from spellchecker import SpellChecker
from PIL import Image, ImageTk

# APP SETUP
APP_NAME = "🪄Magic Spell"
WINDOW_DIMENSIONS = "800x400"

# COLORS
LIGHT_GREY = "#BFCFE7"
DARK_GREY = "#3D3B40"
BLUE = "#525CEB"

# FONT
TITLE_FONT = ("American Typewriter", 50)
LARGE_TEXT = ("American Typewriter", 30)
SMALL_TEXT = ("American Typewriter", 20)


# function takes a word any returns a string giving spelling suggestions / confirming spelling is correct
def check_spelling(word):
    spell = SpellChecker()
    misspelled = spell.unknown([word.lower()])

    if word == "":
        return "You didn't enter a word!"
    elif len(misspelled) == 0:
        return "You got it right!"

    for word in misspelled:
        suggestions = spell.candidates(word)
    if not suggestions:
        return f"Oops, that's not right!\nSorry, I don't have any suggestions."
    top_three_suggestions = list(suggestions)[:2]
    return f"Oops, that's not right!\nBest suggestions: {', '.join(top_three_suggestions)}"


# function is called when "Check my spelling button" is pressed - changes display text to the return value of
# the check_spelling function for the word entered in the text entry box
def on_click():
    result["text"] = check_spelling(entry.get())


# set up tkinter window
window = Tk()
window.title(APP_NAME)
window.geometry(WINDOW_DIMENSIONS)
window.config(background=LIGHT_GREY)

# "Magic Spell" heading
heading = Label(text="Magic Spell!", font=TITLE_FONT, foreground=DARK_GREY, background=LIGHT_GREY)
heading.place(x=180, y=50)

# magic wand image
wand = Image.open("magic-wand.png")
image = ImageTk.PhotoImage(wand)
image_label = Label(window, image=image, background=LIGHT_GREY)
image_label.place(x=50, y=50)

# "Enter a word:" text
text = Label(text="Enter a word:", font=SMALL_TEXT, foreground=DARK_GREY, background=LIGHT_GREY)
text.place(x=180, y=140)

# text entry box
entry = Entry(window, font=LARGE_TEXT, foreground=BLUE, width=18)
entry.place(x=180, y=175)
entry.focus()

# "Check my spelling!" button
button = customtkinter.CTkButton(window, text="Check my spelling!", font=SMALL_TEXT,
                                 fg_color=DARK_GREY, hover_color=BLUE,
                                 height=35, width=100, command=on_click)
button.place(x=180, y=230)

# Display result of spell check
result = Label(text="", background=LIGHT_GREY, font=LARGE_TEXT, foreground=DARK_GREY, justify="left")
result.place(x=180, y=280)

window.mainloop()
