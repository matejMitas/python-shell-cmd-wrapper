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
	],
	'test_output_string': [
		'kdu_compress -i in.ppm Cblk={32,64} Creversible=no Stiles={432,765}', 
		'kdu_compress -i in.ppm Cblk={32,64} Creversible=no Stiles={111,122}'
	],
	'test_simple_toggle': [
		['kdu_compress', '-rgb_to_420']
	],
	'test_simple_match': [
		['kdu_compress', 'Creversible=yes']
	],
	'test_toggle_match': [
		['opj_compress', '-I']
	]
}

@pytest.fixture
def wget():
	return Library(blueprint='wget')

@pytest.fixture
def kdu_compress():
	return Library(blueprint='compress_libs', command='kdu_compress')

@pytest.fixture
def opj_compress():
	return Library(blueprint='compress_libs', command='opj_compress')

"""
Handling assertions
"""
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

"""
General testing
"""
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

def test_custom_blueprint():
	Library(blueprint='./example_blueprint/wget_example.json')

"""
Optional parameters for main class
"""
def test_output_string():
	kdu = Library(blueprint='compress_libs', command='kdu_compress', output_format_list=False)

	kdu.set_fixed(
		input='in.ppm', 
		blocks=(32, 64),
		compression="lossy"
	)

	kdu.set_variable(tiles=[(432, 765), (111, 122)])
	handle_output(kdu, test_output_string)



"""
Toggle and toggle match
"""
def test_simple_toggle(kdu_compress):
	kdu_compress.set_fixed(
		inline_rgb_420=True
	)

	handle_output(kdu_compress, test_simple_toggle)

def test_toggle_match(opj_compress):
	opj_compress.set_fixed(
		compression="lossy"
	)

	handle_output(opj_compress, test_toggle_match)


"""
Match
"""
def test_simple_match(kdu_compress):
	kdu_compress.set_fixed(
		compression="lossless"
	)

	handle_output(kdu_compress, test_simple_match)