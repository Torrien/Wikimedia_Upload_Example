import tkinter as tk
import imghdr
from tkinter import filedialog, Canvas, messagebox

API_URL = "https://test.wikipedia.org/w/api.php"

# root = tk.Tk()

# API_URL = "https://test.wikipedia.org/w/api.php"
# file = ""

# canvas1 = tk.Canvas(
#     root, 
#     width=400, 
#     height=300, 
#     bg='white', 
#     relief='raised')
# canvas1.pack()

# label1 = tk.Label(root, text="Wiki Image Upload", background="white")
# label1.config(font=('helvetica', 20))
# canvas1.create_window(150, 60, window=label1)



# def exitApplication():
#     MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
#     if MsgBox == 'yes':
#        root.destroy()

# exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 230, window=exitButton)

WIKI_METADATA_LABELS=['author', 'name', 'date', 'permissions', ]
class wikiImageUploader(tk.Tk):
    def __init__(self, api_url=API_URL, screenName=None, baseName=None, className="tk", useTk=1, sync=0, use=None):
        super().__init__(screenName=screenName, baseName=baseName, className=className, useTk=useTk, sync=sync, use=use)
        self.title("Wiki Image Uploader")
        self.minsize(300,200)
        # self.wm_iconbitmap('icon.ico')
        self.image = wikiImage(api_url=api_url)
        self.api_url = api_url
        self.prepareWindow()
    
    def exitApplication(self):
        MsgBox = messagebox.askquestion ('Exit?','Do you really want to leave',icon = 'warning')
        if MsgBox == 'yes':
            self.destroy()
    
    def getImageFilename(self):
        self.image.set_filename(filedialog.askopenfilename())
        if self.image.filename is not None:
            self.displayInfo = f"File: {self.image.filename}\nAPI: {self.api_url}\n\n\n\ntest"
            self.fileDisplay.config(state="normal")
            self.fileDisplay.delete(1.0,tk.END)
            self.fileDisplay.insert(tk.END, self.displayInfo)
            self.fileDisplay.config(state="disabled")
        else:
            tk.messagebox.showinfo("File Selection Error", "File selected does not appear to be an image.\n\nPlease select correct file or verify if file is corrupted.")
    
    def setTemplate(self):
        pass
    
    def uploadImage(self):
        pass


    
    def prepareWindow(self, w=400, h=500, bg='white', relief='raised'):
        self.mainCanvas = tk.Canvas(
            self, 
            width=w, 
            height=h, 
            bg=bg, 
            relief=relief)
        self.mainCanvas.pack()

        # Insert Main Label
        self.mainLabel = tk.Label(self, text="Wiki Image Uploader", background="white")
        self.mainLabel.config(font=('helvetica', 20))
        self.mainCanvas.create_window(w/2, 20, window=self.mainLabel)

        # Add Exit Button
        self.exitButton = tk.Button (self, text='       Exit Application     ',command=self.exitApplication, bg='brown', fg='white', font=('helvetica', 10, 'bold'))
        self.mainCanvas.create_window(w/2, 230, window=self.exitButton)
        
        # Add Select Image Button
        self.selectImageFileButton = tk.Button(self, text='     Select Image File      ', command=self.getImageFilename, bg='brown', fg='white', font=('helvetica', 10, 'bold'))
        self.mainCanvas.create_window(w/2, 195, window=self.selectImageFileButton)

        # Add Upload Image Button
        self.uploadImageButton = tk.Button(self, text='     Upload Image      ', command=self.uploadImage, bg='brown', fg='white', font=('helvetica', 10, 'bold'))
        self.mainCanvas.create_window(w/2, 160, window=self.uploadImageButton)
        
        # Add information Display
        self.fileDisplay = tk.Text(self, width=50, height=3, bg='white', fg='black', font=('helvetica', 8, 'bold'),padx=4, pady=4)
        self.fileDisplay.pack()
        self.displayInfo = f"File: {self.image.filename}\nAPI: {self.api_url}"
        self.fileDisplay.insert(tk.END, self.displayInfo)
        self.mainCanvas.create_window(200, 70, window=self.fileDisplay)
        self.fileDisplay.config(state="disabled")

class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        super().__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)
        
class wikiImage():
    def __init__(self, filename=None, api_url=API_URL):
        assert filename is None or self.fileIsImage(filename), "Initialized with file that is not an image."
        self.filename = filename
        self.api_url = api_url
        self.metadata = {}
    
    def set_filename(self, filename):
        if self.fileIsImage(filename):
            self.filename = filename
    
    @staticmethod
    def fileIsImage(filename):
        return imghdr.what(filename) is not None
    
    def add_metadata(self, **kwargs):
        for key in kwargs.keys():
            if key in WIKI_METADATA_LABELS:
                self.metadata.update({key: kwargs[key]})
    
    def genInfoTemplate(self):
        try:
            assert "description" and "source" and "date" and "author" in self.metadata.keys(), "Missing metadata to generate Information Template"
            return self.informationTemplate(**self.metadata)
        except:
            print("")
    
    @staticmethod
    def informationTemplate(description: str, source: str, date: str, author: str, permission = None, other_versions=None, additional_information=None):
        output = f"""{{{{Information
| description = {description}
| source      = {source}
| date        = {date}
| author      = {author}"""
        if permission is not None:
            output += f"\n| permission  = {permission}"
        if other_versions is not None:
            output += f"\n| permission  = {other_versions}"
        if additional_information is not None:
            output += f"\n| permission  = {additional_information}""
        output += "\n}}"
        return output
    
    @staticmethod
    def artworkTemplate(artist="", author="", title="", description="", depicted_people="", date="", medium="", dimensions=""):
        output = f"""{{{{Artwork
 |artist             = {artist}
 |author             = {author}
 |title              = {title}
 |description        = {description}
 |depicted people    = {depicted_people}
 |date               = {date}
 |medium             = {medium}
 |dimensions         = {dimensions}
 |institution        = {institution}
 |department         = {department}
 |place of discovery = {place of discovery}
 |object history     =
 |exhibition history =
 |credit line        =
 |inscriptions       =
 |notes              =
 |accession number   =
 |place of creation  =
 |source             = {source}
 |permission         =
 |other_versions     =
 |references         =
 |depicted place     =
 |wikidata           =
}} """
        output = f"""{{{{Information
| description = {description}
| source      = {source}
| date        = {date}
| author      = {author}"""
        if permission is not None:
            output += f"\n| permission  = {permission}"
        if other_versions is not None:
            output += f"\n| permission  = {other_versions}"
        if additional_information is not None:
            output += f"\n| permission  = {additional_information}""
        output += "\n}}"
        return output
        
    
    




if __name__ == "__main__":
    root = wikiImageUploader()
    root.mainloop()