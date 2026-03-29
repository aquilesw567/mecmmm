# Project Manager

"""
A project manager for organizing and managing project structure and files.
"""

class ProjectManager:
    def __init__(self, project_name):
        self.project_name = project_name
        self.files = []

    def add_file(self, file_name):
        self.files.append(file_name)
        print(f'File {file_name} added to project {self.project_name}.')

    def remove_file(self, file_name):
        if file_name in self.files:
            self.files.remove(file_name)
            print(f'File {file_name} removed from project {self.project_name}.')
        else:
            print(f'File {file_name} not found in project {self.project_name}.')

    def list_files(self):
        return self.files

# Example usage:
# pm = ProjectManager('MyProject')
# pm.add_file('file1.txt')
# pm.list_files()