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

"""
Fixed flags
"""

def test_no_flag(wget):
	with pytest.raises(KeyError):
		wget.set_fixed(no_existent_flag=True)

def test_multiple_fixed(wget):
	with pytest.raises(ValueError):
		wget.set_fixed(source='google.com')
		wget.set_fixed(source='google.com')

"""
Faulty commands
"""
def test_command_wrong_index():
	with pytest.raises(IndexError):
		lib = Library(blueprint='compress_libs', command=8)

def test_command_wrong_type():
	with pytest.raises(TypeError):
		lib = Library(blueprint='compress_libs', command=1.7)

def test_command_wrong_negative_index():
	with pytest.raises(IndexError):
		lib = Library(blueprint='compress_libs', command=-1)

def test_command_wrong_wrong_name():
	with pytest.raises(ValueError):
		lib = Library(blueprint='compress_libs', command="das")
