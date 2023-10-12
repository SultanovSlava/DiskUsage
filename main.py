import os
import files_walking
path = 'C:\Drivers\Cardreader'
files_and_dirs = os.listdir(path)
level = 1



w = files_walking.files_walking()
w.walking(path)
