from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension("src.lz77_fast", ["src/lz77_fast.pyx"], include_dirs=[np.get_include()])
]

setup(ext_modules=cythonize(extensions))
