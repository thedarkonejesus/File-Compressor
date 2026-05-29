"""
VectorZip Engine
----------------
A high-performance hybrid compression library.
Combines LZ77 sliding window dictionary matching with Huffman entropy coding.

Usage:
    from VectorZip import compress_file

Attributes:
    __version__ (str): 1.0.0
"""

from .lz77 import lz77_compress
from .huffman import huffman_encode
from .compressor import compress_file

# Public API Surface
__all__ = [
    'lz77_compress', 
    'huffman_encode', 
    'compress_file'
]

__version__ = '1.0.0'
