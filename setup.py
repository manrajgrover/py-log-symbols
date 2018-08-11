import sys

from setuptools import setup, find_packages  # pylint: disable=no-name-in-module,import-error

install_requires = []

# Python < 3.4 doesn't have enum34
if sys.version_info[0:2] < (3, 4):
    install_requires = ['enum34==1.1.6']


def dependencies(file):
    with open(file) as f:
        return f.read().splitlines()


setup(
    name='log_symbols',
    packages=find_packages(exclude=('tests', 'examples')),
    version='0.0.13',
    license='MIT',
    description='Colored symbols for various log levels for Python',
    long_description='Colored symbols for various log levels for Python. Find the documentation here: https://github.com/manrajgrover/py-log-symbols.',
    author='Manraj Singh',
    author_email='manrajsinghgrover@gmail.com',
    url='https://github.com/manrajgrover/py-log-symbols',
    keywords=[
        'log symbols',
        'symbols',
        'log'
    ],
    install_requires=dependencies('requirements.txt') + install_requires,
    tests_require=dependencies('requirements-dev.txt'),
    include_package_data=True
)
