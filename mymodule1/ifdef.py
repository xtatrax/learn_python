"""
C の #ifdef 的なことしたい
"""

from . import _module_var_data_list_
print(_module_var_data_list_.is_def)
#global is_def
print("1try:")
try:
	if _module_var_data_list_.is_def:
		print("2is_def = true")
		print(_module_var_data_list_.is_def)
	else :
		print("3is_def = false")
		print(_module_var_data_list_.is_def)
except:
	print("4is_def = ndef")

print("5ifdef")


def init():
	try:
		if is_def:
			print("6is_def = true")
			print(is_def)
		else :
			print("7is_def = false")
			print(is_def)
	except:
		print("8is_def = ndef")

