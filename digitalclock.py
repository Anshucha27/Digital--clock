from tkinter import *
import time
root = Tk()
root.title('Clock')
def present_time():
 display_time =time.strftime("%H:%M:%S %p")
 digi_clock.config(text=display_time)
 digi_clock.after(200,present_time)
digi_clock= Label(root, font=('Bodoni MT', 150),background='black',foreground='green')
digi_clock.pack()
present_time()
root.mainloop()
