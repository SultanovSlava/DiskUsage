
import tabulate
from datetime import datetime


class outputer:
    def get_visual_procent(self, procent):
        visual = '['
        sharp_count = int(round(procent // 10))
        visual += '#' * sharp_count
        visual += ' ' * (10 - sharp_count) + ']'
        return visual

    def output(self, directory):
        data = [
            ['Name', 'Procent', 'Size/FilesNum', 'Extension', 'Time']
        ]
        all_size = sum([el.size for el in directory])
        for el in directory:
            size = str(el.size)
            if len(size) > 5:
                size = size[:-3] + 'kB'
            else:
                size += 'B'
            if el.extension == 'folder':
                size = el.files_number
            procent_size = el.get_procent(all_size)
            data.append([el.name, self.get_visual_procent(procent_size), size, el.extension,
                         datetime.fromtimestamp(el.time)])

        print(tabulate.tabulate(data))
