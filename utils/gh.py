import json
import subprocess
from typing import Any


class ApiError(Exception):
    pass


def api_paginated(url: str) -> list[Any]:
    res = subprocess.run(
        ["gh", "api", "--paginate", url],
        stdout=subprocess.PIPE,
    )
    body = json.loads(res.stdout.decode())
    if res.returncode != 0:
        raise ApiError(body)
    return body


def edit_pr(*args: str):
    subprocess.run(["gh", "pr", "edit", *args])
