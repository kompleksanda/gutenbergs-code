import repos
from os import system

settings = False
all_cons =['D','DH','T','TH','B','CH','F','G','HH','JH','K','L','M','N','NG','P','R','S','SH','V','W','Y','Z','ZH']
h = ['HH']
#repos.silent = all_cons
#repos.anyhow = True
#repos.reverse_all_pron = True
#repos.m_as_group = True

def call():
        #getpron("read.txt")
        for i in range(10):
                #cons_m(action=1,cc=2,ce=1,anywhere=True,only_sound=False, repeatables=[])
                alt(-1, action=1)
                #get_alt_syll(columns = 7)
                #pron_w(2, action=1)
                #pron_ws(use_match_ending=False)
                #pron_d(action=1, ml=2, me=0, mt="v", consonants=None)
                #altmatch(action=-1,level=2,levelexact=1, columns=3)
                #sta_ma(1, lent=1, rep_times = 1, exa=1, anyw=False, only_s=False, repeatable=[], columns=3)
                #getpos()
                #getpron("")
                #words_stress()

                continue

def words_stress():
    repos.pron_str = True
    repos.activate("pron")
    inp = input("Enter words: ")
    t = inp.replace(' ','-')
    dire = "C:\\Users\\USER\\Desktop\\moby\\stress\\words_stress\\"
    #dire = "/storage/emulated/0/moby/rim/stress/words_stress/"
    if not inp.isdecimal(): stress = repos.pron_get_word_stress(inp)
    else: stress = inp
    repos.pron_get_words_stress(stress, t, dire)

def stress():
    inp = input("Enter stress pattern: ")
    repos.pron_str = True
    repos.activate("pron")
    words = repos.pron_get_word_with_str(inp)
    print(words)


def get_res(prompt,opt=['y','n']):
        res = input(prompt+': ')
        while res not in opt:
                if res == 'cc': return res
                elif res == '': return 'n'
                res = input(prompt+': ')
        return res

def get_inp(prompt='input: '):
        res = input(prompt)
        return res

def change_pron_settings():
        o = get_res('Do you wish to change pronunciation settings?[y/n]')
        if o == 'y':
                tt = 'do you wish to invert'
                t = tt+' repos.anyhow='+str(repos.anyhow)+' [y/n]'
                a = get_res(t)
                if a == 'y': repos.anyhow = not(repos.anyhow)
                elif a == 'cc': return
                t = tt+' repos.m_as_group='+str(repos.m_as_group)+' [y/n]'
                a = get_res(t)
                if a == 'y': repos.m_as_group = not(repos.m_as_group)
                elif a == 'cc': return
                t = tt+' repos.reverse_all_pron='+str(repos.reverse_all_pron)+' [y/n]'
                a = get_res(t)
                if a == 'y': repos.reverse_all_pron=not(repos.reverse_all_pron)
                elif a == 'cc': return
                tt = 'Do you wish to edit to'
                t = tt+' repos.silent='+str(repos.silent)+' [y/n]'
                a = get_res(t)
                if a == 'y':
                        t = 'append/clear[a/c]'
                        a = get_res(t, ['a','c'])
                        if a in ['a', 'c']:
                                r = input('input: ')
                                r = r.replace(' ','')
                                l = r.split(',')
                                if a == 'a': repos.silent += l
                                elif a == 'c': repos.silent = l
                        else: return
                        try:
                                if repos.pron_fd_content_len:
                                        del(repos.pron_fd_content_len)
                        except NameError: pass
                elif a == 'cc': return

def pron_ws(use_match_ending=True):
        if settings: change_pron_settings()
        repos.pron_syll_no = True
        repos.activate("pron")
        word = input("Enter words: ").strip().lower()
        t = word.replace(' ','-')
        t = t.replace(",","-")
        if not use_match_ending: t+="_NOT-ME"
        if repos.anyhow: t+='_CONS-AH'
        if repos.m_as_group: t+='_GROUP'
        if repos.reverse_all_pron: t+='_REV'
        if repos.silent == all_cons: t+='_SIL-CONS'
        dire = "C:\\Users\\USER\\Desktop\\moby\\rim\\match\\pron_ws\\"+t
        #dire = "/storage/emulated/0/moby/rim/match/pron_ws/"+t
        system("cls")
        repos.get_word_ending_with_pron_of_words(word, dire, use_match_ending)
