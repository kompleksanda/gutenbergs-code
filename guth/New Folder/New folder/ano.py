
def group2(pron, grouped=False):
	def ungrouped(pron):
		ret_list = []
		ret_str = ""; list_str = []
		pron_len = len(pron)
		for i in range(pron_len):
			if pron[i][-1] in ["0", "1", "2"]:
				if i == 0:
					if pron_len == 1: return [[pron[i]]]
					else:
						if all(mm[-1] not in ["0", "1", "2"] for mm in pron[i+1:]):
							ret_list.append(pron[i:])
							return ret_list
						elif all(mm[-1] in ["0", "1", "2"] for mm in pron[i+1:]):
							for i in pron: ret_list.append([i])
							return ret_list
						else: ret_str += pron[i]; list_str += [pron[i]]
				else:
					if last_is_vowel:
						pron_rem = pron[i+1:]
						if pron_rem != []:
							if all(mm[-1] not in ["0", "1", "2"] for mm in pron_rem):
								if "0" in ret_str or "1" in ret_str or "2" in ret_str:
									ret_list.append(list_str)
									ret_str = "".join(pron[i:]); list_str = pron[i:]
									ret_list.append(list_str)
									return ret_list
								else:
									ret_str += "".join(pron[i:]); list_str += pron[i:]
									ret_list.append(list_str)
									return ret_list
							else:
								if pron[i+1][-1] not in ["0", "1", "2"]:
									if "0" in ret_str or "1" in ret_str or "2" in ret_str:
										ret_list.append(list_str)
										ret_str = pron[i]; list_str = [pron[i]]
									else:
										ret_str += pron[i]; list_str += [pron[i]]
										ret_list.append(list_str)
										ret_str = ""; list_str = []
								else:
									if "0" in ret_str or "1" in ret_str or "2" in ret_str:
										ret_list.append(list_str)
										ret_str = pron[i]; list_str = [pron[i]]
									else: ret_str += pron[i]; list_str += [pron[i]]
						else:
							if "0" in ret_str or "1" in ret_str or "2" in ret_str:
								ret_list += [list_str, [pron[i]]]
								return ret_list
							else:
								ret_str += pron[i]; list_str += [pron[i]]
								ret_list.append(list_str)
								return ret_list
					else:
						pron_rem = pron[i+1:]
						if pron_rem != []:
							if all(mm[-1] not in ["0", "1", "2"] for mm in pron_rem):
								ret_str += "".join(pron[i:]); list_str += pron[i:]
								ret_list.append(list_str)
								return ret_list
							else:
								if pron[i+1][-1] not in ["0", "1", "2"]:
									try:
										mmm = pron[i+2]
										if mmm[-1] in ["0", "1", "2"]:
											ret_str += pron[i]; list_str += [pron[i]]
											ret_list.append(list_str)
											ret_str = ""; list_str = []
										else: ret_str += pron[i]; list_str += [pron[i]]
									except IndexError: pass
								else:
									if "0" in ret_str or "1" in ret_str or "2" in ret_str:
										ret_list.append(list_str)
										ret_str = pron[i]; list_str = [pron[i]]
									else: ret_str += pron[i]; list_str += [pron[i]]
						else:
							ret_str += pron[i]; list_str += [pron[i]]
							ret_list.append(list_str)
							return ret_list
				last_is_vowel = True
			else:
				if i == 0:
					if pron_len == 1: return [[pron[i]]]
					else: ret_str += pron[i]; list_str += [pron[i]]
				else:
					if last_is_vowel:
						pron_rem = pron[i+1:]
						if pron_rem != []:
							if all(mm[-1] not in ["0", "1", "2"] for mm in pron_rem):
								ret_str += "".join(pron[i:]); list_str = [pron[i:]]
								ret_list.append(list_str)
								return ret_list
							else:
								if pron[i+1][-1] in ["0", "1", "2"]:
									if ret_str != "":
										ret_list.append(list_str)
										ret_str = pron[i]; list_str = [pron[i]]
									else: ret_str = pron[i]; list_str = [pron[i]]
								else:
									try:
										mmm = pron[i+2]
										if mmm[-1] in ["0", "1", "2"]:
											ret_str += pron[i]; list_str += [pron[i]]
											ret_list.append(list_str)
											ret_str = ""; list_str = []
										else: ret_str += pron[i]; list_str += [pron[i]]
									except IndexError: pass
						else:
							ret_str += pron[i]; list_str += [pron[i]]
							ret_list.append(list_str)
							return ret_list
					else:
						pron_rem = pron[i+1:]
						if pron_rem != []:
							if all(mm[-1] not in ["0", "1", "2"] for mm in pron_rem):
								ret_str += "".join(pron[i:]); list_str += pron[i:]
								ret_list.append(list_str)
								return ret_list
							else:
								if pron[i+1][-1] in ["0", "1", "2"]:
									if "0" in ret_str or "1" in ret_str or "2" in ret_str:
										ret_list.append(list_str)
										ret_str = pron[i]; list_str = [pron[i]]
									else: ret_str += pron[i]; list_str += [pron[i]]
								else:
									ret_str += pron[i]; list_str += [pron[i]]
									ret_list.append(list_str)
									ret_str = ""; list_str = []
						else:
							ret_str += pron[i]; list_str += [pron[i]]
							ret_list.append(list_str)
							return ret_list
				last_is_vowel = False
	if grouped:
		import pron_grouped
		return pron_grouped.group2(pron)
	else:
		return ungrouped(pron)
a=['AH1','EH11','NG1','GG1','AH1','TT1','IH1']
#a=['T','I2','DD', 'GG','AA2','T','U2','A2']
print(group2(a))
