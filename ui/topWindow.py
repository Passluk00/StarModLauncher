import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox




class TopWindow(tk.Toplevel):

    def __init__(self, parent, setup):
        super().__init__(parent)
        self.setup = setup
        self.title("Select Root File .asar")
        self.geometry("800x200")
        self.resizable(False, False)
        
        self.selected_file = tk.StringVar()
        
        ttk.Label(self, text="File Path Selected: ").pack(pady=5)
        self.entry = ttk.Entry(self, textvariable=self.selected_file, width=50, state="readonly")
        self.entry.pack(padx=10, pady=5)
        
        ttk.Button(self, text="Select File", command=self.select_file).pack(pady=5)
        ttk.Button(self, text="confirm", command=self.confirm_selection).pack(pady=5)
        
        
    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select .asar file", filetypes=[("Asar File", "*.asar")])
        if file_path:
            self.selected_file.set(file_path)
            
    def confirm_selection(self):
        file_path = self.selected_file.get()
        if file_path:
            self.setup.SaveRootPath(file_path)
            messagebox.showinfo("Success", f"Path Saved :{file_path}")
            self.destroy()