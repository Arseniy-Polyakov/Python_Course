import re
from PyPDF2 import PdfReader

reader = PdfReader("files\grammar.pdf")
number_of_pages = len(reader.pages)
pages = [reader.pages[i].extract_text() for i in range(len(reader.pages))]
pages_str = "".join(pages)

pages_str_final = re.sub(r"[^A-Za-z0-9-\.\?\! ]", "", pages_str)

with open("files_final/pdf_final.txt", "wt", encoding="utf-8") as file:
    file.write(pages_str_final)