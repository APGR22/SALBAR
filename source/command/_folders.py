import os

def make_directories(s: str, d: str) -> tuple[list[str], list[str]]:
    path_s = []
    only_path_s = []
    path_d = []
    only_path_d = []

    len_s = len(s)

    for path, folders, files in os.walk(s): #cari semua jalur file di dalam folder
        if path[len_s:] == "":
            path = s
        else:
            path = path[len_s:]

        if folders == [] and files == []: #jika suatu folder kosong (tidak ada file dan folder)
            #daftarkan hanya path (sama saja dengan memindahkan folder)
            only_path_s.append(path)
        else:
            for file in files:
                path_s.append(os.path.join(path, file)) #daftarkan setiap jalur file
                only_path_s.append(path)

    for path in path_s:
        path_d.append(os.path.join(d, path[len_s+1:])) #hasil #panjangnya akan sama

    #pisahkan agar ketika kedua panjang list tidak sama maka tidak akan terganggu
    for only_path in only_path_s:
        if only_path[len_s:] == "":
            only_path_d.append(d)
        else:
            only_path_d.append(os.path.join(d, only_path)) #hasil #panjangnya akan sama

    for path in only_path_d:
        try:
            os.makedirs(path)
        except FileExistsError:
            pass

    return path_s, path_d