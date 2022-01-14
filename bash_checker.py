
import os
import subprocess


def check_bash_command_exists_single(command: str) -> None:
    """
    Checks if a bash command exists.
    """
    subprocess.check_output([command, '--version'])


def check_bash_command_exists(command: list) -> None:
    """
    Checks if a bash command exists.
    """
    for cmd in command:
        check_bash_command_exists_single(cmd)
