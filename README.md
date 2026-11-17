# Binary Extensions

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ysskrishna/binary-extensions/blob/main/LICENSE)
[![Tests](https://github.com/ysskrishna/binary-extensions/actions/workflows/test.yml/badge.svg)](https://github.com/ysskrishna/binary-extensions/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/binary-extensions)](https://pypi.org/project/binary-extensions/)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/binary-extensions?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/binary-extensions)
[![Author site](https://img.shields.io/badge/author-ysskrishna.space-informational)](https://ysskrishna.space)
[![Context7](https://img.shields.io/badge/Context7-docs-18181B)](https://context7.com/ysskrishna/binary-extensions)
[![Ask DeepWiki](https://img.shields.io/badge/DeepWiki-ask-18181B)](https://deepwiki.com/ysskrishna/binary-extensions)

Check if a file or extension is binary, and iterate over 250+ known binary file types including images, videos, archives, and executables. Python port of [binary-extensions](https://github.com/sindresorhus/binary-extensions) npm package.

## Features

- Immutable collection of hundreds of known binary file extensions  
- Fast membership checks using `frozenset`  
- Case-insensitive and dot-aware checks  
- Works for both extensions and full file paths  
- Supports dotfiles (e.g., `.DS_Store`)  
- Zero dependencies, minimal overhead  

## Installation

```bash
pip install binary-extensions
```

Or using `uv`:

```bash
uv add binary-extensions
```

## Usage

### Check if an extension is binary

```python
from binary_extensions import is_binary_extension

is_binary_extension("png")      # True
is_binary_extension(".jpg")     # True (dot-aware)
is_binary_extension("PDF")      # True (case-insensitive)
is_binary_extension("txt")      # False
```

### Check if a file path has a binary extension

```python
from binary_extensions import is_binary_path

is_binary_path("image.png")                    # True
is_binary_path("/path/to/file.JPG")            # True (case-insensitive)
is_binary_path("document.pdf")                 # True
is_binary_path("document.txt")                 # False
is_binary_path(".DS_Store")                     # True (dotfile support)
```

### Access the list of binary extensions

```python
from binary_extensions import BINARY_EXTENSIONS, BINARY_EXTENSIONS_LOWER

# BINARY_EXTENSIONS is a frozenset of all known binary extensions
print(len(BINARY_EXTENSIONS))  # Number of supported extensions
"png" in BINARY_EXTENSIONS     # True
"txt" in BINARY_EXTENSIONS     # False

# BINARY_EXTENSIONS_LOWER contains all extensions in lowercase
# Useful for case-insensitive lookups without calling .lower() repeatedly
"PNG" in BINARY_EXTENSIONS_LOWER  # True (case-insensitive)
```

## API Reference

Install with `pip install binary-extensions` and import from `binary_extensions`. Signatures and descriptions below match the source code of `binary_extensions`.

### `BINARY_EXTENSIONS`

Constant: `frozenset` with 262 entries.

### `BINARY_EXTENSIONS_LOWER`

Constant: `frozenset` with 262 entries.

### `is_binary_extension(ext: str) -> bool`

Return True if the given file extension is known to be binary.

**Example**

```python
from binary_extensions import is_binary_extension

is_binary_extension("png")  # True
is_binary_extension(".txt")  # False
```

### `is_binary_path(file_path: str) -> bool`

Return True if the file path has a binary file extension.

**Example**

```python
from binary_extensions import is_binary_path

is_binary_path("image.png")  # True
is_binary_path("document.txt")  # False
is_binary_path("/path/to/file.JPG")  # True
```

## Supported Extensions

The package includes support for hundreds of binary file extensions, including:

- **Images**: png, jpg, gif, bmp, webp, ico, and more
- **Audio**: mp3, wav, flac, aac, ogg, and more
- **Video**: mp4, avi, mkv, mov, webm, and more
- **Archives**: zip, tar, gz, 7z, rar, and more
- **Documents**: pdf, doc, docx, xls, xlsx, ppt, pptx, and more
- **Executables**: exe, dll, so, dmg, appimage, and more
- **Fonts**: ttf, otf, woff, woff2, and more
- And many more...


## Credits

This package is a Python port of the [binary-extensions](https://github.com/sindresorhus/binary-extensions) npm package by [Sindre Sorhus](https://github.com/sindresorhus).


## Contributing

Contributions are welcome! Please read our [Contributing Guide](https://github.com/ysskrishna/binary-extensions/blob/main/CONTRIBUTING.md) for details on our code of conduct, development setup, and the process for submitting pull requests.

## Built and maintained by

Binary Extensions is built and maintained by:

| | Name | GitHub | Role |
|---|------|--------|------|
| <img src="https://github.com/ysskrishna.png?size=120" width="60" height="60" alt="Y. Siva Sai Krishna"> | **Y. Siva Sai Krishna** | [@ysskrishna](https://github.com/ysskrishna) | Creator |

## Changelog

See [CHANGELOG](CHANGELOG.md) for release history.

## Support

If you find this library helpful:

- ⭐ Star the repository
- 🐛 [Report issues](https://github.com/ysskrishna/binary-extensions/issues)
- 🔀 Submit pull requests
- 💝 [Sponsor on GitHub](https://github.com/sponsors/ysskrishna)

## License

MIT © [Y. Siva Sai Krishna](https://github.com/ysskrishna) — see [LICENSE](LICENSE) for details.

---

<p align="left">
  <a href="https://github.com/ysskrishna">Author's GitHub</a> •
  <a href="https://linkedin.com/in/ysskrishna">Author's LinkedIn</a> •
  <a href="https://ysskrishna.space">Author's site</a> •
  <a href="https://pypi.org/project/binary-extensions/">Package on PyPI</a> •
  <a href="https://github.com/ysskrishna/binary-extensions/issues">Report Issues</a>
</p>
