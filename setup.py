from setuptools import setup

setup(
    name='filetalk',
    version='0.1.0',
    packages=['main'], 
    package_dir={'':'src'},
    entry_points={
        'console_scripts': [
            'filetalk=src.main:main',  
        ],
    },
    install_requires=[
        'numpy',
        'sentence_transformers',
    ],
    python_requires='>=3.9',  
)

