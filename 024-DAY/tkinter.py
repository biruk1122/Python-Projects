from tkinter import *

window = Tk()
window.title("GUI Interface")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label

my_label = Label(text="This is Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button


def button_clicked():
    print("I got clicked")
    input_text = entry.get()
    my_label.config(text=input_text)
    my_label.grid(column=0, row=0)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry

entry = Entry(width=10)
print(entry.get())
entry.grid(column=2, row=2)

window.mainloop()
