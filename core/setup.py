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
            return self.dati[projectName]
        
        else:
            print("Project not Found")
            return None
        
    
    
    ## TODO DA controllare se va implementato meglio 
    
    def SaveData(self, key, val):    
        if key in self.dati:
            if isinstance(self.dati[key], list):
                self.dati[key].append(val)
            else:
                self.dati[key] = [self.dati[key], val]
                
        else:
            self.dati[key] = [val]
            
        self.WriteFile(self.dati);
        print(f"Valore aggiunto {key}: {val}")
    
    
    # Salva projetto tramite il nome gia dato 
    
    
    
    
    
    
    
    def GetRootPath(self):
        if self.dati:
            return self.dati["PathFile"]