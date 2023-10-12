import os
import file_info
class files_walking:
    def __init__(self, level = 0):
        self.level = level
        self.level_files_and_dirs = dict()

    def walking(self, path):
        if len(self.level_files_and_dirs) == self.level:
            self.level_files_and_dirs[path] = []
        files_and_dirs = os.listdir(path)
        for f in files_and_dirs:  # [f for f in files_and_dirs if os.path.isfile(f)]:
            if os.path.isfile(os.path.join(path, f)):
                file = file_info.my_file(os.path.join(path, f), self.level)
                self.level_files_and_dirs[path].append(file)
                # print(file.size)
            else:

                folder = file_info.folder(os.path.join(path, f), self.level)
                self.level_files_and_dirs[path].append(folder)
                # print('!!! : ', os.path.join(path, f))
                # print(folder.size)
                self.level += 1
                self.walking(os.path.join(path, f))

