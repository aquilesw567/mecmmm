import git

class VersionControl:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = git.Repo(repo_path)

    def commit_changes(self, message):
        self.repo.git.add(A=True)  # Add all changes to staging
        self.repo.index.commit(message)  # Commit changes with message

    def push_changes(self, branch='main'):
        origin = self.repo.remote(name='origin')
        origin.push(branch)  # Push changes to the specified branch

    def pull_changes(self, branch='main'):
        origin = self.repo.remote(name='origin')
        origin.pull(branch)  # Pull changes from the specified branch

# Example usage:
# vc = VersionControl('/path/to/repo')
# vc.commit_changes('Commit message')
# vc.push_changes()