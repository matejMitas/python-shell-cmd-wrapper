from lib.library import Library

correct_results = {
	'test_only_fixed_1': [
		['kdu_compress', '-i', 'in_file', '-o', 'out_file']
	],
	'test_only_fixed_2': [
		['kdu_compress', '-i', 'in_file', '-o', 'out_file', 'Stiles={256,256}']
	],
	'test_fixed_wget': [
		['wget', '--output-document=out.html', 'google.com'], ['wget', '--output-document=out.html', 'yahoo.com'], ['wget', '--output-document=out.html', 'bing.com']
	]
}

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


def test_only_fixed_1():
	lib = Library(blueprint='compress_libs', lib='kdu_compress')
	lib.set_fixed(input='in_file', output='out_file')
	
	handle_output(lib, test_only_fixed_1)

def test_only_fixed_2():
	lib = Library(blueprint='compress_libs', lib='kdu_compress')
	lib.set_fixed(input='in_file', output='out_file', tiles=(256,256))
	
	handle_output(lib, test_only_fixed_2)

def test_fixed_wget():
	lib = Library(blueprint='wget')
	lib.set_fixed(output='out.html')
	lib.set_variable(source=["google.com", "yahoo.com", "bing.com"])

	handle_output(lib, test_fixed_wget)

