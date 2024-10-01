import repos
from os import system

settings = False
all_cons =['D','DH','T','TH','B','CH','F','G','HH','JH','K','L','M','N','NG','P','R','S','SH','V','W','Y','Z','ZH']
h = ['HH']
repos.silent = h
repos.transform = {'NG':['N','G']}
#repos.anyhow = True
#repos.m_as_group = True
#repos.reverse_all_pron = True

def call():
	for i in range(10):
		#cons_m(action=-1,cc=1,ce=0,anywhere=True,only_sound=True,repeatables=[])
		#alt(-1, action=-2)
		#pron_w(2, action=-2)
		pron_ws() # for every syllable
		#pron_d(action=-1, ml=1, me=1, mt="v", consonants=None) #for pronunciation
		#altmatch(action=-1, columns=3)
		#sta_ma(-1, lent=2, rep_times = 1, exa=1, anyw=False, only_s=False, repeatable=[], columns=3) #for a word
		continue

def get_res(prompt,opt=['y','n']):
	res = input(prompt+': ')
	while res not in opt:
		if res == 'cc': return res
		elif res == '': return 'n'
		res = input(prompt+': ')
	return res

def get_inp(prompt='input: '):
	res = input(prompt)
	return res

def change_pron_settings():
	o = get_res('Do you wish to change pronunciation settings?[y/n]')
	if o == 'y':
		tt = 'do you wish to invert'
		t = tt+' repos.anyhow='+str(repos.anyhow)+' [y/n]'
		a = get_res(t)
		if a == 'y': repos.anyhow = not(repos.anyhow)
		elif a == 'cc': return
		t = tt+' repos.m_as_group='+str(repos.m_as_group)+' [y/n]'
		a = get_res(t)
		if a == 'y': repos.m_as_group = not(repos.m_as_group)
		elif a == 'cc': return
		t = tt+' repos.reverse_all_pron='+str(repos.reverse_all_pron)+' [y/n]'
		a = get_res(t)
		if a == 'y': repos.reverse_all_pron=not(repos.reverse_all_pron)
		elif a == 'cc': return
		tt = 'Do you wish to edit to'
		t = tt+' repos.silent='+str(repos.silent)+' [y/n]'
		a = get_res(t)
		if a == 'y':
			t = 'append/clear[a/c]'
			a = get_res(t, ['a','c'])
			if a in ['a', 'c']:
				r = input('input: ')
				r = r.replace(' ','')
				l = r.split(',')
				if a == 'a': repos.silent += l
				elif a == 'c': repos.silent = l
			else: return
			try:
				if repos.pron_fd_content_len:
					del(repos.pron_fd_content_len)
			except NameError: pass
		elif a == 'cc': return

def pron_ws():
	if settings: change_pron_settings()
	repos.pron_syll_no = True
	repos.activate("pron")
	word = input("Enter words: ")
	t = word.replace(' ','-')
	if repos.silent == all_cons: t+="_VOWONLY"
	if repos.reverse_all_pron: t+='_REV'
	if repos.anyhow: t+='_ANYHOW'
	if repos.m_as_group: t+='_GROUP'
	dire = "/sdcard/work/rim/match/words/"+t
	system("clear")
	repos.get_word_ending_with_pron_of_words(word, dire)
def pron_w(limit=1, action=1):
	if settings:
		change_pron_settings()
		tt = 'Do you wish to change pron_w settings'
		a = get_res(tt)
		if a == 'y':
			tt = 'Do you wish to change '
			t = tt+'limit='+str(limit)
			a = get_res(t)
			if a == 'y': limit = int(get_inp())
			elif a == 'cc': return
			t = tt+'action='+str(action)
			a = get_res(t)
			if a == 'y': action = int(get_inp())
	repos.activate("pron")
	word = input("Enter word: ")
	system("clear")
	t = ''
	if repos.anyhow: t+='_ANYHOW'
	if repos.m_as_group: t+='_GROUP'
	dire = "/sdcard/work/rim/match/"+word+t+".txt"
	a = repos.get_word_ending_with_pron_of_word(word, limit)
	repos.write_to_file(a, dire, action=action)

def alt(limit=-40, action=1):
	if settings:
		tt = 'Do you wish to change alt settings'
		a = get_res(tt)
		if a == 'y':
			tt = 'Do you wish to change '
			t = tt+'limit='+str(limit)
			a = get_res(t)
			if a == 'y': limit = int(get_inp())
			elif a == 'cc': return
			t = tt+'action='+str(action)
			a = get_res(t)
			if a == 'y': action = int(get_inp())
	repos.activate("alt")
	print("\n")
	word = input("Enter word: ")
	t = word.replace(' ','-')
	dire = "/sdcard/work/rim/alt/"+t+".txt"
	system("clear")
	a = repos.get_alt_of_word(word, limit, request=False)
	system("clear")
	def pr(a):
		for i in a:
			print("\n"*2)
			print(i)
	if action < 0:
		print ('-------------------results for',word)
		pr(a)
	else: repos.write_to_file(a, dire, action=action, nested=True)

