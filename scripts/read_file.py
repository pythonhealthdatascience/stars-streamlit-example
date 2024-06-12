import io


def read_file_contents(path):
    """
    Import local file and return as a UTF-8 string

    Parameters:
    ----------
    path: str
        e.g. file_name.md

    Returns:
    --------
    utf-8 str

    """
    file = io.open(path, mode="r", encoding="utf-8")
    return file.read()
