from setuptools import setup, find_packages

setup(
    name="VectorZip",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],  # Add dependencies like 'pytest' here if needed
    author="Your Name",
    description="A high-performance LZ77 + Huffman compression engine",
    entry_points={
        'console_scripts': [
            'vzip=main:main',
        ],
    },
)
