"""
VectorZip Test Suite
--------------------
Verifies the integrity of the VectorZip compression pipeline.
"""

import unittest
import tempfile
import os
import shutil

# Importing from the VectorZip package
from VectorZip.compressor import compress_file, decompress_file
from VectorZip.lz77 import lz77_compress
from VectorZip.huffman import huffman_encode

class TestCompression(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test artifacts
        self.test_dir = tempfile.mkdtemp()
        self.input_path = os.path.join(self.test_dir, "input.txt")
        self.test_content = b"This is a test file for compression." * 100
        
        with open(self.input_path, 'wb') as f:
            f.write(self.test_content)
    
    def tearDown(self):
        # Clean up the entire temporary directory
        shutil.rmtree(self.test_dir)
    
    def test_lz77_compression(self):
        """Verify LZ77 produces expected output for simple patterns."""
        compressed = lz77_compress(b"aaaaaaa")
        # Ensure output is a byte sequence
        self.assertTrue(isinstance(compressed, bytes))
        self.assertGreater(len(compressed), 0)
    
    def test_huffman_encoding(self):
        """Verify Huffman encoding produces valid structures."""
        encoded, padding, table = huffman_encode(b"aaabbbcc")
        self.assertTrue(isinstance(encoded, bytes))
        self.assertTrue(isinstance(padding, int))
        self.assertTrue(isinstance(table, dict))
    
    def test_file_compression_pipeline(self):
        """Verify the full round-trip: Compress -> Decompress -> Validate."""
        # 1. Compress
        compressed_path = compress_file(self.input_path)
        self.assertTrue(os.path.exists(compressed_path))
        
        # 2. Decompress
        # Note: We will implement decompress_file fully in the next step
        decompressed_path = decompress_file(compressed_path)
        
        # 3. Validate
        with open(decompressed_path, 'rb') as f:
            decompressed_content = f.read()
        
        self.assertEqual(decompressed_content, self.test_content)

if __name__ == '__main__':
    unittest.main()
