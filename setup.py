# Setting up for pypi

from setuptools import setup

setup(
    name='filetalk',
    version='0.1.0',
    packages=['your_package'],  # Replace 'your_package' with the actual package name
    entry_points={
        'console_scripts': [
            'filetalk=your_package.main:main',  # Ensure 'your_package.main:main' points to the correct location
        ],
    },
    install_requires=[
        'numpy',  # Specify package names as strings
        'sentence_transformers',  # Ensure these are the correct package names as they appear on PyPI
    ],
    python_requires='>=3.9' # Specify Python version requirement
    # Other relevant package info
)