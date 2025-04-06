import tkinter as tk 
import shutil
import os
import numpy as np
from PIL import Image
from tkinter import ttk, colorchooser
from tkhtmlview import HTMLLabel
from PIL import Image, ImageTk
import customtkinter as ctk
from customtkinter import CTkImage
from CTkColorPicker import *

class MainContent(ctk.CTkFrame):
    
    def __init__(self,parent, setup):
        
        super().__init__(parent)
        
        self.currentPath= None
        self.setup = setup
        self.original_image = None
        self.tk_image = None
        
        
        
        self.logo = Image.open("ui/asset/MadeByTheCommunity_Black.png")
        
        self.logo_img = CTkImage(light_image=self.logo, dark_image=self.logo, size=(150, 150))
        
        self.labelImg = ctk.CTkLabel(self, image=self.logo_img, text="")
        self.labelImg.pack(pady=10)
        
        self.label = ctk.CTkLabel(self, text="To get Started Select a Project or Create One").pack(padx=4, pady=20)
      
       
       
        
        
    def updateContent(self, project_name):
        
        
        # InitalVariables    
        
        self.solcolorprimary1 = "#0a1d29"            # Usage: Darkest background area, the subpage on the right in options uses it.
        self.solcolorprimary2 = "#0f2c3e"            # Usage: Used together with primary-1 and is one of the most used colors.
        self.solcolorprimary3 = "#143a52"            # Usage: Secondary background elements or subtle highlights.
        self.solcolorprimary4 = "#194967"            # Usage: Borders and dividers within the UI.
        self.solcolorprimary5 = "#1e577b"            # Usage: Highlight in darker areas.
        self.solcolorprimary6 = "#2875a4"            # Usage: No use as of now
        self.solcolorprimary7 = "#6fb2dc"            # Usage: Highlighted text or selected states.
        self.solcolorprimary8 = "#add4eb"            # Usage: Most of the launcher text utilises this together with --sol-color-neutral-4
        
        self.solcolorneutral1 = "#000"               # Usage: Button text and other primary text elements.
        self.solcolorneutral4 = "#FFF"               # Usage: Most of the launcher text utilises this together with --sol-color-primary-8
        
        self.solcoloraccent1 = "#54adf7"             # Usage: Default state for accent elements, such as buttons or highlights.
        self.solcoloraccent2 = "#6db9f8"             # Usage: Pressed state for interactive accented elements
        self.solcoloraccent3 = "#9ed0fa"             # Usage: Hovered state for interactive accented elements.
       
        self.solcgamepagebackground= "6 17 25"       # Usage: The gradient background of the game page.
       
        self.solcolorprimary1rgb = "10 29 41"        # Usage: Launch game button background
        self.solcolorprimary2rgb = "15 44 62"
        self.solcolorprimary3rgb = "20 58 82"   
        self.solcolorprimary4rgb = "25 73 103"
        self.solcolorprimary5rgb = "30 87 123"
        self.solcolorprimary6rgb = "40 117 164"
        self.solcolorprimary7rgb = "111 178 220"
        self.solcolorprimary8rgb = "173 212 235"
       
        self.solcolorneutral1rgb = "0 0 0"           # Usage: Element shadows and interactive elements hover effect

        self.solcoloraccent1rgb = "84 173 247"  
        self.solcoloraccent2rgb = "109 185 248"  
        self.solcoloraccent3rgb = "158 208 250"            
        
        
        # Updated Variables
        
        self.solcolorprimary1New = "#0a1d29"            # Usage: Darkest background area, the subpage on the right in options uses it.
        self.solcolorprimary2New = "#0f2c3e"            # Usage: Used together with primary-1 and is one of the most used colors.
        self.solcolorprimary3New = "#143a52"            # Usage: Secondary background elements or subtle highlights.
        self.solcolorprimary4New = "#194967"            # Usage: Borders and dividers within the UI.
        self.solcolorprimary5New = "#1e577b"            # Usage: Highlight in darker areas.
        self.solcolorprimary6New = "#2875a4"            # Usage: No use as of now
        self.solcolorprimary7New = "#6fb2dc"            # Usage: Highlighted text or selected states.
        self.solcolorprimary8New = "#add4eb"            # Usage: Most of the launcher text utilises this together with --sol-color-neutral-4
        
        self.solcolorneutral1New = "#000"               # Usage: Button text and other primary text elements.
        self.solcolorneutral4New = "#FFF"               # Usage: Most of the launcher text utilises this together with --sol-color-primary-8
        
        self.solcoloraccent1New = "#54adf7"             # Usage: Default state for accent elements, such as buttons or highlights.
        self.solcoloraccent2New = "#6db9f8"             # Usage: Pressed state for interactive accented elements
        self.solcoloraccent3New = "#9ed0fa"             # Usage: Hovered state for interactive accented elements.
       
        self.solcgamepagebackgroundNew = "6 17 25"       # Usage: The gradient background of the game page.
       
        self.solcolorprimary1rgbNew = "10 29 41"        # Usage: Launch game button background
        self.solcolorprimary2rgbNew = "15 44 62"
        self.solcolorprimary3rgbNew = "20 58 82"   
        self.solcolorprimary4rgbNew = "25 73 103"
        self.solcolorprimary5rgbNew = "30 87 123"
        self.solcolorprimary6rgbNew = "40 117 164"
        self.solcolorprimary7rgbNew = "111 178 220"
        self.solcolorprimary8rgbNew = "173 212 235"
       
        self.solcolorneutral1rgbNew = "0 0 0"           # Usage: Element shadows and interactive elements hover effect

        self.solcoloraccent1rgbNew = "84 173 247"  
        self.solcoloraccent2rgbNew = "109 185 248"  
        self.solcoloraccent3rgbNew = "158 208 250"            
            
       
        # Update Setup
        
        self.currentPath = self.setup.ReadPath(project_name)
        self.projectName = project_name
        for widget in self.winfo_children():
            widget.destroy()
    
        # Load Project Data
        self.loadOrCreateSetup(self.projectName)
    
        # Preview Image
        self.image_label = ctk.CTkLabel(self, text="", width=1440, height=810)
        self.image_label.pack(pady=10)
        self.LoadImg(self.projectName)

        # Color Picker
        self.TestColorpicker = CTkColorPicker(self, width=300, command=self.select_color1, initial_color=(self.solcolorprimary1)).pack()
        self.confirm = ctk.CTkButton(self,command=self.Confirm_change_Color, text="Conferma Colore").pack()
        
    
       
    # Utility Function
    
    def Confirm_change_Color(self):
        
        toRGBOld = self.HexToRGB(self.solcolorprimary1)
        toRGBNew = self.HexToRGB(self.solcolorprimary1New)
        self.replace_color_in_image(toRGBOld, toRGBNew)
        self.salvaSuFile()
        print(f"Colore 1 Salvato {self.solcolorprimary1}")

        
    def select_color1(self,color):
        self.solcolorprimary1New = color
        print(f"Colore 1 Selezionato : {self.solcolorprimary1New}")
   
    
    def printVal(self):
        print("\n")
        print(f"--sol-color-primary-1: {self.solcolorprimary1New}")
        print(f"--sol-color-primary-2: {self.solcolorprimary2New}")
        print(f"--sol-color-primary-3: {self.solcolorprimary3New}")
        print(f"--sol-color-primary-4: {self.solcolorprimary4New}")
        print(f"--sol-color-primary-5: {self.solcolorprimary5New}")
        print(f"--sol-color-primary-6: {self.solcolorprimary6New}")
        print(f"--sol-color-primary-7: {self.solcolorprimary7New}")
        print(f"--sol-color-primary-8: {self.solcolorprimary8New}")
        print("\n")
        print(f"--sol-color-neutral-1: {self.solcolorneutral1New}")
        print(f"--sol-color-neutral-4: {self.solcolorneutral4New}")
        print("\n")
        print(f"--sol-color-accent-1: {self.solcoloraccent1New}")
        print(f"--sol-color-accent-2: {self.solcoloraccent2New}")
        print(f"--sol-color-accent-3: {self.solcoloraccentNew}")
        print("\n")
        print(f"--sol-c-game-page-background: {self.solcgamepagebackgroundNew}")
        print("\n")
        print(f"--sol-color-primary-1-rgb: {self.solcolorprimary1rgbNew}")
        print(f"--sol-color-primary-2-rgb: {self.solcolorprimary2rgbNew}")
        print(f"--sol-color-primary-3-rgb: {self.solcolorprimary3rgbNew}")
        print(f"--sol-color-primary-4-rgb: {self.solcolorprimary4rgbNew}")
        print(f"--sol-color-primary-5-rgb: {self.solcolorprimary5rgbNew}")
        print(f"--sol-color-primary-6-rgb: {self.solcolorprimary6rgbNew}")
        print(f"--sol-color-primary-7-rgb: {self.solcolorprimary7rgbNew}")
        print(f"--sol-color-primary-8-rgb: {self.solcolorprimary8rgbNew}")
        print("\n")
        print(f"--sol-color-neutral-1-rgb: {self.solcolorneutral1rgbNew}")
        print("\n")
        print(f"--sol-color-accent-1-rgb: {self.solcoloraccent1rgbNew}")
        print(f"--sol-color-accent-2-rgb: {self.solcoloraccent2rgbNew}")
        print(f"--sol-color-accent-3-rgb: {self.solcoloraccent3rgbNew}")
        
    
    def salvaSuFile(self):
        
        colors = {
            "--sol-color-primary-1": self.solcolorprimary1New,
            "--sol-color-primary-2": self.solcolorprimary2New,
            "--sol-color-primary-3": self.solcolorprimary3New,
            "--sol-color-primary-4": self.solcolorprimary4New,
            "--sol-color-primary-5": self.solcolorprimary5New,
            "--sol-color-primary-6": self.solcolorprimary6New,
            "--sol-color-primary-7": self.solcolorprimary7New,
            "--sol-color-primary-8": self.solcolorprimary8New,
            
            "--sol-color-neutral-1" :self.solcolorneutral1New,
            "--sol-color-neutral-4" :self.solcolorneutral4New,
            
            "--sol-color-accent-1":  self.solcoloraccent1New,
            "--sol-color-accent-2":  self.solcoloraccent2New,
            "--sol-color-accent-3":  self.solcoloraccent3New,
            
            "--sol-c-game-page-background":  self.solcgamepagebackgroundNew,
            
            "--sol-color-primary-1-rgb":  self.solcolorprimary1rgbNew,
            "--sol-color-primary-2-rgb":  self.solcolorprimary2rgbNew,
            "--sol-color-primary-3-rgb":  self.solcolorprimary3rgbNew,
            "--sol-color-primary-4-rgb":  self.solcolorprimary4rgbNew,
            "--sol-color-primary-5-rgb":  self.solcolorprimary5rgbNew,
            "--sol-color-primary-6-rgb":  self.solcolorprimary6rgbNew,
            "--sol-color-primary-7-rgb":  self.solcolorprimary7rgbNew,
            "--sol-color-primary-8-rgb":  self.solcolorprimary8rgbNew,
            
            "--sol-color-neutral-1-rgb": self.solcolorneutral1rgbNew,
            
            "--sol-color-accent-1-rgb": self.solcoloraccent1rgbNew,
            "--sol-color-accent-2-rgb": self.solcoloraccent2rgbNew,
            "--sol-color-accent-3-rgb": self.solcoloraccent3rgbNew,            
            
        }
       
        self.setup.SaveData(self.projectName, "colors", colors)


    def loadColor(self, projectname):
        
        self.colors = self.setup.LoadData(projectname, "colors")
        
        self.solcolorprimary1 = self.colors["--sol-color-primary-1"]
        self.solcolorprimary2 = self.colors["--sol-color-primary-2"]
        self.solcolorprimary3 = self.colors["--sol-color-primary-3"]
        self.solcolorprimary4 = self.colors["--sol-color-primary-4"]
        self.solcolorprimary5 = self.colors["--sol-color-primary-5"]
        self.solcolorprimary6 = self.colors["--sol-color-primary-6"]
        self.solcolorprimary7 = self.colors["--sol-color-primary-7"]
        self.solcolorprimary8 = self.colors["--sol-color-primary-8"]
        
        self.solcolorneutral1 = self.colors["--sol-color-neutral-1"]
        self.solcolorneutral4 = self.colors["--sol-color-neutral-4"]
        
        self.solcoloraccent1 = self.colors["--sol-color-accent-1"]
        self.solcoloraccent2 = self.colors["--sol-color-accent-2"]
        self.solcoloraccent3 = self.colors["--sol-color-accent-3"]
        
        self.solcgamepagebackground = self.colors["--sol-c-game-page-background"]
        
        self.solcolorprimary1rgb = self.colors["--sol-color-primary-1-rgb"]
        self.solcolorprimary2rgb = self.colors["--sol-color-primary-2-rgb"]
        self.solcolorprimary3rgb = self.colors["--sol-color-primary-3-rgb"]
        self.solcolorprimary4rgb = self.colors["--sol-color-primary-4-rgb"]
        self.solcolorprimary5rgb = self.colors["--sol-color-primary-5-rgb"]
        self.solcolorprimary6rgb = self.colors["--sol-color-primary-6-rgb"]
        self.solcolorprimary7rgb = self.colors["--sol-color-primary-7-rgb"]
        self.solcolorprimary8rgb = self.colors["--sol-color-primary-8-rgb"]
        
        self.solcolorneutral1rgb = self.colors["--sol-color-neutral-1-rgb"]
        
        self.solcoloraccent1rgb = self.colors["--sol-color-accent-1-rgb"]
        self.solcoloraccent2rgb = self.colors["--sol-color-accent-2-rgb"]
        self.solcoloraccent3rgb = self.colors["--sol-color-accent-3-rgb"]
        
    
    def modData(self):
        
        ToMod = {
            "--sol-color-primary-1": self.solcolorprimary1New,
            "--sol-color-primary-2": self.solcolorprimary2New,
            "--sol-color-primary-3": self.solcolorprimary3New,
            "--sol-color-primary-4": self.solcolorprimary4New,
            "--sol-color-primary-5": self.solcolorprimary5New,
            "--sol-color-primary-6": self.solcolorprimary6New,
            "--sol-color-primary-7": self.solcolorprimary7New,
            "--sol-color-primary-8": self.solcolorprimary8New,
            
            "--sol-color-neutral-1" :self.solcolorneutral1New,
            "--sol-color-neutral-4" :self.solcolorneutral4New,
            
            "--sol-color-accent-1":  self.solcoloraccent1New,
            "--sol-color-accent-2":  self.solcoloraccent2New,
            "--sol-color-accent-3":  self.solcoloraccent3New,
            
            "--sol-c-game-page-background":  self.solcgamepagebackgroundNew,
            
            "--sol-color-primary-1-rgb":  self.solcolorprimary1rgbNew,
            "--sol-color-primary-2-rgb":  self.solcolorprimary2rgbNew,
            "--sol-color-primary-3-rgb":  self.solcolorprimary3rgbNew,
            "--sol-color-primary-4-rgb":  self.solcolorprimary4rgbNew,
            "--sol-color-primary-5-rgb":  self.solcolorprimary5rgbNew,
            "--sol-color-primary-6-rgb":  self.solcolorprimary6rgbNew,
            "--sol-color-primary-7-rgb":  self.solcolorprimary7rgbNew,
            "--sol-color-primary-8-rgb":  self.solcolorprimary8rgbNew,
            
            "--sol-color-neutral-1-rgb": self.solcolorneutral1rgbNew,
            
            "--sol-color-accent-1-rgb": self.solcoloraccent1rgbNew,
            "--sol-color-accent-2-rgb": self.solcoloraccent2rgbNew,
            "--sol-color-accent-3-rgb": self.solcoloraccent3rgbNew,
        }
        
        self.setup.ModData(self, self.currentPath, ToMod)
    
        
    def loadOrCreateSetup(self,projectName):
        
        try:
            self.loadColor(projectName)
            print(f"Loading colors from file was successfully")
        
        except:
            print("Loading from file Failed")
            print("Save default Data in File")
            self.salvaSuFile()
            print("Save in file was Successful")
            self.loadColor(projectName)
            print("Load Color Data From File")
              
            
    def LoadImg(self, projectName):
        
        project_path = self.setup.LoadData(projectName, "Path")
        file_path = project_path + "\\theme_img.png"
        
        if os.path.isfile(file_path):
            print(f"File found: {file_path}")
            self.original_image = Image.open(file_path).convert("RGBA")
            
            
        else:
            print("File not found will be created now")
            shutil.copyfile("ui\\asset\\default_img.png", file_path)
            self.original_image = Image.open(file_path).convert("RGBA")        
        
        self.update_preview(self.original_image)
        
        
        
        
        
    
    def update_preview(self, image):
        
        image.save(self.currentPath + "\\theme_img.png", format="PNG")
        
        # Resize for Preview
        preview_image = image.copy()
        preview_image.thumbnail((1440, 810), Image.LANCZOS)
        
        self.tk_image = CTkImage(light_image=preview_image.convert("RGBA"), dark_image=preview_image.convert("RGBA"),size=(1440,810))
        self.image_label.configure(image=self.tk_image)
        
        
    def HexToRGB(self, hex):
        
        print(f"hex: {hex}")
        
        hex_color = hex.lstrip('#')  # Remove # if Present
        if len(hex_color) != 6:
            raise ValueError("The hexadecimal color must be 6 characters long.")
        
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
    

        return (r, g, b)
            
        
    def replace_color_in_image(self, old, new):
        if self.original_image is None or new is None:
            print("Seleziona un'immagine e un colore da modificare.")
            return

        # Converti l'immagine in un array numpy
        image_np = np.array(self.original_image)

        # Tolleranza per trovare i pixel da cambiare
        tolleranza = 1
        r, g, b = old

        # Se l'immagine ha 3 canali (RGB)
        if image_np.shape[2] == 3:
            mask = (
                (np.abs(image_np[:, :, 0] - r) < tolleranza) &
                (np.abs(image_np[:, :, 1] - g) < tolleranza) &
                (np.abs(image_np[:, :, 2] - b) < tolleranza)
            )

            image_np[mask] = new  # new deve essere (r, g, b)

            # Crea la nuova immagine
            nuova_immagine = Image.fromarray(image_np.astype('uint8'), 'RGB')

        # Se l'immagine ha 4 canali (RGBA)
        elif image_np.shape[2] == 4:
            mask = (
                (np.abs(image_np[:, :, 0] - r) < tolleranza) &
                (np.abs(image_np[:, :, 1] - g) < tolleranza) &
                (np.abs(image_np[:, :, 2] - b) < tolleranza)
            )

            # Aggiungi il valore alfa se manca
            if len(new) == 3:
                new = (*new, 255)

            image_np[mask] = new  # new deve essere (r, g, b, a)

            nuova_immagine = Image.fromarray(image_np.astype('uint8'), 'RGBA')

        else:
            print("Formato immagine non supportato.")
            return

        # Aggiorna l'anteprima con l'immagine modificata
        self.update_preview(nuova_immagine)
