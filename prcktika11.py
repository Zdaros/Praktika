# Priklad 1

from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Example')
content = ttk.Frame(root, padding=(3, 3, 12, 12))
frame = ttk.Frame(content, borderwidth=5,
 relief="sunken", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)
onevar = BooleanVar()
twovar = BooleanVar()

threevar = BooleanVar()
one = ttk.Checkbutton(content, text="One",
 variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two",
 variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three",variable=threevar, onvalue=True)
ok = ttk.Button(content, text="OK")
cancel = ttk.Button(content, text="Cancel")
content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2,sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N,W),padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E,W), pady=5,padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)
root.mainloop()

# Priklad 2

from tkinter import *
import tkinter.filedialog
def LoadFile(ev):
 fn = tkinter.filedialog.Open(root, filetypes=[('*.txt files', '.txt')]).show()
 if fn == '':
  return
 textbox.delete('1.0', 'end')
 textbox.insert('1.0', open(fn, 'rt').read())
root = Tk()
panelFrame = Frame(root, height=20, bg='blue')
textFrame = Frame(root, height=40, width=50)
panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)
textbox = Text(textFrame, font='Arial 12', wrap='word')
scrollbar = Scrollbar(textFrame)
scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')
loadBtn = Button(panelFrame, text='Open')
loadBtn.bind("<Button-1>", LoadFile)
loadBtn.place(x=10, y=1, width=40, height=20)
root.mainloop()

# Priklad 3

from tkinter import *
def triangle():
 canvas.coords(r, (0, 0, 0, 0))
 canvas.itemconfig(t, fill='yellow', outline='white')
 canvas.coords(t, (50, 200, 340, 200, 110, 60))
 text.delete(1.0, END)
 text.insert(1.0, 'Зображення трикутника')
 text.tag_add('title', '1.0', '1.end')
 text.tag_config('title', font=('Times', 14), foreground='blue')
def rectangle():
 canvas.coords(t, (0, 0, 0, 0, 0, 0))
 canvas.itemconfig(r, fill='blue', outline='white')
 canvas.coords(r, (80, 50, 320, 200))
 text.delete(1.0, END)
 text.insert(1.0, 'Зображення прямокутника')
 text.tag_add('title', '1.0', '1.end')

 text.tag_config('title', font=('Times', 14), foreground='black')
win = Tk()
b_triangle = Button(text="Трикутник", width=15, command=triangle)
b_rectangle = Button(text="Прямокутник", width=15, command=rectangle)
canvas = Canvas(width=400, height=300, bg='#fff')
text = Text(width=55, height=5, bg='#fff', wrap=WORD)
t = canvas.create_polygon(0, 0, 0, 0, 0, 0)
r = canvas.create_rectangle(0, 0, 0, 0)
b_triangle.grid(row=0, column=0)
b_rectangle.grid(row=1, column=0)
canvas.grid(row=0, column=1, rowspan=10)
text.grid(row=11, column=1, rowspan=3)
win.mainloop()

# Task 1
fn = "global"
def LoadFile(ev):
 fn = tkinter.filedialog.Open(root, filetypes=[('*.txt files', '.txt')]).show()
 if fn == '':
  return
 textbox.delete('1.0', 'end')
 textbox.insert('1.0', open(fn, 'rt').read())
def SaveFile (ev):
 f = tkinter.filedialog.asksaveasfile(mode='w', defaultextension='.txt')
 if f is None:
     return
 text2save=str(textbox.get(1.0,END))
 f.write(text2save)
 f.close()
root = Tk()
panelFrame = Frame(root, height=20, bg='blue')
textFrame = Frame(root, height=40, width=50)
panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)
textbox = Text(textFrame, font='Arial 12', wrap='word')
scrollbar = Scrollbar(textFrame)
scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')
loadBtn = Button(panelFrame, text='Open')
loadBtn.bind("<Button-1>", LoadFile)
loadBtn.place(x=10, y=1, width=40, height=20)
loadBtn = Button(panelFrame, text='Save')
loadBtn.bind("<Button-1>", SaveFile)
loadBtn.place(x=50, y=1, width=40, height=20)
root.mainloop()

# Task 2
def triangle():
 canvas.coords(r, (0, 0, 0, 0))
 canvas.itemconfig(t, fill='yellow', outline='white')
 canvas.coords(t, (50, 200, 340, 200, 110, 60))
 text.delete(1.0, END)
 text.insert(1.0, 'Зображення трикутника')
 text.tag_add('title', '1.0', '1.end')
 text.tag_config('title', font=('Times', 14), foreground='blue')
def rectangle():
 canvas.coords(t, (0, 0, 0, 0, 0, 0))
 canvas.itemconfig(r, fill='blue', outline='white')
 canvas.coords(r, (80, 50, 320, 200))
 text.delete(1.0, END)
 text.insert(1.0, 'Зображення прямокутника')
 text.tag_add('title', '1.0', '1.end')
def circle():
 canvas.coords(r, (0, 0, 0, 0))
 canvas.itemconfig(c, fill='red', outline='white')
 canvas.coords(c, (80, 50, 200, 200))
 text.delete(1.0, END)
 text.insert(1.0, 'Зображення кола')
 text.tag_add('title', '1.0', '1.end')
def clean():
 canvas.coords(t, (0, 0, 0, 0, 0, 0))
 canvas.coords(c, (0, 0, 0, 0))
 canvas.coords(r, (0, 0, 0, 0))
 text.delete(1.0, END)
 text.insert(1.0, 'Зображення стерто')
 text.tag_add('title', '1.0', '1.end')
 
win = Tk()
b_triangle = Button(text="Трикутник", width=15, command=triangle)
b_rectangle = Button(text="Прямокутник", width=15, command=rectangle)
b_circle = Button(text="Коло", width=15, command=circle)
b_clean = Button(text="Очистити", width=15, command=clean)
canvas = Canvas(width=400, height=300, bg='#fff')
text = Text(width=50, height=5, bg='#fff', wrap=WORD)
t = canvas.create_polygon(0, 0, 0, 0, 0, 0)
r = canvas.create_rectangle(0, 0, 0, 0)
c = canvas.create_oval(0 , 0 , 0 ,0 )
b_triangle.grid(row=0, column=0)
b_rectangle.grid(row=1, column=0)
b_circle.grid(row=2, column=0)
b_clean.grid(row=3,column=0)
canvas.grid(row=0, column=1, rowspan=10)
text.grid(row=11, column=1, rowspan=3)
win.mainloop()

