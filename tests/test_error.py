from pyshellwrapper.wrapper import PyShellWrapper as Library
import pytest


def test_no_blueprint():
	with pytest.raises(FileNotFoundError):
		lib = Library(blueprint='lib')

def test_no_library():
	with pytest.raises(ValueError):
		lib = Library(blueprint='compress_libs')