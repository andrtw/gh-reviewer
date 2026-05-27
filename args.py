import argparse

import update_reviewer
from utils import logger


def setup_argparse():
    parser = argparse.ArgumentParser(
        description="Fuzzy find reviewers and add/remove them to/from a pull request",
    )
    subparsers = parser.add_subparsers(required=True)

    __add_add_reviewer_parser(subparsers)
    __add_remove_reviewer_parser(subparsers)

    args = parser.parse_args()
    logger.debug(args)
    args.func(args)


def __add_add_reviewer_parser(subparsers: argparse._SubParsersAction):
    add_subparser = subparsers.add_parser(
        "add",
        help="add reviewer(s)",
    )
    add_subparser.add_argument(
        "number",
        nargs="?",
        help="pull request number. If empty, the reviewer(s) are added to the pull request that belongs to the current branch",
    )
    add_subparser.set_defaults(func=update_reviewer.add_reviewer)


def __add_remove_reviewer_parser(subparsers: argparse._SubParsersAction):
    rm_subparser = subparsers.add_parser(
        "rm",
        help="remove reviewer(s)",
    )
    rm_subparser.add_argument(
        "number",
        nargs="?",
        help="pull request number. If empty, the reviewer(s) are removed from the pull request that belongs to the current branch",
    )
    rm_subparser.set_defaults(func=update_reviewer.rm_reviewer)
