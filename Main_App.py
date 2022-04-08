from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        master.title('Pantalla Principal')
        master.iconbitmap(r"C:\Users\XMX4374\Documents\Python\pythonProject01\App_Project\img\ladybug-virus.ico")

        pad = 250
        self._geom = '200x20+0+0'
        master.geometry("{0}x{1}+{0}+1".format(master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)
        master.bind('<F11>', lambda event: master.attributes('-fullscreen', not master.attributes('-fullscreen')))
        master.configure(bg='grey')
        # Instrucciones para salir de la pantalla completa
        # master.bind('<F11>', lambda event: master.attributes('-fullscreen', not master.attributes('-fullscreen')))
        # master.bind('<Escape>', lambda event: master.attributes('-fullscreen',False))

        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=lambda: self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)

        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.donothing)
        editmenu.add_command(label="Copy", command=self.donothing)
        editmenu.add_command(label="Paste", command=self.donothing)
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing)

        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        root.config(menu=menubar)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

    def donothing(self):
        filewin = Toplevel(root)
        button = Button(filewin, text="Hola Mundo")
        button.pack()

    def OpenFile(self):
        name = askopenfilename(initialdir="C:/Users/XMX4374/Documents/",
                               filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                               title="Choose a file."
                               )
        print(name)
        # Using try in case user types in unknown file or closes without choosing a file.
        try:
            with open(name, 'r') as UseFile:
                print(UseFile.read())
        except:
            print("No file exists")


if "__main__" == __name__:
    root = Tk()
    app = FullScreenApp(root)
    root.mainloop()
