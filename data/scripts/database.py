import os, pathlib as path, re , shutil





"""
root /
    14th/
        sessiona/
            # cam1/
            # cam2/
            # cam3/
            # cam4/
        session B/
    15th/16th


Out_root/
    1/
    1.jpg 2.jpg 3.jpg 4.jpg
    2/
     1.jpg 2.jpg 3.jpg 4.jpg
     ....

"""
# class Organizer():
    
#     def __init__(self, src_root : Path, dst_root: Path, dry_run : bool = False):


#         def inventory():
            
#             dic = {(day_14th, session_a, cam1
#                     )}
            

import os
from pathlib import Path

searchdir = r'D:\resized\organized files\rose_decay\14th\2-14TH9PMTO15TH9AM'  # your search starts in this directory (your root) 

count = 0
files = Path(searchdir).glob("*")
for name in files:
        (base, ext) = os.path.splitext(name) # split base and extension
        if ext in ('.jpg'):          # check the extension
            count += 1
            full_name = os.path.join(name, name) # create full path
            print(full_name)

print('\ntotal number of .jpg and .gif files found: %d' % count)
