import os


class MyFile:
    def get_procent(self, mother_folder_size):
        try:
            return self.size / mother_folder_size * 100
        except ZeroDivisionError:
            return 100

    def get_size(self, folder_path):
        size = 0
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for f in filenames:
                file_path = os.path.join(dirpath, f)
                if not os.path.islink(file_path):
                    size += os.path.getsize(file_path)
        return size

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
        self.procent = None
