import os
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = abspath(dirname(__file__))
os.chdir(HERE)  # allow setup.py to be run from any path

try:
    # Use pypandoc to convert Markdown to RST; Markdown is not supported on PyPI
    import pypandoc
    print("Converting README.md to RST")
    README = pypandoc.convert(join(HERE, 'README.md'), 'rst')
except(IOError, ImportError):
    print("Markdown unsupported by PyPI, README.md will be plain-text.")
    print("Recommend installing pypandoc.")
    with open(join(HERE, 'README.md')) as readme:
        README = readme.read()

with open(join(HERE, 'requirements.txt')) as requirements:
    REQUIREMENTS = list(requirements.readlines())

setup(
    name='django-realme',
    version='1.0',
    packages=find_packages(exclude=('samples', 'example')),
    include_package_data=True,
    description='A Django app client for the RealMe service',
    long_description=README,
    url='https://github.com/catalyst/django-realme',
    author='Catalyst IT',
    author_email='pypi@catalyst.net.nz',
    license='GPL',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=REQUIREMENTS,
)
