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
	return r

print(exe([1,2,3]))