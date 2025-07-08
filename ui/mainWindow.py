import tkinter as tk 
import shutil
import os
import numpy as np
import logging
from core.log import *
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
        self.solcolorneutral4 = "#FFFFFF"               # Usage: Most of the launcher text utilises this together with --sol-color-primary-8
        
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
        self.image_label = ctk.CTkLabel(self, text="", width=1080, height=608)
        self.image_label.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
        self.LoadImg(self.projectName)

        self.update_preview(self.original_image)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.frame = ctk.CTkScrollableFrame(self, orientation="vertical")
        self.frame.grid(row=1, column=2, sticky="nsew", padx=150, pady=(10,2))
        
        
        

        # Scrollable Elements

        
        ##############################################################################################################################
        
        
# First Row
        self.row1 = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.row1.pack(fill="x", pady=(20,20))
        
        
    # Sub Row 1: Label
        self.label1 = ctk.CTkFrame(self.row1, fg_color="transparent")
        self.label1.pack(fill="x")
        
        
        # Sub-frame Left
        left_frame11 = ctk.CTkFrame(self.label1, fg_color="transparent")
        left_frame11.pack(side="left", expand=True)

        # Sub-frame Central
        center_frame12 = ctk.CTkFrame(self.label1, fg_color="transparent")
        center_frame12.pack(side="left", expand=True)

        # Sub-frame Right
        right_frame13 = ctk.CTkFrame(self.label1, fg_color="transparent")
        right_frame13.pack(side="left", expand=True)


        # Label
        self.lab11 = ctk.CTkLabel(left_frame11, text="--sol-color-primary-1", text_color="white", font=("Arial", 20, "bold"))
        self.lab11.pack(side="left", padx=90)

        # Label
        self.lab12 = ctk.CTkLabel(center_frame12, text="--sol-color-primary-2", text_color="white", font=("Arial", 20, "bold"))
        self.lab12.pack(side="right", padx=90)

        # Label
        self.lab13 = ctk.CTkLabel(right_frame13, text="--sol-color-primary-3", text_color="white", font=("Arial", 20, "bold"))
        self.lab13.pack(side="right", padx=90)


    # Sub Row 2: Color Picker
        self.ColorPicker1 = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.ColorPicker1.pack(fill="x", pady=5)

        # Sub-frame Left
        left_frame14 = ctk.CTkFrame(self.ColorPicker1, fg_color="transparent")
        left_frame14.pack(side="left", expand=True)

        # Sub-frame Central
        center_frame15 = ctk.CTkFrame(self.ColorPicker1, fg_color="transparent")
        center_frame15.pack(side="left", expand=True)

        # Sub-frame Right
        right_frame16 = ctk.CTkFrame(self.ColorPicker1, fg_color="transparent")
        right_frame16.pack(side="left", expand=True)


        # ColorPicker
        self.Colorpicker11 = CTkColorPicker(left_frame14, width=300, command=self.select_color1, initial_color="#FF0000")
        self.Colorpicker11.pack(padx=10)

        # ColorPicker
        self.Colorpicker12 = CTkColorPicker(center_frame15, width=300, command=self.select_color2, initial_color="#FF0000")
        self.Colorpicker12.pack(padx=10)

        # ColorPicker
        self.Colorpicker13 = CTkColorPicker(right_frame16, width=300, command=self.select_color3, initial_color="#FF0000")
        self.Colorpicker13.pack(padx=10)


    # Sub Row 2: Button
        self.button1 = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.button1.pack(fill="x", pady=5)


        # Sub-frame Left
        left_frame17 = ctk.CTkFrame(self.button1, fg_color="transparent")
        left_frame17.pack(side="left", expand=True)

        # Sub-frame Center
        center_frame18 = ctk.CTkFrame(self.button1, fg_color="transparent")
        center_frame18.pack(side="left", expand=True)

        # Sub-frame Right
        right_frame19 = ctk.CTkFrame(self.button1, fg_color="transparent")
        right_frame19.pack(side="left", expand=True)


        # Button
        self.confirm11 = ctk.CTkButton(left_frame17, command=self.Confirm_change_Color1, text="Conferma Colore 1")
        self.confirm11.pack(side="left", padx=110)

        # Button
        self.confirm12 = ctk.CTkButton(center_frame18, command=self.Confirm_change_Color2, text="Conferma Colore 2")
        self.confirm12.pack(side="left", padx=110)

        
        # Button    TODO attualmente usato per provare modificare i file
        self.confirm13 = ctk.CTkButton(right_frame19, command=self.modLauncher, text="Conferma Colore 3")
        self.confirm13.pack(side="left", padx=110)

    
        ##############################################################################################################################
        
        
