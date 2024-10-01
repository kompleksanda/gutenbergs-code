import repos, os, json
repos.activate("alt")
dire = r"C:\Users\pc\Desktop\moby\rim\alt\nnnn"
dire2 = r"C:\Users\pc\Desktop\moby\rim\alt\nnnn2"
#words = list(set(repos.flatten(repos.alt_file_fd_content_lists)))
#with open(r"C:\Users\pc\Desktop\moby\jsson.txt", "w") as op:
#    json.dump(words, op)
with open(r"C:\Users\pc\Desktop\moby\jsson.txt") as op:
    words = json.load(op)
l = len(words)
for word in words:
	l -= 1
	print("remains",l)
	word = word.upper()
	if os.access(dire+"\\"+word+".txt",os.F_OK) or os.access(dire2+"\\"+word+".txt",os.F_OK):
		continue
	else:
		result = repos.get_alt_of_word(word, -1, request=False)
		if result == []:
			continue
		with open(dire2+"\\"+word+".txt", "w") as worda:
			for resi in result:
				count = 0
				for resi2 in resi:
					if count == 5:
						worda.write(resi2+"\n")
						count = 0
					else:
						worda.write(resi2+",   ")
						count += 1
				worda.write("\n\n---------------------------------------------------------\n")
			