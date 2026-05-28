import subprocess
from argparse import Namespace
from typing import Callable

from utils import gh, git, logger

GH_ADD_REVIEWER_FLAG = "--add-reviewer"
GH_REMOVE_REVIEWER_FLAG = "--remove-reviewer"


def add_reviewer(args: Namespace):
    __update_reviewer(
        args,
        lambda num, members: gh.edit_pr(num, GH_ADD_REVIEWER_FLAG, members),
    )


def rm_reviewer(args: Namespace):
    __update_reviewer(
        args,
        lambda num, members: gh.edit_pr(num, GH_REMOVE_REVIEWER_FLAG, members),
    )


def __update_reviewer(args: Namespace, updater: Callable[[str, str], None]):
    if not git.is_git_repo():
        print("Not a git repository")
        return

    members = __get_members()
    logger.debug(f"Got {len(members)} members")
    if not members:
        return

    selected = __fzf_members(members)
    logger.debug(f"Selected {selected}")
    if not selected:
        return

    num = args.number or ""
    members_param = ",".join(selected)
    updater(num, members_param)


def __get_members() -> list[str]:
    try:
        members_json = gh.api_paginated("orgs/{owner}/members")
        return [m["login"] for m in members_json]
    except gh.ApiError as e:
        print(f"Error fetching members: {e}")
        return []


def __fzf_members(members: list[str]) -> list[str]:
    members_list = "\n".join(members)
    selected_res = subprocess.run(
        ["fzf", "-m"],
        input=members_list.encode(),
        stdout=subprocess.PIPE,
    )
    selected = selected_res.stdout.decode()
    return [s.strip() for s in selected.split("\n") if s]
