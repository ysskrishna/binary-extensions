import pytest
from binaryextensions import (
    BINARY_EXTENSIONS,
    is_binary_extension,
    is_binary_path,
)


class TestBinaryExtensions:
    """Test the BINARY_EXTENSIONS constant."""

    def test_binary_extensions_is_frozenset(self):
        """Test that BINARY_EXTENSIONS is a frozenset."""
        assert isinstance(BINARY_EXTENSIONS, frozenset)

    def test_binary_extensions_not_empty(self):
        """Test that BINARY_EXTENSIONS contains extensions."""
        assert len(BINARY_EXTENSIONS) > 0

    def test_common_binary_extensions_present(self):
        """Test that common binary extensions are present."""
        common_extensions = ["png", "jpg", "gif", "pdf", "zip", "mp3", "mp4"]
        for ext in common_extensions:
            assert ext in BINARY_EXTENSIONS, f"{ext} should be in BINARY_EXTENSIONS"


class TestIsBinaryExtension:
    """Test the is_binary_extension function."""

    def test_known_binary_extensions(self):
        """Test that known binary extensions return True."""
        binary_exts = ["png", "jpg", "gif", "pdf", "zip", "mp3", "mp4", "exe", "dll"]
        for ext in binary_exts:
            assert is_binary_extension(ext) is True, f"{ext} should be binary"

    def test_extension_with_dot(self):
        """Test that extensions with leading dot work correctly."""
        assert is_binary_extension(".png") is True
        assert is_binary_extension(".jpg") is True
        assert is_binary_extension(".txt") is False

    def test_case_insensitive(self):
        """Test that the function is case-insensitive."""
        assert is_binary_extension("PNG") is True
        assert is_binary_extension("Png") is True
        assert is_binary_extension("pNg") is True
        assert is_binary_extension("JPG") is True
        assert is_binary_extension("PDF") is True

    def test_non_binary_extensions(self):
        """Test that non-binary extensions return False."""
        text_exts = ["txt", "md", "py", "js", "html", "css", "json", "xml"]
        for ext in text_exts:
            assert is_binary_extension(ext) is False, f"{ext} should not be binary"

    def test_empty_string(self):
        """Test that empty string returns False."""
        assert is_binary_extension("") is False
        assert is_binary_extension(".") is False

    def test_unknown_extension(self):
        """Test that unknown extensions return False."""
        assert is_binary_extension("xyz") is False
        assert is_binary_extension("unknown") is False


class TestIsBinaryPath:
    """Test the is_binary_path function."""

    def test_known_binary_paths(self):
        """Test that paths with binary extensions return True."""
        binary_paths = [
            "image.png",
            "photo.jpg",
            "document.pdf",
            "archive.zip",
            "video.mp4",
            "audio.mp3",
            "program.exe",
        ]
        for path in binary_paths:
            assert is_binary_path(path) is True, f"{path} should be binary"

    def test_case_insensitive_paths(self):
        """Test that paths are case-insensitive."""
        assert is_binary_path("IMAGE.PNG") is True
        assert is_binary_path("Photo.JPG") is True
        assert is_binary_path("Document.PDF") is True
        assert is_binary_path("file.TXT") is False

    def test_paths_with_directories(self):
        """Test that paths with directories work correctly."""
        assert is_binary_path("/path/to/image.png") is True
        assert is_binary_path("folder/subfolder/file.jpg") is True
        assert is_binary_path("C:\\Users\\file.pdf") is True
        assert is_binary_path("/path/to/document.txt") is False

    def test_non_binary_paths(self):
        """Test that paths with non-binary extensions return False."""
        text_paths = [
            "readme.txt",
            "script.py",
            "style.css",
            "index.html",
            "data.json",
            "config.xml",
        ]
        for path in text_paths:
            assert is_binary_path(path) is False, f"{path} should not be binary"

    def test_paths_without_extension(self):
        """Test that paths without extensions return False."""
        assert is_binary_path("file") is False
        assert is_binary_path("path/to/file") is False
        assert is_binary_path("/absolute/path/file") is False

    def test_paths_with_multiple_dots(self):
        """Test that paths with multiple dots work correctly."""
        assert is_binary_path("file.backup.zip") is True
        assert is_binary_path("archive.tar.gz") is True
        assert is_binary_path("file.name.txt") is False

    def test_empty_path(self):
        """Test that empty path returns False."""
        assert is_binary_path("") is False

    def test_paths_with_only_dot(self):
        """Test edge cases with dots."""
        assert is_binary_path(".") is False
        assert is_binary_path("..") is False
        assert is_binary_path("file.") is False

    def test_hidden_files(self):
        """Test hidden files (starting with dot)."""
        # Files starting with dot that have extensions work correctly
        assert is_binary_path(".hidden.png") is True
        assert is_binary_path(".config.jpg") is True
        assert is_binary_path(".gitignore") is False


class TestIntegration:
    """Integration tests for both functions."""

    def test_consistency_between_functions(self):
        """Test that both functions return consistent results."""
        test_cases = [
            ("png", "file.png", True),
            ("jpg", "image.jpg", True),
            ("txt", "readme.txt", False),
            ("pdf", "document.pdf", True),
            ("py", "script.py", False),
        ]
        for ext, path, expected in test_cases:
            assert is_binary_extension(ext) == expected
            assert is_binary_path(path) == expected

    def test_all_extensions_in_set(self):
        """Test that all extensions in BINARY_EXTENSIONS are recognized."""
        for ext in BINARY_EXTENSIONS:
            assert is_binary_extension(ext) is True
            assert is_binary_path(f"file.{ext}") is True

