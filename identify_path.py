import os

def separate(path: str, return_bool: bool = False) -> (list | bool):
    path = path.replace('" "', '"')
    paths = path.split('"')
    while True:
        try:
            paths.remove("")
        except:
            break #buat daftar untuk setiap jalur
    if return_bool:
        abs_path = False
        for path in paths:
            if os.path.isabs(path):
                abs_path = True #jika sudah ketemu meski cuman 1 maka akan dianggap ada
                break
        return abs_path
    else:
        return path