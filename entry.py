from lib.library import Library

compress_lib = Library('kakadu', library='kdu_compress')
compress_lib.test()

convert_lib = Library('convert')
convert_lib.test()