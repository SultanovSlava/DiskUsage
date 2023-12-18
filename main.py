import calendar
import os
import time

import files_walking
import catalog_filter
import outputing
from command_line import command_line

date = '+' + str(calendar.timegm(time.strptime('Jul 9, 2009 @ 00:00:00 UTC', '%b %d, %Y @ %H:%M:%S UTC')))
path = r'C:\Users\sulta\OneDrive\Документы\PythonTask\DiskUsage'
files_and_dirs = os.listdir(path)
# level = 3#int(input())


s = command_line()
# w = files_walking.files_detector()
# w.walking(r'C:\Users\sulta\OneDrive\Документы')
# level_files_and_dirs = w.level_files_and_dirs[path]
# f = catalog_filter.catalog_filter(level_files_and_dirs)
# output.output(f.set_filter(date=date, level='=5').values())
# output.output(f.group_by('extension'))
# output.output(level_files_and_dirs)
