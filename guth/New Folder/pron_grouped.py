def group2(pron):
	ret_list = []
	ret_str = ""
	last_is_vowel = False
	pron_len = len(pron)
	for i in range(pron_len):
		if pron[i][-1] in ["0", "1", "2"]:
			if i == 0:
				ret_str += pron[i]
			else:
				if last_is_vowel:
					pron_rem = pron[i+1:]
					if pron_rem != []:
						if all(mm[-1] not in ["0", "1", "2"] for mm in pron_rem) or all(mm[-1] in ["0", "1", "2"] for mm in pron_rem):
							ret_str += "".join(pron[i:])
							ret_list.append(ret_str)
							return " ".join(ret_list)
						else:
							if pron[i+1][-1] not in ["0", "1", "2"]:
								ret_str += pron[i]
								ret_list.append(ret_str)
								ret_str = ""
							else:
								if "0" in ret_str or "1" in ret_str or "2" in ret_str:
									ret_str += pron[i]
									ret_list.append(ret_str)
									ret_str = ""
								else:
									ret_str += pron[i]
					else:
						ret_str += pron[i]
						ret_list.append(ret_str)
						return " ".join(ret_list)
				else:
					pron_rem = pron[i+1:]
					if pron_rem != []:
						if all(mm[-1] not in ["0", "1", "2"] for mm in pron_rem) or all(mm[-1] in ["0", "1", "2"] for mm in pron_rem):
							ret_str += "".join(pron[i:])
							ret_list.append(ret_str)
							return " ".join(ret_list)
						else:
							if pron[i+1][-1] not in ["0", "1", "2"]:
								ret_str += pron[i]
								ret_list.append(ret_str)
								ret_str = ""
							else:
								ret_str += pron[i]
					else:
						ret_str += pron[i]
						ret_list.append(ret_str)
						return " ".join(ret_list)
			last_is_vowel = True
		else:
			if i == 0:
				ret_str += pron[i]
			else:
				if last_is_vowel:
					pron_rem = pron[i+1:]
					if pron_rem != []:
						if all(mm[-1] not in ["0", "1", "2"] for mm in pron_rem):
							ret_str += "".join(pron[i:])
							ret_list.append(ret_str)
							return " ".join(ret_list)
						else:
							if pron[i+1][-1] in ["0", "1", "2"]:
								ret_list.append(ret_str)
								ret_str = pron[i]
							else:
								if "0" in ret_str or "1" in ret_str or "2" in ret_str:
									ret_str += pron[i]
									ret_list.append(ret_str)
									ret_str = ""
								else:
									ret_str += pron[i]
					else:
						ret_str += pron[i]
						ret_list.append(ret_str)
						return " ".join(ret_list)
				else:
					pron_rem = pron[i+1:]
					if pron_rem != []:
						if all(mm[-1] not in ["0", "1", "2"] for mm in pron_rem):
							ret_str += "".join(pron[i:])
							ret_list.append(ret_str)
							return " ".join(ret_list)
						else:
							if pron[i+1][-1] in ["0", "1", "2"]:
								if "0" in ret_str or "1" in ret_str or "2" in ret_str:
									ret_list.append(ret_str)
									ret_str = pron[i]
								else: ret_str += pron[i]
							else:
								ret_str += pron[i]
								ret_list.append(ret_str)
								ret_str = ""
					else:
						ret_str += pron[i]
						ret_list.append(ret_str)
						return " ".join(ret_list)
			last_is_vowel = False
