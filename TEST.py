def foo(a,b,c):
	return (a**b)**c

def fun(*args):
	empty=""
	for i in args:
		empty= empty + i
	return empty
