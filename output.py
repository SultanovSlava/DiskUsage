def output(level_files_and_dirs):
    print('Name:  ', 'Size:  ', 'Time:  ')
    for f in level_files_and_dirs:
        print()
        print(f.name, f.extension)
        try: print(f.files_number)
        except Exception:
            pass