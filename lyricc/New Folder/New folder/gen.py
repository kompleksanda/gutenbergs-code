import repos, random
verbose = True
#all_cons =['D','DH','T','TH','B','CH','F','G','HH','JH','K','L','M','N','NG','P','R','S','SH','V','W','Y','Z','ZH']
h = ['HH']
repos.silent = h
repos.anyhow = True
repos.transform = {'NG':['N','G']}
#repos.reverse_all_pron = True
#repos.m_as_group = True

#style = ['do','re','mi','fa','so','la','ti']
#style = ['do', 're', 'mi']
#style = ['0.5','1','1.5','2']

def call():
	time = 5000
	at(time)
	#me(time)
	#stre(time)
	#pos(time)
	#vowe(2)
	#scale(11, time, action=2)

def timeit(stmt):
	import time
	a = time.time()
	stmt()
	print('took',time.time()-a)

def choose(l):
	list_ret = []
	for j in l:
		if j == []: j=['----']
		list_ret.append(random.choice(j))
	return list_ret

def pos(time=10, action = 1):
	#repos.pron_syll_no = True
	repos.activate('pos')
	sentence = input("Enter words: ")
	f = sentence.replace(' ','-')+".txt"
	dire = "/sdcard/work/rim/word/pos/"+f
	orig = []
	dd = []
	for word in sentence.split():
		if verbose: print('proccessing',word)
		if word in dd:
			id = dd.index(word)
			orig.append(orig[id])
			dd.append(word)
			continue
		dd.append(word)
		#id = repos.pron_cmd_fd_content_word.index(word.upper())
		#n=repos.pron_cmd_fd_content_syll_no[id]
		p = repos.get_word_pos(word)
		#r = repos.get_word_ending_with_pron_of_word(word, 1)
		#r = repos.pron_get_syll_no_word(n, dbwords=r)
		#for i in range(len(r)):
		#	r[i]=	r[i].lower()
		mode='atleast'
		#mode='exactly'
		r = repos.get_pos_word(p, mode)
		#r = repos.pron_get_syll_no_word(n, dbwords=r)
		orig.append(r)
	if action >= 0: fil=open(dire, 'w')
	g=[]
	for i in range(time):
		list_ret = choose(orig)
		if list_ret not in g: g.append(list_ret)
		else:
			list_ret = choose(orig)
			if list_ret not in g: g.append(list_ret)
			else:
				list_ret = choose(orig)
				if list_ret not in g: g.append(list_ret)
				else: continue	
	g.sort()
	for i in g:
		te = ' '.join(i)+'...\n'
		if action < 0: print(te)
		elif action == 0:
			print(te)
			fil.write(te)
		else: fil.write(te)
	if action >= 0:fil.close()

def me(time=10, action = 1):
	repos.pron_syll_no = True
	repos.activate('pron')
	#repos.activate('pos')
	sentence = input("Enter words: ")
	f = sentence.replace(' ','-')+".txt"
	dire = "/sdcard/work/rim/word/match/"+f
	orig = []
	dd = []
	for word in sentence.split():
		if verbose: print('proccessing',word)
		if word in dd:
			id = dd.index(word)
			orig.append(orig[id])
			dd.append(word)
			continue
		dd.append(word)
		try:
			#y = repos.get_word_pos(word)
			word=word.upper()
			n = repos.pron_cmd_fd_content_word.index(word)
			n=repos.pron_cmd_fd_content_syll_no[n]	
			r = repos.get_word_ending_with_pron_of_word(word, n, 0, n)
			#r = repos.get_pos_word(y, dbwords=r)
		except ValueError: r=[]
		orig.append(r)
	del(dd)
	g = []
	if action >= 0: fil=open(dire, 'w')
	for i in range(time):
		list_ret = choose(orig)
		if list_ret not in g: g.append(list_ret)
		else:
			list_ret = choose(orig)
			if list_ret not in g: g.append(list_ret)
			else:
				list_ret = choose(orig)
				if list_ret not in g: g.append(list_ret)
				else: continue	
	g.sort()
	for i in g:
		te = ' '.join(i)+'...\n'
		if action < 0: print(te)
		elif action == 0:
			print(te)
			fil.write(te)
		else: fil.write(te)
	if action >= 0:fil.close()

