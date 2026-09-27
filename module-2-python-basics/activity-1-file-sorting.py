"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Tulabut Adrian A]
Date: [9-27-26]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]


============================================
KEY VOCABULARY
============================================
- os module:
- shutil module:
- file path:
- directory:
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""


import os
import shutil

os.makedirs("messy_folder", exist_ok=True)
open("messy_folder/notes.pdf", "w").close()
open("messy_folder/essay.pdf", "w").close()
open("messy_folder/selfie.jpg", "w").close()

messy_folder = "messy_folder"
pdf_box = "messy_folder/PDFs"

os.makedirs(pdf_box, exist_ok=True)

all_files = os.listdir(messy_folder)

for file in all_files:
  if file.endswith(".pdf"):
    where_it_is_now = messy_folder + "/" + file
    shutil.move(where_it_is_now, pdf_box)
    print("moved", file)
    

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
