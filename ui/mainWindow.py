import tkinter
from tkinter import ttk
from PIL import Image, ImageTk


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
        
        ttk.Label(self,text=f"path: {self.currentPath}").pack(pady=20)
        
