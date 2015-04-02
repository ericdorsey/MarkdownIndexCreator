from __future__ import print_function
import os

#md_files = []
dir_to_walk = "."

md_files = []
md_dict = {}

def md_finder():
    for root, dirs, files in os.walk(dir_to_walk):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for i in files:
            if i.endswith(".md"):
                print("i is:", i, i.endswith(".md"), "root is:", root, root == ".")
                full_filename = os.path.join(root, i)
                md_files.append(full_filename.lstrip("."))
                if root == ".":
                    temp_root = "falalah"
                else:
                    temp_root = root.lstrip(".")
                try:
                    md_dict[temp_root].append(i)
                except KeyError:
                    md_dict[temp_root] = []
                    md_dict[temp_root].append(i)
        for i in dirs:
            full_dirname = os.path.join(root, i)
            #print(full_dirname)

md_finder()
print("\nList:")
md_files.sort()
for i in md_files:
    print(i)

print("\nDict:")
#print(md_dict)
for key, value in sorted(md_dict.items()):
    print(key, value)