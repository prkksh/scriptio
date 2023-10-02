from setuptools import setup

setup(
    name='scriptio',
    version='1.0',
    description='This script will connect to open ai completions api to process a prompt',
    author='Prakash',
    author_email='jpdmprsh@gmail.com',
    packages=['scriptio'],
    install_requires=[
        'requests',
    ],
)
