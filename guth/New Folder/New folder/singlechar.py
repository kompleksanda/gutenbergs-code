import sys
def gett(prompt=''):
	sys.stdout.write(prompt)
	while True:
		d = sys.stdin.read()
		l = len(d)
		if l <= 1:
			print(d)
			return d

res = gett('enter character: ')
print('enter char is',res)

