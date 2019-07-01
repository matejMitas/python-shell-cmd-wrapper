"""
Functional testing
"""

"""
Generic library imports
"""
from pyshellwrapper.wrapper import PyShellWrapper as Library
import pytest

"""
Since 'construct()' is a generator results is always 2D list
even for single item
"""
correct_results = {
	'test_only_fixed_1': [
		['kdu_compress', '-i', 'in_file', '-o', 'out_file']
	],
	'test_only_fixed_2': [
		['kdu_compress', '-i', 'in_file', '-o', 'out_file', 'Stiles={256,256}']
	],
	'test_variable_wget': [
		['wget', '--output-document=out.html', 'google.com'], ['wget', '--output-document=out.html', 'yahoo.com'], ['wget', '--output-document=out.html', 'bing.com']
	],
	'test_fixed_wget': [
		['wget', '--output-document=out.html', 'google.com']
	]
}

@pytest.fixture
def wget():
	return Library(blueprint='wget')

@pytest.fixture
def kdu_compress():
	return Library(blueprint='compress_libs', lib='kdu_compress')

def get_res(fn_name):
	try:
		return correct_results[fn_name]
	except KeyError:
		pass

def handle_output(lib, fn_name):
	it = lib.construct()
	it_list = []

	for item in it:
		it_list.append(item)

	assert it_list == get_res(fn_name.__name__)


def test_only_fixed_1(kdu_compress):
	kdu_compress.set_fixed(input='in_file', output='out_file')
	handle_output(kdu_compress, test_only_fixed_1)

def test_only_fixed_2(kdu_compress):
	kdu_compress.set_fixed(input='in_file', output='out_file', tiles=(256,256))
	handle_output(kdu_compress, test_only_fixed_2)

def test_variable_wget(wget):
	wget.set_fixed(output='out.html')
	wget.set_variable(source=['google.com', 'yahoo.com', 'bing.com'])

	handle_output(wget, test_variable_wget)

def test_fixed_wget(wget):
	wget.set_fixed(output='out.html', source='google.com')

	handle_output(wget, test_fixed_wget)

