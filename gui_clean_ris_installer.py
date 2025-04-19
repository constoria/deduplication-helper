# -*- coding: utf-8 -*-
import re
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def clean_file(input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    def clean_doi_line(match):
        doi = match.group(1).strip()
        if not doi.startswith("http"):
            doi = "https://dx.doi.org/" + doi
        doi = doi.replace("%28", "(").replace("%29", ")")
        return "DO  - {}".format(doi)

    text = re.sub(r"DO  -\s*(.+)", clean_doi_line, text)

    def expand_pages(match):
        start = match.group(1)
        end_suffix = match.group(2)
        if len(end_suffix) >= len(start):
            return match.group(0)
        expanded = start[:-len(end_suffix)] + end_suffix
        return "SP  - {}-{}".format(start, expanded)

    text = re.sub(r"\bSP  - (\d{2,4})[-–](\d{1,2})\b", expand_pages, text)

    base, ext = os.path.splitext(input_path)
    output_path = base + "_CLEANED" + ext
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    return output_path

def select_file():
    filepath = filedialog.askopenfilename(filetypes=[("RIS or TXT files", "*.ris *.txt")])
    if filepath:
        try:
            output = clean_file(filepath)
            messagebox.showinfo("Ready ✅", "File saved:\n\n{}".format(output))
        except Exception as e:
            messagebox.showerror("Error ❌", str(e))

root = tk.Tk()
root.title("DOI and page numbers cleaner")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Choose RIS or TXT file", font=("Arial", 12))
label.pack(pady=10)

button = tk.Button(frame, text="📂 Select file", command=select_file, font=("Arial", 11))
button.pack(pady=5)

root.mainloop()
