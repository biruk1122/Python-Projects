from tkinter import *

window = Tk()
window.title("GUI Interface")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="This is Label", font=("Arial", 24, "bold"))
my_label.pack(expand=True)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button


def button_clicked():
    print("I got clicked")
    input_text = entry.get()
    my_label.config(text=input_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

entry = Entry(width=10)
entry.pack()
print(entry.get())

window.mainloop()
