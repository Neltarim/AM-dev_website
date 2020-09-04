from shutil import copyfile
from os import remove, getcwd, chdir, listdir
from os.path import isfile
from pathlib import Path

STATICS_SRC = {
    "js/jquery.min.js",
    "js/popper.min.js",
    "js/bootstrap.min.js",
    "js/mdb.min.js",
    "js/modules/cards.min.js",
    "js/modules/scrolling-navbar.min.js",
    "js/modules/smooth-scroll.min.js",
    "css/bootstrap.min.css",
    "css/mdb.min.css",
    "css/style.css",
    "img/highway-animated-wallpaper-4k-3840x2160.jpg",
    "img/sleepless_icon.png"
}

class migration():
    def __init__(self):
        self.root_path = getcwd()
        self.dest_path = self.root_path + "/am_django/mainapp/static/mainapp"
        self.html_dest_path = self.root_path + "/am_django/mainapp/templates/mainapp"
        self.src_path = self.root_path + "/am_front_static/new_model"

        self.empty_static()
        self.fill_static()
        self.copy_html()


    def empty_static(self):

        files_to_delete = []

        for path in STATICS_SRC:
            absolute = self.dest_path + "/" + path
            
            if isfile(absolute):
                files_to_delete.append(absolute)

        print("Files to delete before migration ... " + str(len(files_to_delete)))

        if len(files_to_delete) > 0:
            for file in files_to_delete:
                print(file)

            delete = input("Delete (y/n) ? ")
            if delete == "yes" or delete == "y":
                for file in files_to_delete:
                    remove(file)

    def fill_static(self):
        print("Copying ...")

        for path in STATICS_SRC:
            src = self.src_path + "/" + path
            dest = self.dest_path + "/" + path

            
            copyfile(src, dest)
            print(path)

        print("Migration successfull.")

    def copy_html(self):
        print("WARNING: Don't copy html if you already have templates in your django project.")
        aw = input("Copy html files too (yes/n) ? ")

        if aw == "yes" or aw == "y" :

            count = 0
            for file in listdir(self.src_path):
                if Path(file).suffix == '.html':
                    src = self.src_path + "/" + file
                    dest = self.html_dest_path + "/" + file

                    print(src)

                    copyfile(src, dest )
                    count += 1

            print("Html files copied :" + str(count))
            

migr = migration()