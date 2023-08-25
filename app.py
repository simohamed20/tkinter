import tkinter as tk
from tkinter import filedialog
import os
import shutil
from PyPDF2 import PdfReader


class PDFClassifierApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Classifier")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.select_file_btn = tk.Button(self, text="Select PDF", command=self.select_file)
        self.select_file_btn.pack(pady=20)

        self.category_label = tk.Label(self, text="Select Category:")
        self.category_label.pack()

        self.category_var = tk.StringVar(self)
        self.category_var.set("Select Category")

        self.category_menu = tk.OptionMenu(self, self.category_var, "tp", "cv", "autre")
        self.category_menu.pack(pady=10)

        self.classify_btn = tk.Button(self, text="Classify", command=self.classify_pdf)
        self.classify_btn.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.selected_file = file_path
            self.select_file_btn.config(text="Selected PDF")

    def classify_pdf(self):
        if hasattr(self, 'selected_file'):
            selected_category = self.category_var.get()
            if selected_category != "Select Category":
                dest_folder = os.path.join(os.path.expanduser("-"), "Desktop", selected_category)
                os.makedirs(dest_folder, exist_ok=True)

                file_name = os.path.basename(self.selected_file)
                dest_path = os.path.join(dest_folder, file_name)

                shutil.move(self.selected_file, dest_path)

                self.select_file_btn.config(text="Select PDF")
                self.selected_file = None
                self.category_var.set("Select Category")

                tk.messagebox.showinfo("Classification", "PDF file classified successfully!")

if __name__ == "__main__":
    app = PDFClassifierApp()
    app.mainloop()
