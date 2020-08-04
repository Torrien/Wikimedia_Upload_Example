import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog

root = tk.Tk()

API_URL = "https://test.wikipedia.org/w/api.php"
file = ""

canvas1 = tk.Canvas(
    root, 
    width=400, 
    height=300, 
    bg='white', 
    relief='raised')
canvas1.pack()

label1 = tk.Label(root, text="Wiki Image Upload", background="white")
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)



def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()

exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

class wikiImageUploader(tk.Tk):
    def __init__(self, API_URL="https://test.wikipedia.org/w/api.php", screenName=None, baseName=None, className, useTk=1, sync=0, use=None):
        super().__init__(screenName=screenName, baseName=baseName, className, useTk=useTk, sync=sync, use=use)
        self.title("Wiki Image Uploader")
        self.minsize(300,200)
        # self.wm_iconbitmap('icon.ico')
        self.prepareWindow()
    
    def exitApplication(self):
        MsgBox = tk.messagebox.askquestion ('Exit?','Do you really want to leave',icon = 'warning')
        if MsgBox == 'yes':
            self.destroy()
    
    def prepareWindow(self, w=400, h=300, bg='white', relief='raised'):
        self.mainCanvas = tk.Canvas(
            self, 
            width=w, 
            height=h, 
            bg=bg, 
            relief=relief)
        self.mainCanvas.pack()
        self.mainLabel = tk.Label(self, text="Wiki Image Upload", background="white")
        self.mainLabel.config(font=('helvetica', 20))
        self.mainCanvas.create_window(150, 60, window=self.mainLabel)
        self.exitButton = tk.Button (self, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
        self.mainCanvas.create_window(150, 230, window=self.exitButton)


root = wikiImageUploader()
root.mainloop()