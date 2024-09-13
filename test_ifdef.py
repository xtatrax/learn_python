

global is_def
is_def = True
from mymodule1 import ifdef
import mymodule1.lib_test

ifdef.is_def = True
ifdef.init()

mymodule1.lib_test.lib_test()
print(mymodule1.lib_test.lib_test_data)