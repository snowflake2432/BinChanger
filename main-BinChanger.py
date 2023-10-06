import tkinter as tk
from PIL import ImageTk, Image
import PIL.ImageTk

list1 = []

BinChanger = tk.Tk()
BinChanger.title("BinChanger")
BinChanger.resizable(0, 0)
photo = PIL.Image.open("logo-BinChanger.png")
LOGO = PIL.ImageTk.PhotoImage(photo)

OptionList = [
    "Binary",
    "Octal",
    "Decimal",
    "Hexadecimal"
]

variable = tk.StringVar(BinChanger)
variable.set(OptionList[0])
variable2 = tk.StringVar(BinChanger)
variable2.set(OptionList[0])


show = tk.Label(BinChanger, image=LOGO)
show.image = LOGO  # keep a reference!
show.grid()

entry1 = tk.StringVar()


def validate(P):
    if str.isdigit(P) or P == '':
        return True
    else:
        return False


entry1.set("Choose Type and entry:")

vcmd = (BinChanger.register(validate), '%P')
Entry1 = tk.Entry(BinChanger, validate='key', validatecommand=vcmd)
Entry1.grid(row=2, column=0)

label = tk.Label(textvariable=entry1)
label.grid(row=1, column=0)
entry2 = tk.StringVar()


entry2.set("Change to:")
Entry2 = tk.Entry(BinChanger, )
Entry2.grid(row=7, column=0)
label1 = tk.Label(textvariable=entry2)
label1.grid(row=6, column=0)


def optionmenu():
    get_from = variable.get()
    get_to = variable2.get()
    if get_from == "Binary":
        Entry2.delete(0, 'end')
        list1.clear()
        list1.append(Entry1.get())
        list1_change = int(list1[0])
        Entry2.insert(tk.END, bin(list1_change))
    elif get_from == "Octal":
        Entry2.delete(0, 'end')
        list1.clear()
        list1.append(Entry1.get())
        list1_change = int(list1[0])
        Entry2.insert(tk.END, oct(list1_change))
    elif get_from == "Decimal":
        Entry2.delete(0, 'end')
        list1.clear()
        list1.append(Entry1.get())
        list1_change = int(list1[0])
        Entry2.insert(tk.END, int(list1_change))
    elif get_from == "Hexadecimal":
        Entry2.delete(0, 'end')
        list1.clear()
        list1.append(Entry1.get())
        list1_change = int(list1[0])
        Entry2.insert(tk.END, hex(list1_change))


opt = tk.OptionMenu(BinChanger, variable, *OptionList)
opt.config(width=10, font=('Helvetica', 12))
opt.grid()
tk.Button(BinChanger, text='Start', command=optionmenu).grid(row=9, column=0)

BinChanger.mainloop()
