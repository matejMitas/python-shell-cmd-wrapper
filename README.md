# python-shell-cmd-wrapper
Based on one of the parts of my bachelor thesis testing framework. Enables to call shell programs seamlessly within Python workflow. Derived from my [bachelor thesis](https://github.com/matejMitas/VUT_FIT-bakalarka) 

Motivation
------------
Whilst working with not very widespread libraries/commands one might struggle using them without proper Python wrapper. Oftentimes nothing fancy is really required, simple abstraction layer is all that is needed. I encountered this very problem in my bachelor thesis when trying to automate image compression pipeline (JPEG2000) using various libraries. This package builds abstraction layer over base set of libraries, at the same time enabling users to easily add new ones.

Base usage
------------
Firstly, let's look onto basic usage with predefined library (wget)

```console
$ pip install grip
```
