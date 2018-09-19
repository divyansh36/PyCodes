import tkinter as tk
import webbrowser

def google(event):
    webbrowser.open_new_tab('www.google.com')
    
def fb(event):
    webbrowser.open_new_tab('www.facebook.com')
    
def twttr(event):
    webbrowser.open_new_tab('www.twitter.com')
    
window = tk.Tk()

window.geometry("400x400")

label1 = tk.Label(window, text = 'GOOGLE')
label1.grid(column=0, row = 0)

label2 = tk.Label(window, text='Facebook')
label2.grid(column=1, row = 0)

label3 =  tk.Label(window, text = 'Twitter')
label3.grid(column=2, row=0)

button1 = tk.Button(window, text='google')
button1.grid(column=0, row=1)

button2 = tk.Button(window, text='fb')
button2.grid(column=1, row=1)

button3 = tk.Button(window, text='twttr')
button3.grid(column=2, row=1)

button1.bind('<Button-1>', google)
button2.bind('<Button-1>', fb)
button3.bind('<Button-1>', twttr)


window.mainloop()
