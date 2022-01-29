import tkinter as tk

window = tk.Tk()
window.rowconfigure(list(range(10)),  weight=1)
window.columnconfigure(list(range(10)), weight=1)
for i in range(10):
    for j in range(10):
        cimke = tk.Label(text="", borderwidth=1, relief="solid")
        cimke.grid(row=i, column=j, ipadx=20, ipady=15)

window.mainloop()