import platform

if platform.system() == "Windows":
    before_symbol = "/"
    after_symbol = "\\"
elif platform.system() == "Linux":
    before_symbol = "\\"
    after_symbol = "/"


path = "Paths"+after_symbol