import repos
tags = ["AA","AE","AW","AY","EH","EY","IH","OY","UH", "IY","UW", "AH","AO", "OW","ER"]
gen_tags = ["AW","AY","EH","EY","OY","UH", "IY", "AH", "OW","AO"]
num = 1
repos.use_gen_cmd = True
repos.activate("pron")
tag = gen_tags
while num <= 5:
	print("doing",num,"folder")
	for i in range(len(tag)):
		print("----",tag[i],"----")
		#word = input("Enter word: ")
		a = repos.get_word_starting_pron(tag[i]+"1",num,0, anywhere=True, only_sound=True)
		if tag == tags: dire = "C:\\Users\\pc\\Desktop\\moby\\rim\\cmd\\"+str(num)+"\\"+tag[i]+".txt"
		elif tag == gen_tags: dire = "C:\\Users\\pc\\Desktop\\moby\\rim\\gen_cmd\\"+str(num)+"\\"+tag[i]+".txt"
		repos.write_to_file(a, dire, action=1, columns=7)
	num += 1
print("Done?")
