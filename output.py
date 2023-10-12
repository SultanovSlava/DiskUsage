def output(level_files_and_dirs):
    print('Name:  ', 'Size:  ', 'Time:  ')
    for f in level_files_and_dirs:
        print()
        print(f.name, f.size, f.time)