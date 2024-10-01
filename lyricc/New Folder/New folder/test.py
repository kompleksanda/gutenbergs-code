use_gen_cmd = True

gen_cmd_wtp = [ ["AW"], ["AY"], ["IY","IH"], ["EY"],["OY"], ["UH","UW"], ["AE","AH","AA"] ,["AO"],["EH","ER"], ["OW"] ]
cmd_wtp = [["AE"],["AW"],["AY"],["IY"],["IH"],["EY"],["OY"],["UH"],["UW"],["AH"],["AO"],["AA"],["EH"],["OW"],["ER"]]

gen_c =[['D','DH'],['T','TH'],['B'],['CH'],['F'],['G'],['HH'],['JH'],['K'],['L'],['M'],['N'],['NG'],['P'],['R'],['S'],['SH'],['V'],['W'],['Y'],['Z'],['ZH']]

co_spec =[['D'],['T'],['B'],['CH'],['DH'],['F'],['G'],['HH'],['JH'],['K'],['L'],['M'],['N'],['NG'],['P'],['R'],['S'],['SH'],['TH'],['V'],['W'],['Y'],['Z'],['ZH']]

def group(pron):
	ret_list = []
	inner_list = []
	last_is_vowel = False
	pron_last = len(pron) - 1
	counter = 0
	for l in pron:
		if l[-1] in ["0", "1", "2"]:
			if last_is_vowel: inner_list.append(l)
			else:
				if inner_list == []: inner_list.append(l)
				else:
					ret_list.append(inner_list)
					inner_list = [l]
			last_is_vowel =  True
		else:
			if last_is_vowel:
				ret_list.append(inner_list)
				inner_list = [l]
			else: inner_list.append(l)
			last_is_vowel =  False
		if counter == pron_last: ret_list.append(inner_list)
		counter += 1
	return ret_list

def zipper(list1, list2):
	ret_list = []
	len_to_use = min(len(list1), len(list2))
	for i in range(len_to_use): ret_list.append([list1[i], list2[i]])
	return ret_list

def is_vowel_cmd(first, second, listed=False):
	if not(listed):
		if first[-1] in ["0", "1", "2"] and second[-1] in ["0", "1", "2"]: return True
		return False
	else: return is_vowel_cmd(first[0], second[0])

def is_consonant_cmd(first, second, listed=False):
	if not(listed):
		if first[-1] not in ["0", "1", "2"] and second[-1] not in ["0", "1", "2"]: return True
		return False
	else: return is_consonant_cmd(first[0], second[0])
def match_vowel_cmd(first, second):
	first = first[:len(first)-1]
	second = second[:len(second)-1]
	if not(use_gen_cmd): val = cmd_wtp
	else: val = gen_cmd_wtp
	for values in val:
		if first in values and second in values: return True
	return False

def match_conso_cmd(first, second):
	first, second = first[:], second[:]
	if not(use_gen_cmd): val = co_spec
	else: val = gen_c
	for values in val:
		if first in values and second in values: return True
	return False

def all_in_match(first, second, better=False, type='v'):
	first, second = first[:], second[:]
	tot = []
	prev = []
	m_prev = []
	if type == 'v':
		for i in second:
			fin = []
			mat = False
			for j in first:
				if is_vowel_cmd(i,j):
					if match_vowel_cmd(i,j):
						mat = True
						if j not in m_prev: m_prev.append(j)
						for k in prev:
							if match_vowel_cmd(j, k):prev.remove(k)
					else:
						yes = False
						for k in m_prev:
							if match_vowel_cmd(j,k): yes=True
						if not(yes):
							if j not in prev: fin.append(j)
				else: return False
			tot += [mat]
			prev += fin
	else:
		for i in second:
			fin = []
			mat = False
			for j in first:
				if is_consonant_cmd(i,j):
					if match_conso_cmd(i,j):
						mat = True
						if j not in m_prev: m_prev.append(j)
						for k in prev:
							if match_conso_cmd(j, k):prev.remove(k)
					else:
						yes = False
						for k in m_prev:
							if match_conso_cmd(j,k): yes=True
						if not(yes):
							if j not in prev: fin.append(j)
				else: return False
			tot += [mat]
			prev += fin
	if all(tot):
		if prev:
			if better: return 2
		else:
			if better: return 1
		return True
	else: return False

a, b = ['AH2','IH1'], ['AH2']
print(all_in_match(a,b))
print(all_in_match(a,b,True))
