# VectorZip

**VectorZip** is a high-performance, lossless file compression library that combines **LZ77** sliding window dictionary matching with **Huffman** entropy coding.



## Features
- **Hybrid Compression:** Leverages LZ77 for redundancy elimination and Huffman for optimal bit-packing.
- **Lossless:** Guarantees 100% data integrity during compression and restoration.
- **Memory-Efficient:** Optimized for low-overhead processing of binary streams.
- **Portable:** Written with strict cross-version compatibility for Python 2.7 and 3.x.
- **Developer-Friendly:** Clean API designed for both CLI and programmatic integration.

## Installation

```bash
git clone [https://github.com/thedarkonejesus/VectorZip](https://github.com/thedarkonejesus/VectorZip)
cd VectorZip
pip install .

