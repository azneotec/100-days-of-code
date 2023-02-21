from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
# my_label.config(text="New Text")


# Button

def button_clicked():
    print("I got clicked")
    my_label.config(text="Button Got Clicked")
    text_input = input.get()
    my_label.config(text=text_input)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()
# print(input.get())

window.mainloop()
