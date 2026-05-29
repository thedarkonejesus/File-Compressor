from setuptools import setup, find_packages

setup(
    name="VectorZip",
    version="1.0.0",
    description="A high-performance, chunked-processing compression utility.",
    author="VectorZip Developer",
    packages=find_packages(),
    install_requires=[
        "tqdm>=4.60.0",
    ],
    entry_points={
        'console_scripts': [
            'vzip=main:main',
        ],
    },
    python_requires='>=2.7',
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
)
