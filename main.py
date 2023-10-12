import os
import files_walking
import output
path = 'C:\Drivers\Cardreader'
files_and_dirs = os.listdir(path)
level = 3#int(input())



w = files_walking.files_walking()
w.walking('C:\Drivers')
level_files_and_dirs = w.level_files_and_dirs[path]
output.output(level_files_and_dirs)

