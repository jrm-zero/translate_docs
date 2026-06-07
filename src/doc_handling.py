from PyPDF2 import PdfReader
import re
import os
import pathlib
import shutil

def read_doc(from_path, base_path=None):
    print(f"Pulling text from {from_path} to be translated.")

    source_file = open(from_path)
    source = source_file.read()
    source_file.close()

    return source

def pdf_to_text(from_path, base_path=None):
    print(f"Converting {from_path} to text.")

    source = PdfReader(from_path)
    page = source.pages[0]
    return page.extract_text()

def write_doc(from_path, dest_path, base_path=None):
    print(f"Converting {from_path} from pdf to text doc, writing in {dest_path}.")

    source = pdf_to_text(from_path)
    if os.path.exists(os.path.dirname(dest_path)) != True:
        dest_path_dir = os.path.dirname(dest_path)
        os.makedirs(dest_path_dir)
    dest_file = open(dest_path, "w")
    dest_file.write(source)
    dest_file.close()

    print(f"{from_path} sucessfully written to {dest_path}")
    return 