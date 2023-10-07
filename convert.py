import base64
def make(stri: str):
    stri = base64.b64encode(stri.encode()).decode()
    return stri

def read(stri: str):
    stri = base64.b64decode(stri.encode()).decode()
    return stri
