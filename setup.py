from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'Switch kubernetes namespace'
LONG_DESCRIPTION = 'A package that allows to switch kubernetes namespaces easily.'

# Setting up
setup(
    name="ksns",
    version=VERSION,
    py_modules=['ksns'],
    include_package_data=True,
    author="Ratul Basak",
    author_email="ratulbasak93@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/ratulbasak/ksns",
    packages=find_packages(),
    install_requires=['click', 'kubernetes', 'PyYAML', 'requests'],
    entry_points='''
        [console_scripts]
        ksns=ksns.cli:main
    ''',
    keywords=['python', 'kubernetes', 'namespace', 'switch namespace', 'k8s', 'package'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)