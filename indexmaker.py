from __future__ import print_function
import os

dir_to_walk = "." # default start in current dir

md_dict = {} # all Markdown files found

md_extensions = [
    "markdown",
    "mdown",
    "mkdn",
    "md",
    "mkd",
    "mdwn"
]

link_ending = {
    1: "  \n",
    2: "\n\n"
}

def md_finder():
    for root, dirs, files in os.walk(dir_to_walk):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for i in files:
            if i == "index.md":
                os.rename("index.md", "index_old.md")
            if i != "index.md" and i != "index_old.md":
                extension = i.split(".")[1]
                if extension in md_extensions:
                    if root == ".":
                        temp_root = "/"
                    else:
                        temp_root = root.lstrip(".")
                    try:
                        md_dict[temp_root].append(i)
                    except KeyError:
                        md_dict[temp_root] = []
                        md_dict[temp_root].append(i)

def index_maker(md_dict, link_ending):
    print("\nMarkdown files found:\n")
    for key, value in sorted(md_dict.items()):
        key = key.lstrip("/")
        key = "{0}/".format(key)
        print(key)
        if len(value) == 1:
            if key == "/":
                format_var = [value[0], "./{0}".format(value[0])]
            else:
                format_var = [key + value[0], key + value[0]]
            write_to_file_string = "[{0}]({1}){2}".\
                format(format_var[0], format_var[1], link_ending)
            print(write_to_file_string.rstrip(link_ending))
            with open("index.md", "a") as out_file:
                    out_file.write(write_to_file_string)
        else:
            for i in value:
                if key == "/":
                    format_var = [i, "./{0}".format(i)]
                else:
                    format_var = [key + i, key + i]
                write_to_file_string = "[{0}]({1}){2}".\
                    format(format_var[0], format_var[1], link_ending)
                print(write_to_file_string.rstrip(link_ending))
                with open("index.md", "a") as out_file:
                    out_file.write(write_to_file_string)
        print()

md_finder()
index_maker(md_dict, link_ending[2])