import os
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QApplication


class WebPreviewQ(QWidget):
    
    def __init__(self,currentPath):
        
        if not QApplication.instance():
            self.app = QApplication(sys.argv)
        else:
            self.app = QApplication.instance()

        
        
        super().__init__()
        
        self.project_path = currentPath

        # Aggiungi la vista web
        self.layout = QVBoxLayout(self)
        self.browser = QWebEngineView(self)
        
        # Abilita JavaScript nel browser
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        
        index_path = self.project_path + "/app/index.html"
        
        test = "http://www.google.it"
        
        if os.path.exists(index_path):
            self.browser.setUrl(QUrl.fromLocalFile(index_path))  # Carica il file HTML come URL locale
        else:
            print("Errore: working directory not found")
        
        # Aggiungi il browser alla finestra
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)

        # Imposta una dimensione minima per il browser
        self.setMinimumSize(800, 600)
        
        
    def show_preview(self):
        self.show()