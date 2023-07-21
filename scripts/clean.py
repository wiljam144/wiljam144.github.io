import os
import shutil

if os.path.exists("./build"):
    shutil.rmtree("./build")