def pron_w(limit=1, action=1):
        if settings:
                change_pron_settings()
                tt = 'Do you wish to change pron_w settings'
                a = get_res(tt)
                if a == 'y':
                        tt = 'Do you wish to change '
                        t = tt+'limit='+str(limit)
                        a = get_res(t)
                        if a == 'y': limit = int(get_inp())
                        elif a == 'cc': return
                        t = tt+'action='+str(action)
                        a = get_res(t)
                        if a == 'y': action = int(get_inp())
        repos.activate("pron")
        word = input("Enter word: ").strip().lower()
        system("cls")
        t = ''
        if repos.anyhow: t+='_CONS-ANYHOW'
        if repos.m_as_group: t+='_GROUP'
        if repos.reverse_all_pron: t+='_REV'
        if repos.silent == all_cons: t+='_SIL-CONS'
        dire = "C:\\Users\\USER\\Desktop\\moby\\rim\\match\\"+word+t+".txt"
        #dire = "/storage/emulated/0/moby/rim/match/"+word+t+".txt"
        a = repos.get_word_ending_with_pron_of_word(word, limit)
        repos.write_to_file(a, dire, action=action)

def alt(limit=-40, action=1):
        if settings:
                tt = 'Do you wish to change alt settings'
                a = get_res(tt)
                if a == 'y':
                        tt = 'Do you wish to change '
                        t = tt+'limit='+str(limit)
                        a = get_res(t)
                        if a == 'y': limit = int(get_inp())
                        elif a == 'cc': return
                        t = tt+'action='+str(action)
                        a = get_res(t)
                        if a == 'y': action = int(get_inp())
        repos.activate("alt")
        print("\n")
        word = input("Enter word: ").strip().lower()
        t = word.replace(' ','-')
        dire = "C:\\Users\\USER\\Desktop\\moby\\rim\\alt\\"+t+".txt"
        #dire = "/storage/emulated/0/moby/rim/alt/"+t+".txt"
        system("cls")
        a = repos.get_alt_of_word(word, limit, request=False)
        system("cls")
        if a: repos.write_to_file(a, dire, action=action, columns=7)

def cons_m(action=-1, cc=1, ce =0, repeatables=[], anywhere=False, only_sound=False):
        if settings:
                change_pron_settings()
                a = get_res('Do you wish to change cons_m settings')
                if a == 'y':
                        n = ['cc','ce','repeatables', 'action']
                        tv = ['anywhere', 'only_sound']
                        tn = 'Do you want to change '
                        ttv = 'Do you want to invert '
                        for nn in n:
                                ev = eval(nn)
                                t = tn+nn+'='+str(ev)
                                a = get_res(t)
                                if a == 'y':
                                        h = get_inp()
                                        if type(ev) == type(1): ttt = nn+'=int(h)'
                                        elif type(ev) == type([]):
                                                h = h.replace(' ','')
                                                h = h.split(',')
                                                ttt = nn+'=h'
                                        else: ttt = nn+'=str(h)'
                                        exec(ttt)
                                elif a == 'cc': return
                        for nn in tv:
                                t = ttv+nn+'='+str(eval(nn))
                                a = get_res(t)
                                if a == 'y':
                                        ttt = nn+'='+'not('+nn+')'
                                        exec(ttt)
                                if a == 'cc': return
        repos.activate("pron")
        word = input("Enter pronunciation: ").upper()
        system("cls")
        t1 = word.replace(' ', '-')
        t = ""
        if repos.anyhow: t+='_CONS-ANYHOW'
        if repos.m_as_group: t+='_GROUP'
        if repos.reverse_all_pron: t+='_REV'
        if repos.silent == all_cons: t+='_SIL-CONS'
        dire = "C:\\Users\\USER\\Desktop\\moby\\rim\\conso_m\\"+t1+t+".txt"
        #dire = "/storage/emulated/0/moby/rim/conso_m/"+t1+t+".txt"
        a = repos.get_word_starting_pron(word, cc, ce, repeatables, anywhere, only_sound)
        if a: repos.write_to_file(a, dire, action=action)

