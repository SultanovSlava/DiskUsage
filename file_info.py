import shutil
import os

def get_procent(size):
    return size / shutil.disk_usage("/").total * 100

class my_file:
    def get_size(self, folder_path):
        try:
            size = 0
            for ele in os.scandir(folder_path):
                size += os.path.getsize(ele)
            return size
            # self.is_file = False
            # self.is_folder = False
        except PermissionError:
            return -5

    def __init__(self, file):
        self.name = file.split("\\")[-1]
        self.path = file
        self.time = os.path.getctime(file)
        self.author = os.stat(file).st_uid
        self.nesting_level = 0
        self.files_number = 0
        if os.path.isfile(file):
            self.extension = file.split('.')[-1]
            self.size = os.path.getsize(file)
        else:
            self.size = self.get_size(file)
            self.extension = 'folder'
        self.procent = get_procent(self.size)


