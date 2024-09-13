"""
C の #ifdef 的なことしたい
"""

global is_def
try:
	if is_def:
		print("is_def = true")
	else :
		print("is_def = false")
except:
	print("is_def = ndef")

print("ifdef")


def init():
	try:
		if is_def:
			print("is_def = true")
			print(is_def)
		else :
			print("is_def = false")
			print(is_def)
	except:
		print("is_def = ndef")
