from lib.library import Library

correct_results = {
	'test_only_fixed_1': ['kdu_compress', '-i', 'in_file', '-o', 'out_file'],
	'test_only_fixed_2': ['kdu_compress', '-i', 'in_file', '-o', 'out_file', 'Stiles={256,256}']
}

def get_res(fn_name):
	return correct_results[fn_name]


def test_only_fixed_1():
	lib = Library(blueprint='compress_libs', lib='kdu_compress')
	lib.set_fixed(input='in_file', output='out_file')
	assert lib.construct() == get_res('test_only_fixed_1')

def test_only_fixed_2():
	lib = Library(blueprint='compress_libs', lib='kdu_compress')
	lib.set_fixed(input='in_file', output='out_file', tiles=(256,256))
	assert lib.construct() == get_res('test_only_fixed_2')
