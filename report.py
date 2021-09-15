class Report:
    def __init__(self, name: str):
        self.name = name
        self.__all_line = []

    def create_txt_report(self):
        self.name += '.txt'
        f = open(self.name, 'w')
        f.write(self.name.upper()[:-4] + '\n\n')
        f.close()

    def add_text_block(self, name: str, *args):
        self.__all_line.append(name + '\n\n')
        for string in args:
            self.__all_line.append(str(string) + '\n')
        self.__all_line.append('---------------------\n\n')
        print(self.__all_line)

    def insert_all_line(self, mode:str):
        with open(self.name, mode) as f:
            for line in self.__all_line:
                f.write(line)
