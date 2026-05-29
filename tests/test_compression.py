import os
import unittest
from src.compressor import compress_file, decompress_file

class TestVectorZip(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_data.txt"
        with open(self.test_file, "w") as f:
            f.write("VectorZip - " * 1000)

    def test_full_cycle(self):
        compressed = compress_file(self.test_file)
        restored = decompress_file(compressed)
        
        with open(self.test_file, "rb") as f1, open(restored, "rb") as f2:
            self.assertEqual(f1.read(), f2.read(), "Restored file content does not match original!")

    def tearDown(self):
        for f in [self.test_file, self.test_file + ".vzip", self.test_file.replace(".txt", ".restored")]:
            if os.path.exists(f): os.remove(f)

if __name__ == "__main__":
    unittest.main()
