import re, random
from os import mkdir

be_smart = True
limit = 0
pron_use_cmd = True
with_support = True
cmudict_has_pos = True
pron_syll_no = True
verbose = True
very_verbose = False
use_gen_cmd = True
silent = ['HH']
transform = {'NG':['N','G']}
alt_in_caps = False

include_pos = False
accented = False
pron_str = False
m_as_group = False
anyhow = False
reverse_all_pron = False
y_sign = chr(165)


ltw = {"N":"noun", "p":"plural", "h":"noun phrase","V":"verb(participle)","t":"verb(transitive)", "i":"verb(intransitive)", "A":"adjective", "v":"adverb", "C":"conjunction", "P":"preposition","!":"interjection", "r":"pronoun", "D":"definite article", "I":"indefinite article", "o":"nominative"}
wtl = {}
for key, value in ltw.items(): wtl[value] = key

gen_cmd_wtp = ( ("AW"), ("AY"), ("IY","IH"), ("EY"),("OY"), ("UH","UW"), ("AE","AH","AA") ,("AO"),("EH","ER"), ("OW") )
cmd_wtp = (("AE"),("AW"),("AY"),("IY"),("IH"),("EY"),("OY"),("UH"),("UW"),("AH"),("AO"),("AA"),("EH"),("OW"),("ER"))

gen_c =(('B'), ('D','DH'),('CH'),('F'),('G'),('HH'),('JH'),('K'),('L'),('M'),('N', 'NG'),('P'),('R'),('S'),('SH'), ('T','TH'), ('V'),('W'),('Y'),('Z'),('ZH'))
co_spec =(('D'),('T'),('B'),('CH'),('DH'),('F'),('G'),('HH'),('JH'),('K'),('L'),('M'),('N'),('NG'),('P'),('R'),('S'),('SH'),('TH'),('V'),('W'),('Y'),('Z'),('ZH'))


if not(use_gen_cmd):
    valv = cmd_wtp
    valc = co_spec
else:
    valv = gen_cmd_wtp
    valc = gen_c

def write_to_file(data, file_path=None, delimiter=", ", action=1, columns=3):
        def normal(dat):
                if isinstance(dat, (str, int)): return str(dat)
                if isinstance(dat, (list, tuple)):
                    s = "("
                    for i in dat: s += normal(i)+"         "
                    return s.rstrip()+")"

        if action >= 0:
                import os
                if isinstance(data, dict):
                    if not(os.access(file_path, os.F_OK)): os.makedirs(file_path)
                else:
                    if not(os.access(file_path, os.F_OK)):
                        dirname = os.path.dirname(file_path)
                        try: os.makedirs(dirname)
                        except FileExistsError: pass
                    file_path_fd = open(file_path, "w")
        if isinstance(data, (list, tuple)):
                ten = " "*10
                count = 1
                for item in data:
                    text = normal(item)
                    if count == columns:
                            if action == 0:
                                    file_path_fd.write(text+"\n")
                                    print(text)
                            elif action > 0: file_path_fd.write(text+"\n")
                            else: print(text)
                            count = 1
                    else:
                            if action == 0:
                                    file_path_fd.write(text+ten)
                                    print(text, end="\t")
                            elif action > 0: file_path_fd.write(text+ten)
                            else: print(text, end="\t")
                            count += 1
        elif isinstance(data, str):
                data = data.split(delimiter)
                write_to_file(data, file_path, action=action, columns=columns)
        elif isinstance(data, dict):
            for k,v in data.items():
                write_to_file(v, file_path+"/"+str(k)+".txt", delimiter, action, columns)
            return
        if action >= 0: file_path_fd.close()

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

def group2_imp(pron, grouped=False):
        def check_i_vowel(obj):
                if isinstance(obj, str):
                        if obj[-1] in ["0","1","2"]: return True
                elif isinstance(obj, list):
                        if isinstance(obj[0], list):
                                if obj[0][0][-1] in ["0","1","2"]: return True
                        else:
                                if obj[0][-1] in ["0","1","2"]: return True
                return False
        def vowel_i_hold(hold):
                for i in hold:
                        if check_i_vowel(i): return True
                return False    
        def ungrouped(pron):
                ret_list = []
                list_str = []
                pron_len = len(pron)
                for i in range(pron_len):
                        if check_i_vowel(pron[i]):
                                if i == 0:
                                        if pron_len == 1: return [[pron[i]]]
                                        else:
                                                if all(not check_i_vowel(mm) for mm in pron[i+1:]):
                                                        ret_list.append(pron[i:])
                                                        return ret_list
                                                elif all(check_i_vowel(mm) for mm in pron[i+1:]):
                                                        for i in pron: ret_list.append([i])
                                                        return ret_list
                                                else: list_str += [pron[i]]
                                else:
                                        if last_is_vowel:
                                                pron_rem = pron[i+1:]
                                                if pron_rem != []:
                                                        if all(not check_i_vowel(mm) for mm in pron_rem):
                                                                if vowel_i_hold(list_str):
                                                                        ret_list.append(list_str)
                                                                        list_str = pron[i:]
                                                                        ret_list.append(list_str)
                                                                        return ret_list
                                                                else:
                                                                        list_str += pron[i:]
                                                                        ret_list.append(list_str)
                                                                        return ret_list
                                                        else:
                                                                if not check_i_vowel(pron[i+1]):
                                                                        if vowel_i_hold(list_str):
                                                                                ret_list.append(list_str)
                                                                                list_str = [pron[i]]
                                                                        else:
                                                                                ret_str += pron[i]; list_str += [pron[i]]
                                                                                ret_list.append(list_str)
                                                                                list_str = []
                                                                else:
                                                                        if vowel_i_hold(list_str):
                                                                                ret_list.append(list_str)
                                                                                list_str = [pron[i]]
                                                                        else: list_str += [pron[i]]
                                                else:
                                                        if vowel_i_hold(list_str):
                                                                ret_list += [list_str, [pron[i]]]
                                                                return ret_list
                                                        else:
                                                                list_str += [pron[i]]
                                                                ret_list.append(list_str)
                                                                return ret_list
                                        else:
                                                pron_rem = pron[i+1:]
                                                if pron_rem != []:
                                                        if all(not check_i_vowel(mm) for mm in pron_rem):
                                                                list_str += pron[i:]
                                                                ret_list.append(list_str)
                                                                return ret_list
                                                        else:
                                                                if not check_i_vowel(pron[i+1]):
                                                                        try:
                                                                                mmm = pron[i+2]
                                                                                if check_i_vowel(mmm):
                                                                                        list_str += [pron[i]]
                                                                                        ret_list.append(list_str)
                                                                                        list_str = []
                                                                                else: list_str += [pron[i]]
                                                                        except IndexError: pass
                                                                else:
                                                                        if vowel_i_hold(list_str):
                                                                                ret_list.append(list_str)
                                                                                list_str = [pron[i]]
                                                                        else: list_str += [pron[i]]
                                                else:
                                                        list_str += [pron[i]]
                                                        ret_list.append(list_str)
                                                        return ret_list
                                last_is_vowel = True
                        else:
                                if i == 0:
                                        if pron_len == 1: return [[pron[i]]]
                                        else: list_str += [pron[i]]
                                else:
                                        if last_is_vowel:
                                                pron_rem = pron[i+1:]
                                                if pron_rem != []:
                                                        if all(not check_i_vowel(mm) for mm in pron_rem):
                                                                list_str = [pron[i:]]
                                                                ret_list.append(list_str)
                                                                return ret_list
                                                        else:
                                                                if check_i_vowel(pron[i+1]):
                                                                        if list_str != []:
                                                                                ret_list.append(list_str)
                                                                                list_str = [pron[i]]
                                                                        else: list_str = [pron[i]]
                                                                else:
                                                                        try:
                                                                                mmm = pron[i+2]
                                                                                if check_i_vowel(mmm):
                                                                                        list_str += [pron[i]]
                                                                                        ret_list.append(list_str)
                                                                                        list_str = []
                                                                                else: list_str += [pron[i]]
                                                                        except IndexError: pass
                                                else:
                                                        list_str += [pron[i]]
                                                        ret_list.append(list_str)
                                                        return ret_list
                                        else:
                                                pron_rem = pron[i+1:]
                                                if pron_rem != []:
                                                        if all(not check_i_vowel(mm) for mm in pron_rem):
                                                                list_str += pron[i:]
                                                                ret_list.append(list_str)
                                                                return ret_list
                                                        else:
                                                                if check_i_vowel(pron[i+1]):
                                                                        if vowel_i_hold(list_str):
                                                                                ret_list.append(list_str)
                                                                                list_str = [pron[i]]
                                                                        else: list_str += [pron[i]]
                                                                else:
                                                                        list_str += [pron[i]]
                                                                        ret_list.append(list_str)
                                                                        list_str = []
                                                else:
                                                        list_str += [pron[i]]
                                                        ret_list.append(list_str)
                                                        return ret_list
                                last_is_vowel = False
        if grouped:
                print("Group function isn't available for now.")
                #import pron_grouped
                #return pron_grouped.group2(pron)
                return ungrouped(pron)
        else:
                return ungrouped(pron)

                

