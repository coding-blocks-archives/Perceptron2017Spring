print "hello world!"
# write a function
# add(1, 2, 3)

a = 1
print a

a = 'abc'
print a

b = "abc"
print a==b

#string, lists and dicts

l = []
print l

l.append('a')
print l

l1 = list([1, 2, 3])
print l1

L = [1, 2, 'abc', [11, 11.91, 1e-10], None]
print type(L)
print type(1.0), type(1), type('a'), type("abc")
print [1, 2] + [3, 4]

print L[-2]

a = [1, 3, 2, 4, 6, 2, 4, 'a']
print a[::-1]

# list[start:(end+1):skip]

# dictionary
d = {'k': 'v', 'k2':'value2', 2: 'abc', 'l': 1.0}
print d

a = """
This is a comment
"""

def fname(c, a=1, b=0, **kwargs):
	# print args
	print kwargs
	# return sum(args)
	return a**2 + b + c
b = 20
print fname(3, b=b, a=20, f1=10, f2=20)
pack = 10
print pack

import pack
print pack

print pack.add(1, 3, 2, 5, 4)