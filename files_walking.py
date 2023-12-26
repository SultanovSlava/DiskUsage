import os
import file_info
from alive_progress import alive_bar


class FilesDetector:
    def __init__(self, level=0):
        self.cur_level = level
        self.level_files_and_dirs = dict()
        self.total_size = 0

    def walking(self, start_path):
        self.total_size = 0
        for dirpath in os.walk(start_path):
            self.total_size += 1

        return self.walking_to_get_info(start_path)

    def walking_to_get_info(self, path):
        with alive_bar(self.total_size) as bar:
            self.walking_to_folder(path, bar)

    def walking_to_folder(self, path, bar):
        self.level_files_and_dirs[path] = []
        self.cur_level += 1
        cur_level = 0
        level = 0
        try:
            files_number = 0
            files_and_dirs = os.listdir(path)
            for f in files_and_dirs:
                file = file_info.MyFile(os.path.join(path, f))
                self.level_files_and_dirs[path].append(file)

                if os.path.isfile(os.path.join(path, f)):
                    files_number += 1
                    self.cur_level = 0
                else:
                    prev_files_number, cur_level = self.walking_to_folder(os.path.join(path, f), bar)
                    file.files_number += prev_files_number
                    files_number += file.files_number
                    cur_level += 1
                    file.nesting_level = max(cur_level, file.nesting_level)

                level = max(level, cur_level)
            bar()
            return files_number, level
        except PermissionError as e:
            print(f"Error: {e} in {path}. It was ignored")
            self.level_files_and_dirs[path] = f"Error: {e} in {path}. It was ignored"
