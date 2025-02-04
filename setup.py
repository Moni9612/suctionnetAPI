from distutils.core import setup
import setuptools
from setuptools import find_packages
from setuptools.command.install import install

setup(
    name='suctionnetAPI',
    version='1.0.0',
    description='suctionnet API',
    author='Hanwen Cao',
    author_email='hwcao17@gmail.com',
    url='https://graspnet.net',
    packages=find_packages(),
    install_requires=[
        'point_cloud_utils',
        'suction_nms'
    ]
)
