import os
import files_walking
import output, filter
import calendar
import time
date = '+' + str(calendar.timegm(time.strptime('Jul 9, 2009 @ 00:00:00 UTC', '%b %d, %Y @ %H:%M:%S UTC')))
path = r'C:\Users\sulta\OneDrive\Документы\READy'
files_and_dirs = os.listdir(path)
# level = 3#int(input())



w = files_walking.files_walking()
w.walking(r'C:\Users\sulta\OneDrive\Документы')
level_files_and_dirs = w.level_files_and_dirs[path]
f = filter.filter(level_files_and_dirs)
output.output(f.set_filter(date=date, extension=['md']).values())
#output.output(level_files_and_dirs)

