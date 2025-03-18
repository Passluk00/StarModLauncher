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
    def __init__(self, parent, setup):
        super().__init__(parent)
        self.currentPath = None
        self.setup = setup
        # DA Rifattorizzare
        self.logo = Image.open("ui/asset/MadeByTheCommunity_Black.png")
        self.logo_img = CTkImage(light_image=self.logo, dark_image=self.logo, size=(150, 150))
        self.labelImg = ctk.CTkLabel(self, image=self.logo_img, text="")
        self.labelImg.pack(pady=10)
        self.label = ctk.CTkLabel(self, text="To get Started Select a Project or Create One").pack(padx=4, pady=20)

    ## Aggiungere una Label con il nome del Progetto
    # Nuovo codice
    def updateContent(self, project_name):
        # Variabili da Modificare
        self.color1 = "#65aaf2"  # Scritta Rsi
        self.color2 = "#a6cef7"  # Scritta Rsi Hover
        self.color3 = "#152b3d"  # Scritte Rsi BackGround Color
        self.color4 = "#0d1a25"  # Scritte Rsi BackGround Color Hover
        self.color5 = "#FFFFFF"  # Scritte Bianche
        # Update Setup
        self.currentPath = self.setup.ReadPath(project_name)
        self.projectName = project_name
        for widget in self.winfo_children():
            widget.destroy()
        self.loadColor(project_name)
        # Creazione del canvas scrollabile
        container = ctk.CTkScrollableFrame(self)
        container.pack(fill="both", expand=True)

        # Widget
        ctk.CTkLabel(container, text=f"Project: {project_name}", font=("Roboto", 30, "bold")).pack(pady=10)

        # widget for modifying colors
        self.add_color_row(container, [
            ("Scritta Rsi", self.select_color1, self.color1),
            ("Scritta Rsi Hover", self.select_color2, self.color2)
        ])
        self.add_color_row(container, [
            ("Scritta Rsi Background Color", self.select_color3, self.color3),
            ("Scritta Rsi Background Color Hover", self.select_color4, self.color4)
        ])
        self.add_color_row(container, [
            ("Scritta Biache", self.select_color5, self.color5),
        ])

        # Bottone per salvare i colori nel file
        ctk.CTkButton(container, text="Salva i colori", command=self.salvaSuFile).pack(pady=10)
        ctk.CTkButton(container, text="Applica colori").pack(pady=10)
        ctk.CTkButton(container, text="Stampa tutti i colori", command=self.printVal).pack(pady=10)

    def add_color_row(self, parent, color_data):
        row_frame = ctk.CTkFrame(parent, fg_color="transparent")
        row_frame.pack(pady=4, padx=10, fill='x')
        num_elements = len(color_data)
        for i, (text, command, initial_color) in enumerate(color_data):
            frame = ctk.CTkFrame(row_frame, fg_color="transparent")
            frame.pack(side='left', padx=10, expand=True) # expand True per centrare
            label_frame = ctk.CTkFrame(frame, fg_color="transparent")
            label_frame.pack(pady=2)
            ctk.CTkLabel(label_frame, text=text, font=("Tekton Pro", 20, "bold")).pack()
            CTkColorPicker(frame, width=300, command=command, initial_color=initial_color).pack(pady=2)


    
    
    def select_color1(self, color):
        self.color1 = color

    def select_color2(self, color):
        self.color2 = color

    def select_color3(self, color):
        self.color3 = color

    def select_color4(self, color):
        self.color4 = color

    def select_color5(self, color):
        self.color5 = color

    def printVal(self):
        print(f"Colore 1: {self.color1}\nColore 2: {self.color2}\nColore 3: {self.color3}\nColore 4: {self.color4}\nColore 5: {self.color5}\n")

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
        self.color2 = self.colors["col2"]
        self.color3 = self.colors["col3"]
        self.color4 = self.colors["col4"]
        self.color5 = self.colors["col5"]