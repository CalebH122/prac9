import os
import shutil


def main():
    category = {}
    os.chdir("FilesToSort2")
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue
        extension = filename.split(".")[-1]
        if extension not in category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        shutil.move(filename, category[extension])


main()
