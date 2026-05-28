import subprocess

DEPS = ["fzf"]


def check_dependencies() -> list[str]:
    """
    Returns a list containing the names of the missing required executables,
    or an empty list if all the required dependencies are installed.
    """
    return [d for d in DEPS if __which(d).returncode == 1]


def __which(arg: str) -> subprocess.CompletedProcess:
    return subprocess.run(["which", arg], stdout=subprocess.PIPE)