def cons_m(action=-1, cc=1, ce =0, repeatables=[], anywhere=False, only_sound=False):
	if settings:
		change_pron_settings()
		a = get_res('Do you wish to change cons_m settings')
		if a == 'y':
			n = ['cc','ce','repeatables', 'action']
			tv = ['anywhere', 'only_sound']
			tn = 'Do you want to change '
			ttv = 'Do you want to invert '
			for nn in n:
				ev = eval(nn)
				t = tn+nn+'='+str(ev)
				a = get_res(t)
				if a == 'y':
					h = get_inp()
					if type(ev) == type(1): ttt = nn+'=int(h)'
					elif type(ev) == type([]):
						h = h.replace(' ','')
						h = h.split(',')
						ttt = nn+'=h'
					else: ttt = nn+'=str(h)'
					exec(ttt)
				elif a == 'cc': return
			for nn in tv:
				t = ttv+nn+'='+str(eval(nn))
				a = get_res(t)
				if a == 'y':
					ttt = nn+'='+'not('+nn+')'
					exec(ttt)
				if a == 'cc': return
	#repos.silent = all_cons
	repos.activate("pron")
	word = input("Enter pronunciation: ")
	system("clear")
	t = word.replace(' ', '-')
	dire = "/sdcard/work/rim/conso_m/"+t+".txt"
	a = repos.get_word_starting_pron(word, cc, ce, repeatables, anywhere, only_sound)
	repos.write_to_file(a, dire, action=action)

def pron_d(action=-1, ml=1, me=1, sy=0, se=0, mt="v", cmt="exactly", consonants=None):
	"""
	ml = limit of match, maybe the first vowel second vowel etc
	me = used if to match more, less or equal to ml 0=equal, >0=more, <0=less
	sy = no of syllables to match
	se = used if to match more, less or equal to sy 0=equal, >0=more, <0=less
	mt = match type 'c' or 'v' ie consonant or vowel matching
	cmt = consonants match type specifies if to match exactly or whole group of consonant, or any consonant in the group. 'exactly', 'atleast', 'any'
	consonants = list of consonants and vowels that should be included in match

	"""
	if settings:
		change_pron_settings()
		a = get_res('Do you wish to change pron_d settings')
		if a == 'y':
			n = ['ml','me','cmt', 'consonants', 'mt', 'action']
			tn = 'Do you want to change '
			for nn in n:
				ev = eval(nn)
				t = tn+nn+'='+str(ev)
				a = get_res(t)
				if a == 'y':
					h = get_inp()
					if type(ev) == type(1): ttt = nn+'=int(h)'
					elif type(ev) == type([]):
						h = h.replace(' ','')
						h = h.split(',')
						ttt = nn+'=h'
					else: ttt = nn+'=str(h)'
					exec(ttt)
				elif a == 'cc': return
	if sy > 0: repos.pron_syll_no = True
	repos.activate("pron")
	word = input("Enter pronunciation: ")
	system("clear")
	t = word.replace(' ', '-')
	dire = "/sdcard/work/rim/match/"+t+".txt"
	a = repos.get_word_ending_with_pron(word, ml, me, sy, se, mt, cmt, consonants)
	repos.write_to_file(a, dire, action=action)

def altmatch(action=-1, columns=3):
	if settings:
		change_pron_settings()
		t = 'Do you want to change alt_match settings'
		a = get_res(t)
		if a == 'y':
			t = 'Do you want to edit action='+str(action)
			a = get_res(t)
			if a == 'y':
				action = int(get_inp())
			if a == 'cc': return
	repos.activate('alt','pron')
	word = input('Enter word: ')
	system('clear')
	t = word.replace(' ','-')
	dire = "/sdcard/work/rim/alt_match/"+t+".txt"
	res = repos.get_alt_and_rhyming_word(word)
	repos.write_to_file(res, dire, action=action, columns=columns)

def sta_ma(action = -1, lent = 1, rep_times = 1, exa=1, anyw=False, only_s=False, repeatable=[], columns=3):
	if settings:
		change_pron_settings()
		a = get_res('Do you wish to change sta_ma settings')
		if a == 'y':
			n = ['lent','rep_times', 'exa', 'repeatables','action']
			tv = ['anyw', 'only_s']
			tn = 'Do you want to change '
			ttv = 'Do you want to invert '
			for nn in n:
				ev = eval(nn)
				t = tn+nn+'='+str(ev)
				a = get_res(t)
				if a == 'y':
					h = get_inp()
					if type(ev) == type(1): ttt = nn+'=int(h)'
					elif type(ev) == type([]):
						h = h.replace(' ','')
						h = h.split(',')
						ttt = nn+'=h'
					else: ttt = nn+'=str(h)'
					exec(ttt)
				elif a == 'cc': return
			for nn in tv:
				t = ttv+nn+'='+str(eval(nn))
				a = get_res(t)
				if a == 'y':
					ttt = nn+'='+'not('+nn+')'
					exec(ttt)
				if a == 'cc': return
	repos.activate('pron')
	word = input('Enter word: ')
	system('clear')
	dire = "/sdcard/work/rim/match/"+word+"_REV.txt"
	res = repos.start_match(word, lent, rep_times, exa, anyw, only_s, repeatable)
	repos.write_to_file(res, dire, action=action, columns = columns)

call()
