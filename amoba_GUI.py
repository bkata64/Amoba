import tkinter as tk

def onclick(event):
    global player
    if player == 1:
        event.widget["text"] = "X"
        player = 2
    else:
        event.widget["text"] = "O"
        player = 1
    if nyert_sor(event):
        window.title(f"Nyertél, {event.widget['text']}!")

def nyert_sor(event):
    jatekos = event.widget["text"]
    sor = event.widget.sor
    oszlop = event.widget.oszlop
    szamol = 1
    col = oszlop - 1
    while col >= 0 and labels[sor][col]["text"] == jatekos:
        szamol += 1
        col -= 1
    col = oszlop + 1
    while col < n and labels[sor][col]["text"] == jatekos:
        szamol += 1
        col += 1
    return szamol == 5

n = 10
window = tk.Tk()
window.title("Amőba")
window.geometry("400x400")
window.rowconfigure(list(range(n)),  weight=1)
window.columnconfigure(list(range(n)), weight=1)
labels = []
for i in range(n):
    sor = []
    for j in range(n):
        cimke = tk.Label(text="  ", borderwidth=1, relief="solid", font=("Arial", 16))
        cimke.sor = i
        cimke.oszlop = j
        cimke.bind("<Button-1>", onclick)        
        cimke.place(relwidth= 1/n, relheight=1/n, x=j*40, y=i*40)
        sor.append(cimke)
    labels.append(sor)

player = 1

window.mainloop()