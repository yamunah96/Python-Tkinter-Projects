import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File type categories
file_types = {
    'Images': ['.jpg', '.jpeg', '.png'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov'],
    'Others': []
}

def organize_files(folder):
    if not os.path.exists(folder):
        messagebox.showerror("Error", "Folder does not exist.")
        return

    # Create subfolders if they don’t exist
    for category in file_types:
        category_path = os.path.join(folder, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Go through each file
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)

        if os.path.isdir(file_path):
            continue  # skip folders

        file_ext = os.path.splitext(file_name)[1].lower()
        moved = False

        for category, extensions in file_types.items():
            if file_ext in extensions:
                dest_path = os.path.join(folder, category, file_name)
                shutil.move(file_path, dest_path)
                moved = True
                break

        if not moved:
            dest_path = os.path.join(folder, 'Others', file_name)
            shutil.move(file_path, dest_path)

    messagebox.showinfo("Success", "Files organized successfully!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

def start_organizing():
    folder = folder_path.get()
    organize_files(folder)

# ----------------- GUI Code -----------------
window = tk.Tk()
window.title("Simple File Organizer")
window.geometry("400x200")
window.configure(bg="lightblue")

folder_path = tk.StringVar()

label = tk.Label(window, text="Select folder to organize:", bg="lightblue", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(window, textvariable=folder_path, width=40)
entry.pack(pady=5)

browse_btn = tk.Button(window, text="Browse", command=browse_folder)
browse_btn.pack(pady=5)

organize_btn = tk.Button(window, text="Organize Files", command=start_organizing, bg="green", fg="white")
organize_btn.pack(pady=20)

window.mainloop()
