"""
Error testing
"""

"""
Generic library imports
"""
from pyshellwrapper.wrapper import PyShellWrapper as Library
import pytest

@pytest.fixture
def wget():
	return Library(blueprint='wget')

def test_no_blueprint():
	with pytest.raises(FileNotFoundError):
		lib = Library(blueprint='lib')

def test_no_library():
	with pytest.raises(ValueError):
		lib = Library(blueprint='compress_libs')

def test_no_flag(wget):
	with pytest.raises(KeyError):
		wget.set_fixed(no_existent_flag=True)

def test_multiple_fixed(wget):
	with pytest.raises(ValueError):
		wget.set_fixed(source='google.com')
		wget.set_fixed(source='google.com')

