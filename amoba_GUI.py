import tkinter as tk

def onclick(event):
    global player
    if player == 1:
        event.widget["text"] = "X"
        player = 0
    else:
        event.widget["text"] = "O"
        player = 1

n = 10
window = tk.Tk()
window.title("Amőba")
window.geometry("400x400")
window.rowconfigure(list(range(n)),  weight=1)
window.columnconfigure(list(range(n)), weight=1)
for i in range(n):
    for j in range(n):
        cimke = tk.Label(text="  ", borderwidth=1, relief="solid", font=("Arial", 16))
        cimke.bind("<Button-1>", onclick)        
        cimke.place(relwidth= 1/n, relheight=1/n, x=i*40, y=j*40)

player = 1

window.mainloop()