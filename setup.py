from setuptools import find_packages, setup

setup(
    name='langprobe',
    packages=find_packages(exclude=['tests']),
    version='0.0.1',
    description='A small library made for LabV2 shenanigans',
    author='cheese-research',
    license='BSD 3-clause'
)
