#!/usr/bin/env python
from __future__ import print_function
import os
import argparse
import shutil

# Python 3 compatibility; override builtin
try:
    input = raw_input
except NameError:
    pass

# Start in current dir
dir_to_walk = "."

# All Markdown files found
md_dict = {}

# Markdown extensions
md_extensions = [
    ".markdown",
    ".mdown",
    ".mkdn",
    ".md",
    ".mkd",
    ".mdwn"
]

# Single or double line break
link_ending = {
    1: "  \n",
    2: "\n\n"
}


def custom_labeler(link_to_ask_about):
    """
    Allow user to choose link labels, per item, for hyperlinks created.

    :param link_to_ask_about: str
    :return: str
    """
    question_string = "Label for '{0}'? <enter> to use default: ".\
        format(link_to_ask_about)
    link_label = input(question_string)
    if link_label is "":
        link_label =  link_to_ask_about
    return link_label


def md_finder():
    """
    Recursively searches directory and subdirectories finding
    any files that match extensions in md_extensions.

    :return:
    """
    for root, dirs, files in os.walk(dir_to_walk):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for i in files:
            if i == "index.md":
                shutil.move("index.md", "index_old.md")
            if i != "index.md" and i != "index_old.md":
                extension = os.path.splitext(i)[1]
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


def index_maker(md_dict, link_ending, interactive):
    """
    Write output to screen and index.md.

    :param md_dict: dict
    :param link_ending: dict
    :param interactive: bool
    :return:
    """
    def write_to_screen_and_index(link_ending, interactive):
        """
        Closure for repetitive actions after root link established.

        :param link_ending: dict
        :param interactive: bool
        :return:
        """
        if interactive is True:
            custom_label = custom_labeler(format_var[1])
            format_var[0] = custom_label
        write_to_file_string = "[{0}]({1}){2}".\
            format(format_var[0], format_var[1], link_ending)
        print(write_to_file_string.rstrip(link_ending))
        with open("index.md", "a") as out_file:
            out_file.write(write_to_file_string)
        print("")

    print("\nReviewing Markdown files found:")
    for key, value in sorted(md_dict.items()):
        key = key.lstrip("/")
        key = "{0}/".format(key)
        print("Current folder '{0}'".format(key))
        if len(value) == 1:
            if key == "/":
                format_var = [value[0], "./{0}".format(value[0])]
            else:
                format_var = [key + value[0], key + value[0]]
            write_to_screen_and_index(link_ending, interactive)
        else:
            for i in value:
                if key == "/":
                    format_var = [i, "./{0}".format(i)]
                else:
                    format_var = [key + i, key + i]
                write_to_screen_and_index(link_ending, interactive)

def main(link_ending, single=False, interactive=False):
    """
    Main program body.

    :param link_ending: dict
    :param single: boolean
    :param interactive: boolean
    :return:
    """
    if single == True:
        link_ending = link_ending[1]
    else:
        link_ending = link_ending[2]
    md_finder()
    index_maker(md_dict, link_ending, interactive)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IndexMaker")
    parser.add_argument(
        "--single", "-s",
        help="use single line break after links",
        required=False,
        action="store_true"
    )
    parser.add_argument(
        "--interactive", "-i",
        help="choose link labels",
        required=False,
        action="store_true"
    )

    args = parser.parse_args()
    main(link_ending, single=args.single, interactive=args.interactive)
