import subprocess

class ShellCommand:
    description = "Used to execute local commands."
    public_description = "Execute local commands."
    arg_description = (
        "The input should be a command. "
        "This should be executed by the AI. "
        "commands, shell, output"
    )
    image_url = "/tools/shell.png"
    """
    Allows to execute local commands.
    """
    @staticmethod
    def execute_command(command: str) -> str:
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f"Error executing command: {e.output.decode('utf-8')}"


