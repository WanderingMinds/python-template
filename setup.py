from setuptools import find_packages, setup

setup(
    name='mysrc',
    packages=find_packages(include=['src']),
    version='0.1.0',
    description='Demo of a python package',
    author='Andreas Putz',
    license='MIT',
)