def pron_d(action=-1, ml=1, me=1, sy=0, se=0, mt="v", cmt="exactly", consonants=None):
        """
        pron_d tries to match from end of pronunciation
        ml = limit of match, maybe the first vowel second vowel etc
        me = used if to match more, less or equal to ml 0=equal, >0=more, <0=less
        sy = no of syllables to match
        se = used if to match more, less or equal to sy 0=equal, >0=more, <0=less
        mt = match type 'c' or 'v' ie consonant or vowel matching
        cmt = consonants match type specifies if to match exactly or whole group of consonant, or any consonant in the group. 'exactly', 'atleast', 'any'
        consonants = list of consonants and vowels that should be included in match

        """
        if settings:
                change_pron_settings()
                a = get_res('Do you wish to change pron_d settings')
                if a == 'y':
                        n = ['ml','me','cmt', 'consonants', 'mt', 'action']
                        tn = 'Do you want to change '
                        for nn in n:
                                ev = eval(nn)
                                t = tn+nn+'='+str(ev)
                                a = get_res(t)
                                if a == 'y':
                                        h = get_inp()
                                        if type(ev) == type(1): ttt = nn+'=int(h)'
                                        elif type(ev) == type([]):
                                                h = h.replace(' ','')
                                                h = h.split(',')
                                                ttt = nn+'=h'
                                        else: ttt = nn+'=str(h)'
                                        exec(ttt)
                                elif a == 'cc': return
        if sy > 0: repos.pron_syll_no = True
        repos.activate("pron")
        word = input("Enter pronunciation: ").upper()
        system("cls")
        t1 = word.replace(' ', '-')
        t = ""
        if repos.anyhow: t+='_CONS-ANYHOW'
        if repos.m_as_group: t+='_GROUP'
        if repos.reverse_all_pron: t+='_REV'
        if repos.silent == all_cons: t+='_SIL-CONS'
        dire = "C:\\Users\\USER\\Desktop\\moby\\rim\\match\\pron_d\\"+t1+t+".txt"
        #dire = "/storage/emulated/0/moby/rim/match/pron_d/"+t1+t+".txt"
        a = repos.get_word_ending_with_pron(word, ml, me, sy, se, mt, cmt, consonants)
        repos.write_to_file(a, dire, action=action)

def altmatch(action=-1,level=1,levelexact=1, columns=3):
        if settings:
                change_pron_settings()
                t = 'Do you want to change alt_match settings'
                a = get_res(t)
                if a == 'y':
                        t = 'Do you want to edit action='+str(action)
                        a = get_res(t)
                        if a == 'y':
                                action = int(get_inp())
                        if a == 'cc': return
        repos.activate('alt','pron')
        word = input('Enter word: ').strip().lower()
        system('cls')
        t1 = word.replace(' ','-')
        t = ""
        if repos.anyhow: t+='_CONS-ANYHOW'
        if repos.m_as_group: t+='_GROUP'
        if repos.reverse_all_pron: t+='_REV'
        if repos.silent == all_cons: t+='_SIL-CONS'
        dire = "C:\\Users\\USER\\Desktop\\moby\\rim\\alt_match\\"+t1+t+".txt"
        #dire = "/storage/emulated/0/moby/rim/alt_match/"+t1+t+".txt"
        res = repos.get_alt_and_rhyming_word(word, l=level,le=levelexact)
        if res: repos.write_to_file(res, dire, action=action, columns=columns)

