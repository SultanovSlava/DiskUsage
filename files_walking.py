import os
import file_info
class files_walking:
    def __init__(self, level=0):
        self.cur_level = level
        self.level_files_and_dirs = dict()

    def walking(self, path):
        self.level_files_and_dirs[path] = []
        try:
            files_number = 0
            files_and_dirs = os.listdir(path)
            for f in files_and_dirs:  # [f for f in files_and_dirs if os.path.isfile(f)]:
                if os.path.isfile(os.path.join(path, f)):
                    file = file_info.my_file(os.path.join(path, f), self.cur_level)
                    # print(file.name)
                    self.level_files_and_dirs[path].append(file)
                    # print(file.size)
                    files_number += 1
                else:

                    folder = file_info.folder(os.path.join(path, f), self.cur_level)
                    # print(folder.name)
                    self.level_files_and_dirs[path].append(folder)
                    # print('!!! : ', os.path.join(path, f))
                    # print(folder.size)
                    self.cur_level += 1
                    folder.files_number += self.walking(os.path.join(path, f))
                    files_number += folder.files_number

            return files_number
        except PermissionError as e:
            print(f"Error: {e} in {path}. It was ignored")
            self.level_files_and_dirs[path] = f"Error: {e} in {path}. It was ignored"
