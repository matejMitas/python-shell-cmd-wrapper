from lib.library import Library
import sys

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
	input='in.ppm', 
	blocks=(32, 64),
	compression="lossy"
)
"""
Set variable parameters
"""
convert_lib.set_variable(
	tiles=[
		(128,128), 
		(432, 765), 
		(477,997), 
		(450, 1097)
	],
	# precincts=[
	# 	(
	# 		(128,128), (432, 765)
	# 	), 
	# 	(
	# 		(477,997), (450, 1097)
	# 	)
	# ],
	# output=[
	# 	'out_1.ppm', 
	# 	'out_2.ppm', 
	# 	'out_3.ppm', 
	# 	'out_4.ppm'
	# ]
)

#convert_lib.set_variable(output='out_1.ppm')
convert_lib.set_variable(tiles=(432, 765))
"""
Set variable parameters
"""
print(convert_lib.construct())

a = [6]
b = (2,5)