# THE ACTIVATORS
# THIS FUNCTION IS FUCKED UP! ANDROID KEEPS KILLING IT!!
def activate2(*words):
        import total
        if "all" in words:
                activate("alt","pron","syl","pos")
                return
        if "alt" in words:
                global alt_file_fd_content_len
                try:
                        if alt_file_fd_content_len: pass
                except NameError:
                        alt_file_fd_content_len = total.alt_file_fd_content_len()
                        alt_file_fd_content_lists = total.alt_file_fd_content_lists()
        if "pos" in words:
                global pos_file_fd_content_len
                try:
                        if pos_file_fd_content_len: pass
                except NameError:
                        pos_file_fd_content_len = total.pos_file_fd_content_len()
                        pos_file_fd_content_lists_word = total.pos_file_fd_content_lists_word()
                        pos_file_fd_content_lists_pos = total.pos_file_fd_content_lists_pos()
        if "syl" in words:
                global hype_file_fd_content_len
                try:
                        if hype_file_fd_content_len: pass
                except NameError:
                        hype_file_fd_content_len = total.hype_file_fd_content_len()
                        hype_file_fd_content_word = total.hype_file_fd_content_word()
                        hype_file_fd_content_nos = total.hype_file_fd_content_nos()
                        hype_file_fd_content_s = total.hype_file_fd_content_s()
        if "pron" in words:
                global pron_cmd_fd_content_len
                try:
                        if pron_cmd_fd_content_len: pass
                except NameError:
                        pron_cmd_fd_content_len = total.pron_cmd_fd_content_len()
                        pron_cmd_fd_content_word = total.pron_cmd_fd_content_word()
                        pron_cmd_fd_content_pron = total.pron_cmd_fd_content_pron()
                        pron_cmd_fd_content_syll_no = total.pron_cmd_fd_content_syll_no()
        
def activate(*words):
        if "all" in words:
                activate("alt","pron","syl","pos")
                return
        pos_file = "C:\\Users\\USER\\Music\\lyricc\\gutenberg\\part of speech\\files\\mobypos.txt"
        #pos_file = r"/storage/emulated/0/gutenberg/part of speech/files/mobypos.txt"
        hype_file = "C:\\Users\\USER\\Music\\lyricc\\gutenberg\\hyphen\\files\\mhyph.txt"
        #hype_file = r"/storage/emulated/0/gutenberg/hyphen/files/mhyph.txt"
        pron_cmd = "C:\\Users\\USER\\Music\\lyricc\\gutenberg\\pronunciation\\files\\cmudictTotal.txt"
        #pron_cmd = r"/storage/emulated/0/gutenberg/pronunciation/files/cmudictTotal.txt"
        pron_support = "C:\\Users\\USER\\Music\\lyricc\\gutenberg\\pronunciation\\files\\cmudict_support.txt"
        #pron_support = r"/storage/emulated/0/gutenberg/pronunciation/files/cmudict_support.txt"
        alt_file = "C:\\Users\\USER\\Music\\lyricc\\gutenberg\\alt\\files\\mthesaur.txt"
        #alt_file = r"/storage/emulated/0/gutenberg/alt/files/mthesaur.txt"
        if "alt" in words:
                global alt_file_fd_content_len
                try:
                        if alt_file_fd_content_len: pass
                except NameError:
                        with open(alt_file, encoding="iso8859-1") as alt_file_fd:
                                alt_file_fd_content = alt_file_fd.readlines()
                                alt_file_fd_content_len = len(alt_file_fd_content)
                        global alt_file_fd_content_lists
                        alt_file_fd_content_lists = []
                        for line in alt_file_fd_content:
                                line = line.rstrip("\n").lower().split(",")
                                for i in range(len(line)):
                                    if " " in line[i]: line[i] = line[i].replace(" ", "-")
                                alt_file_fd_content_lists.append(line)
                        alt_file_fd_content_lists = tuple(alt_file_fd_content_lists)
                        """
                        l = ["alt_file_fd_content_len", "alt_file_fd_content_lists"]
                        for i in l:
                                with open(dire+i, "w") as i_fd:
                                        json.dump(eval(i), i_fd)"""
        if "pos" in words:
                global pos_file_fd_content_len
                try:
                        if pos_file_fd_content_len: pass
                except NameError:
                        with open(pos_file, encoding="iso8859-1")  as pos_file_fd:
                                pos_file_fd_content = pos_file_fd.readlines()
                                pos_file_fd_content_len = len(pos_file_fd_content)
                        global pos_file_fd_content_lists_word, pos_file_fd_content_lists_pos
                        pos_file_fd_content_lists_word, pos_file_fd_content_lists_pos = [], []
                        for line in pos_file_fd_content:
                                split = line.rstrip("\n").rsplit("\\", 1)
                                pos_file_fd_content_lists_word.append(split[0].lower())
                                pos_file_fd_content_lists_pos.append(split[1])
                        pos_file_fd_content_lists_word, pos_file_fd_content_lists_pos = tuple(pos_file_fd_content_lists_word), tuple(pos_file_fd_content_lists_pos)
                        """
                        l = ["pos_file_fd_content_lists_word", "pos_file_fd_content_lists_pos", "pos_file_fd_content_len"]
                        for i in l:
                                with open(dire+i, "w") as i_fd:
                                        json.dump(eval(i), i_fd)"""
        if "syl" in words:
                global hype_file_fd_content_len
                try:
                        if hype_file_fd_content_len: pass
                except NameError:
                        with open(hype_file, encoding="iso8859-1")  as hype_file_fd:
                                hype_file_fd_content = hype_file_fd.readlines()
                                hype_file_fd_content_len = len(hype_file_fd_content)
                        global hype_file_fd_content_word, hype_file_fd_content_nos, hype_file_fd_content_s
                        hype_file_fd_content_word, hype_file_fd_content_nos, hype_file_fd_content_s = [], [], []
                        for line in hype_file_fd_content:
                                line = line.rstrip("\n").strip().lower()
                                if " " in line:
                                        word = line.replace(" ","-")
                                        split = line.split()
                                        pron = []
                                        syllables = 0
                                        for whole_word in split:
                                                sp = whole_word.split(y_sign)
                                                syllables += len(sp)
                                                pron += sp
                                else:
                                        word = line
                                        if "-" in line:
                                                split = line.split("-")
                                                pron = []
                                                syllables = 0
                                                for whole_word in split:
                                                        sp = whole_word.split(y_sign)
                                                        syllables += len(sp)
                                                        pron += sp
                                        else:
                                                split = line.split(y_sign)
                                                syllables = len(split)
                                                pron = split
                                word = word.replace(y_sign, "")
                                hype_file_fd_content_word.append(word)
                                hype_file_fd_content_nos.append(syllables)
                                hype_file_fd_content_s.append(pron)
                        hype_file_fd_content_word, hype_file_fd_content_nos, hype_file_fd_content_s = tuple(hype_file_fd_content_word), tuple(hype_file_fd_content_nos), tuple(hype_file_fd_content_s)
                        """
                        l = ["hype_file_fd_content_len", "hype_file_fd_content_word", "hype_file_fd_content_nos", "hype_file_fd_content_s"]
                        for i in l:
                                with open(dire+i, "w") as i_fd:
                                        json.dump(eval(i), i_fd)"""
        if "pron" in words:
                global pron_cmd_fd_content_len
                try:
                        if pron_cmd_fd_content_len: pass
                except NameError:
                        with open(pron_cmd, encoding="iso8859-1") as pron_cmd_fd:
                                pron_cmd_fd_content = pron_cmd_fd.readlines()
                                pron_cmd_fd_content_len = len(pron_cmd_fd_content)
                        if with_support:
                                with open(pron_support, encoding="iso8859-1") as pron_cmd_fd:
                                        li = pron_cmd_fd.readlines()
                                        pron_cmd_fd_content += li
                                        pron_cmd_fd_content_len += len(li)
                        global pron_cmd_fd_content_word, pron_cmd_fd_content_pron
                        if include_pos:
                                global pron_cmd_fd_content_pos
                                pron_cmd_fd_content_pos = []
                        if pron_syll_no:
                                global pron_cmd_fd_content_syll_no
                                pron_cmd_fd_content_syll_no = []
                        if pron_str:
                                global pron_cmd_fd_content_str
                                pron_cmd_fd_content_str = []
                        pron_cmd_fd_content_word, pron_cmd_fd_content_pron = [], []
                        for line in pron_cmd_fd_content:
                                line = line.rstrip("\n")
                                split = line.split()
                                pron_word = split[0]
                                if cmudict_has_pos:
                                        if include_pos:
                                                pron_cmd_fd_content_pos.append(split[1])
                                        split = split[2:]
                                else: split = split[1:]
                                if pron_syll_no or pron_str or transform:
                                        phones = " ".join(split)
                                if pron_syll_no:
                                        #syll_no = len(group2(split))
                                        syll_no = sum(phones.count(i) for i in '012')
                                        pron_cmd_fd_content_syll_no.append(syll_no)
                                if pron_str:
                                        pron_cmd_fd_content_str.append(re.sub(r"[^012]", "", phones).replace("2","1"))
                                if transform:
                                        for key,value in transform.items():
                                                value = ' '.join(value)
                                                if value in phones:
                                                        split = phones.replace(value, key)
                                        if isinstance(split, str):
                                                split = split.split()
                                if silent:
                                        for cons in silent:
                                                while cons in split: split.remove(cons)
                                pron_cmd_fd_content_word.append(pron_word.lower())
                                if reverse_all_pron:
                                        pron_cmd_fd_content_pron.append(split[::-1])
                                else: pron_cmd_fd_content_pron.append(split)
                        if pron_syll_no: pron_cmd_fd_content_syll_no = tuple(pron_cmd_fd_content_syll_no)
                        if include_pos: pron_cmd_fd_content_pos = tuple(pron_cmd_fd_content_pos)
                        if pron_str: pron_cmd_fd_content_str = tuple(pron_cmd_fd_content_str)
                        pron_cmd_fd_content_word, pron_cmd_fd_content_pron = tuple(pron_cmd_fd_content_word), tuple(pron_cmd_fd_content_pron)
                        """
                        l = ["pron_cmd_fd_content_len", "pron_cmd_fd_content_word", "pron_cmd_fd_content_pron", "pron_cmd_fd_content_syll_no"]
                        for i in l:
                                with open(dire+i, "w") as i_fd:
                                        json.dump(eval(i), i_fd)"""

