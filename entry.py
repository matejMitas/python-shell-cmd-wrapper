from lib.library import Library

# compress_lib = Library('compress_libs', 'kdu_compress')
# compress_lib.set_io('file1.ppm', 'file2.jp2')
# compress_lib.set_fixed()
# compress_lib.construct()

convert_lib = Library(blueprint='convert', reset_after_construct=True)
"""
Set fixed parameters
"""
convert_lib.set_fixed(
	input='./tests/output.ppm', 
	output='./tests/output2.ppm', 
	colorspace='rgb'
)
"""
Set variable parameters
"""
convert_lib.set_variable(
	resize=[10, 20, 50, 70, 90]
)
"""
Set variable parameters
"""
convert_lib.construct()