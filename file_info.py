import shutil
import os

def get_procent(size):
    return size / shutil.disk_usage("/").total * 100

class my_file:
    def __init__(self, file, level):
        self.time = os.path.getmtime(file)
        self.author = os.stat(file).st_uid
        self.level = level
        self.extension = file.split('.')[-1]
        self.size = os.path.getsize(file)
        self.procent = get_procent(self.size)
        # self.is_file = False
        # self.is_folder = False


class folder:
    def __init__(self, folder, level):
        self.time = os.path.getmtime(folder)
        self.author = os.stat(folder).st_uid
        self.level = level
        #self.files_number = len(folder)
        self.size = self.get_size(folder)
        self.procent = get_procent(self.size)

    def get_size(self, folder_path):
        size = 0
        for ele in os.scandir(folder_path):
            size += os.path.getsize(ele)
        return size
        # self.is_file = False
        # self.is_folder = False