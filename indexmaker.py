from __future__ import print_function
import os

#md_files = []
dir_to_walk = "."

md_files_dict = {

}

def md_finder():
    md_files = []
    for root, dirs, files in os.walk(dir_to_walk):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for i in files:
            full_filename = os.path.join(root, i)
            #print(root)
            #print(i)
            if i.endswith(".md"):
                # if root == ".":
                #     root = "/"
                md_files_dict[root.lstrip(".")] = i
            print(full_filename)
            if full_filename.endswith(".md"):
                md_files.append(full_filename.lstrip("."))
        for i in dirs:
            full_dirname = os.path.join(root, i)
            #print(full_dirname)
    return md_files

md_files = md_finder()
print("\nList:")
md_files.sort()
for i in md_files:
    print(i)
print("\nDict:")
for key, value in sorted(md_files_dict.items()):
    print(key, value)