def at(time=10, action = 1):
	done=[]
	repos.activate('alt')
	#repos.activate('pos')
	sentence = input("Enter words: ")
	f = sentence.replace(' ','-')+".txt"
	dire = "/sdcard/work/rim/word/alt/"+f
	out=[]
	for word in sentence.split():
		if verbose: print('proccessing',word)
		if word in done:
			id=done.index(word)
			out.append(out[id])
			done.append(word)
			continue
		done.append(word)
		tot=repos.get_alt_of_word(word, -1)
		to = []
		for i in tot:
			to += i
		del(tot)
		to = list(set(to))
		if to == []: to = [word]
		#p = repos.get_word_pos(word)
		#to = repos.get_pos_word(p , dbwords=to[:400])
		out.append(to)
	if action >= 0: fil=open(dire, 'w')
	g = []
	for i in range(time):
		list_ret = choose(out)
		if list_ret not in g: g.append(list_ret)
		else:
			list_ret = choose(out)
			if list_ret not in g: g.append(list_ret)
			else:
				list_ret = choose(out)
				if list_ret not in g: g.append(list_ret)
				else: continue	
	g.sort()
	for i in g:
		te = ' '.join(i)+'...\n'
		if action < 0: print(te)
		elif action == 0:
			print(te)
			fil.write(te)
		else: fil.write(te)
	if action >= 0:fil.close()

def stre(time=10, action = 1):
	repos.pron_str = True
	repos.activate('pron')
	#repos.activate('pos')
	sentence = input("Enter words: ")
	f = sentence.replace(' ','-')+".txt"
	dire = "/sdcard/work/rim/word/stress/"+f
	done=[]
	out=[]
	for word in sentence.split():
		if verbose: print('proccessing', word)
		try:
			id = repos.pron_cmd_fd_content_word.index(word.upper())
			st=repos.pron_cmd_fd_content_str[id]
			if st in done:
				id = done.index(st)
				w=out[id]
				out.append(w)
				done.append(st)
				continue
			else:
				done.append(st)
				w=repos.pron_get_word_with_str('^'+st+'$')
				#p = repos.get_word_pos(word)
				#w = repos.get_pos_word(p, 'any', dbwords=w[:400])
				out.append(w)
		except ValueError: out.append([])
	if action >= 0: fil=open(dire, 'w')
	g = []
	for i in range(time):
		list_ret = choose(out)
		if list_ret not in g: g.append(list_ret)
		else:
			list_ret = choose(out)
			if list_ret not in g: g.append(list_ret)
			else:
				list_ret = choose(out)
				if list_ret not in g: g.append(list_ret)
				else: continue	
	g.sort()
	for i in g:
		te = ' '.join(i)+'...\n'
		if action < 0: print(te)
		elif action == 0:
			print(te)
			fil.write(te)
		else: fil.write(te)
	if action >= 0:fil.close()

def vowe(action=2):
	all_cons =['D','DH','T','TH','B','CH','F','G','HH','JH','K','L','M','N','NG','P','R','S','SH','V','W','Y','Z','ZH']
	repos.silent = all_cons
	repos.activate('pron')
	pro = input('Enter pronunciation: ')
	fil2 = pro.replace(' ','-')
	fil2 = '/sdcard/work/rim/word/vowel/'+fil2+'.txt'
	repos.get_words_from_vowel_comb2(pro, fil2, action)


def scale(length=3, times=100, action=2):
	fil = '/sdcard/work/rim/scale/'
	fil += str(length)+'-'+str(times)+'.txt'
	ret_list = []
	for i in range(times):
		hol = []
		for j in range(length):
			choice = random.choice(style)
			hol.append(choice)
		if hol not in ret_list: ret_list.append(hol)
	ret_list.sort()
	if action >= 0: fil = open(fil, 'w')
	if action < 0:
		for i in ret_list: print(', '.join(i))
	elif action == 0:
		for i in ret_list:
			tt = ', '.join(i)
			print(tt)
			fil.write(tt+'\n')
	else:
		for i in ret_list: fil.write(', '.join(i)+'\n')
	if action >= 0: fil.close()

timeit(call)
