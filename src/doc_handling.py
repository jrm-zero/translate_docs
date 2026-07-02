from PyPDF2 import PdfReader # type: ignore
from user_interface import *
import os

def read_doc(from_path):
    directories_and_files = from_path.split("/")
    file = directories_and_files[len(directories_and_files) - 1]

    print(f"\nAttempting to read {file} to be translated.\n")
    try:
        source_file = open(from_path)
        source = source_file.read()
        source_file.close()
        return 0, source
    except:
        return 1, f"'{from_path}' is not a valid path!"
    
def pdf_to_text(from_path):
    directories_and_files = from_path.split("/")
    file = directories_and_files[len(directories_and_files) - 1]

    print(f"\nAttempting to convert {file} to text.\n")
    try:
        source = PdfReader(from_path)
        page = source.pages[0]
        return page.extract_text()
    except:
        return 1, f"{from_path} is not a valid path!"
    
def write_doc(from_path, dest_path):
    directories_and_files_from = from_path.split("/")
    directories_and_files_dest = dest_path.split("/")
    from_file_name = directories_and_files_from[len(directories_and_files_from) - 1]
    dest_file_name = directories_and_files_dest[(len(directories_and_files_dest) - 1)]

    print(f"\nConverting {from_file_name} from pdf to text doc. New file is {dest_file_name}.\n")
    if os.path.exists(os.path.dirname(dest_path)) != True:
            print(f"\n{dest_file_name} does not exist, creating new file.\n")
            dest_path_dir = os.path.dirname(dest_path)
            os.makedirs(dest_path_dir)

    try:
        source = pdf_to_text(from_path)
        dest_file = open(dest_path, "w")
        dest_file.write(source)
        dest_file.close()
        print(f"{from_file_name} successfully written to {dest_file_name}")
        return
    except:
        print(f"{from_path} is not a valid path!")
        return