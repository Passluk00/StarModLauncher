import os
import json
from core.config import config_file



class LoadSetup:
    
    def __init__(self):
        self.filePath = os.path.join(os.getcwd(), config_file)
        self.dati = self.LoadOrCreateData()
        
    def LoadOrCreateData(self):
        if os.path.exists(self.filePath):
            print("Loading file")
            return self.LoadFile()
            
        else:
            print("File not found, new one will be created")
            predef_data = {"PathFile": "", "Projects": []}
            self.WriteFile(predef_data)
            return predef_data
            
    def LoadFile(self):
        
        try:
            with open(self.filePath, "r", encoding="utf-8") as f:
                var = json.load(f)
                
                if var:
                    return var
                else:
                    return {} 
            
        except json.JSONDecodeError:
            print("Error found while loading file: config.json")
            return self.LoadOrCreateData()
      
        
    def WriteFile(self, newData):
            
        with open(self.filePath, "w", encoding="utf-8") as f:
            json.dump(newData, f, indent=4)
            
        print("New Data succesfully Saved")
        self.LoadOrCreateData()
      
        
    def GetData(self):
        if self.dati is None:
            print("Error Loading Data from config.json file")
            return {}
        else:
            return self.dati
    
    
    def SaveRootPath(self, data):
        if data:
            self.dati["PathFile"] = data
            self.WriteFile(self.dati)
    
    
    def ReadPath(self, projectName):
        
        if projectName in self.dati:
            string = str(self.dati[projectName]["Path"]).strip("[]")  # Converte la lista in una stringa
            string = os.path.normpath(string).replace("\\", "/").replace("'","")
            
            print(f"{string}")
                    
            return string
        
        else:
            print("Project not Found")
            return None
        
    
    
    ## TODO DA controllare se va implementato meglio 
    
    
    def SaveData(self, key, sub_key, val):    
    # Se la key principale non esiste, la creiamo come dizionario vuoto
        if key not in self.dati:
            self.dati[key] = {}

        # Se la sub_key non esiste, la creiamo con il valore in una lista
        if sub_key not in self.dati[key]:
            self.dati[key][sub_key] = val
        else:
            # Se la sub_key esiste già, aggiungiamo il valore
            if self.dati[key][sub_key]:
                self.dati[key][sub_key] = (val)
            else:
                self.dati[key][sub_key] = [self.dati[key][sub_key], val]

        # Scriviamo i dati aggiornati nel file
        self.WriteFile(self.dati)
    
    
    
    def GetRootPath(self):
        if self.dati:
            return self.dati["PathFile"]
        
    
    
    def LoadData(self,projectname, key):
        
        if self.dati:
            
            if self.dati[projectname]:
                
                if self.dati[projectname][key]:
                    return self.dati[projectname][key]

                else:
                    print(f"Dato non trovato: {projectname}, {key}")
                []
                
            else:
                print(f"Project non trovato: {projectname}")
                []
            
        else:
            print(f"File non valido errore")
            return []
                

    