# FOR PART OF SPEECH
"""
def perm(word, skip=False):
        global pos_file_fd_content_lists_word, limit
        try:
                id = pos_file_fd_content_lists_word.index(word)
                return id
        except ValueError:
                if len(word) == 1: n = word[0].swapcase()
                else: n = word[0].swapcase()+word[1:]
                try: 
                        id = pos_file_fd_content_lists_word.index(n)
                        return id
                except ValueError:
                        try:
                                id = pos_file_fd_content_lists_word.index(word.title())
                                return id
                        except ValueError:
                                if limit < 1 or limit == 3:
                                        if word.isupper(): word2 = word.lower()
                                        else: word2 = word.upper()
                                        limit += 1
                                        id = perm(word2)
                                        if id > -1: limit = 0
                                        return id
                                elif limit < 4:
                                        word = word.replace('-', ' ')
                                        limit += 1
                                        id= perm(word)
                                        return id
                                else:
                                        limit = 0
                                       return -1
"""
def get_pos_word(words,exactly='atleast', dbwords=None, use_pron_pos=False):
        ret_list = []
        for i in range(len(words)): words[i] = wtl[words[i]]
        def filter(words, pos, exactly, word):
                if exactly == "atleast":
                                if all(letter in pos for letter in words): ret_list.append(word)
                elif exactly == "any":
                        for letter in words:
                                if letter in pos:
                                        ret_list.append(word)
                                        break
                elif exactly == "exactly":
                        if len(words) == len(pos):
                                if all(letter in pos for letter in words): ret_list.append(word)
        if use_pron_pos:
                global pron_cmd_fd_content_pos, pron_cmd_fd_content_word, pron_cmd_fd_content_len
                if dbwords:
                        for word in dbwords:
                                if word in pron_cmd_fd_content_word:
                                        id = pron_cmd_fd_content_word.index(word)
                                        pos = pron_cmd_fd_content_pos[id]
                                        if pos == "*": continue
                                        filter(words, pos, exactly, word)
                else:
                        for i in range(pron_cmd_fd_content_len):
                                pos = pron_cmd_fd_content_pos[i]
                                if pos == "*": continue
                                filter(words, pos, exactly, pron_cmd_fd_content_word[i])
        else:
                global pos_file_fd_content_lists_word, pos_file_fd_content_lists_pos, pos_file_fd_content_len
                if dbwords:
                        for word in dbwords:
                            if word in pos_file_fd_content_lists_word:
                                pos = pos_file_fd_content_lists_pos[pos_file_fd_content_lists_word.index(word)]
                                filter(words, pos, exactly, word)
                else:
                        for i in range(pos_file_fd_content_len):
                                pos = pos_file_fd_content_lists_pos[i]
                                filter(words, pos, exactly, pos_file_fd_content_lists_word[i])
        return ret_list

def get_word_pos(word, use_pron_pos=False):
        if word.isspace() or len(word) < 1 : return []
        if use_pron_pos:
                global pron_cmd_fd_content_pos, pron_cmd_fd_content_word
                if word in pron_cmd_fd_content_word:
                        id = pron_cmd_fd_content_word.index(word)
                        paofsp = []
                        for letter in pron_cmd_fd_content_pos[id]: paofsp.append(ltw[letter])
                        return paofsp
                else: return []
        else:
                global limit, pos_file_fd_content_len, pos_file_fd_content_lists_word, pos_file_fd_content_lists_pos
                def get_word_pos_plural(word, second=False):
                        #print("calling for plural")
                        global limit
                        if limit >= 1:
                                #print("was returning here")
                                return []
                        limit += 1
                        word_len = len(word)
                        if word.endswith("ies"):
                                new_word = word[:word_len-3]+"y"
                                result = get_word_pos(new_word)
                                if result == []:return []
                                else: return ['noun','plural']
                        elif word.endswith("es") and not second:
                                #print("first")
                                limit += 1
                                new_word = word[:word_len-2]
                                result = get_word_pos(new_word)
                                if result == []:return []
                                else: return ['noun','plural']
                        elif word.endswith("es") and second:
                                #print("second")
                                new_word = word[:word_len-1]
                                result = get_word_pos(new_word)
                                if result == []:return []
                                else: return ['noun','plural']
                        elif word.endswith("s"):
                                new_word = word[:word_len-1]
                                result = get_word_pos(new_word)
                                if result == []:return []
                                else: return ['noun','plural']
                        elif word.endswith("ing"):
                                new_word = word[:word_len-3]
                                result = get_word_pos(new_word)
                                if result == []:return []
                                else: return ['noun', 'verb(participle)']
                        else:
                                return []
                if word in pos_file_fd_content_lists_word:
                        i = pos_file_fd_content_lists_word.index(word)
                        paofsp = []
                        for letter in pos_file_fd_content_lists_pos[i]:
                                paofsp.append(ltw[letter])
                        #print("something was returned", paofsp)
                        return paofsp
                else:
                        if be_smart:
                                #print("was smart", limit)
                                if limit >= 1: return []
                                res=get_word_pos_plural(word)
                                if not(res):
                                        if limit >= 2:
                                                limit = 0
                                                res = get_word_pos_plural(word, True)
                                                limit = 0
                                                return res
                                limit = 0
                                return res
                        else: return []

