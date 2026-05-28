from pathlib import Path

GIT_DIR = Path(".git")


def is_git_repo() -> bool:
    return GIT_DIR.exists()
