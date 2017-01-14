import math

def add(*args):
	return sum(args)


class A:
	def __init__(self, x=1, y=2):
		self.x = x
		self.y = y

def fname(a, l=None):
	l = list(l)
	l.append(a)
	return l


if __name__ == '__main__':
	v1 = fname(1)
	v2 = fname('a', ['b'])
	v3 = fname(100)

	print v1
	print v2
	print v3