# FOR SYLLABLE
def get_syllable_no_word(number, exactly=0, dbwords=None):
        global hype_file_fd_content_len, hype_file_fd_content_word, hype_file_fd_content_nos
        ret_list = []
        number = int(number)
        if dbwords:
                for word in dbwords:
                    if word in hype_file_fd_content_word:
                                syllables=hype_file_fd_content_nos[hype_file_fd_content_word.index(word)]
                                if exactly == 0 and syllables == number: ret_list.append(word)
                                elif exactly > 0 and syllables >= number: ret_list.append(word)
                                elif exactly < 0 and syllables <= number: ret_list.append(word)
        else:
                for i in range(hype_file_fd_content_len):
                        word = hype_file_fd_content_word[i]
                        syllables = hype_file_fd_content_nos[i]
                        if exactly == 0 and syllables == number: ret_list.append(word)
                        elif exactly > 0 and syllables >= number: ret_list.append(word)
                        elif exactly < 0 and syllables <= number: ret_list.append(word)
        return ret_list

def get_word_syllable_no(word):
        if word.isspace(): return "EMPTY"
        global limit, hype_file_fd_content_len, hype_file_fd_content_word, hype_file_fd_content_nos
        if word in hype_file_fd_content_word:
                return hype_file_fd_content_nos[hype_file_fd_content_word.index(word)]
        else: return "NOT RECOGNIZED"
def get_word_syllable(word):
        if word.isspace(): return "EMPTY"
        global hype_file_fd_content_len, hype_file_fd_content_s, hype_file_fd_content_word
        if word in hype_file_fd_content_word:
                return " ".join(hype_file_fd_content_s[hype_file_fd_content_word.index(word)])
        return "NOT RECOGNIZED"

# FOR PRONUNCIATION
#        Syllabes
def pron_get_syll_no_word(number, exactly=0, dbwords=None):
        ret_list = []
        global pron_cmd_fd_content_word, pron_cmd_fd_content_syll_no, pron_cmd_fd_content_len
        if dbwords:
                for word in dbwords:
                    if word in pron_cmd_fd_content_word:
                        syllables=pron_cmd_fd_content_syll_no[pron_cmd_fd_content_word.index(word)]
                        if exactly == 0 and syllables == number: ret_list.append(word)
                        elif exactly > 0 and syllables >= number: ret_list.append(word)
                        elif exactly < 0 and syllables <= number: ret_list.append(word)
        else:
                for i in range(pron_cmd_fd_content_len):
                        word=pron_cmd_fd_content_word[i]
                        syllables=pron_cmd_fd_content_syll_no[i]
                        if exactly == 0 and syllables == number: ret_list.append(word)
                        elif exactly > 0 and syllables >= number: ret_list.append(word)
                        elif exactly < 0 and syllables <= number: ret_list.append(word)
        return ret_list

#        Stress
def pron_get_word_stress(word):
        global pron_cmd_fd_content_word, pron_cmd_fd_content_str, pron_cmd_fd_content_len
        stress = ""
        word = word.lower().strip()
        if " " in word:
            words = word.split()
        else:
            words = [word]
        for w in words:
            if w in pron_cmd_fd_content_word:
                stress += pron_cmd_fd_content_str[pron_cmd_fd_content_word.index(w)]
            else:
                print("word not found")
                return ""
        return stress

def pron_get_words_stress(pat, word, fil=None):
    stress_list = generate_diff_pron(pat, True)
    word_list = generate_word_str(stress_list)
    print_word_str(stress_list, word_list, fil, pat, word)

def pron_get_word_with_str(pat, mode="exactly", dbwords=None):
        global pron_cmd_fd_content_word, pron_cmd_fd_content_str, pron_cmd_fd_content_len
        matches = []
        regexp = re.compile(pat)
        if dbwords:
                for word in dbwords:
                    if word in pron_cmd_fd_content_word:
                        st=pron_cmd_fd_content_str[pron_cmd_fd_content_word.index(word)]
                        if regexp.search(st):
                                matches.append(word)
        else:
                for i in range(pron_cmd_fd_content_len):
                        word = pron_cmd_fd_content_word[i]
                        st=pron_cmd_fd_content_str[i]
                        if mode == "in":
                            if regexp.search(st):
                                matches.append(word)
                        elif mode == "exactly":
                            if pat == st or pat == "^" + st + "$":
                                matches.append(word)
        return matches
def generate_word_str(listt):
        ret_list = []
        for i in listt:
                if verbose: print(i)
                syl = int(i[-1])
                i = i[:len(i)-1]
                result = pron_get_word_with_str("".join(i))
                if result == []:
                        ret_list.append([])
                        continue
                #result = trim_to_syllable(result, syl)
                ret_list.append(result)
        return ret_list
def print_word_str(pron_list, word_list, fil2, pr, words):
        if fil2:
                wr = False
                #fil = open(fil2+"\\"+words.replace(" ","-")+".txt", "w")
                fil = open(fil2+"/"+words.replace(" ","-")+".txt", "w")
        else: wr = True
        line = "-"*20
        ex = exe(pr)
        for whole in ex:
                whole_l = []
                t = ""
                for each in whole:
                        each = flatten(each)
                        t += "["+"".join(each)+"]"
                        for i in range(len(pron_list)):
                                pr = pron_list[i][:]
                                pr.pop()
                                pr = ["".join(pr)]
                                if each == pr:
                                    whole_l.append(word_list[i])
                                    break
                if wr:
                        print("\n\n----------------------------------------")
                        print(t)
                else:
                        fil.write("\n\n\n------------------------------------\n")
                        fil.write(t+"\n")
                hold = []
                count = 0
                for i in range(1000):
                        t = ""
                        for j in whole_l:
                                if j: t += random.choice(j)+" "
                                else:
                                        t = "-------"
                                        break
                        if t == "-------": continue
                        t = t.rstrip()
                        if t not in hold:
                                if count < 4:
                                        if wr: print(t, end=", ")
                                        else: fil.write(t+"     ")
                                        count += 1
                                else:
                                        if wr: print(t)
                                        else: fil.write(t+"\n")
                                        count = 0
                                hold.append(t)

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

def is_vowel_cmd(first, second, listed=False):
        if not(listed):
                if first[-1] in ["0", "1", "2"] and second[-1] in ["0", "1", "2"]: return True
                return False
        else:
            first, second = first[0], second[0]
            while isinstance(first[0], list): first = first[0]
            while isinstance(second[0], list): second = second[0]
            return is_vowel_cmd(first[0], second[0])
def is_a_vowel_cmd(first):
        if first[-1] in ["0", "1", "2"]: return  True
        return False
def is_consonant_cmd(first, second, listed=False):
        if not(listed):
                if first[-1] not in ["0", "1", "2"] and second[-1] not in ["0", "1", "2"]: return True
                return False
        else: return is_consonant_cmd(first[0], second[0])
def match_vowel_cmd(first, second):
        for values in valv:
            if first[:-1] in values and second[:-1] in values: return True
        return False

def match_conso_cmd(first, second):
        for values in valc:
                if first in values and second in values: return True
        return False

def pron_trim_to_syllable(word, number=1, exactly=0):
        ret_list = []
        global pron_cmd_fd_content_word, pron_cmd_fd_content_syll_no
        for i in word:
                if verbose: print("doing", i)
                res = pron_cmd_fd_content_syll_no[pron_cmd_fd_content_word.index(i)]
                if exactly == 0 and res == number: ret_list.append(i)
                elif exactly < 0 and res <= number: ret_list.append(i)
                elif exactly > 0 and res >= number: ret_list.append(i)
        return ret_list

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

def all_in(first, second, better=False):
        first, second = list(first), list(second)
        for i in range(len(first)):
                if is_a_vowel_cmd(first[i]): first[i] = first[i][:len(first[i])-1]
        for i in range(len(second)):
                if is_a_vowel_cmd(second[i]): second[i] = second[i][:len(second[i])-1]
        if all(i in first for i in second):
                if better:
                        if all(i in second for i in first): return 1
                        else: return 2
                else: return True
        else: return False

def all_in_match(first, second, better=False, type='v'):
        first, second = first[:], second[:]
        if not isinstance(first, list) or not isinstance(second, list):
                raise TypeError("all_in_match: arguments are not list.")
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

