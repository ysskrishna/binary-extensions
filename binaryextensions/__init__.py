from binaryextensions._data import BINARY_EXTENSIONS

__all__ = ["BINARY_EXTENSIONS", "is_binary_extension"]

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
