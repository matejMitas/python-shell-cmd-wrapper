from setuptools import setup, find_packages

setup(
    name='pyshellwrapper', 
    version="0.1.0",
    description='Working with shell programs in Python made easier.',
    author='Matěj Mitaš',
    author_email='contact@matejmitas.com',
    license='MIT',
    packages=['pyshellwrapper'],
    install_requires=['jsonschema'],
)