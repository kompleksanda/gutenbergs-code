import repos

repos.activate('pron','pos')

rea = open('C:\\Users\\pc\\Desktop\\moby\\ccccc3.txt', 'w')
print('starting...')
ll = repos.pron_cmd_fd_content_len
for i in range(repos.pron_cmd_fd_content_len):
	word = repos.pron_cmd_fd_content_word[i]
	if ll % 100 == 0: print(ll)
	ll -= 1
	pron = repos.pron_cmd_fd_content_pron[i]
	if word[-1] == ")": word2 = word[:len(word)-3]
	else: word2 = word
	word2 = word2.replace('.','')
	if word2[0] in ["\"","#","%","&","'","(",")","+",",",":",";","?","/","{","}"]: word2 = word2[1:]
	elif word2[:3] == "...": word2 = word2[3:]
	elif word2[:2] == "--": word2 = word2[2:]
	elif word2[0]in [".","-"]:word2 = word2[1:]
	id = repos.perm(word2)
	if id > -1:pos = repos.pos_file_fd_content_lists_pos[id]
	else:
		word2 = word2.lower()
		word_len = len(word2)
		if word2.endswith("ies"):
			new_word = word2[:word_len-3]+"y"
			id = repos.perm(new_word)
			if id > -1:pos = repos.pos_file_fd_content_lists_pos[id]
			else: pos = ''
		elif word2.endswith("es"):
			new_word = word2[:word_len-2]
			id = repos.perm(new_word)
			if id > -1:pos = repos.pos_file_fd_content_lists_pos[id]
			else:
				new_word = word2[:word_len-1]
				id = repos.perm(new_word)
				if id > -1:pos = repos.pos_file_fd_content_lists_pos[id]
				else: pos = ''
		elif word2.endswith("s"):
			new_word = word2[:word_len-1]
			id = repos.perm(new_word)
			if id > -1: pos = repos.pos_file_fd_content_lists_pos[id]
			else: pos = ''
		else: pos = ''
	if pos == '': pos = '*'		
	rea.write(word+' '+pos+' '+' '.join(pron)+'\n')
rea.close()
