class ProjectSidebar:
    def __init__(self, projects):
        """Initialize the ProjectSidebar with a list of projects."""
        self.projects = projects

    def display_projects(self):
        """Display the list of projects in the sidebar."""
        for project in self.projects:
            print(f'- {project}')

    def add_project(self, project):
        """Add a new project to the sidebar."""
        self.projects.append(project)
        print(f'Project {project} added!')

    def remove_project(self, project):
        """Remove a project from the sidebar."""
        if project in self.projects:
            self.projects.remove(project)
            print(f'Project {project} removed!')
        else:
            print(f'Project {project} not found!')
