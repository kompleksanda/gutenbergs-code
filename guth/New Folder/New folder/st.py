import symtable

fd = open('/sdcard/work/mobygutenberg/samp.py')
c = fd.read()
n = 'samp.py'
mode = 'exec'

tab = symtable.symtable(c,n,mode)
if tab.has_children():
	children = tab.get_children()
	p = children[0]
	t = p.get_parameters()
	print(t)

t = tab.get_identifiers()
