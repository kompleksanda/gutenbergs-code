import repos
tags = ["AA","AE","AW","AY","EH","EY","IH","OY","UH", "IY","UW", "AH","AO", "OW","ER"]
gen_tags = ["AW","AY","EH","EY","OY","UH", "IY", "AH", "OW","AO"]
repos.pron_syll_no = True
repos.use_gen_cmd = True
repos.silent = ['HH']
repos.activate('pron')
tag = tags

len1="/sdcard/work/mobygutenberg/len1.py"
len2="/sdcard/work/mobygutenberg/len2.py"
len3="/sdcard/work/mobygutenberg/len3.py"
len4="/sdcard/work/mobygutenberg/len4.py"
len1fd = open(len1, 'w')
len2fd = open(len2, 'w')
len3fd = open(len3, 'w')
len4fd = open(len4, 'w')

text2 = """
def get(s): return(eval(s))
"""

def do():
	r = gene()
	lent = len(r)
	for i in r:
		ii = []
		for j in i: ii.append(j+'1')
		i = ii
		print("doing",i,"rem",lent-1)
		li = len(i)
		nm = '_'.join(i)
		nm = nm.replace('1','').replace('0','').replace('2','')
		a = repos.get_word_ending_with_pron(i, li, 0, li)
		print(a)
		if li == 1:
			len1fd.write(nm+" = [")
			t = ''
			for j in a:
				t += '"'+j+'",'
			t = t.rstrip(',')
			t += ']\n\n'
			len1fd.write(t)
		elif li == 2:
			len2fd.write(nm+" = [")
			t = ''
			for j in a:
				t += '"'+j+'",'
			t = t.rstrip(',')
			t += ']\n\n'
			len2fd.write(t)
		elif li == 3:
			len3fd.write(nm+" = [")
			t = ''
			for j in a:
				t += '"'+j+'",'
			t = t.rstrip(',')
			t += ']\n\n'
			len3fd.write(t)
		elif li == 4:
			len1fd.write(nm+" = [")
			t = ''
			for j in a:
				t += '"'+j+'",'
			t = t.rstrip(',')
			t += ']\n\n'
			len4fd.write(t)
		lent -= 1
		print(t)
	len1fd.write(text2)
	len2fd.write(text2)
	len3fd.write(text2)
	len4fd.write(text2)
	print("Done?")

def gene():
	res = []
	for i in tags: res.append([i])
	for i in tags:
		for j in tags:
			n = [i, j]
			res.append(n)
			for k in tags:
				n = [i, j, k]
				res.append(n)
				for l in tags:
					n = [i, j, k, l]
					res.append(n)
	return res
do()
#print(gen())
len1fd.close()
len2fd.close()
len3fd.close()
len4fd.close()
len2fd.close()
