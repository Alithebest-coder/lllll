from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("Event Handler")
window.geometry("200x200")

def handle_click(event):
    print("button pressed")

def handle_keypress(event):
    print(event.char)

window.bind("<Key>" ,handle_keypress)


btn=Button(text="HI ._. :3:]:)")
btn.pack()
btn.bind("<Button-1>" ,handle_click)

def msg():
    messagebox.showwarning("Alert", "hi virus is hear stay indoors do not go outside")


btn1=Button(window,text="scan virus" , command=msg)
btn1.pack()

window.mainloop()