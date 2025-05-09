import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from ui.topWindow import TopWindow
import subprocess
import uuid

import customtkinter as ctk



class SideBar(ctk.CTkFrame):
    
    def __init__(self, parent, setup, mainContent):
        super().__init__(parent, width=200)
        
        
        self.setup = setup
        self.mainContent = mainContent
        self.projects = setup.GetData().get("Projects", [])
        print(f"dati progetti: {self.projects}")
        
    
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
        
        new_project_name = simpledialog.askstring("New Project", "Insert Name For the Project:")
        
        if not new_project_name:
            messagebox.showerror("Error", "Project name cannot be empty!")
            return
        
        if new_project_name:
            if new_project_name in self.projects:
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
            print( f"Errore apertura file il percorso non è valido: {pathFile}")

        extraction_path = os.path.join(os.getcwd(), "projects" , newProjectName)  # Definisci la cartella dove vuoi decomprimere
    
        # Verifica se la cartella di destinazione esiste, se no la crea
        if not os.path.exists(extraction_path):
            os.makedirs(extraction_path)
            print(f"Cartella creata: {extraction_path}")
            
        self.setup.SaveData(newProjectName, "Path", extraction_path)





    ###  TODO   Da spostare ora non viene piu decompressa al momento della creazione del progetto ma quando viene applicato
    def decomprimi(self, newProjectName):

         
    
        com = f'npx asar extract "{pathFile}" {extraction_path}'
        
        print(f"Comando: {com}")

        try: 
            subprocess.run(com, check=True, shell=True)
            
            
            
            self.setup.SaveData(newProjectName, "Path", extraction_path)
            
            
            print("Estrazione avventua con successo!")
        except subprocess.CalledProcessError as e:
        # Stampa l'errore specifico che si verifica durante l'esecuzione del comando
            print(f"Errore durante l'estrazione: {e}")
            print(f"Output: {e.output}")
            print(f"Codice di ritorno: {e.returncode}")
        except FileNotFoundError as e:
        # Gestione dell'errore se il comando o il programma non è trovato
            print(f"Comando non trovato: {e}")
        except Exception as e:
        # Gestione di eventuali altri errori generali
            print(f"Errore generico: {e}")


    # Open the file selector Window

    def openFileSelector(self):
        TopWindow(self, self.setup)