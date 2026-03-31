Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # src/__init__.py
from .lz77 import lz77_compress
from .huffman import huffman_encode
from .compressor import compress_file

# Define what gets imported with "from src import *"
__all__ = ['lz77_compress', 'huffman_encode', 'compress_file']

# Package version
__version__ = '1.0.0'