def mv_c(pron, split, mt='v', cmt='atleast', grouped=False, ml=1,me=1):
        matched = 0
        if mt == 'v':
                if grouped:
                        zipped = zip(group(pron[::-1]), group(split[::-1]))
                        for item in zipped:
                                if is_vowel_cmd(*item, listed=True):
                                        if cmt == "atleast":
                                                if (all_in_match(item[0], item[1])):
                                                    matched += 1
                                                    if (me > 0 and matched >= ml): return True
                                                else: break
                                        elif cmt == "exactly":
                                                r = all_in_match(item[0], item[1], True)
                                                if r == 1:
                                                    matched += 1
                                                    if (me > 0 and matched >= ml): return True
                                                else: break
                                        elif cmt == "any":
                                                yes = False
                                                for a in item[1]:
                                                        for b in item[0]:
                                                                if match_vowel_cmd(a, b):
                                                                        yes = True
                                                                        break
                                                if yes:
                                                    matched += 1
                                                    if (me > 0 and matched >= ml): return True
                                                else: break
                                elif is_consonant_cmd(*item, listed=True):
                                        if anyhow: continue
                                        else:
                                                if cmt == 'atleast':
                                                        if (all_in_match(item[0], item[1], type='c')): continue
                                                        else: break
                                                elif cmt == 'exactly':
                                                        r = all_in_match(item[0], item[1], True, 'c')
                                                        if r == 1: continue
                                                        else: break
                                                elif cmt == 'any':
                                                        yes = False
                                                        for a in item[1]:
                                                                for b in item[0]:
                                                                        if match_conso_cmd(a, b):
                                                                                yes = True
                                                                                break
                                                        if yes: continue
                                                        else: break
                                else: break
                else:
                        zipped = zip(pron[::-1], split[::-1])
                        for s in zipped:
                                if is_vowel_cmd(*s):
                                        if match_vowel_cmd(*s):
                                                matched += 1
                                                if (me > 0 and matched >= ml): return True
                                        else: break
                                elif is_consonant_cmd(*s):
                                        if anyhow:continue
                                        else:
                                                if match_conso_cmd(s[0],s[1]): continue
                                                else: break
                                else: break
        elif mt == 'c':
                if grouped:
                        zipped = zip(group(pron[::-1]), group(split[::-1]))
                        for item in zipped:
                                if is_consonant_cmd(*item, listed=True):
                                        if cmt == "atleast":
                                                if (all_in_match(item[0], item[1], type='c')):
                                                    matched += 1
                                                    if (me > 0 and matched >= ml): return True
                                                else: break
                                        elif cmt == "exactly":
                                                        r = all_in_match(item[0], item[1], True, 'c')
                                                        if r == 1:
                                                            matched += 1
                                                            if (me > 0 and matched >= ml): return True
                                                        else: break
                                        elif cmt == "any":
                                                yes = False
                                                for a in item[1]:
                                                        for b in item[0]:
                                                                if match_conso_cmd(a, b):
                                                                        yes = True
                                                                        break
                                                if yes:
                                                    matched += 1
                                                    if (me > 0 and matched >= ml): return True
                                                else: break
                                elif is_vowel_cmd(*item, listed=True):
                                        if anyhow: continue
                                        else:
                                                if cmt == 'atleast':
                                                        if (all_in_match(item[0], item[1])): continue
                                                        else: break
                                                elif cmt == 'exactly':
                                                        r = all_in_match(item[0], item[1], True)
                                                        if r and r == 1: continue
                                                        else: break
                                                elif cmt == 'any':
                                                        yes = False
                                                        for a in item[1]:
                                                                for b in item[0]:
                                                                        if match_vowel_cmd(a, b):
                                                                                yes = True
                                                                                break
                                                        if yes: continue
                                                        else: break
                                else: break
                else:
                        zipped = zip(pron[::-1], split[::-1])
                        for s in zipped:
                                if is_consonant_cmd(*s):
                                        if match_conso_cmd(*s):
                                                matched += 1
                                                if (me > 0 and matched >= ml): return True
                                        else: break
                                elif is_vowel_cmd(*s):
                                        if anyhow:continue
                                        else:
                                                if match_vowel_cmd(s[0],s[1]): continue
                                                else: break
                                else: break
        if (matched != 0) and ((me < 0 and matched <= ml) or (me == 0 and matched == ml) or (me > 0 and matched >= ml)): return True
        return False


def get_many(word):
        ret = []
        ret2 = []
        done = []
        global pron_cmd_fd_content_len, pron_cmd_fd_content_word, pron_cmd_fd_content_pron, pron_cmd_fd_content_syll_no
        for i in range(pron_cmd_fd_content_len):
                w = pron_cmd_fd_content_word[i]
                if word in w:
                        if (word == w) or (word+"(" in w and w.startswith(word)): ret.append(i)
        for i in ret:
                pron_i = pron_cmd_fd_content_pron[i]
                rem = ret[ret.index(i)+1:]
                if rem:
                        for j in rem:
                                if i in done: continue
                                pron_j = pron_cmd_fd_content_pron[j]
                                if mv_c(pron_i, pron_j, "v", "exactly", True, pron_cmd_fd_content_syll_no[i], 0): done.append(j)
                                if i not in ret2: ret2.append(i)
                else:
                        if i not in done: ret2.append(i)
        print(pron_cmd_fd_content_word[-2:])
        return ret2

def remove_duplicates(li):
                ret = []
                done = []
                li = list(set(li))
                for i in li:
                        rem = li[li.index(i)+1:]
                        if rem:
                                for j in rem:
                                        if i in done: continue
                                        if (is_a_vowel_cmd(i) and is_a_vowel_cmd(j) and match_vowel_cmd(i,j)) or (not is_a_vowel_cmd(i) and not is_a_vowel_cmd(j) and match_conso_cmd(i,j)): done.append(j)
                                        if i not in ret: ret.append(i)
                        else:
                                if i not in done: ret.append(i)
                return ret
def remove_same(*lists):
                ret = []
                ret_n = []
                done = []
                for i in lists:
                        rem = lists[lists.index(i)+1:]
                        if rem:
                                for j in rem:
                                        if i in done: continue
                                        if is_a_vowel_cmd(i[0]): mt = "v"
                                        else: mt = "c"
                                        if len(i) > len(j): res = all_in_match(i, j, True, mt)
                                        else: res = all_in_match(j, i, True, mt)
                                        if res == 1: done.append(j)
                                        if i not in ret:
                                                ret.append(i)
                                                if len(i) == 1: ret_n.append(i[0])
                                                else: ret_n.append(i)
                        else:
                                if i not in done:
                                        ret.append(i)
                                        if len(i) == 1: ret_n.append(i[0])
                                        else: ret_n.append(i)
                if len(ret_n) == 1: return ret_n[0]
                return ret_n
        
def get_word_pron(word):
        if word.isspace(): return "EMPTY"
        global pron_cmd_fd_content_word, pron_cmd_fd_content_len, pron_cmd_fd_content_pron
        if accented:
                #from itertools import zip_longest
                ret = []
                r = get_many(word)
                if r:
                        """
                        for i in r: ret.append(group(pron_cmd_fd_content_pron[i]))#[::-1])
                        ret = list(zip_longest(*ret))#[::-1]
                        for i in range(len(ret)):
                                ret[i] = list(ret[i])
                                while None in ret[i]: ret[i].remove(None)
                                ret[i] = remove_same(*ret[i])
                        return ret
                        """
                        ret.append(pron_cmd_fd_content_pron[i])
                        return ret
                else: return []
        else:
                if word in pron_cmd_fd_content_word:
                        pron = pron_cmd_fd_content_pron[pron_cmd_fd_content_word.index(word)]
                        return " ".join(pron)
                else: return "NOT RECOGNIZED"