def sta_ma(action = -1, lent = 1, rep_times = 1, exa=1, anyw=False, only_s=False, repeatable=[], columns=3):
        if settings:
                change_pron_settings()
                a = get_res('Do you wish to change sta_ma settings')
                if a == 'y':
                        n = ['lent','rep_times', 'exa', 'repeatables','action']
                        tv = ['anyw', 'only_s']
                        tn = 'Do you want to change '
                        ttv = 'Do you want to invert '
                        for nn in n:
                                ev = eval(nn)
                                t = tn+nn+'='+str(ev)
                                a = get_res(t)
                                if a == 'y':
                                        h = get_inp()
                                        if type(ev) == type(1): ttt = nn+'=int(h)'
                                        elif type(ev) == type([]):
                                                h = h.replace(' ','')
                                                h = h.split(',')
                                                ttt = nn+'=h'
                                        else: ttt = nn+'=str(h)'
                                        exec(ttt)
                                elif a == 'cc': return
                        for nn in tv:
                                t = ttv+nn+'='+str(eval(nn))
                                a = get_res(t)
                                if a == 'y':
                                        ttt = nn+'='+'not('+nn+')'
                                        exec(ttt)
                                if a == 'cc': return
        repos.activate('pron')
        word = input('Enter word: ').strip().lower()
        system('cls')
        t = ""
        if repos.anyhow: t+='_CONS-ANYHOW'
        if repos.m_as_group: t+='_GROUP'
        if repos.reverse_all_pron: t+='_REV'
        if repos.silent == all_cons: t+='_SIL-CONS'
        dire = "C:\\Users\\USER\\Desktop\\moby\\rim\\match\\"+word+t+"_REV.txt"
        #dire = "/storage/emulated/0/moby/rim/match/"+word+t+"_REV.txt"
        res = repos.start_match(word, lent, rep_times, exa, anyw, only_s, repeatable)
        repos.write_to_file(res, dire, action=action, columns = columns)
def getpos():
        repos.cmudict_has_pos = True
        repos.include_pos = True
        #repos.with_support = True
        repos.activate('pron')
        word = input('Enter word: ').strip().lower()
        for w in word.split():
                if w in repos.pron_cmd_fd_content_word:
                        id = repos.pron_cmd_fd_content_word.index(w)
                        pa = repos.pron_cmd_fd_content_pos[id]
                        total = []
                        for ii in pa:
                                try:total.append(repos.ltw[ii])
                                except KeyError: total = []
                        print(w,"=",total)
                else:print(w,"= []")
def getpron(fil=None):
        #gen_cmd_wtp = ( ("AW"), ("AI","AY"), ("IH","IY"), ("EY"),("OY"), ("UH","UW"), ("AH","AE","AA") ,("AO"),("ER","EH"), ("OW") )
        gen_cmd_wtp = ( ("AW"), ("AI","AY"), ("IH","IY"), ("EY"),("OY"), ("UH","UW"), ("AH","AE","AA","AO"),("EH","ER"), ("OW") )
        repos.activate("pron")
        if fil:
                res = []
                out = fil+"_PRON"
                with open(fil) as fil:
                        fil = fil.readlines()
                for i in fil:
                        t = ""
                        word = i.lower().rstrip("\n").strip()
                        for w in word.split():
                                if w in repos.pron_cmd_fd_content_word:
                                        id = repos.pron_cmd_fd_content_word.index(w)
                                        pr = "".join(repos.pron_cmd_fd_content_pron[id]).replace("0","").replace("1","").replace("2","")
                                        t += pr+" "
                                else:
                                        t += w+" "
                        res.append(t.strip().lower()+"\n")
                with open(out, "w") as ou:
                        ou.writelines(res)
        else:
                word = input('Enter word: ').strip().lower()
                res = ""
                for w in word.split():
                        if w in repos.pron_cmd_fd_content_word:
                                id = repos.pron_cmd_fd_content_word.index(w)
                                pr = "".join(repos.pron_cmd_fd_content_pron[id]).replace("0","").replace("1","").replace("2","")
                                res += pr+" "
                        else:
                                res += w+" "
                print(res.lower())

def get_alt_syll(columns=7):
    repos.activate("alt","syl")
    word = input('Enter word ').strip().lower().replace(" ", "-")
    system('cls')
    dire = "/storage/emulated/0/moby/rim/alt/"+word
    sa = repos.get_alt_and_syll_classes(word)
    repos.write_to_file(sa, dire, columns=columns)

call()
