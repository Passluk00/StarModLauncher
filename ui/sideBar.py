import os
import tkinter as tk
import logging
from core.log import *
from tkinter import ttk, filedialog, messagebox, simpledialog
from ui.topWindow import TopWindow
import uuid

import customtkinter as ctk



class SideBar(ctk.CTkFrame):
    
    def __init__(self, parent, setup, mainContent):
        super().__init__(parent, width=200)
        
        
        self.setup = setup
        self.mainContent = mainContent
        self.projects = setup.GetData().get("Projects", [])
        logging.info(LOAD_ALL_PROJECTS + f"{self.projects}")
        
        
    
        # Pulsante per selezionare la root path del file sorgente
        root = ctk.CTkButton(self,text="select Root File", command=self.openFileSelector)
        root.pack(fill="x", padx=5, pady=5)
        
        # Tree Viewper la lita dei progetti
        self.project_list =ttk.Treeview(self, show="tree")
        self.project_list.pack(fill="both", expand=True, padx=5, pady=5)
        
        
        # Carica i Progetti
        self.update_project_list()
        
        
        # Pulsante per aggiungere un nuovo progetto
        add_button = ctk.CTkButton(self, text="+ Nuovo Progetto", command=self.add_project)
        add_button.pack(fill="x", padx=5, pady=5)
        
        self.project_list.bind("<<TreeviewSelect>>", self.select_project)
        
             
    def update_project_list(self):
        
        self.project_list.delete(*self.project_list.get_children())  # Svuota la lista
        
        for project in self.projects:
            unique_id = f"{project}_{uuid.uuid4().hex[:6]}"
            self.project_list.insert("", "end", iid=unique_id, text=project)


        
    def add_project(self):
        
        logging.info(CREATE_NEW_PROJECT)
        new_project_name = simpledialog.askstring("New Project", "Insert Name For the Project:")
        
        if not new_project_name:
            logging.warning(ERROR_EMPTY_PROJECT_NAME)
            messagebox.showerror("Error", "Project name cannot be empty!")
            return
        
        if new_project_name:
            if new_project_name in self.projects:
                logging.warning(ERROR_PROJECT_NAME_ALREADY_IN_USE)
                messagebox.showwarning("Error", "Project already exist!")
                return

        self.projects.append(new_project_name)
        
        # va aggiornato viene creata la cartella ma ancora non decomprimo waaste of space
        
        self.createFolder(new_project_name)
        
        self.update_project_list()


    def select_project(self, event):
        """Quando l'utente seleziona un progetto, mostra un messaggio di conferma."""
        selected_item = self.project_list.selection()
        if selected_item:
            project_name = self.project_list.item(selected_item[0], "text")
            self.mainContent.updateContent(project_name)

    def createFolder(self, newProjectName):
        
        pathFile = self.setup.GetOriginalPath()

        if not os.path.exists(pathFile):
            logging.error(ERROR_INVALID_FILE_PATH.format(pathFile))
            

        extraction_path = os.path.join(os.getcwd(), "projects" , newProjectName)  # Definisci la cartella dove vuoi decomprimere
    
        # Verifica se la cartella di destinazione esiste, se no la crea
        if not os.path.exists(extraction_path):
            os.makedirs(extraction_path)
            print(f"Cartella creata: {extraction_path}")
            logging.info(NEW_FOLDER.format(extraction_path))
            
        self.setup.SaveData(newProjectName, "Path", extraction_path)







    # Open the file selector Window

    def openFileSelector(self):
        TopWindow(self, self.setup)