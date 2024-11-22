import re
with open("files/ielts.txt", "rt", encoding="utf-8") as file:
    text_raw = file.read()

text_without_punc = re.sub(r"[^A-Za-z0-9-\.\?\! ]", " ", text_raw)
text_splitted = text_without_punc.split()
text_final = " ".join(text_splitted)

with open("files_final/ielts_final.txt", "wt", encoding="utf-8") as file:
    file = file.write(text_final)
