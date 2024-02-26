from setuptools import setup

setup(
    name='filetalk',
    version='0.1.0',
    packages=['your_package'],  # Replace 'your_package' with the actual package name
    entry_points={
        'console_scripts': [
            'filetalk=your_package.main:main',  # Ensure this points to the correct location
        ],
    },
    install_requires=[
        'numpy',
        'sentence_transformers',
    ],
    python_requires='>=3.9',  # Specify Python version requirement
    # Other relevant package info
)
