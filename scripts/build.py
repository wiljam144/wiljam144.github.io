import os
import shutil
import fnmatch
from glob import glob

import markdown

def create_build_file(filepath, text):
    path_split = filepath.split("/")[2:-1]
    path = "/".join(path_split)
    filebasename = filepath.split("/")[-1].split(".")[0]
    buildpath = "build/" + path + "/" + filebasename + ".html"

    if not os.path.exists("build/" + path):
        os.makedirs("build/" + path)

    modstring = ""
    if not os.path.exists(buildpath):
        modstring = "x"
    else:
        modstring = "w"

    with open(buildpath, modstring) as nf:
        nf.write(text)

def get_other_files(directory):
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not fnmatch.fnmatch(file, "*.md"):
                files_list.append(os.path.join(root, file))

    return files_list

template = ""
with open("layouts/base.html", "r") as f:
    template = f.read()


markdown_filepaths = [y for x in os.walk("./src/") for y in glob(os.path.join(x[0], "*.md"))]
other_filepaths = get_other_files("./src")

if os.path.exists("build/lib"):
    shutil.rmtree("build/lib")
shutil.copytree("./lib", "build/lib")

for filepath in markdown_filepaths:
    with open(filepath, "r") as f:
        text = f.read()
        html = markdown.markdown(text)

        buildtext = template.replace("{{content}}", html)

        create_build_file(filepath, buildtext)

for filepath in other_filepaths:
    path_split = filepath.split("/")[2:-1]
    filename = filepath.split("/")[-1]

    path = "build/" + "/".join(path_split)

    if not os.path.exists(path):
        os.makedirs(path)

    shutil.copy(filepath, path + "/" + filename)
