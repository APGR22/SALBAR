total_errors = 6

errors = {
    1: "too few arguments",
    2: "cannot open file from arguments",
    3: "cannot open source file",
    4: "cannot open destination file",
    5: "the process is stopped",
    6: "cannot delete unfinished file"
}

def identify(s: int | str | bytes) -> str:
    for i in range(total_errors):
        if i+1 in s:
            return errors[i+1]

    return "success"