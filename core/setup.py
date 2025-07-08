import os
import re
import json
import subprocess
import logging
from core.log import *
from pathlib import Path
from core.config import config_file



class LoadSetup:
    
    def __init__(self):
        logging.info(START_LOAD_CONFIG)
        self.filePath = os.path.join(os.getcwd(), config_file)
        self.dati = self.LoadOrCreateData()
        
    def LoadOrCreateData(self):
        if os.path.exists(self.filePath):
            logging.info(LOADING_FILE)
            return self.LoadFile()
            
        else:
            logging.info(CREATE_CONFIG_FILE)
            predef_data = {"PathFile": "","OrigianlFile": "" ,"DefaultImg": "ui\asset\Default_Img.png" , "Projects": []}
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
            logging.error(ERROR_LOADING_CONFIG_FILE)
            return self.LoadOrCreateData()
      
        
    def WriteFile(self, newData):
            
        with open(self.filePath, "w", encoding="utf-8") as f:
            json.dump(newData, f, indent=4)
            
        logging.info(WRITING_NEW_DATA)
        self.LoadOrCreateData()
      
        
    def GetData(self):
        if self.dati is None:
            logging.error(ERROR_LOADING_DATA)
            return {}
        else:
            logging.info(DATA_LOADED_SUCCESSFULLY)
            return self.dati
    
    
    def SaveRootPath(self, data):
        if data:
            logging.info(ROOT_PATH_SAVED)
            self.dati["PathFile"] = data
            self.WriteFile(self.dati)
        else:
            logging.error(ERROR_SAVING_ROOT_PATH)
    
    def SaveBackUpPath(self,data):
        if data:
            self.dati["OrigianlFile"] = data
            self.WriteFile(self.dati)    
    
    def ReadPath(self, projectName):
        
        if projectName in self.dati:
            logging.info(READ_PROJECT_PATH)
            string = str(self.dati[projectName]["Path"]).strip("[]")  # Converte la lista in una stringa
            string = os.path.normpath(string).replace("\\", "/").replace("'","")
            
            logging.info(f"Path: {string}")
            print(f"{string}")
                    
            return string
        
        else:
            logging.warning(PROJECT_PATH_NOT_FOUND)
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
    
    def GetOriginalPath(self):
        if self.dati:
            return self.dati["OrigianlFile"]
        
    def GetDefaultImg(self):
        if self.dati:
            return self.dati["DefaultImg"]
    
    
    def LoadData(self,projectname, key):
        
        if self.dati:
            
            if self.dati[projectname]:
                
                if self.dati[projectname][key]:
                    return self.dati[projectname][key]

                else:
                    
                    logging.warning(f"Data not found: {projectname}, {key}")
                                       
                    return []
                
            else:
                print(f"Project non trovato: {projectname}")
                logging.warning(f"Project with name: {projectname} - Not Found")
                return []
            
        else:
            logging.error(FILE_NOT_FOUND + f"{projectname} - {key}")
            return []
                

    def ModData(self, rootPath, projectName, data):
        
        
        projectPath = self.ReadPath(projectName)
        
        
        success = self.unpack_asar(rootPath,projectName)
        
        if not success:
            logging.error(ERROR_UNPACK_ASAR)

        
        self.mod_index(projectPath,data)
        self.mod_js(projectPath,data)
        self.repack_asar(os.path.join(projectPath,"Data"))
        
    
        
    def unpack_asar(self,rootPath, projectName):
        
        projectPath = self.ReadPath(projectName)
        
        com = f'npx asar extract "{rootPath}" {os.path.join(projectPath,"Data")}'
        
        logging.info(UNPACK_COMMAND.format(com))
        
        try: 
            subprocess.run(com, check=True, shell=True)
          
            self.SaveData(projectName, "DataPath", os.path.join(projectPath,"Data")) 
            logging.info(EXTRACTION_SUCCESSFUL)
            return True
        except subprocess.CalledProcessError as e:
            logging.error(ERROR_EXTRACTION_FAILED.format(e))
            logging.error(ERROR_EXTRACTION_OUTPUT.format(e.output))
            logging.error(ERROR_EXTRACTION_RETURN_CODE.format(e.returncode))

        except FileNotFoundError as e:
            logging.error(ERROR_COMMAND_NOT_FOUND.format(e))

        except Exception as e:
            logging.error(ERROR_GENERIC.format(e))



    def repack_asar(self,dataProjectPath):
        
        
        destinationAsar = self.GetRootPath() # il percorso dove salvare il nuovo .asar

        com = f'npx asar pack "{dataProjectPath}" "{destinationAsar}"'

        logging.info(PACK_COMMAND.format(com))

        try:
            subprocess.run(com, check=True, shell=True)
            logging.info(PACKING_SUCCESSFUL)

        except subprocess.CalledProcessError as e:
            logging.error(ERROR_DURING_PACKING.format(e))
            logging.error(ERROR_PACKING_OUTPUT.format(e.output))
            logging.error(ERROR_PACKING_RETURN_CODE.format(e.returncode))

        except FileNotFoundError as e:
            logging.error(ERROR_COMMAND_NOT_FOUND.format(e))

        except Exception as e:
            logging.error(ERROR_GENERIC.format(e))



    def mod_index(self, projectPath, data):
        
        
        file_html = next( ( file for file in Path(os.path.join(projectPath,"Data")).rglob("index.html")),None  )
        
        if not file_html:
            logging.error(ERROR_MAIN_HTML_NOT_FOUND)
            raise FileNotFoundError("Main html file not found.")
        
        with open(file_html, "r", encoding="utf-8") as file:
            content = file.read()
                
        content = self.add_version_disclaimer(content)
    
        with open(file_html, "w", encoding="utf-8") as file:
            file.write(content)   
            
        logging.info(INDEX_UPDATE_SUCCESSFUL)

        
    
    def mod_js(self,projectPath,data):
        
        logging.info(f"Project path: {projectPath}")
        logging.info("Path js: " + os.path.join(projectPath,"Data/app/static/js"))
        
        file_js = next( ( file for file in Path(os.path.join(projectPath,"Data/app/static/js")).rglob("main.*.js")),None  )

        if not file_js:
            logging.error(ERROR_MAIN_JS_NOT_FOUND)
            raise FileNotFoundError("Main js file not found")
        
        with open(file_js, "r", encoding="utf-8") as file:
            
            content = file.read()
        
        content = self.modColor(content,data)
        content = self.add_modding_disclaimer(content)
        
        
        ## TODO cambiare per inserire file diversi
        ##content = self.apply_mods(content, data)
        
        with open(file_js, "w", encoding="utf-8") as file:
            file.write(content)
        
        logging.info(JS_UPDATE_SUCCESSFUL)
    
    
    
    
    
    def modColor(self,content, data):
        for theme_var, new_theme_color in data.items():
            content = re.sub(
                rf"({theme_var}:\s*[^;]+)", rf"{theme_var}: {new_theme_color}", content
            )
        return content
        
        

        
        
    
    def apply_mods(
        content, mods_replacements
    ):  # all mods.json contents aswell as mods folder
        for original_code, replacement_code in mods_replacements.items():
            escaped_pattern = re.escape(original_code)
            content = re.sub(
                escaped_pattern, replacement_code, content, flags=re.DOTALL
            )
        return content
 
        
        
    def add_modding_disclaimer(self,content):
        pattern = re.escape(
            'children:[" ",n("settings_about_launcher_preversion")]})]})]})})'
        )  # Don't touch this - in fact don't even look at it :D
        replacement = (
            'children:[" ",n("settings_about_launcher_preversion")]}), (0, wR.jsx)("br", {}), (0, wR.jsx)("br", {}),'
            '(0, wR.jsx)("b", { children: "This is a Fan modification of the RSI Launcher." }), '
            '(0, wR.jsx)("p", { children: "This project is not endorsed by or affiliated with the Cloud Imperium or '
            "Roberts Space Industries group of companies. All game content and materials are copyright Cloud    Imperium Rights "
            "LLC and Cloud Imperium Rights Ltd.. Star Citizen®, Squadron 42®, Roberts Space Industries®, and Cloud Imperium® "
            'are registered trademarks of Cloud Imperium Rights LLC. All rights reserved." })]}),]})});'
        )
        return re.sub(pattern, replacement, content, flags=re.DOTALL)






    





    def add_version_disclaimer(
            self, content
        ):  # This is the little text at the bottom left that contains the version number and we're adding a modded disclaimer to it.
            return re.sub(
                r'(<div [^>]*id=["\']app-version["\'][^>]*>)([0-9]+\.[0-9]+\.[0-9]+)(</div>)',
                r"\1\2 (modded)\3",
                content,
            )