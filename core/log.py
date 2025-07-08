import logging

logging.basicConfig( 
                    level=logging.INFO,
                    filename="log.log",
                    filemode="w",
                    format="%(asctime)s, %(levelname)s, %(message)s"
                    )


#####   Log Messages   #####



    ##  StartUp and Initializzation ##

LOG_STARTUP = "Starting StarModLauncher"
INIT_SCREEN = "Window initialization"
START_LOAD_CONFIG = "Start loading config"
LOADING_FILE = "Reading file"
CREATE_CONFIG_FILE = "File not found, new one will be created"
DATA_LOADED_SUCCESSFULLY = "Data loaded successfully"
WRITING_NEW_DATA = "New data successfully saved"
ERROR_LOADING_FROM_FILE = "Loading From File Failed"


    ##  Configuration and Path ##
    
ERROR_LOADING_CONFIG_FILE = "Error found while loading file: config.json"
ERROR_LOADING_DATA = "Error loading data from config.json file"
ROOT_PATH_SAVED = "Root file path successfully saved"
ERROR_SAVING_ROOT_PATH = "Error while saving root path"
READ_PROJECT_PATH = "Start reading project path"
PROJECT_PATH_NOT_FOUND = "Project not found"
FILE_NOT_FOUND = "File not found"
FILE_FOUND = "File found - Path: {}"
WARNING_FILE_NOT_FOUND = "File not found: {}"
ERROR_INVALID_FILE_PATH = "Error opening file: the path is not valid: {}"
NEW_FOLDER = "Folder created successfully - Path: {}"
ERROR_MAIN_HTML_NOT_FOUND = "Main HTML file not found"
ERROR_MAIN_JS_NOT_FOUND = "Main JS file not found"
ERROR_APP_NOT_FOUND = "app.asar not found"
ERROR_DATA_NOT_FOUND = "Project data not found"


    ##  Project Management
    
LOAD_ALL_PROJECTS = "Projects name:"
CREATE_NEW_PROJECT = "Start creating new project folder"
ERROR_EMPTY_PROJECT_NAME = "Project name cannot be empty!"
ERROR_PROJECT_NAME_ALREADY_IN_USE = "Project name already in use!"


    ## Color Management
    
COLORS_LOADED_SUCCESSFULLY = "Loading colors from file was successful"
INFO_LOADING_COLOR_DATA = "Loading color data from file"
INFO_SAVING_DEFAULT_DATA = "Saving default data to file"
INFO_SAVE_SUCCESSFUL = "Saving to file was successful"
COLOR_NUM_SAVED = "Color {} saved: {}"
SAVING_ALL_COLORS_TO_FILE = "Saving all colors to file"
LOADING_ALL_COLORS_FROM_FILE = "Loading all colors from file"


    ## Packing and UnPacking

UNPACK_COMMAND = "Command: {}"
EXTRACTION_SUCCESSFUL = "Extraction completed successfully"
ERROR_UNPACK_ASAR = "Unpack failed"
ERROR_EXTRACTION_FAILED = "Error during extraction: {}"
ERROR_EXTRACTION_OUTPUT = "Output: {}"
ERROR_EXTRACTION_RETURN_CODE = "Return code: {}"
ERROR_COMMAND_NOT_FOUND = "Command not found: {}"
ERROR_GENERIC = "Unexpected error: {}"

PACK_COMMAND = "Command: {}"
PACKING_SUCCESSFUL = "Packing completed successfully"
ERROR_DURING_PACKING = "Error during packing: {}"
ERROR_PACKING_OUTPUT = "Output: {}"
ERROR_PACKING_RETURN_CODE = "Return code: {}"


    ## Mod File
    
INDEX_UPDATE_SUCCESSFUL = "Index modification completed successfully"
JS_UPDATE_SUCCESSFUL = "Js modification completed successfully"


    ## General Error

FORMAT_NOT_SUPPORTED = "Format not supported"


    ## 