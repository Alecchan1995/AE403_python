import tkinter as tk 
def clickME():
    tk.messagebox.showinfo(title="hi",message=entry.get())
window = tk.Tk()
window.title("first of GUI program")
window.geometry("300x300")
label = tk.Label(window,text="hello would",bg="#05A",fg='#5FC')
label.pack()
label2 = tk.Label(window,text="my name is xxx")
label2.pack()
entry = tk.Entry(window,width = 20)
entry.pack()
entry2 = tk.Entry(window,width = 20,show="*")
entry2.pack()
button = tk.Button(window,text="enter",command=clickME)
button.pack()
window.mainloop()
  
