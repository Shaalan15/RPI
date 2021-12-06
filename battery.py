# from tkinter import *
# from tkinter import ttk

# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

# root = Tk()
# root.title("Feet to Meters")

# mainframe = ttk.Frame(root, width=200, height=200, style='Danger.TFrame', padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): 
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)

# root.mainloop()




# from tkinter import *
# from tkinter import ttk
# root = Tk()

# h = ttk.Scrollbar(root, orient=HORIZONTAL)
# v = ttk.Scrollbar(root, orient=VERTICAL)
# canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
# h['command'] = canvas.xview
# v['command'] = canvas.yview

# canvas.grid(column=0, row=0, sticky=(N,W,E,S))
# h.grid(column=0, row=1, sticky=(W,E))
# v.grid(column=1, row=0, sticky=(N,S))
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)

# lastx, lasty = 0, 0

# def xy(event):
#     global lastx, lasty
#     lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

# def setColor(newcolor):
#     global color
#     color = newcolor
#     canvas.dtag('all', 'paletteSelected')
#     canvas.itemconfigure('palette', outline='white')
#     canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
#     canvas.itemconfigure('paletteSelected', outline='#999999')

# def addLine(event):
#     global lastx, lasty
#     x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
#     canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
#     lastx, lasty = x, y

# def doneStroke(event):
#     canvas.itemconfigure('currentline', width=1)        
        
# canvas.bind("<Button-1>", xy)
# canvas.bind("<B1-Motion>", addLine)
# canvas.bind("<B1-ButtonRelease>", doneStroke)

# id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
# canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
# id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
# canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
# id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
# canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

# setColor('black')
# canvas.itemconfigure('palette', width=5)
# root.mainloop()