# fast level = 1
def get_word_ending_with_pron(pron='', match_limit=1, match_exactly=1, syllable=0, syllable_exactly=0, mt="v", conso_match_type="atleast", consonants=None, dbwords=None):
        def check_xyz(index):
                split = pron_cmd_fd_content_pron[index]
                pron_word = pron_cmd_fd_content_word[index]
                if syllable > 0:
                        try: sy = pron_cmd_fd_content_syll_no[index]
                        except Exception: return []
                        if ((syllable_exactly == 0 and sy == syllable) or (syllable_exactly > 0 and sy >= syllable) or (syllable_exactly < 0 and sy <= syllable)): pass
                        else: return []
                if mv_c(pron, split, mt, conso_match_type, m_as_group, match_limit, match_exactly): return [pron_word]
        if type(pron) == type(''):
                pron = pron.replace(" ", "")
                if "," in pron:
                        pron = pron.split(",")
                        while "" in pron: pron.remove("")
                else: pron = [pron]
        ret_list = []
        global pron_cmd_fd_content_word, pron_cmd_fd_content_len, pron_cmd_fd_content_pron
        if dbwords:
                for word in dbwords:
                        if word in pron_cmd_fd_content_word:
                                i = pron_cmd_fd_content_word.index(word)
                                if consonants:
                                        pr = pron_cmd_fd_content_pron[i]
                                        if not all_in(pr, consonants): continue
                                result = check_xyz(i)
                                if result: ret_list += result
        else:
                for i in range(pron_cmd_fd_content_len):
                        if consonants:
                                pr = pron_cmd_fd_content_pron[i]
                                if not all_in(pr, consonants): continue
                        result = check_xyz(i)
                        if result: ret_list += result
        return ret_list

def get_word_ending_with_pron_of_word(word, level=1, levelexa=1, sylla=0, syllaexa=0, dbwords=None, match_t="v"):
        global pron_cmd_fd_content_len, pron_cmd_fd_content_word, pron_cmd_fd_content_pron
        if word.isspace(): return []
        if accented:
                ret = []
                rr = get_many(word)
                if rr:
                        for i in rr:
                                ret += get_word_ending_with_pron(pron_cmd_fd_content_pron[i], level, levelexa, sylla, syllaexa, match_t, dbwords=dbwords)
                return sorted(list(set(ret)))
        else:
                if word in pron_cmd_fd_content_word:
                        id=pron_cmd_fd_content_word.index(word)
                        return get_word_ending_with_pron(pron_cmd_fd_content_pron[id], level, levelexa, sylla, syllaexa, match_t, dbwords=dbwords)
                return []

def flatten(listt, level = -1):
        new_list = []
        if level == 0: return listt
        elif level > 0:
                new_list = listt
                for i in range(level):
                        if all(isinstance(v, (list, tuple)) for v in new_list):
                                new_list = []
                                for j in listt: new_list += j
                                listt = new_list
                                if i == level - 1: return new_list
                        else: return new_list
        elif level < 0:
                for i in listt:
                        if isinstance(i, (list,tuple)): new_list += flatten(i)
                        else: new_list.append(i)
                return new_list

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

def get_word_ending_with_pron_of_words(words, fs=None, use_match_ending=True):
        def generate_diff_pron2(orig_pron):
                ret_list = []
                orig_len = len(orig_pron)
                for i in range(orig_len - 1):
                        for j in range(orig_len):
                                if i == 0:
                                        if j == 0: ret_list.append(orig_pron)
                                        else:
                                                list_ret = flatten(orig_pron[0:j+1])
                                                rem_list = orig_pron[j+1:]
                                                if rem_list == []: ret_list.append([list_ret])
                                                else: ret_list.append([list_ret]+rem_list)
                                else:
                                        if j > i:
                                                prev_list = orig_pron[0:i]
                                                list_ret = flatten(orig_pron[i:j+1])
                                                rem_list = orig_pron[j+1:]
                                                if rem_list == []:
                                                        prev_list.append(list_ret)
                                                        ret_list.append(prev_list)
                                                else:
                                                        prev_list.append(list_ret)
                                                        ret_list.append(prev_list + rem_list)
                return ret_list
        def trim_to_syllable(listt, number=1, exactly=0):
                ret_list = []
                for i in listt:
                        syll = get_word_syllable_no(i)
                        if isinstance(syll, str):
                            if syll == "NOT RECOGNIZED":
                                ret_list.append(i)
                                continue
                        else: syll = int(syll)
                        if exactly == 0 and syll == number: ret_list.append(i)
                        elif exactly < 0 and syll <= number: ret_list.append(i)
                        elif exactly > 0 and syll >= number: ret_list.append(i)
                return ret_list
        def generate_word_pron(listt, use_match_ending=True):
                ret_list = []
                for i in listt:
                        if verbose: print(i)
                        syl = int(i[-1])
                        i = i[:len(i)-1]
                        if use_match_ending: result = get_word_ending_with_pron(i, syl, syllable=syl)
                        else:
                                if syl > 1:
                                        for j in range(len(i)):
                                                if is_a_vowel_cmd(i[j]):
                                                        del(i[:j])
                                                        break
                                result = get_word_starting_pron(i, 1, 1, anywhere=True, only_sound=False, syll=syl, sylla_exactly=0)
                        if result == "NO MATCH" or result == []:
                                ret_list.append([])
                                continue
                        if isinstance(result, str): result = result.split(", ")
                        """for i in range(len(result)):
                                result[i] = result[i].lower()
                                if result[i].endswith(")"):
                                        result[i] = result[i][:len(result[i])-3]"""
                        #result = trim_to_syllable(result, syl)
                        ret_list.append(result)
                return ret_list
        def print_word(pron_list, word_list, fil2):
                if fil2:
                        wr = False
                        import os
                        if not(os.access(fil2, os.F_OK)): os.makedirs(fil2)
                else: wr = True
                line = "-"*20
                for i in range(len(pron_list)):
                        if wr:
                                print(line)
                                print("-".join(pron_list[i][:len(pron_list[i])-1]))
                                try: print(word_list[i])
                                except IndexError: pass
                        else:
                                pppp = "-".join(pron_list[i][:len(pron_list[i])-1])+'.txt'
                                fil = open(fil2+'/'+pppp, 'w')
                                try: fil.write(", ".join(word_list[i]) + "\n")
                                except IndexError: pass
                                fil.close()
        def print_word2(pron_list, word_list, fil2, pr):
                if fil2:
                        wr = False
                        #fil = open(fil2+"\\"+words.replace(" ","-")+".txt", "w")
                        fil = open(fil2+"/"+words.replace(" ","-")+".txt", "w")
                else: wr = True
                line = "-"*20
                ex = exe(pr)
                for whole in ex:
                        whole_l = []
                        t = ""
                        for each in whole:
                                each = flatten(each)
                                t += "["+"".join(each)+"]"
                                for i in range(len(pron_list)):
                                        pr = pron_list[i][:]
                                        pr.pop()
                                        if each == pr:
                                            whole_l.append(word_list[i])
                                            break
                        if wr:
                                print("\n\n----------------------------------------")
                                print(t)
                        else:
                                fil.write("\n\n\n------------------------------------\n")
                                fil.write(t+"\n")
                        hold = []
                        count = 0
                        for i in range(1000):
                                t = ""
                                for j in whole_l:
                                        if j: t += random.choice(j)+" "
                                        else:
                                                t = "-------"
                                                break
                                if t == "-------": continue
                                t = t.rstrip()
                                if t not in hold:
                                        if count < 4:
                                                if wr: print(t, end=", ")
                                                else: fil.write(t+"     ")
                                                count += 1
                                        else:
                                                if wr: print(t)
                                                else: fil.write(t+"\n")
                                                count = 0
                                        hold.append(t)
        words = words.strip()
        if words.isspace(): return "EMPTY"
        if "," in words:
                word = words.upper().split(",")
                while "" in word: word.remove("")
                pron = group2(word)
                result_pron = generate_diff_pron(pron, True)
                result = generate_word_pron(result_pron, use_match_ending)
                print_word(result_pron, result, fs)
                print_word2(result_pron, result, fs, pron)
        elif " " in words:
                pron = []
                word = words.split()
                br = False
                for w in word:
                        r = get_word_pron(w)
                        if r == "NOT RECOGNIZED":
                                br = True
                                break
                        r = group2(r.split())
                        pron += r
                if br: print("Word not recognised.")
                else:
                        result_pron = generate_diff_pron(pron, True)
                        result = generate_word_pron(result_pron, use_match_ending)
                        print_word(result_pron, result, fs)
                        print_word2(result_pron, result, fs, pron)
        else:
                pron = get_word_pron(words)
                if pron == "NOT RECOGNIZED": print("Word not recognised.")
                else:
                        result1 = group2(pron.split())
                        result_pron = generate_diff_pron(result1,True)
                        result = generate_word_pron(result_pron, use_match_ending)
                        print_word(result_pron, result, fs)
                        print_word2(result_pron, result, fs, result1)
                                
        print(pron)
        print(words)

