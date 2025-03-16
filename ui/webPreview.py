
import os
import sys
import json
import tkinter as tk
from tkinter import ttk
from tkinterweb import HtmlFrame


class WebPreview(tk.Frame):
    
    def __init__(self, parent,currentPath):
        super().__init__(parent)

        self.project_path = currentPath
        self.layout = HtmlFrame(self, javascript_enabled=True, horizontal_scrollbar="auto")
        
        index_path = self.project_path + "/app/index.html"
        
        
        print(f"test path index: {index_path}")
        # Verifica se il percorso esiste e carica il file
        if os.path.exists(index_path):
  
  
  
            self.layout.load_url(f"file:///{index_path}")  # Carica il file HTML come URL locale
  #          self.layout.load_url("https://www.google.it/")
        else:
            print("Errore: working directory not found")
        
        # Aggiungi l'HtmlFrame al layout
        self.layout.pack(fill="both", expand=True)
        
    