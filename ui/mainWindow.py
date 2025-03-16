import tkinter
from tkinter import ttk
from tkhtmlview import HTMLLabel
from PIL import Image, ImageTk
from ui.webPreview import WebPreview
from ui.webPreviewQ import WebPreviewQ
import customtkinter as ctk
from customtkinter import CTkImage
from CTkColorPicker import *

class MainContent(ctk.CTkFrame):
    
    def __init__(self,parent, setup):
        
        super().__init__(parent)
        
        self.currentPath= None
        self.setup = setup
        
        
        self.logo = Image.open("ui/asset/MadeByTheCommunity_Black.png")
        
        self.logo_img = CTkImage(light_image=self.logo, dark_image=self.logo, size=(150, 150))
        
        self.labelImg = ctk.CTkLabel(self, image=self.logo_img, text="")
        self.labelImg.pack(pady=10)
        
        self.label = ctk.CTkLabel(self, text="To get Started Select a Project or Create One").pack(padx=4, pady=20)
      
        ## Aggiungere una Label con il nome del Progetto
        
        
    def updateContent(self, project_name):
        
        
        # Variabili da Modificare
        
        self.color1 = "#65aaf2"                  # Scritta Rsi
        self.color2 = "#a6cef7"                  # Scritta Rsi Hover
        self.color3 = "#152b3d"                  # Scritte Rsi BackGround Color
        self.color4 = "#0d1a25"                  # Scritte Rsi BackGround Color Hover
        self.color5 = "#FFFFFF"                  # Scritte Bianche
        
        
        # Update Setup
        
        self.currentPath = self.setup.ReadPath(project_name)
        self.projectName = project_name
        for widget in self.winfo_children():
            widget.destroy()
    
        self.loadColor(project_name)
    
    
        # Widget 
    
        ctk.CTkLabel(self, text=f"Project: {project_name}",font=("Roboto", 30, "bold")).grid(row=0, column=1, pady=10, padx=10)
        ctk.CTkLabel(self, text="").grid(row=0, column=7)
        
        
        # Space
        ctk.CTkLabel(self,text="").grid(row=1)
        
        
        ###   Test code
        
            # test con pyqt5
                # self.web_preview = WebPreviewQ(self.currentPath)
                # self.web_preview.show_preview()
                
            # Crea una finestra di WebPreview con tkinterweb
                # self.window = WebPreview(self,self.currentPath)
                # self.window.pack(fill="both", expand=True, padx=5, pady=5)
                
        ###
        
        # widget for modify the Scritta Rsi color
        self.color1Lable = ctk.CTkLabel(self, text="Scritta Rsi",font=("Tekton Pro", 20, "bold")).grid(row=2, column=0, pady=4, padx=10)
        self.colorpicker = CTkColorPicker(self, width=300, command=self.select_color1, initial_color=(self.color1)).grid(row=3, column=0, pady=4, padx=10)
        
        
        # widget for modify the Scritta Rsi Hover Color
        self.color2Lable = ctk.CTkLabel(self, text="Scritta Rsi Hover",font=("Tekton Pro", 20, "bold")).grid(row=2, column=2, pady=4, padx=10)
        self.colorpicker2 = CTkColorPicker(self, width=300, command=self.select_color2, initial_color=(self.color2)).grid(row=3, column=2, pady=4, padx=10)
        
        
        # Space
        ctk.CTkLabel(self,text="").grid(row=4)
        # Space
        
        
        # widget for modify the BackGround Color Scritta RSI
        self.color3Lable = ctk.CTkLabel(self, text="Scritta Rsi Background Color",font=("Tekton Pro", 20, "bold")).grid(row=5, column=0, pady=4, padx=10)
        self.colorpicker3 = CTkColorPicker(self, width=300, command=self.select_color3, initial_color=(self.color3)).grid(row=6, column=0, pady=4, padx=10)
        
        
        # widget for modify the BackGround Color Scritta RSI Hover
        self.color4Lable = ctk.CTkLabel(self, text="Scritta Rsi Background Color Hover",font=("Tekton Pro", 20, "bold")).grid(row=5, column=2, pady=4, padx=10)
        self.colorpicker4 = CTkColorPicker(self, width=300, command=self.select_color4, initial_color=(self.color4)).grid(row=6, column=2, pady=4, padx=10)
        
        
        # Space
        ctk.CTkLabel(self,text="").grid(row=7)
        # Space
        
        
        # widget for modify the White Scritta Color
        self.colo51Lable = ctk.CTkLabel(self, text="Scritta Biache",font=("Tekton Pro", 20, "bold")).grid(row=8, column=0, pady=4, padx=10)
        self.colorpicker5 = CTkColorPicker(self, width=300, command=self.select_color5, initial_color=(self.color5)).grid(row=9, column=0, pady=4, padx=10)
        
        
        # widget for modify the  Color
       # self.color1Lable = ctk.CTkLabel(self, text="  ",font=("Tekton Pro", 20, "bold")).grid(row=8, column=2, pady=4, padx=10)
       # self.colorpicker2 = CTkColorPicker(self, width=300, command=self.select_color2).grid(row=9, column=2, pady=4, padx=10)
        
        
        # Bottone per salvare i colori inel file
        ctk.CTkButton(self, text="Salva i colori", command=self.salvaSuFile).grid(row=11, column=1, pady=10)
        
        
        # Bottone per applicare i colori direttamente sul file 
        ctk.CTkButton(self, text="Applica colori").grid(row=12, column=1, pady=10)
        
        
        # Bottone per verificare i colori salvati
        ctk.CTkButton(self, text="Stampa tutti i colori", command=self.printVal).grid(row=13, column=1, pady=10)
        
        
    # Utility Function
        
        
    def select_color1(self,color):
        self.color1 = color
        print(f"Colore 1 Salvato: {self.color1}")
        
    
    def select_color2(self,color):
        self.color2 = color
        print(f"Colore 2 Salvato: {self.color2}")
        
    def select_color3(self,color):
        self.color3= color
        print(f"Colore 3 Salvato: {self.color3}")
        
    def select_color4(self,color):
        self.color4 = color
        print(f"Colore 4 Salvato: {self.color4}")
        
    def select_color5(self,color):
        self.color5 = color
        print(f"Colore 5 Salvato: {self.color5}")
        
    
    def printVal(self):
        print("\n")
        print(f"Colore 1: {self.color1}")
        print(f"Colore 2: {self.color2}")
        print(f"Colore 3: {self.color3}")
        print(f"Colore 4: {self.color4}")
        print(f"Colore 5: {self.color5}")
        print("\n")
        
        
    def salvaSuFile(self):
        
        colors = {
            "col1": self.color1,
            "col2": self.color2,
            "col3": self.color3,
            "col4": self.color4,
            "col5": self.color5
        }
       
        self.setup.SaveData(self.projectName, "colors", colors)
        
    def loadColor(self, projectname):
        
        self.colors = self.setup.LoadData(projectname, "colors")
        
        self.color1 = self.colors["col1"]
        