def get_word_starting_pron(consonant, conso_count=1, exactly=0, repeatables=[], anywhere=False, only_sound=False, syll=0, sylla_exactly=0):
        def uniq(orig, new):
                for i in new:
                        if i not in orig: orig.append(i)
        def extract(pron):
                ret_list = []
                for i in range(len(pron)):
                        if is_a_vowel_cmd(pron[i]):
                                rpt = pron[i][:len(pron[i])-1]
                                for j in valv:
                                        if rpt in j:
                                                uniq(ret_list, j)
                                                break
                        else: ret_list += [pron[i]]
                return ret_list
        def pron_matches_all(prons, repeatabs, matcher, mode):
                repeatabs = extract(repeatabs)
                prons = extract(prons)
                if mode == "all":return all(cons in prons for cons in repeatabs)
                elif mode == "exactly":
                        if type(matcher) == type(""): rp = repeatabs+[matcher]
                        else:
                                rp = repeatabs
                                uniq(rp, extract(matcher))
                        if all(cons in prons for cons in rp) and not any(cons not in rp for cons in prons): return True
                        return False
        def match_multiple(prons, cons, result=0):
                if len(prons) < len(cons): return result
                if ((is_a_vowel_cmd(cons[0]) and is_a_vowel_cmd(prons[0]) and match_vowel_cmd(cons[0], prons[0])) or (not is_a_vowel_cmd(cons[0]) and not is_a_vowel_cmd(prons[0]) and match_conso_cmd(cons[0], prons[0]))):
                        zipp = zip(prons, cons)
                        yes = False
                        count = -1
                        for i in zipp:
                                count += 1
                                if ((not is_a_vowel_cmd(i[0]) and not is_a_vowel_cmd(i[1]) and match_conso_cmd(i[0], i[1])) or (is_a_vowel_cmd(i[0]) and is_a_vowel_cmd(i[1]) and match_vowel_cmd(i[0], i[1]))): yes = True
                                else:
                                        yes = False
                                        break
                        if yes:
                                result += 1
                                return match_multiple(prons[len(cons):], cons, result)
                        else: return match_multiple(prons[count:], cons, result)
                else: return match_multiple(prons[1:], cons, result)                                                     
        global pron_cmd_fd_content_len, pron_cmd_fd_content_word, pron_cmd_fd_content_pron, pron_cmd_fd_content_syll_no
        ret_list = []
        if type(consonant) == type(''):
                consonant = consonant.replace(" ","")
                if "," in consonant:
                        consonant = consonant.split(",")
                        while "" in consonant: consonant.remove("")
        elif type(consonant) == type([]):
                if len(consonant) == 1: consonant = consonant[0]
        for i in range(pron_cmd_fd_content_len):
                if syll > 0:
                        c = pron_cmd_fd_content_syll_no[i]
                        if (sylla_exactly == 0 and c == syll) or (sylla_exactly < 0 and c <= syll) or (sylla_exactly > 0 and c >= syll): pass
                        else: continue
                pronlo = pron_cmd_fd_content_pron[i]
                if type(consonant) == type(""):
                        if consonant[-1] in ["0", "1", "2"]:
                                conso_b = consonant[:len(consonant)-1]
                                if not(anywhere):
                                        if is_a_vowel_cmd(pronlo[0]) and match_vowel_cmd(pronlo[0], consonant):
                                                c = 0
                                                for k in pronlo:
                                                        if is_a_vowel_cmd(k) and match_vowel_cmd(k, consonant): c += 1
                                                if (exactly == 0 and c == conso_count) or (exactly < 0 and c <= conso_count) or (exactly > 0 and c >= conso_count):
                                                        if repeatables == []:
                                                                if only_sound:
                                                                        yes = False
                                                                        for a in pronlo:
                                                                                if is_a_vowel_cmd(a):
                                                                                        if match_vowel_cmd(a, consonant): yes = True
                                                                                        else:
                                                                                                yes = False
                                                                                                break
                                                                        if yes: ret_list.append(pron_cmd_fd_content_word[i])
                                                                else: ret_list.append(pron_cmd_fd_content_word[i])
                                                        else:
                                                                if only_sound: word = "exactly"
                                                                else: word = "all"
                                                                if pron_matches_all(pronlo, repeatables, conso_b, word): ret_list.append(pron_cmd_fd_content_word[i])
                                else:
                                        c = 0
                                        for k in pronlo:
                                                if is_a_vowel_cmd(k) and match_vowel_cmd(k, consonant): c += 1
                                        if (exactly == 0 and c == conso_count) or (exactly < 0 and c <= conso_count) or (exactly > 0 and c >= conso_count):
                                                if repeatables == []:
                                                        if only_sound:
                                                                yes = False
                                                                for a in pronlo:
                                                                        if is_a_vowel_cmd(a):
                                                                                if match_vowel_cmd(a, consonant): yes = True
                                                                                else:
                                                                                        yes = False
                                                                                        break
                                                                if yes: ret_list.append(pron_cmd_fd_content_word[i])
                                                        else: ret_list.append(pron_cmd_fd_content_word[i])
                                                else:
                                                        if only_sound: word = "exactly"
                                                        else: word = "all"
                                                        if pron_matches_all(pronlo, repeatables, conso_b, word): ret_list.append(pron_cmd_fd_content_word[i])
                        else:
                                if not(anywhere):
                                        if pronlo[0] == consonant:
                                                c = pronlo.count(consonant)
                                                if (exactly == 0 and c == conso_count) or (exactly < 0 and c <= conso_count) or (exactly > 0 and c >= conso_count):
                                                        if repeatables == []:
                                                                if only_sound:
                                                                        yes = False
                                                                        for a in pronlo:
                                                                                if not(is_a_vowel_cmd(a)):
                                                                                        if a == consonant: yes = True
                                                                                        else:
                                                                                                yes = False
                                                                                                break
                                                                        if yes: ret_list.append(pron_cmd_fd_content_word[i])
                                                                else: ret_list.append(pron_cmd_fd_content_word[i])
                                                        else:
                                                                if only_sound: word = "exactly"
                                                                else: word = "all"
                                                                if pron_matches_all(pronlo, repeatables, consonant, word): ret_list.append(pron_cmd_fd_content_word[i])
                                else:
                                        c = pronlo.count(consonant)
                                        if (exactly == 0 and c == conso_count) or (exactly < 0 and c <= conso_count) or (exactly > 0 and c >= conso_count):
                                                if repeatables == []:
                                                        if only_sound:
                                                                yes = False
                                                                for a in pronlo:
                                                                        if not(is_a_vowel_cmd(a)):
                                                                                if a == consonant: yes = True
                                                                                else:
                                                                                        yes = False
                                                                                        break
                                                                if yes: ret_list.append(pron_cmd_fd_content_word[i])
                                                        else: ret_list.append(pron_cmd_fd_content_word[i])
                                                else:
                                                        if only_sound: word = "exactly"
                                                        else: word = "all"
                                                        if pron_matches_all(pronlo, repeatables, consonant, word): ret_list.append(pron_cmd_fd_content_word[i])
                elif type(consonant) == type([]):
                        result = match_multiple(pronlo, consonant)
                        if result != 0:
                                if ((is_a_vowel_cmd(consonant[0]) and is_a_vowel_cmd(pronlo[0]) and match_vowel_cmd(consonant[0], pronlo[0])) or (not is_a_vowel_cmd(consonant[0]) and not is_a_vowel_cmd(pronlo[0]) and match_conso_cmd(consonant[0], pronlo[0]))):
                                        zipp = zip(pronlo, consonant)
                                        yes = False
                                        for j in zipp:
                                                if ((not is_a_vowel_cmd(j[0]) and not is_a_vowel_cmd(j[1]) and match_conso_cmd(j[0], j[1])) or (is_a_vowel_cmd(j[0]) and is_a_vowel_cmd(j[1]) and match_vowel_cmd(j[0], j[1]))): yes = True
                                                else:
                                                        yes = False
                                                        break
                                        if yes: result = [result, True]
                                        else: result = [result, False]
                                else: result = [result, False]
                        else: result = [result, False]
                        yes = True
                        for j in pronlo:
                                if is_a_vowel_cmd(j):
                                        for k in consonant:
                                                if is_a_vowel_cmd(k):
                                                        if match_vowel_cmd(j, k): yes = True
                                                        else:
                                                                yes = False
                                                                break
                                        if not yes: break
                        if yes: result.append(True)
                        else: result.append(False)
                        c = result[0]
                        if anywhere:
                                #if result[1]: continue
                                if c == 0: continue
                                if (exactly == 0 and c == conso_count) or (exactly < 0 and c <= conso_count) or (exactly > 0 and c >= conso_count):
                                        if repeatables == []:
                                                if only_sound:
                                                        if result[2]: ret_list.append(pron_cmd_fd_content_word[i])
                                                else: ret_list.append(pron_cmd_fd_content_word[i])
                                        else:
                                                if only_sound: word = "exactly"
                                                else: word = "all"
                                                if pron_matches_all(pronlo, repeatables, consonant, word): ret_list.append(pron_cmd_fd_content_word[i])
                        else:
                                if not(result[1]): continue
                                if c == 0: continue
                                if (exactly == 0 and c == conso_count) or (exactly < 0 and c <= conso_count) or (exactly > 0 and c >= conso_count):
                                        if repeatables == []:
                                                if only_sound:
                                                        if result[2]: ret_list.append(pron_cmd_fd_content_word[i])
                                                else: ret_list.append(pron_cmd_fd_content_word[i])
                                        else:
                                                if only_sound: word = "exactly"
                                                else: word = "all"
                                                if pron_matches_all(pronlo, repeatables, consonant, word): ret_list.append(pron_cmd_fd_content_word[i])
        return ret_list

