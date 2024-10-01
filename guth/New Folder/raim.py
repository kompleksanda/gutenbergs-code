import repos, os, json, re
repos.activate("pron","syl")
dire = r"C:\Users\pc\Desktop\moby\raim"
#with open(r"C:\Users\pc\Desktop\moby\jsson.txt") as op:
#    totalWords = json.load(op)
tt = repos.pron_cmd_fd_content_len
for i in range(repos.pron_cmd_fd_content_len):
	tt = tt -1
	word = repos.pron_cmd_fd_content_word[i]
	dir_wrd = dire+"\\"+word
	try:
		os.mkdir(dir_wrd)
	except Exception: continue
	print(word,"remains",tt)
	w_pron = repos.pron_cmd_fd_content_pron[i]
	sy_n = int(repos.pron_cmd_fd_content_syll_no[i])
	for j in range(1,sy_n+1):
		dir_wrd_n = dir_wrd+"\\"+str(j)+".txt"
		result = repos.get_word_ending_with_pron_of_word(word, j, 0)
		if result == []: continue
		repos.write_to_file(result, dir_wrd_n, columns=6)