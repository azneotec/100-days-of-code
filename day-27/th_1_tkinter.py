from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New Text"
# my_label.config(text="New Text")


# Button

def button_clicked():
    print("I got clicked")
    my_label.config(text="Button Got Clicked")
    text_input = input.get()
    my_label.config(text=text_input)


button = Button(text="Click Me", command=button_clicked)
# button.pack(side="left")
button.grid(row=1, column=1)

new_button = Button(text="New Button")
new_button.grid(row=0, column=2)

# Entry
input = Entry(width=10)
# input.pack(side="left")
# print(input.get())
input.grid(row=2, column=3)

window.mainloop()
