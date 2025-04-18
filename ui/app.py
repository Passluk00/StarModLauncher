import tkinter as tk
from core.config import name, version, minDim
from ui.sideBar import SideBar

from ui.mainWindow import MainContent
from core.setup import LoadSetup

import customtkinter as ctk



class App(ctk.CTk):
    
    
    def __init__(self):
        
        super().__init__()
        self.setup = LoadSetup()
        
        
        
        x = (self.winfo_screenwidth() // 2) - (minDim[0] // 2)
        y = (self.winfo_screenheight() // 2) - (minDim[1] // 2)
        
        
        
        
    # Main Setup
        self.title(f'{name} {version}')
        self.geometry( f'{minDim[0]}x{minDim[1]}+{x}+{y}' )        
        self.minsize( minDim[0],minDim[1] )
        
    # Grid Setup

        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)
        
        
    #SideBar

        self.sidebar = SideBar(self, self.setup, None)
        self.sidebar.grid(row=0, column=0, sticky="ns")
      #  self.sidebar.pack(side="left", fill="y")
        
         
    # Main Page
    
        self.mainContent = MainContent(self,self.setup)
        self.mainContent.grid(row=0, column=1 , sticky="nsew")
      #  self.sidebar.pack( fill="both")
        
    
    # Passo il riferimento di main content a sidebar
    
        self.sidebar.mainContent = self.mainContent
    
        
    # Main Loop
    
        self.mainloop()