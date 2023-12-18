import tabulate
from datetime import datetime

class outputer:
    def output(self, directory):
        data = [
            ['Name', ' ', 'Size/FilesNum', 'Extension', 'Author', 'Time']
        ]
        for el in directory:
            size = str(el.size) + 'b'
            if el.extension == 'folder':
                size = el.files_number
            data.append([el.name, 0, size, el.extension, el.author, datetime.fromtimestamp(el.time)])

        print(tabulate.tabulate(data))