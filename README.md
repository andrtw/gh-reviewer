# gh-reviewer

A [GitHub CLI](https://cli.github.com/) extension for fuzzy finding and updating pull request reviewers. The available reviewers are all the organisation’s members of the repository in the current directory.

## Installation

```sh
gh extension install andrtw/gh-reviewer
```

To upgrade to the latest version:

```sh
gh extension upgrade gh-reviewer
```

## Requirements

- [fzf](https://github.com/junegunn/fzf) to fuzzy find reviewers

## Usage

```sh
gh reviewer add     # Add reviewers to the current pull request
gh reviewer rm      # Remove reviewers from the current pull request
gh reviewer add 123 # Add reviewers to pull request 123
```
Supports multi-select mode to add/remove multiple reviewers at once. See [Using the finder](https://github.com/junegunn/fzf#using-the-finder) for guidance on how to use fzf.
