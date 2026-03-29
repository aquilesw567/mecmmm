class CodeEditor:
    def __init__(self):
        self.code = ""

    def edit(self, new_code):
        self.code = new_code

    def get_code(self):
        return self.code

    def clear_code(self):
        self.code = ""

    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(self.code)