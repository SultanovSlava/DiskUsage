import os
import file_info
class files_walking:
    def __init__(self, level = 0):
        self.level = level
    def walking(self, path):
        files_and_dirs = os.listdir(path)
        for f in files_and_dirs:  # [f for f in files_and_dirs if os.path.isfile(f)]:
            if os.path.isfile(os.path.join(path, f)):
                file = file_info.my_file(os.path.join(path, f), self.level)
                print(file.size)
            else:
                self.level += 1
                folder = file_info.folder(os.path.join(path, f), self.level)
                print('!!! : ', os.path.join(path, f))
                print(folder.size)
                self.walking(os.path.join(path, f))