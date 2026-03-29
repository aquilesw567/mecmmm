class FileManager:
    def create_file(self, file_name, content):
        with open(file_name, 'w') as file:
            file.write(content)
        print(f'File {file_name} created successfully.')

    def open_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                content = file.read()
            print(f'Content of {file_name}: \n{content}')
        except FileNotFoundError:
            print(f'File {file_name} not found.')

    def save_file(self, file_name, content):
        with open(file_name, 'w') as file:
            file.write(content)
        print(f'File {file_name} saved successfully.')

    def delete_file(self, file_name):
        import os
        try:
            os.remove(file_name)
            print(f'File {file_name} deleted successfully.')
        except FileNotFoundError:
            print(f'File {file_name} not found.')
        except PermissionError:
            print(f'Permission denied to delete {file_name}.')