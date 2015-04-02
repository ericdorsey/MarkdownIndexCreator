from __future__ import print_function
import os

# TODO: option: double space ending or \n\n ending

dir_to_walk = "."

md_files = []
md_dict = {}

# def make_output_dir():
#     if not os.path.exists("./output"):
#         os.makedirs("./output")

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
                    temp_root = "/"
                else:
                    temp_root = root.lstrip(".")
                try:
                    md_dict[temp_root].append(i)
                except KeyError:
                    md_dict[temp_root] = []
                    md_dict[temp_root].append(i)
        # for i in dirs:
        #     full_dirname = os.path.join(root, i)
        #     #print(full_dirname)


def index_maker(md_dict):
    print()
    for key, value in sorted(md_dict.items()):
        key = key.lstrip("/")
        key = "{0}/".format(key)
        print(key)
        #format_var = None
        if len(value) == 1:
            print("length was 1")
            if key == "/":
                key = value[0]
                format_var = [value[0], "./" + value[0]]
            else:
                format_var = [key + value[0], key + value[0]]
            write_to_file_string = "[{0}]({1})\n\n".format(format_var[0], format_var[1])
            print(write_to_file_string)
            with open("index.md", "a") as out_file:
                    out_file.write(write_to_file_string)
            #print()
        else:
            print("length not 1")
            for i in value:
                if key == "/":
                    #key = i
                    format_var = [i, "./" + i]
                else:
                    format_var = [key + i, key + i]
                write_to_file_string = "[{0}]({1})\n\n".format(format_var[0], format_var[1])
                print(write_to_file_string)
                with open("index.md", "a") as out_file:
                    out_file.write(write_to_file_string)
            #print()

# make_output_dir()

md_finder()
# print("\nList:")
# md_files.sort()
# for i in md_files:
#     print(i)
#
# print("\nDict:")
# #print(md_dict)
# for key, value in sorted(md_dict.items()):
#     print(key, value)

index_maker(md_dict)