# Second Row    
        self.row2 = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.row2.pack(fill="x", pady=(20,20))
            
            
    # Sub Row 1: Label        
        self.label2 = ctk.CTkFrame(self.row2, fg_color="transparent")
        self.label2.pack(fill="x")
        
        
        # Sub-frame Left
        left_frame21 = ctk.CTkFrame(self.label2, fg_color="transparent")
        left_frame21.pack(side="left", expand=True)

        # Sub-frame Central
        center_frame22 = ctk.CTkFrame(self.label2, fg_color="transparent")
        center_frame22.pack(side="left", expand=True)

        # Sub-frame Right
        right_frame23 = ctk.CTkFrame(self.label2, fg_color="transparent")
        right_frame23.pack(side="left", expand=True)


        # Label
        self.lab21 = ctk.CTkLabel(left_frame21, text="--sol-color-primary-4", text_color="white", font=("Arial", 20, "bold"))
        self.lab21.pack(side="left", padx=90)

        # Label
        self.lab22 = ctk.CTkLabel(center_frame22, text="--sol-color-primary-5", text_color="white", font=("Arial", 20, "bold"))
        self.lab22.pack(side="right", padx=90)

        # Label
        self.lab23 = ctk.CTkLabel(right_frame23, text="--sol-color-primary-6", text_color="white", font=("Arial", 20, "bold"))
        self.lab23.pack(side="right", padx=90)

        
    # Sub Row 2: Color Picker
        self.ColorPicker2 = ctk.CTkFrame(self.row2, fg_color="transparent")
        self.ColorPicker2.pack(fill="x")
    
    
        # Sub-frame Left
        left_frame24 = ctk.CTkFrame(self.ColorPicker2, fg_color="transparent")
        left_frame24.pack(side="left", expand=True)

        # Sub-frame Center
        center_frame25 = ctk.CTkFrame(self.ColorPicker2, fg_color="transparent")
        center_frame25.pack(side="left", expand=True)

        # Sub-frame Right
        right_frame26 = ctk.CTkFrame(self.ColorPicker2, fg_color="transparent")
        right_frame26.pack(side="left", expand=True)


        # ColorPicker
        self.Colorpicker21 = CTkColorPicker(left_frame24, width=300, command=self.select_color4, initial_color="#FF0000")
        self.Colorpicker21.pack(padx=10)

        # ColorPicker
        self.Colorpicker22 = CTkColorPicker(center_frame25, width=300, command=self.select_color5, initial_color="#FF0000")
        self.Colorpicker22.pack(padx=10)

        # ColorPicker
        self.Colorpicker23 = CTkColorPicker(right_frame26, width=300, command=self.select_color_neutral_4, initial_color="#00FF00")
        self.Colorpicker23.pack(padx=10)


    # Sub Row 2: Button
        self.Button2 = ctk.CTkFrame(self.row2, fg_color="transparent")
        self.Button2.pack(fill="x")


        # Sub-frame Left
        left_frame27 = ctk.CTkFrame(self.Button2, fg_color="transparent")
        left_frame27.pack(side="left", expand=True)

        # Sub-frame Central
        center_frame28 = ctk.CTkFrame(self.Button2, fg_color="transparent")
        center_frame28.pack(side="left", expand=True)

        # Sub-frame Right
        right_frame29 = ctk.CTkFrame(self.Button2, fg_color="transparent")
        right_frame29.pack(side="left", expand=True)
    
    
        # Button
        self.confirm21 = ctk.CTkButton(left_frame27, command=self.Confirm_change_Color4, text="Conferma Colore 1")
        self.confirm21.pack(side="left", padx=110)

        # Button
        self.confirm22 = ctk.CTkButton(center_frame28, command=self.Confirm_change_Color5, text="Conferma Colore 2")
        self.confirm22.pack(side="left", padx=110)

        
        # Button
        self.confirm23 = ctk.CTkButton(right_frame29, command=self.Confirm_change_Color6, text="Conferma Colore 3")
        self.confirm23.pack(side="left", padx=110)

    
       
       
       
    # Utility Function
    
    def Confirm_change_Color1(self):
        
        toRGBOld = self.HexToRGB(self.solcolorprimary1)
        toRGBNew = self.HexToRGB(self.solcolorprimary1New)
        self.replace_color_in_image(toRGBOld, toRGBNew)
        self.salvaSuFile()
        self.solcolorprimary1 = self.solcolorprimary1New
        logging.info(COLOR_NUM_SAVED.format(1,self.solcolorprimary1))
        print(f"Colore 1 Salvato {self.solcolorprimary1}")
    
    def select_color1(self,color):
        self.solcolorprimary1New = color
        print(f"Colore 1 Selezionato : {self.solcolorprimary1New}")
    
        
    def Confirm_change_Color2(self):
        
        toRGBOld = self.HexToRGB(self.solcolorprimary2)
        toRGBNew = self.HexToRGB(self.solcolorprimary2New)
        self.replace_color_in_image(toRGBOld, toRGBNew)
        self.salvaSuFile()
        self.solcolorprimary2 = self.solcolorprimary2New
        logging.info(COLOR_NUM_SAVED.format(2,self.solcolorprimary2))
        print(f"Colore 2 Salvato {self.solcolorprimary2}")
    
    def select_color2(self,color):
        self.solcolorprimary2New = color
        print(f"Colore 2 Selezionato : {self.solcolorprimary2New}")
    
        
    def Confirm_change_Color3(self):
        
        toRGBOld = self.HexToRGB(self.solcolorprimary3)
        toRGBNew = self.HexToRGB(self.solcolorprimary3New)
        self.replace_color_in_image(toRGBOld, toRGBNew)
        self.solcolorprimary3 = self.solcolorprimary3New
        self.salvaSuFile()
        logging.info(COLOR_NUM_SAVED.format(3,self.solcolorprimary3))
        print(f"Colore 3 Salvato {self.solcolorprimary3}")

    def select_color3(self,color):
        self.solcolorprimary3New = color
        print(f"Colore 3 Selezionato : {self.solcolorprimary3New}")

    
    def Confirm_change_Color4(self):
        
        toRGBOld = self.HexToRGB(self.solcolorprimary4)
        toRGBNew = self.HexToRGB(self.solcolorprimary4New)
        self.replace_color_in_image(toRGBOld, toRGBNew)
        self.salvaSuFile()
        self.solcolorprimary4 = self.solcolorprimary4New
        logging.info(COLOR_NUM_SAVED.format(4,self.solcolorprimary4))
        print(f"Colore 4 Salvato {self.solcolorprimary4}")
    
    def select_color4(self,color):
        self.solcolorprimary4New = color
        print(f"Colore 4 Selezionato : {self.solcolorprimary4New}")
    
    
    def Confirm_change_Color5(self):
        
        toRGBOld = self.HexToRGB(self.solcolorprimary5)
        toRGBNew = self.HexToRGB(self.solcolorprimary5New)
        self.replace_color_in_image(toRGBOld, toRGBNew)
        self.salvaSuFile()
        self.solcolorprimary5 = self.solcolorprimary5New
        logging.info(COLOR_NUM_SAVED.format(5,self.solcolorprimary5))
        print(f"Colore 5 Salvato {self.solcolorprimary5}")
        
    def select_color5(self,color):
        self.solcolorprimary5New = color
        print(f"Colore 5 Selezionato : {self.solcolorprimary5New}")
    
    
    def Confirm_change_Color6(self):
    
        toRGBOld = self.HexToRGB(self.solcolorprimary6)
        toRGBNew = self.HexToRGB(self.solcolorprimary6New)
        self.replace_color_in_image(toRGBOld, toRGBNew)
        self.salvaSuFile()
        self.solcolorprimary6 = self.solcolorprimary6New
        logging.info(COLOR_NUM_SAVED.format(6,self.solcolorprimary6))
        print(f"Colore 6 Salvato {self.solcolorprimary6}")
    
    def select_color6(self,color):
        self.solcolorprimary6New = color
        print(f"Colore 6 Selezionato : {self.solcolorprimary6New}")
    
        
    def Confirm_change_Color7(self):
    
        toRGBOld = self.HexToRGB(self.solcolorprimary7)
        toRGBNew = self.HexToRGB(self.solcolorprimary7New)
        self.replace_color_in_image(toRGBOld, toRGBNew)
        self.salvaSuFile()
        self.solcolorprimary7 = self.solcolorprimary7New
        logging.info(COLOR_NUM_SAVED.format(7,self.solcolorprimary7))
        print(f"Colore 7 Salvato {self.solcolorprimary7}")
    
    def select_color7(self,color):
        self.solcolorprimary7New = color
        print(f"Colore 7 Selezionato : {self.solcolorprimary7New}")
    
    
    def Confirm_change_Color8(self):
        
        toRGBOld = self.HexToRGB(self.solcolorprimary8)
        toRGBNew = self.HexToRGB(self.solcolorprimary8New)
        self.replace_color_in_image(toRGBOld, toRGBNew)
        self.salvaSuFile()
        self.solcolorprimary8 = self.solcolorprimary8New
        logging.info(COLOR_NUM_SAVED.format(8,self.solcolorprimary8))
        print(f"Colore 8 Salvato {self.solcolorprimary8}")
        
    def select_color8(self,color):
        self.solcolorprimary8New = color
        print(f"Colore 8 Selezionato : {self.solcolorprimary8New}")
    
    
    def Confirm_change_Color_neutral_4(self):
    
        toRGBOld = self.HexToRGB(self.solcolorneutral4)
        toRGBNew = self.HexToRGB(self.solcolorneutral4New)
        self.replace_color_in_image(toRGBOld, toRGBNew)
        self.salvaSuFile()
        self.solcolorneutral4 = self.solcolorneutral4New
        logging.info(COLOR_NUM_SAVED.format(4,self.solcolorneutral4))
        print(f"Colore Neutrl 4 Salvato {self.solcolorneutral4}")
    
    def select_color_neutral_4(self,color):
        self.solcolorneutral4New = color
        print(f"Colore Neutral 4 Selezionato : {self.solcolorneutral4New}")
    
    
    

    
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
        logging.info(SAVING_ALL_COLORS_TO_FILE)
       
        self.setup.SaveData(self.projectName, "colors", colors)


    def loadColor(self, projectname):
        
        logging.info(LOADING_ALL_COLORS_FROM_FILE)
        
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
        
        
    def loadOrCreateSetup(self,projectName):
        
        try:
            self.loadColor(projectName)
            logging.info(COLORS_LOADED_SUCCESSFULLY)
        
        except:
            
            logging.error(ERROR_LOADING_FROM_FILE)
            logging.info(INFO_SAVING_DEFAULT_DATA)
            self.salvaSuFile()
            
            logging.info(INFO_SAVE_SUCCESSFUL)
            self.loadColor(projectName)
            logging.info(INFO_LOADING_COLOR_DATA)
           
            
    def LoadImg(self, projectName):
        
        project_path = self.setup.LoadData(projectName, "Path")
        file_path = project_path + "\\theme_img.png"
        
        if os.path.isfile(file_path):
            logging.info(FILE_FOUND.format(file_path))
            self.original_image = Image.open(file_path).convert("RGBA")
            
            
        else:
            logging.info(WARNING_FILE_NOT_FOUND.format(" will be created now"))
            shutil.copyfile("ui\\asset\\default_img.png", file_path)
            self.original_image = Image.open(file_path).convert("RGBA")        
        
        self.update_preview(self.original_image)
        
    
    def update_preview(self, image):
        
        image.save(self.currentPath + "\\theme_img.png", format="PNG")
        self.original_image = image     
        
        # Resize for Preview
        preview_image = image.copy()
        preview_image.thumbnail((1080, 608), Image.LANCZOS)
        
        self.tk_image = CTkImage(light_image=preview_image.convert("RGBA"), dark_image=preview_image.convert("RGBA"),size=(1080,608))
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
        
        if self.original_image is None or new is None or old is None:
            logging.warning("Select an immage and one color to modify")
            return

        # Convert img to an numpy array
        image_np = np.array(self.original_image)

         # Define Tollerance
        tolleranza = 1
        r, g, b = old

        # If Img have a 3 chanel (RGB)
        if image_np.shape[2] == 3:
            mask = (
                (np.abs(image_np[:, :, 0] - r) < tolleranza) &
                (np.abs(image_np[:, :, 1] - g) < tolleranza) &
                (np.abs(image_np[:, :, 2] - b) < tolleranza)
            )

            image_np[mask] = new  # new deve essere (r, g, b)

            # Create a new Img
            nuova_immagine = Image.fromarray(image_np.astype('uint8'), 'RGB')

        # If Img have a 4 chanel (RGBA)
        elif image_np.shape[2] == 4:
            mask = (
                (np.abs(image_np[:, :, 0] - r) < tolleranza) &
                (np.abs(image_np[:, :, 1] - g) < tolleranza) &
                (np.abs(image_np[:, :, 2] - b) < tolleranza)
            )

            # Add alfa Value if missing
            if len(new) == 3:
                new = (*new, 255)

            image_np[mask] = new  # ned to be (r, g, b, a)

            nuova_immagine = Image.fromarray(image_np.astype('uint8'), 'RGBA')

        else:
            logging.error(FORMAT_NOT_SUPPORTED)
            return

        # Update Preview with the new Img
        self.update_preview(nuova_immagine)


    def modLauncher(self, ):
        pathFile = self.setup.GetRootPath()
        
        if not pathFile:
            logging.error(ERROR_APP_NOT_FOUND)
            raise FileNotFoundError("app.asar Not Found")
        
        data = self.setup.LoadData(self.projectName,"colors")
        
        if not data:
            logging.error(ERROR_DATA_NOT_FOUND)
            raise FileNotFoundError("Project data not found")
        
        self.setup.ModData(pathFile,self.projectName ,data)
        