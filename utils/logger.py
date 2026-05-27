DEBUG = True


def debug(*values):
    if not DEBUG:
        return
    print("D | ", end="")
    print(*values)
