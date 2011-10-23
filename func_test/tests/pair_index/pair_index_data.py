
def url(path):
    full_path = "http://localhost:8000" + path
    if not full_path.endswith("/"):
        full_path += "/"
    return full_path
PAIR_STAIR_PAGE = url('/pair/')