def get_word_with_pos(words, pos, exactly="atleast"):
        global pos_file_fd_content_len, pos_file_fd_content_lists_word, pos_file_fd_content_lists_pos
        for i in range(len(pos)): pos[i] = wtl[pos[i]]
        ret_list = []
        for word in words:
                if word.endswith(")"): worda = word[:len(word)-3]
                else: worda = word
                if worda in pos_file_fd_content_lists_word:
                        poss = pos_file_fd_content_lists_pos[pos_file_fd_content_lists_word.index(worda)]
                        if exactly == "atleast":
                                if all (c in poss for c in pos): ret_list.append(word)
                        elif exactly == "exactly":
                                if len(pos) != len(poss): continue
                                if all (c in poss for c in pos): ret_list.append(word)
                        elif exactly == "any":
                                if any (c in poss for c in pos): ret_list.append(word)
                else: ret_list.append(word+"--")
        return ret_list

# FOR ALTERNATIVE WORDS
def accept(l, options = ['y','n','c','r'],prompt='Do you accept? [y/n/c/r]: '):
        print(l)
        print()
        resp = input(prompt)
        while resp not in options:
                print('Input a correct option')
                resp = input(prompt)
        return resp

def get_alt_of_word (word, limit=-1, dbwords=None, request = True):
        global alt_file_fd_content_lists
        ret_list = []
        if word.isspace(): return "EMPTY"
        if dbwords:
                result = get_alt_of_word(word,limit=limit, request=False)
                if result:
                        for i in dbwords:
                            if i in result:
                                ret_list.append(i)
        else:
                for li in alt_file_fd_content_lists:
                        if (word in li):
                                if limit < 0:
                                        if request:
                                                resp = accept(li)
                                                if resp == 'y':ret_list += li
                                                elif resp == 'n':continue
                                                elif resp == 'c':break
                                                else:
                                                        ret_list += li
                                                        request = False
                                        else: ret_list += li
                                else:
                                        if request:
                                                resp = accept(li)
                                                if resp == 'y':
                                                        new_list = []
                                                        for k in range(limit):
                                                                try: new_list.append(li[k])
                                                                except IndexError: break
                                                        ret_list += new_list
                                                elif resp == 'n':continue
                                                elif resp == 'c':break
                                                else:
                                                        new_list = []
                                                        for k in range(limit):
                                                                try: new_list.append(li[k])
                                                                except IndexError: break
                                                        ret_list += new_list
                                                        request = False
                                        else:
                                                new_list = []
                                                for k in range(limit):
                                                        try: new_list.append(li[k])
                                                        except IndexError: break
                                                ret_list += new_list
        return list(set(ret_list))

def get_alt_and_rhyming_word(word, match_type='v', l=1, le=1):
        global pron_cmd_fd_content_word, pron_cmd_fd_content_pron
        ret = []
        if word in pron_cmd_fd_content_word:
            pron = get_word_ending_with_pron_of_word(word,l, le)
            ret = get_alt_of_word(word, dbwords=pron)
        return ret

def get_alt_and_syll_classes(word):
    alt = get_alt_of_word(word, request=False)
    print(len(alt))
    alt = alt[:500]
    ret = {}
    for wd in alt:
        syl = get_word_syllable_no(wd)
        if syl in ret: ret[syl].append(wd)
        else: ret[syl] = [wd]
    return ret

def start_match(word, length, repetition, exactly, anywhere, only_sound, repeatables):
        global pron_cmd_fd_content_len, pron_cmd_fd_content_word, pron_cmd_fd_content_pron
        if word in pron_cmd_fd_content_word:
                pr = pron_cmd_fd_content_pron[pron_cmd_fd_content_word.index(word)]
                pr = ','.join(pr[:length])
                res = get_word_starting_pron(pr, repetition, exactly, repeatables, anywhere, only_sound)
                return res
        else: return False

def get_words_from_vowel_comb(pron, fil=None, action=2):
        global pron_cmd_fd_content_len, pron_cmd_fd_content_word, pron_cmd_fd_content_pron, pron_cmd_fd_content_syll_no
        if action >= 0: fil = open(fil, 'w')
        if type(pron) == type(''):
                pron = pron.replace(" ", "")
                if "," in pron:
                        pron = pron.split(",")
                        while "" in pron: pron.remove("")
                else: pron = [pron]
        ret_list = []
        #pron = group2(pron)
        pron = exe(pron)
        rrr = []
        for i in pron:
                h = []
                for a in i:
                        a = a[0]
                        h.append(a)
                rrr.append(h)
        pron = rrr
        del(rrr)
        for i in pron:
                print(i)
                tex = []
                for j in i:
                        res = get_word_starting_pron(j, anywhere=True, only_sound=True)
                        tex.append(res)
                if action < 0:
                        print('------------------------')
                        print(i)
                        print(tex)
                elif action == 0:
                        print('------------------------')
                        print(i)
                        print(tex)
                        tt = ''
                        for j in i:
                                for k in j: tt += '-'+k
                        fil.write(tt+'\n')
                        fil.write(str(tex)+'\n\n')
                elif action > 0:
                        tt = ''
                        for j in i:
                                for k in j: tt += '-'+k
                        fil.write(tt+'\n')
                        fil.write(str(tex)+'\n\n')
        if fil: fil.close()

def get_words_from_vowel_comb2(pron, fil=None, action=2):
        global pron_cmd_fd_content_len, pron_cmd_fd_content_word, pron_cmd_fd_content_pron, pron_cmd_fd_content_syll_no
        if action >= 0: fil = open(fil, 'w')
        if type(pron) == type(''):
                pron = pron.replace(" ", "")
                if "," in pron:
                        pron = pron.split(",")
                        while "" in pron: pron.remove("")
                else: pron = [pron]
        ret_list = []
        pron = generate_diff_pron(pron, True)
        for i in pron:
                i = i[:len(i)-1]
                print(i)
                res = get_word_starting_pron(i, anywhere=True, only_sound=True)
                ret_list.append(res)
        for i in range(len(pron)):
                try: tt = '-'.join(pron[i])
                except Exception: tt = str(pron[i])
                tex = ', '.join(ret_list[i])
                if action < 0:
                        print('------------------------')
                        print(tt)
                        print(tex)
                elif action == 0:
                        print('------------------------')
                        print(tt)
                        print(tex)
                        fil.write(tt+'\n')
                        fil.write(tex+'\n\n')
                elif action > 0:
                        fil.write(tt+'\n')
                        fil.write(tex+'\n\n')
        if fil and not isinstance(fil, str): fil.close()
