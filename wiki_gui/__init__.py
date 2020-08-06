import tkinter as tk
import imghdr
from tkinter import filedialog, Canvas, messagebox
from json import loads as jLoads, dumps as jDumps

API_URL = "https://test.wikipedia.org/w/api.php"

WIKI_METADATA_LABELS = ['author', 'name', 'date', 'permissions', ]


class wikiImage():
    def __init__(self, filename=None, api_url=API_URL):
        assert filename is None or self.fileIsImage(
            filename), "Initialized with file that is not an image."
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
        infoTempReq = ["description", "source", "author"]
        try:
            for meta in infoTempReq:
                assert meta in self.metadata.keys(
                ), f"Missing '{meta}' metadata to generate Information Template"
            return self.informationTemplate(**self.metadata)
        except:
            tk.messagebox.showinfo(
                f"Information template requires this metadata labels: {infoTempReq}.")
            return None

    def genArtworkTemplate(self):
        artworkTempReq = ["source"]
        try:
            for meta in artworkTempReq:
                assert meta in self.metadata.keys(
                ), f"Missing '{meta}' metadata to generate Artwork Template"
            return self.artworkTemplate(**self.metadata)
        except:
            tk.messagebox.showinfo(
                f"Artwork template requires this metadata labels: {infoTempReq}.")
            return None

    @staticmethod
    def informationTemplate(
            description="", source="", date="", author="", permission="",
            other_versions="", additional_information="", **kwargs):
        output = \
            f"""{{{{Information
| description = {description}
| source      = {source}
| date        = {date}
| author      = {author}
| permission  = {permission}
| permission  = {other_versions}
| permission  = {additional_information}
}}}}"""
        final_output_lines = []
        for l in output.split("\n"):
            if l[-1] != '=' and l[-2] != '=':
                final_output_lines.append(l)
        return "\n".join(final_output_lines)

    @staticmethod
    def artworkTemplate(
            artist="", author="", title="", description="", depicted_people="",
            date="", medium="", dimensions="", institution="", department="",
            place_of_discovery="", object_history="", exhibition_history="",
            credit_line="", inscriptions="", notes="", accession_number="",
            place_of_creation="", source="", permission="", other_versions="",
            references="", depicted_place="", wikidata="", **kwargs):
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
|place of discovery = {place_of_discovery}
|object history     = {object_history}
|exhibition history = {exhibition_history}
|credit line        = {credit_line}
|inscriptions       = {inscriptions}
|notes              = {notes}
|accession number   = {accession_number}
|place of creation  = {place_of_creation}
|source             = {source}
|permission         = {permission}
|other_versions     = {other_versions}
|references         = {references}
|depicted place     = {depicted_place}
|wikidata           = {wikidata}
}}}}"""
        # output_lines = output.split("\n")
        final_output_lines = []
        for l in output.split("\n"):
            if l[-1] != '=' and l[-2] != '=':
                final_output_lines.append(l)
        return "\n".join(final_output_lines)


class wikiImageUploader(tk.Tk):
    def __init__(self, api_url=API_URL, screenName=None, baseName=None, className="tk", useTk=1, sync=0, use=None):
        super().__init__(screenName=screenName, baseName=baseName,
                         className=className, useTk=useTk, sync=sync, use=use)
        self.title("Wiki Image Uploader")
        self.minsize(300, 200)
        # self.wm_iconbitmap('icon.ico')
        self.image = wikiImage(api_url=api_url)
        self.api_url = api_url
        self.windowMetadataEdit = None
        self.prepareWindow()

    def exitApplication(self):
        MsgBox = messagebox.askquestion(
            'Exit?', 'Do you really want to leave', icon='warning')
        if MsgBox == 'yes':
            self.destroy()

    def getImageFilename(self):
        self.image.set_filename(filedialog.askopenfilename())
        if self.image.filename is not None:
            self.displayInfo = f"File: {self.image.filename}\nAPI: {self.api_url}\n\n\n\ntest"
            self.fileDisplay.config(state="normal")
            self.fileDisplay.delete(1.0, tk.END)
            self.fileDisplay.insert(tk.END, self.displayInfo)
            self.fileDisplay.config(state="disabled")
        else:
            tk.messagebox.showinfo(
                "File Selection Error", "File selected does not appear to be an image.\n\nPlease select correct file or verify if file is corrupted.")
    
    def disconnectMetaWindow(self, metaWindow):
        self.windowMetadataEdit = None
        return self.windowMetadataEdit is None

    def addMetadata(self):
        if self.windowMetadataEdit is None:
            self.windowMetadataEdit = topMetadata(
                image=self.image, master=self)
            self.windowMetadataEdit.bind(
                "<Destroy>", self.disconnectMetaWindow)
            self.windowMetadataEdit.mainloop()
        else:
            self.windowMetadataEdit.deiconify()
            self.windowMetadataEdit.focus_set()
            self.windowMetadataEdit.attributes("-topmost", 1)
            self.windowMetadataEdit.attributes("-topmost", 0)

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
        self.mainLabel = tk.Label(
            self, text="Wiki Image Uploader", background="white")
        self.mainLabel.config(font=('helvetica', 20))
        self.mainCanvas.create_window(w/2, 20, window=self.mainLabel)

        # Add Exit Button
        self.exitButton = tk.Button(
            self, text='       Exit Application     ',
            command=self.exitApplication, bg='brown', fg='white',
            font=('helvetica', 10, 'bold'))
        self.mainCanvas.create_window(
            w/2, 230, window=self.exitButton)

        # Add Select Image Button
        self.selectImageFileButton = tk.Button(
            self, text='     Select Image File      ',
            command=self.getImageFilename, bg='brown', fg='white',
            font=('helvetica', 10, 'bold'))
        self.mainCanvas.create_window(
            w/2, 195, window=self.selectImageFileButton)

        # Add Upload Image Button
        self.uploadImageButton = tk.Button(
            self, text='     Upload Image      ',
            command=self.uploadImage, bg='brown', fg='white',
            font=('helvetica', 10, 'bold'))
        self.mainCanvas.create_window(w/2, 160, window=self.uploadImageButton)

        # Add Metadata Edit Button
        self.uploadImageButton = tk.Button(
            self, text='     Edit Image Metadata     ',
            command=self.addMetadata, bg='brown', fg='white',
            font=('helvetica', 10, 'bold'))
        self.mainCanvas.create_window(w/2, 125, window=self.uploadImageButton)

        # Add information Display
        self.fileDisplay = tk.Text(
            self, width=50, height=3, bg='white', fg='black',
            font=('helvetica', 8, 'bold'), padx=4, pady=4)
        self.fileDisplay.pack()
        self.displayInfo = f"File: {self.image.filename}\nAPI: {self.api_url}"
        self.fileDisplay.insert(tk.END, self.displayInfo)
        self.mainCanvas.create_window(200, 70, window=self.fileDisplay)
        self.fileDisplay.config(state="disabled")


class topMetadata(tk.Toplevel):
    def __init__(self, image: wikiImage, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        self.title("Image Metadata Editor")
        self.minsize(300, 200)
        # self.wm_iconbitmap('icon.ico')
        self.image = image
        self.prepareWindow()

    def exitMetaEdit(self):
        self.destroy()
        self.update()

    def prepareWindow(self, w=400, h=500, bg='white', relief='raised'):
        self.mainCanvas = tk.Canvas(
            self,
            width=w,
            height=h,
            bg=bg,
            relief=relief)
        self.mainCanvas.pack()

        # Insert Main Label
        self.mainLabel = tk.Label(
            self, text="Metadata Editor", background="white")
        self.mainLabel.config(font=('helvetica', 20))
        self.mainCanvas.create_window(w/2, 20, window=self.mainLabel)

        # Add Exit Button
        self.exitButton = tk.Button(self, text='       Finish Meta Edit      ',
                                    command=self.exitMetaEdit, bg='brown', fg='white', font=('helvetica', 10, 'bold'))
        self.mainCanvas.create_window(w/2, 430, window=self.exitButton)


class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)


if __name__ == "__main__":
    root = wikiImageUploader()
    root.mainloop()
    # metadata = {
    #     "author": "yo", "department": "tu"
    # }
    # print(wikiImage.artworkTemplate(**metadata), "\n\n")
    # print(wikiImage.informationTemplate(**metadata), "\n\n")
