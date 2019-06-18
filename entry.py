from lib.library import Library

compress_lib = Library('kakadu', 'kdu_compress')
compress_lib.set_io('file1.ppm', 'file2.jp2')
compress_lib.set_fixed()
compress_lib.construct()

convert_lib = Library('convert')
convert_lib.set_io('in_file.jpg', 'out_file.jpg')
convert_lib.construct()