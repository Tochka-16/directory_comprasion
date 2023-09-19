import os
import hashlib

file_dir1 = list(os.listdir('D:\prog\direc\dir1'))
file_dir2 = list(os.listdir('D:\prog\direc\dir2'))

fileHash1 = []
count1 = len(file_dir1)
for i in range(count1):

    file_hash1 = hashlib.sha256()
    with open(f'D:\prog\direc\dir1\{file_dir1[i]}', 'rb') as f:
        text = f.read()
        while len(text) > 0:
            file_hash1.update(text)
            text = f.read()

    a = file_hash1.hexdigest()
    fileHash1.append(str(a))

dict1 = dict(zip(file_dir1, fileHash1))


fileHash2 = []
count2 = len(file_dir2)
for i in range(count2):

    file_hash2 = hashlib.sha256()
    with open(f'D:\prog\direc\dir2\{file_dir2[i]}', 'rb') as f:
        text = f.read()
        while len(text) > 0:
            file_hash2.update(text)
            text = f.read()

    b = file_hash2.hexdigest()
    fileHash2.append(str(b))

dict2 = dict(zip(file_dir2, fileHash2))


dict1_values = dict1.values()
dict2_values = dict2.values()


for x in dict1_values:
    if x in dict2_values:
        value1, value2 = {i for i in dict1 if dict1[i]==x}, {i for i in dict2 if dict2[i]==x}
        print(f'''D:\prog\direc\dir1\{value1}
D:\prog\direc\dir2\{value2}
''')
    else:
        continue


