def flatten(listt, level = -1):
	new_list = []
	if level == 0: return listt
	elif level > 0:
		new_list = listt
		for i in range(level):
			if all(isinstance(v, list) for v in new_list):
				new_list = []
				for j in listt: new_list += j
				listt = new_list
				if i == level - 1: return new_list
			else: return new_list
	elif level < 0:
		for i in listt:
			if isinstance(i, list): new_list += flatten(i)
			else: new_list.append(i)
		return new_list

def exe(text):
	def do(text):
		ret_list = []
		lent = len(text)
		if lent <= 1: ret_list.append([[text]])
		else:
			for i in range(1, lent):
				f = text[:i]
				l = text[i:]
				if len(f) == 1:
					tot = [[f],[l]]
					if tot not in ret_list: ret_list.append(tot)
				else:
					res = do(f)
					for k in res:
						tot = k+[[l]]
						if tot not in ret_list: ret_list.append(tot)
				if len(l) == 1:
					tot = [[f],[l]]
					if tot not in ret_list: ret_list.append(tot)
				else:
					res = do(l)
					for k in res:
						tot = [[f]]+k
						if tot not in ret_list: ret_list.append(tot)
				if len(f) > 1 and len(l) > 1:
					tot = [[f],[l]]
					if tot not in ret_list: ret_list.append(tot)
		return ret_list
	r = do(text)
	if len(text) > 1: r.append([[text]])
	print (len(r))
	return r

def generate_diff_pron(orig_pron, include=False):
	ret_list = []
	pron_len = len(orig_pron)
	for i in range(pron_len):
		if i == 0:
			if include:
				for j in range(pron_len): ret_list.append(flatten(orig_pron[0:j+1])+[j+1])
			else:
				for j in range(pron_len - 1): ret_list.append(flatten(orig_pron[0:j+1])+[j+1])
		else:
			for j in range(pron_len - i): ret_list.append(flatten(orig_pron[i:i+j+1])+[j+1])
	return ret_list

print(generate_diff_pron(['AH1','UW2','IH2'], True))
