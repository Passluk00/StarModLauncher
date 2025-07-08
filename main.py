import logging
from core.log import *
from ui.app import App


def main():
    logging.info(LOG_STARTUP)
    App()
    

if __name__ == "__main__":
    main()