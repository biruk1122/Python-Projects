import tkinter

window = tkinter.Tk()
window.title("GUI Interface")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="This is Label", font=("Arial", 24, "bold"))
my_label.pack(expand=True)

window.mainloop()
