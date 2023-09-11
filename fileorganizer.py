import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

# Specify file types
Directories = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "VIDEOS": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".3gp"],
    "DOCUMENTS": [".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "ARCHIVES": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "AUDIO": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
    "PLAINTEXT": [".txt", ".md", ".log", ".json", ".yaml", ".csv"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml", ".xsd", ".dtd", ".xslt"],
    "EXE": [".exe", ".msi"],
    "SHELL": [".sh", ".bash", ".zsh"]
}

FILE_FORMAT = {file_format: directory for directory, file_formats in Directories.items() for file_format in file_formats}

def organize_junk(base):
    for entry in os.scandir(base):
        if entry.is_dir():
            continue

        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMAT:
            directory_name = FILE_FORMAT[file_format]
            directory_path = Path(base, directory_name)
            directory_path.mkdir(parents=True, exist_ok=True)
            new_file_path = directory_path.joinpath(file_path.name)
            file_path.rename(new_file_path)

    # Remove empty directories
    for dir in os.scandir(base):
        if dir.is_dir():
            try:
                os.rmdir(dir)
            except OSError:
                pass

def select_folder_and_organize():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(title="Select a folder to organize")
    if folder_path:
        organize_junk(folder_path)

if __name__ == "__main__":
    select_folder_and_organize()
