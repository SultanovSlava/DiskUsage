import os
import files_walking
import output
path = r'C:\Users\sulta\OneDrive\Документы\READy'
files_and_dirs = os.listdir(path)
# level = 3#int(input())



w = files_walking.files_walking()
w.walking(r'C:\Users\sulta\OneDrive\Документы')
level_files_and_dirs = w.level_files_and_dirs[path]
print('!')
output.output(level_files_and_dirs)

