from outputing import outputer
from catalog_filter import catalog_filter
from files_walking import files_detector


class command_line:
    def __init__(self):
        self.files_detector = files_detector()
        self.catalog_filter = catalog_filter()
        self.directory = []
        self.outputer = outputer()
        self.run()

    def run(self):
        print('Input command:')

        while True:
            command = input()
            try:
                if command == 'stop':
                    print('Stop command line')
                    break
                commands = command.split()
                command_type = commands[0]
                message = commands[1]
                if command_type == 'w':
                    self.files_detector.walking(message)
                    self.directory = self.files_detector.level_files_and_dirs[message]
                    print('w Ok')
                elif command_type == 'd':
                    self.directory = self.files_detector.level_files_and_dirs[message]
                    self.catalog_filter = catalog_filter(self.directory)
                    self.outputer.output(self.directory)
                    print('d Ok')
                elif command_type == 'f':
                    if message == 'reset':
                        self.catalog_filter.reset_filter()
                        print('reset Done')
                    elif len(message) != 0:
                        key, value = message.split(':')
                        self.outputer.output(self.catalog_filter.set_filter(**{key: value}).values())
                    else:
                        print('Unknown filter message type')
                elif command_type == 'g':
                    self.outputer.output(self.catalog_filter.group_by(message))
                else:
                    print('Unknown command')
            except Exception as e:
                print(e)#'Incorrect command')