# Binary Extensions

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Tests](https://github.com/ysskrishna/binary-extensions/actions/workflows/test.yml/badge.svg)

Python port of the popular [binary-extensions](https://github.com/sindresorhus/binary-extensions) npm package: check, classify, and iterate over binary file extensions.

## Features

- ✅ Check if a file extension is binary
- ✅ Check if a file path has a binary extension
- ✅ Access to a comprehensive list of binary extensions
- ✅ Case-insensitive matching
- ✅ Handles extensions with or without leading dots
- ✅ Type hints included
- ✅ Zero dependencies

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
from binaryextensions import is_binary_extension

# Returns True for binary extensions
is_binary_extension("png")      # True
is_binary_extension(".jpg")     # True
is_binary_extension("PDF")      # True (case-insensitive)
```

### Check if a file path has a binary extension

```python
from binaryextensions import is_binary_path

# Returns True for binary files
is_binary_path("image.png")                    # True
is_binary_path("/path/to/file.JPG")            # True (case-insensitive)
is_binary_path("document.pdf")                 # True
```

### Access the list of binary extensions

```python
from binaryextensions import BINARY_EXTENSIONS

# BINARY_EXTENSIONS is a frozenset of all known binary extensions
print(len(BINARY_EXTENSIONS))  # Number of supported extensions
"png" in BINARY_EXTENSIONS     # True
"txt" in BINARY_EXTENSIONS     # False
```

## Supported Extensions

The package includes support for hundreds of binary file extensions, including:

- **Images**: png, jpg, gif, bmp, webp, svg, ico, and more
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


## Support

If you find this library useful, please consider:

- ⭐ **Starring** the repository on GitHub to help others discover it.
- 💖 **Sponsoring** to support ongoing maintenance and development.

[Become a Sponsor on GitHub](https://github.com/sponsors/ysskrishna) | [Support on Patreon](https://patreon.com/ysskrishna)

## License

MIT License - see [LICENSE](https://github.com/ysskrishna/binary-extensions/blob/main/LICENSE) file for details.


## Author

**Y. Siva Sai Krishna**

- GitHub: [@ysskrishna](https://github.com/ysskrishna)
- LinkedIn: [ysskrishna](https://linkedin.com/in/ysskrishna)

