

#global is_def
#is_def = True
from mymodule1 import _module_var_data_list_
print(_module_var_data_list_.is_def)
print("data_list_.is_def")
_module_var_data_list_.ifdef = True
from mymodule1 import ifdef
import mymodule1.lib_test

ifdef.is_def = False
ifdef.init()

mymodule1.lib_test.lib_test()
print(mymodule1.lib_test.lib_test_data)