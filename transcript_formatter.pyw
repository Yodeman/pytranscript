import os
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo

root = Tk()
root.title('PyTranscript')
rad = IntVar()
var = StringVar()
var.set('click open to open file.')
box = Frame(root, bd=2, relief=GROOVE)
ent = Entry(box, width=50)
ent.pack(side=RIGHT)
ent.config(textvariable=var)
Button(box, text='open', command=lambda:Open()).pack(side=LEFT, padx=5, pady=5)
box.pack(side=TOP, expand=YES, fill=X)
for text, value in [('with space?', 1), ('without space?', 2)]:
    Radiobutton(root, text=text, value=value, variable=rad).pack(side=LEFT, anchor=W)
rad.set(1)
Button(root, text='Submit', command=(lambda: format_transcript(var.get()))).pack(side=LEFT, expand=YES, fill=BOTH, padx=5, pady=5)
Button(root, text='Quit', command=root.quit).pack(side=LEFT, expand=YES, fill=BOTH, padx=5, pady=5)

def Open():
    file = askopenfilename()
    var.set(file)

def format_transcript(filename):
    new_name = os.path.basename(filename).split('.')[0]
    newfile = open(new_name+'new.txt', 'w')
    for line in open(filename, 'r').readlines():
        if line == '\n' or line[2] == ':':
            continue
        else:
            if rad.get() == 1:
                newfile.write(line + '\n')
            else:
                 newfile.write(line)
    newfile.close()
    showinfo('PyTranscript', 'formatting done...\nclick quit to exit')

root.mainloop()