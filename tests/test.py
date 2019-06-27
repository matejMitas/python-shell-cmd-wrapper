from lib.library import Library


def test():

	convert_lib = Library(
		blueprint='compress_libs', 
		lib='kdu_compress', 
		reset_after_construct=True
	)


	# convert_lib.set_fixed(
	# 	input='in_file', 
	# 	output='out_file', 
	# 	blocks=[128, 64]
	# )

	# convert_lib.construct()

	# ret = convert_lib.construct()
	# print(type(ret))

	# assert ret == ['kdu_compress', '-i', 'in_file', '-o', 'out_file']