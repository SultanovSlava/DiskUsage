import os
import file_info
class files_walking:
    def __init__(self, level=0):
        self.cur_level = level
        self.level_files_and_dirs = dict()

    def walking(self, path):
        self.level_files_and_dirs[path] = []
        self.cur_level += 1
        cur_level = 0
        level = 0
        try:
            files_number = 0
            files_and_dirs = os.listdir(path)
            for f in files_and_dirs:
                file = file_info.my_file(os.path.join(path, f))
                self.level_files_and_dirs[path].append(file)

                if os.path.isfile(os.path.join(path, f)):
                    files_number += 1
                    self.cur_level = 0
                else:
                    prev_files_number, cur_level = self.walking(os.path.join(path, f))
                    file.files_number += prev_files_number
                    files_number += file.files_number
                    cur_level += 1
                    file.level = max(cur_level, file.level)
                level = max(level, cur_level)
            return files_number, level
        except PermissionError as e:
            print(f"Error: {e} in {path}. It was ignored")
            self.level_files_and_dirs[path] = f"Error: {e} in {path}. It was ignored"
