import os
import hashlib

file_dir1 = list(os.listdir('D:\prog\direc\dir1'))
file_dir2 = list(os.listdir('D:\prog\direc\dir2'))

file_hash = []
count1 = len(file_dir1)
for i in range(count1 - 1):

    file_hash = hashlib.sha256()
    with open(file_dir1[i], 'rb') as f:
        text = f.read()
        while len(text) > 0:
            file_hash.update(text)
            text = f.read()

    file_hash.hexdigest()




