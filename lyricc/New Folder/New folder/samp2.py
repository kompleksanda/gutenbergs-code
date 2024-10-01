import repos

repos.activate('pron','pos')

rea = open('C:\\Users\\pc\\Desktop\\moby\\cccccc.txt', 'w')
print('starting...')
for i in range(repos.pron_cmd_fd_content_len):
	word = repos.pron_cmd_fd_content_word[i]
	print('for',word)
	pron = repos.pron_cmd_fd_content_pron[i]
	if word.endswith(')'): word2 = word[:len(word)-3]
	else: word2 = word
	id = repos.perm(word2)
	if id > -1:
		word2 = repos.pos_file_fd_content_lists_word[id]
		pos = repos.get_word_pos(word2)
	else:
		word2 = word2.lower()
		word_len = len(word2)
		if word2.endswith("ies"):
			new_word = word2[:word_len-3]+"y"
			id = repos.perm(new_word)
			if id > -1:
				word2 = repos.pos_file_fd_content_lists_word[id]
				pos = repos.get_word_pos(word2)
			else: pos = []
		elif word2.endswith("es"):
			new_word = word2[:word_len-1]
			id = repos.perm(new_word)
			if id > -1:
				word2 = repos.pos_file_fd_content_lists_word[id]
				pos = repos.get_word_pos(word2)
			else: pos = ''
		elif word2.endswith("s"):
			new_word = word2[:word_len-1]
			id = repos.perm(new_word)
			if id > -1:
				word2 = repos.pos_file_fd_content_lists_word[id]
				pos = repos.get_word_pos(word2)
			else: pos = ''
		else: pos = ''
	tt = ''
	if pos == '': tt = 'NA'
	else:
		for j in pos: tt += repos.wtl[j]
	rea.write(word+' '+tt+' '+' '.join(pron)+'\n')
rea.close()
