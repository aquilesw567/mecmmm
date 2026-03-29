import subprocess

class Terminal:
    @staticmethod
    def execute_command(command):
        """Executes a command in the shell and returns the output."""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout, result.stderr
        except Exception as e:
            return None, str(e)
