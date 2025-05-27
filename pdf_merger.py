import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

def merge_pdfs():
    files = filedialog.askopenfilenames(title="Select PDFs to Merge", filetypes=[("PDF files", "*.pdf")])
    if not files:
        return

    merger = PdfMerger()
    for pdf in files:
        merger.append(pdf)

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                               filetypes=[("PDF files", "*.pdf")],
                                               title="Save Merged PDF As")
    if output_path:
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Success", f"Merged PDF saved at:\n{output_path}")
    else:
        messagebox.showwarning("Cancelled", "Save operation cancelled.")

# GUI setup
root = tk.Tk()
root.title("PDF Merger Tool")

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

btn = tk.Button(root, text="Merge PDFs", command=merge_pdfs, bg="blue", fg="white")
canvas.create_window(150, 100, window=btn)

root.mainloop()
