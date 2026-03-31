Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # tests/test_compression.py
import unittest
import tempfile
import os
from src.compressor import compress_file, decompress_file

class TestCompression(unittest.TestCase):
    def setUp(self):
        # Create temporary files for testing
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_content = b"This is a test file for compression.\n" * 100
        self.test_file.write(self.test_content)
        self.test_file.close()
    
    def tearDown(self):
        # Clean up temp files
        os.unlink(self.test_file.name)
        if hasattr(self, 'compressed_file'):
            os.unlink(self.compressed_file)
        if hasattr(self, 'decompressed_file'):
            os.unlink(self.decompressed_file)
    
    def test_lz77_compression(self):
        """Test LZ77 compression works correctly"""
        # Test basic functionality
        compressed = lz77_compress(b"aaaaaaa")
        self.assertEqual(compressed, b"\x00\x00\x07a")
        
        # Test edge cases
        self.assertEqual(lz77_compress(b""), b"")
        self.assertEqual(lz77_compress(b"a"), b"a")
    
    def test_huffman_encoding(self):
        """Test Huffman encoding works correctly"""
        # Test basic functionality
        encoded, padding, table = huffman_encode(b"aaabbbcc")
        self.assertTrue(isinstance(encoded, bytes))
        self.assertTrue(isinstance(padding, int))
        self.assertTrue(isinstance(table, dict))
        
        # Test round-trip
        decoded = huffman_decode(encoded, padding, table)
        self.assertEqual(decoded, b"aaabbbcc")
    
    def test_file_compression(self):
        """Test full file compression pipeline"""
        # Compress file
        self.compressed_file = compress_file(self.test_file.name)
        
        # Verify compressed file exists
        self.assertTrue(os.path.exists(self.compressed_file))
        
        # Decompress file
        self.decompressed_file = decompress_file(self.compressed_file)
        
        # Verify decompressed content matches original
        with open(self.decompressed_file, 'rb') as f:
            decompressed = f.read()
        self.assertEqual(decompressed, self.test_content)
    
    def test_empty_file(self):
        """Test compression of empty files"""
        empty_file = tempfile.NamedTemporaryFile(delete=False)
        empty_file.close()
        
        try:
            compressed = compress_file(empty_file.name)
            decompressed = decompress_file(compressed)
            
            with open(decompressed, 'rb') as f:
                self.assertEqual(f.read(), b"")
        finally:
            os.unlink(empty_file.name)
            os.unlink(compressed)
            os.unlink(decompressed)

if __name__ == '__main__':
    unittest.main()
