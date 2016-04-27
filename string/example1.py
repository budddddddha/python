# -*- coding: utf-8 -*-
# http://docs.python.jp/3/library/stdtypes.html#string-methods

text = 'Hello World. Python Code.'
print("text=",text,"\n")

# slice
print('slice'.center(50,'-'))
print('text[0]', text[0])
print('text[-1]', text[-1])
print('text[0:5]', text[0:5])
print('text[-5:]', text[-5:])
print('text[0::2]', text[0::2])

# in
print('in'.center(50,'-'))
print("'r' in text", 'r' in text)
print("'z' in text", 'z' in text)

# find
print('find()'.center(50,'-'))
print("text.find('r')", text.find('r'))
print("text.find('z')", text.find('z'))

# split
print('split(sep=None, maxsplit=-1)'.center(50,'-'))
print("text.split()", text.split())
print("text.split(None,2)", text.split(None,2))
print("text.split('o')", text.split('o'))

# center
print('center(width[, fillchar])'.center(50,'-'))
print("text.center(30,'?')", text.center(50,'?'))

# count
print('count(sub[, start[, end]])'.center(50,'-'))
print("text.count('l')", text.count('l'))
print("text.count('l',3,6)", text.count('l',3,6))
