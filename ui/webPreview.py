
import os
import json
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class WebPreview(ttk.Frame):
    
    def __init__(self, parent, setup):
        
        super().__init__(parent, padding=10)
        
        self.setup = setup

        self.project_path = self.setup.ReadPath("test")     # ha bisogno del nome del progetto per poterlo cercare 
                                                            # Restituisce la path del progetto


        
        
        
    