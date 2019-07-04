from pyshellwrapper.wrapper import PyShellWrapper as Library
import sys

# compress_lib = Library('compress_libs', 'kdu_compress')
# compress_lib.set_io('file1.ppm', 'file2.jp2')
# compress_lib.set_fixed()
# compress_lib.construct()

# convert_lib = Library(
# 	blueprint='compress_libs', 
# 	lib='kdu_compress', 
# 	reset_after_construct=True
# )
"""
Set fixed parameters
"""
# convert_lib.set_fixed(
# 	input='in.ppm', 
# 	blocks=(32, 64),
# 	compression="lossy"
# )
"""
Set variable parameters
"""
# convert_lib.set_variable(
# 	tiles=[
# 		(128,128), 
# 		(432, 765), 
# 		(477,997), 
# 		(450, 1097)
# 	],
# 	# precincts=[
# 	# 	(
# 	# 		(128,128), (432, 765)
# 	# 	), 
# 	# 	(
# 	# 		(477,997), (450, 1097)
# 	# 	)
# 	# ],
# 	# output=[
# 	# 	'out_1.ppm', 
# 	# 	'out_2.ppm', 
# 	# 	'out_3.ppm', 
# 	# 	'out_4.ppm'
# 	# ]
# )

#convert_lib.set_auxiliary('some_filename', [5, 4], (5,1))
#convert_lib.set_variable(output='out_1.ppm')
#convert_lib.set_variable(tiles=(432, 765))

# wget = Library(blueprint='wget', command=0)

# wget.set_fixed(
# 	source='google.com',
# 	max_speed='50k'
# )

# #convert_lib.set_variable(tiles=[(432, 765), (111, 122)])

# """
# Set variable parameters
# """
# for variant in wget.construct():
# 	print(variant)



kdu = Library(blueprint='compress_libs', command='kdu_compress')
kdu.set_fixed(
	input='test.ppm',
	output='test.jp2',
	tiles=(122,211),
	fake_flag=(44,25,84,48)
)

for variant in kdu.construct():
	print(variant)