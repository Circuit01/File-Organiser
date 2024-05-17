# File Organiser

This Python script helps you organise your cluttered files in a specified directory by categorising them into folders based on their file extensions. It utilises the Tkinter library for the graphical user interface (GUI) to select a folder for organisation and the `os` and `pathlib` libraries for file manipulation.

## Usage

1. Clone or download this repository to your local machine.
2. Ensure you have Python installed on your system (Python 3.6+ recommended).
3. Install any required dependencies by running `pip install tk` if not already installed.
4. Run the script by executing `python file_organiser.py` in your terminal or IDE.

## How It Works

1. The script defines a dictionary called `Directories` that associates various file types with their respective categories. For example, HTML files are categorised under "HTML," image files under "IMAGES," etc.

2. The script defines a `FILE_FORMAT` dictionary, which is generated from the `Directories` dictionary. It maps each file extension to its corresponding category.

3. The `organise_junk` function takes a base directory as input, scans the files in that directory, and moves them to their respective category folders based on their file extensions.

4. The `select_folder_and_organise` function uses the Tkinter library to open a file dialog that allows you to select the folder you want to organise. After selecting the folder, the `organise_junk` function is called to organise the files within that folder.

5. The script is set to run the `select_folder_and_organise` function when executed, so you can simply run the script, select a folder, and let it organise the files for you.

## Supported File Types

The script supports the following file types and categories:

- HTML
- Images
- Videos
- Documents
- Archives
- Audio
- Plain Text
- PDF
- Python
- XML
- Executable
- Shell Scripts

## Note

- Empty directories left after organising files will be automatically removed.

Enjoy keeping your files organised with this script!
