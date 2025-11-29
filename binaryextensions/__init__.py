import os.path
from binaryextensions._data import BINARY_EXTENSIONS

__all__ = ["BINARY_EXTENSIONS", "is_binary_extension", "is_binary_path"]

def is_binary_extension(ext: str) -> bool:
    """
    Return True if the given file extension is known to be binary.

    Examples:
        >>> is_binary_extension("png")
        True
        >>> is_binary_extension(".txt")
        False
    """
    return ext.lower().lstrip(".") in BINARY_EXTENSIONS

def is_binary_path(file_path: str) -> bool:
    """
    Return True if the file path has a binary file extension.

    Examples:
        >>> is_binary_path("image.png")
        True
        >>> is_binary_path("document.txt")
        False
        >>> is_binary_path("/path/to/file.JPG")
        True
    """
    _, ext = os.path.splitext(file_path)
    return ext.lstrip(".").lower() in BINARY_EXTENSIONS
