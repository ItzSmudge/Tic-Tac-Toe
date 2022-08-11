#Tic Tac Toe
from tkinter import *
import tkinter.messagebox

window = Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)
window.iconbitmap("Icon.ico")
#Button geometry/appearance 
HEIGHT = 4
WIDTH = 8
BORDER = 0.6
click = True
button_font= ("Sans Serif", 24, "bold")
bg_color = "#ffffff"
fg_color = "#8119ff"

#Updating the game status 
def update_game(buttons):
    global click
    
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False

    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
    
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        tkinter.messagebox.showinfo("GAME OVER!", "PLAYER X WON! :D ")    

    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
        button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
        button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
        button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
        button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
        button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
        button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        tkinter.messagebox.showinfo("GAME OVER!", "PLAYER O WON! :D ")

    elif (button1["text"] != " " and button2["text"] != " " and button3["text"] != " " and
        button4["text"] != " " and button5["text"] != " " and button6["text"] != " " and
        button7["text"] != " " and button8["text"] != " " and button9["text"] != " "):
        tkinter.messagebox.showinfo("GAME OVER!", "GAME DRAWN! :) ")
    
#Buttons
buttons = StringVar()
button1 = Button(window, text=" ", border=BORDER, font=button_font, fg=fg_color, bg=bg_color, height=HEIGHT, width=WIDTH,
                 command=lambda: update_game(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(window, text=" ", border=BORDER, font=button_font, fg=fg_color, bg=bg_color, height=HEIGHT, width=WIDTH,
                 command=lambda: update_game(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(window, text=" ",  border=BORDER, font=button_font, fg=fg_color, bg=bg_color, height=HEIGHT, width=WIDTH,
                 command=lambda: update_game(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(window, text=" ", border=BORDER, font=button_font, fg=fg_color, bg=bg_color, height=HEIGHT, width=WIDTH,
                 command=lambda: update_game(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(window, text=" ", border=BORDER, font=button_font, fg=fg_color, bg=bg_color, height=HEIGHT, width=WIDTH,
                 command=lambda: update_game(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(window, text=" ", border=BORDER, font=button_font, fg=fg_color, bg=bg_color, height=HEIGHT, width=WIDTH,
                 command=lambda: update_game(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(window, text=" ", border=BORDER, font=button_font, fg=fg_color, bg=bg_color, height=HEIGHT, width=WIDTH,
                 command=lambda: update_game(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(window, text=" ", border=BORDER, font=button_font, fg=fg_color, bg=bg_color, height=HEIGHT, width=WIDTH,
                 command=lambda: update_game(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(window, text=" ", border=BORDER, font=button_font, fg=fg_color, bg=bg_color, height=HEIGHT, width=WIDTH,
                 command=lambda: update_game(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)

window.mainloop()