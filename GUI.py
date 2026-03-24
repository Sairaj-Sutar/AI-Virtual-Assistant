

from tkinter import *
from PIL import Image, ImageTk
import os
import action
import speech_to_text


def User_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> " + send + "\n")
    if bot != None:
        text.insert(END, "Bot <-- " + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()


def ask():
    ask_val = speech_to_text.speech_to_text()
    bot_val = action.Action(ask_val)

    text.insert(END, "Me --> " + str(ask_val) + "\n")
    if bot_val != None:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()


def delete_text():
    text.delete("1.0", "end")


root = Tk()
root.geometry("1150x675")
root.title("AI Assistant")
root.resizable(False, False)
root.config(bg="#6F8FAF")

# Main Frame
Main_frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
Main_frame.config(bg="#6F8FAF")
Main_frame.grid(row=0, column=20, padx=55, pady=10)

# -------- IMAGE FIX ONLY (UI SAME) --------
base_dir = os.path.dirname(__file__)
image_path = os.path.join(base_dir, "assets", "logoAI.jpg")

try:
    image = ImageTk.PhotoImage(Image.open(image_path))
    image_label = Label(Main_frame, image=image)
    image_label.image = image   # important
    image_label.grid(row=1, column=0, pady=20)
except Exception as e:
    print("Image error:", e)

# Text Label
Text_lable = Label(Main_frame, text="Virtual AI Assistant", font=("comic Sans ms", 14, "bold"), bg="#356696")
Text_lable.grid(row=0, column=0, padx=20, pady=10)

# Text widget
text = Text(root, font=('Courier 10 bold'), bg="#356696")
text.grid(row=2, column=0)
text.place(x=390, y=375, width=375, height=100)

# Entry widget
entry1 = Entry(root, justify=CENTER)
entry1.place(x=400, y=500, width=350, height=30)

# Buttons
button1 = Button(root, text="ASK", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
button1.place(x=250, y=595)

button2 = Button(root, text="Send", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=User_send)
button2.place(x=520, y=595)

button3 = Button(root, text="Delete", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete_text)
button3.place(x=800, y=595)

root.mainloop()