# python-shell-cmd-wrapper
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/matejMitas/python-shell-cmd-wrapper/blob/master/LICENSE)

Based on one of the parts of my bachelor thesis testing framework. Enables to call shell programs seamlessly within Python workflow. Derived from my [bachelor thesis](https://github.com/matejMitas/VUT_FIT-bakalarka).

Motivation
------------
Whilst working with not very widespread libraries/commands one might struggle using them without proper Python wrapper. Oftentimes nothing fancy is really required, simple abstraction layer is all that is needed. I encountered this very problem in my bachelor thesis when trying to automate image compression pipeline (JPEG2000) using various libraries. This package builds abstraction layer over base set of libraries, at the same time enabling users to easily add new ones.

Notes
------------
Typical CLI use certain naming convension for prompt values.
```
wget google.com -o log.txt
```
`wget` is a command, `google.com` is a parameter and `-o` is switch/flag. Here - in blueprint/routines - is marked as a flag.

Blueprint
------------------
Used for describing flags/parameters of a command.
```json
{
	"settings": {
		"required_flags": [
			"@input", "@output"
		]
	},
	"flags": {
		"@input": [
			{
				"flag"		: null,
				"unifier"	: null,
				"format"	: "single"
			}
		],
		"@output": [
			{
				"flag"		: null,
				"unifier"	: null,
				"format"	: "single"
			}
		],
		"@resize": [
			{
				"flag"		: "-resize",
				"unifier"	: "=",
				"format"	: "single" 
			}
		],
		"@colorspace": [
			{
				"flag"		: "-colorspace",
				"unifier"	: "=",
				"format"	: "single"
			}
		]
	}
}
```

Routine
------------------
More advanced way of controlling generation of command variants.
```json
{
    "routines": [
        {
            "variable_flags" : [
                {
                    "flag" : "resize",
                    "opts" : [10, 20, 50, 70, 90]
                }
            ],
            "fixed_flags"   : {
                "colorspace": "rgb"
            }
        }
    ]
}
```


Base usage
------------------
### `Lib` class

Firstly, let's look onto basic usage with predefined library (Imagemagick `convert`). `Lib` is main class of package wrapping functionality. `blueprint` refers to json file in `./blueprint`.

```python
convert_lib = Lib(
	blueprint='convert' 
)
```
Each blueprint might contain more than one library, `lib` distinguishes particular library. Sometimes one might want to repeat construction of flags for more advanced usage, default behaviour is to discard set flags.

```python
compress = Lib(
	blueprint='compress_libs',
	lib='kdu_compress',
	reset_after_construct=True
)
```

Adding flags
------------
```python
convert_lib.set_fixed(
	colorspace='rgb'
)
```

```python
convert_lib.set_variable(
	resize=[10, 20, 30, 50, 90]
)
```