import os

config_file = "config.json"



class FileHandler():
    
    
    def __init__(self):
        
        self.percorso_file = os.path.join(os.getcwd(), config_file)
        self.dati = self.LoadOrCreateData()
         
        if "pathFile" in Dati:
            pathFile = Dati["pathFile"]
        
        
    def LoadOrCreateData(self):
        
        if os.path.exists(self.percorso_file):
            print("file Caricato con successo")
            return self.LoadFile()
        
        else:
            print("File non trovato ne verra creato uno")
            dati_predefiniti = {"pathFile": ""}
            self.scriviFile(dati_predefiniti)
            return dati_predefiniti
        
    
    def LoadFile(self):
        
        try:
            with open(self.percorso_file, "r", encoding="utf-8") as f:
                return json.load(f)
        
        except json.JSONDecodeError:
            print("Errore nella lettura del file config.json")
            return self.LoadOrCreateData()    
    
    
    def scriviFile(self, nuoviDati):
        
        with open(self.percorso_file, "w", encoding="utf-8") as f:
            json.dump(nuoviDati, f , indent=4)                                  # TODO controllare se questa funzione cancella tutti i dati precedenti o li aggiunge
        print("dati salvati con successo!!")
    
    
    def OttieniDati(self):
        return self.dati
    
    
    def SalvaRootPath(self, newKey, data):
        
        global pathFile
        
        Dati[newKey] = data
        self.scriviFile(Dati)
        pathFile = data
        print(f"Valore Aggiornato: {pathFile}")

        
        
    
    def SalvaNuovoDato(self, nuovaChiave, nuovoDato):
        
        self.dati[nuovaChiave] = nuovoDato
        self.scriviFile(self.dati)
    
    
    def AggiungiAdUnaChiave(self, chiave, valore):
    
        if chiave in self.dati:
            if isinstance(self.dati[chiave], list):
                self.dati[chiave].append(valore)
            else:
                self.dati[chiave] = [self.dati[chiave], valore]
                
        else:
            self.dati[chiave] = [valore]
            
        self.scriviFile(self.dati);
        print(f"Valore aggiunto {chiave}: {valore}")
