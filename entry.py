from lib.library import Library

# compress_lib = Library('compress_libs', 'kdu_compress')
# compress_lib.set_io('file1.ppm', 'file2.jp2')
# compress_lib.set_fixed()
# compress_lib.construct()

convert_lib = Library(
	blueprint='compress_libs', 
	lib='kdu_compress', 
	reset_after_construct=True
)
"""
Set fixed parameters
"""
convert_lib.set_fixed(
	input='./tests/output.ppm', 
	output='./tests/output2.ppm', 
	blocks=[128, 64],
	precincts=[[128, 128], [64, 64]],
	compression="lossy"
)
"""
Set variable parameters
"""
convert_lib.set_variable()
"""
Set variable parameters
"""
print(convert_lib.construct())