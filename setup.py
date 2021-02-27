from setuptools import setup, find_packages

setup(
    name='testSetup',
    version='0.0.1',
    packages=find_packages(),
    author='Victoire Beaufils',
    author_email="victoire.beaufil@gmail.com",
    description='test',
    long_description='test test',
    include_package_data=False,
    url='http://victoirebeaufils.me',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    classifiers=[
        "Programming Language :: Python",
    ]
)