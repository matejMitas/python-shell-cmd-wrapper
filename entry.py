from lib.library import Library

# compress_lib = Library('compress_libs', 'kdu_compress')
# compress_lib.set_io('file1.ppm', 'file2.jp2')
# compress_lib.set_fixed()
# compress_lib.construct()

convert_lib = Library('pnmpsnr')
convert_lib.set_io('./tests/output.ppm', './tests/input.ppm')
convert_lib.construct()