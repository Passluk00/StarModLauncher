import tkinter
from tkinter import ttk
from tkhtmlview import HTMLLabel
from PIL import Image, ImageTk
from ui.webPreview import WebPreview
from ui.webPreviewQ import WebPreviewQ


class MainContent(ttk.Frame):
    
    def __init__(self,parent, setup):
        
        super().__init__(parent)
        
        self.currentPath= None
        self.setup = setup
        
        self.logo = Image.open("ui/asset/MadeByTheCommunity_Black.png")
        self.logo = self.logo.resize((150,150))
        self.logo_img = ImageTk.PhotoImage(self.logo)
        
        self.labelImg = ttk.Label(self, image=self.logo_img)
        self.labelImg.pack(pady=10)
        
        self.label = ttk.Label(self, text="To get Started Select a Project or Create One").pack(padx=4, pady=20)
        
        
        ## Aggiungere una Label con il nome del Progetto
        
        
    def updateContent(self, project_name):
        
        for widget in self.winfo_children():
            widget.destroy()
    
    
        ttk.Label(self, text=f"Project: {project_name}").pack(pady=20)
        
        self.currentPath = self.setup.ReadPath(project_name)
        
       
        # test con pyqt5
        #self.web_preview = WebPreviewQ(self.currentPath)
        #self.web_preview.show_preview()
        
        
       # Crea una finestra di WebPreview con tkinterweb
        self.window = WebPreview(self,self.currentPath)
        self.window.pack(fill="both", expand=True, padx=5, pady=5)
        