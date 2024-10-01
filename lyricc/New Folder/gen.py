import repos, random, re
verbose = True
all_cons =['D','DH','T','TH','B','CH','F','G','HH','JH','K','L','M','N','NG','P','R','S','SH','V','W','Y','Z','ZH']
h = ['HH']
repos.silent = h
repos.anyhow = True
repos.transform = {'NG':['N','G']}
#repos.reverse_all_pron = True
#repos.m_as_group = True

#style = ['do','re','mi','fa','so','la','ti']
#style = ['do', 're', 'mi']
style = ['0.5','1','1.5','2']

def call():
        time = 5000
        #at(time, 1)
        #me(50)
        stre(time)
        #pos(time)
        #vowe(2)
        #scale(11, time, action=2)
        #vowel_match2()

def timeit(stmt):
        import time
        a = time.time()
        stmt()
        a = time.time()-a
        if a < 60: print('took',a,'sec')
        else:
            a = divmod(a,60)
            print('took',int(a[0]),'min',int(a[1]),'sec')

def red(l):
        ll = l[:]
        for i in l:
                if ll.count(i) > 1: del(ll[ll.index(i)])
        return ll
def pos(time=10, action = 1):
        #repos.pron_syll_no = True
        repos.activate('pos')
        sentence = input("Enter words: ").lower()
        f = sentence.replace(' ','-')+".txt"
        dire = "C:\\Users\\USER\\Desktop\\moby\\rim\\word\\pos\\"+f
        #dire = "/storage/emulated/0/moby/rim/word/pos/"+f
        orig = []
        dd = []
        for word in sentence.split():
                if verbose: print('proccessing',word)
                if word in dd:
                        id = dd.index(word)
                        orig.append(orig[id])
                        dd.append(word)
                        continue
                dd.append(word)
                #id = repos.pron_cmd_fd_content_word.index(word)
                #n=repos.pron_cmd_fd_content_syll_no[id]
                p = repos.get_word_pos(word)
                #r = repos.get_word_ending_with_pron_of_word(word, 1)
                #r = repos.pron_get_syll_no_word(n, dbwords=r)
                #for i in range(len(r)):
                #       r[i]=   r[i].lower()
                mode='atleast'
                #mode='exactly'
                r = repos.get_pos_word(p, mode)
                #r = repos.pron_get_syll_no_word(n, dbwords=r)
                orig.append(r)
        if action >= 0: fil=open(dire, 'w')
        g=[]
        for i in range(time):
                ret_list = []
                for j in orig: ret_list.append(random.choice(j))
                g.append(ret_list)
        g = red(g)
        g.sort()
        for i in g:
                te = ' '.join(i)+'...\n'
                if action < 0: print(te)
                elif action == 0:
                        print(te)
                        fil.write(te)
                else: fil.write(te)
        if action >= 0:fil.close()

def me(time=10, action = 1):
        repos.pron_syll_no = True
        repos.activate('pron')
        #repos.activate('pos')
        sentence = input("Enter words: ").lower()
        f = sentence.replace(' ','-')+".txt"
        #dire = "C:\\Users\\USER\\Desktop\\moby\\rim\\word\\match\\"+f
        dire = "/storage/emulated/0/moby/rim/word/match/"+f
        orig = []
        dd = []
        for word in sentence.split():
                if verbose: print('proccessing',word)
                if word in dd:
                        id = dd.index(word)
                        orig.append(orig[id])
                        dd.append(word)
                        continue
                dd.append(word)
                try:
                        #y = repos.get_word_pos(word)
                        n = repos.pron_cmd_fd_content_word.index(word)
                        n=repos.pron_cmd_fd_content_syll_no[n]  
                        r = repos.get_word_ending_with_pron_of_word(word, n, 0, n)
                        #r = repos.get_pos_word(y, dbwords=r)
                except ValueError: r=[]
                orig.append(r)
        del(dd)
        g = []
        if action >= 0: fil=open(dire, 'w')
        for i in range(time):
                ret_list = []
                for j in orig:
                        if j==[] : j=['----']
                        ret_list.append(random.choice(j))
                g.append(ret_list)
        g = red(g)
        g.sort()
        for i in g:
                te = ' '.join(i)+'...\n'
                if action < 0: print(te)
                elif action == 0:
                        print(te)
                        fil.write(te)
                else: fil.write(te)
        if action >= 0:fil.close()

def at2(time=10, action = 1):
        done=[]
        repos.activate('alt')
        repos.activate('pos')
        sentence = input("Enter words: ").lower()
        f = sentence.replace(' ','-')+".txt"
        #dire = "C:\\Users\\USER\\Desktop\\moby\\rim\\word\\alt\\"+f
        dire = "/storage/emulated/0/moby/rim/word/alt/"+f
        out=[]
        for word in sentence.split():
                if verbose: print('proccessing',word)
                if word in done:
                        id=done.index(word)
                        out.append(out[id])
                        done.append(word)
                        continue
                done.append(word)
                to=repos.get_alt_of_word(word, -1)
                if to == []: to = [word]
                else:
                    p = repos.get_word_pos(word)
                    #print(len(to))
                    to = repos.get_pos_word(p , dbwords=to)
                    pass
                out.append(to)
        if action >= 0: fil=open(dire, 'w')
        g = []
        for i in range(time):
                list_ret = []
                for j in out:
                        if j == []: j=['----']
                        list_ret.append(random.choice(j))
                g.append(list_ret)
        g = red(g)
        g.sort()
        for i in g:
                te = ' '.join(i)+'...\n'
                if action < 0: print(te)
                elif action == 0:
                        print(te)
                        fil.write(te)
                else: fil.write(te)
        if action >= 0:fil.close()
def at(time=10, action = 1, with_pos=False):
        done=[]
        repos.activate('alt')
        if with_pos: repos.activate('pos')
        sentence = input("Enter words: ").lower()
        f = sentence.replace(' ','-')+".txt"
        #dire = "C:\\Users\\USER\\Desktop\\moby\\rim\\word\\alt\\"+f
        dire = "/storage/emulated/0/moby/rim/word/alt/"+f
        out=[]
        for word in sentence.split():
                if verbose: print('proccessing',word)
                if with_pos:
                    p = repos.get_word_pos(word)
                    pps = ''.join(map(lambda x: repos.wtl[x], p))
                    yes = False
                    for i in range(len(done)):
                        if len(done[i]) != len(pps):
                            continue
                        else:
                            if all(j in done[i] for j in pps):
                                yes = True
                                break
                    if done and yes:
                        out.append(out[i])
                        done.append(pps)
                        continue
                    done.append(pps)
                    p = repos.get_pos_word(p)
                    to=repos.get_alt_of_word(word, -1, dbwords=p)
                else:
                    if word in done:
                            id=done.index(word)
                            out.append(out[id])
                            done.append(word)
                            continue
                    done.append(word)
                    to=repos.get_alt_of_word(word, -1)
                out.append(to)
        if action >= 0: fil=open(dire, 'w')
        g = []
        for i in range(time):
                list_ret = []
                for j in out:
                        if j == []: j=['----']
                        list_ret.append(random.choice(j))
                g.append(list_ret)
        g = red(g)
        g.sort()
        for i in g:
                te = ' '.join(i)+'...\n'
                if action < 0: print(te)
                elif action == 0:
                        print(te)
                        fil.write(te)
                else: fil.write(te)
        if action >= 0:fil.close()

def stre(time=10, action = 1):
        repos.pron_str = True
        repos.activate('pron')
        #repos.activate('pos')
        sentence = input("Enter words: ").lower()
        f = sentence.replace(' ','-')+".txt"
        dire = "C:\\Users\\USER\\Desktop\\moby\\rim\\word\\stress\\"+f
        #dire = "/storage/emulated/0/moby/rim/word/stress/"+f
        done=[]
        out=[]
        for word in sentence.split():
                if verbose: print('proccessing', word)
                try:
                        id = repos.pron_cmd_fd_content_word.index(word)
                        st=repos.pron_cmd_fd_content_str[id]
                        if st in done:
                                id = done.index(st)
                                w=out[id]
                                out.append(w)
                                done.append(st)
                                continue
                        else:
                                done.append(st)
                                w=repos.pron_get_word_with_str('^'+st+'$')
                                #p = repos.get_word_pos(word)
                                #w = repos.get_pos_word(p, 'any', dbwords=w[:400])
                                out.append(w)
                except ValueError: out.append([])
        if action >= 0: fil=open(dire, 'w')
        g = []
        for i in range(time):
                ret_list = []
                for j in out:
                        if j == []:j=['-----']
                        ret_list.append(random.choice(j))
                g.append(ret_list)
        g = red(g)
        g.sort()
        for i in g:
                te = ' '.join(i)+'...\n'
                if action < 0: print(te)
                elif action == 0:
                        print(te)
                        fil.write(te)
                else: fil.write(te)
        if action >= 0:fil.close()

def vowe(action=2):
        all_cons =['D','DH','T','TH','B','CH','F','G','HH','JH','K','L','M','N','NG','P','R','S','SH','V','W','Y','Z','ZH']
        repos.silent = all_cons
        repos.activate('pron')
        pro = input('Enter pronunciation: ')
        fil2 = pro.replace(' ','-')
        #fil2 = 'C:\\Users\\USER\\Desktop\\moby\\rim\\word\\vowel\\'+fil2+'.txt'
        fil2 = '/storage/emulated/0/moby/rim/word/vowel/'+fil2+'.txt'
        repos.get_words_from_vowel_comb2(pro, fil2, action)


def scale(length=3, times=100, action=2):
        #fil = 'C:\\Users\\USER\\Desktop\\moby\\rim\\scale\\'
        fil = '/storage/emulated/0/moby/rim/scale/'
        fil += str(length)+'-'+str(times)+'.txt'
        ret_list = []
        for i in range(times):
                hol = []
                for j in range(length):
                        choice = random.choice(style)
                        hol.append(choice)
                if hol not in ret_list: ret_list.append(hol)
        ret_list.sort()
        if action >= 0: fil = open(fil, 'w')
        if action < 0:
                for i in ret_list: print(', '.join(i))
        elif action == 0:
                for i in ret_list:
                        tt = ', '.join(i)
                        print(tt)
                        fil.write(tt+'\n')
        else:
                for i in ret_list: fil.write(', '.join(i)+'\n')
        if action >= 0: fil.close()

def vowel_match(times=1000, action=2):
                repos.activate("pron")
                #fil = 'C:\\Users\\USER\\Desktop\\moby\\rim\\vowel_match\\'
                fil = '/storage/emulated/0/moby/rim/vowel_match/'
                words = input("Enter words: ").lower()
                fil += words.replace(" ","-")+".txt"
                vowels = []
                for word in words.split():
                        pron  = repos.get_word_pron(word)
                        if pron != "NOT RECOGNIZED":
                                pron = pron.split()
                                for i in pron:
                                        if i[-1] in ['0', '1','2']:
                                                vowels.append(i)
                        else:
                                print("one word=",word,"was not recognized.")
                                return
                #print(vowels)
                vowels = repos.exe(vowels)
                total = []
                for i in vowels:
                        #print(i,"=1")
                        holder = []
                        for j in i:
                                j = j[0]
                                if len(j) == 1: j = j[0]
                                res =  repos.get_word_starting_pron(j, 1, 0, anywhere=True, only_sound=True)
                                holder.append(res) #[[]]
                        total.append(holder) # [[[]],...]
                if action >= 0: fil = open(fil, 'w')
                #print(vowels)
                #print(total)
                for i in total:
                        column = 0
                        fil.write("\n-----------------------\n")
                        if any(j == [] for j in i): continue
                        for j in range(100):
                                text = ''
                                for k in i:
                                        f = random.choice(k)
                                        text += f+' '
                                if column == 3:
                                        column = 1
                                        fil.write(text+"\n")
                                else:
                                        fil.write(text+"\t")
                                        column += 1

def vowel_match2(times=1000, action=2):
        repos.silent = all_cons
        repos.activate("pron")
        #fil = 'C:\\Users\\USER\\Desktop\\moby\\rim\\vowel_match\\'
        fil = '/storage/emulated/0/moby/rim/vowel_match/'
        words = input("Enter words: ").lower()
        fil += words.replace(" ","-")+".txt"
        vowels = []
        for word in words.split():
                pron  = repos.get_word_pron(word)
                if pron != "NOT RECOGNIZED":
                        pron = pron.split()
                        for i in pron:
                                if i[-1] in ['0', '1','2']:
                                        vowels.append(i)
                else:
                        print("one word=",word,"was not recognized.")
                        return
        vowels = repos.generate_diff_pron(vowels, True)
        for i in range(len(vowels)): vowels[i] = vowels[i][:len(vowels[i])-1]
        total = []
        for i in vowels:
                res =  repos.get_word_starting_pron(i, 1, 0, anywhere=True, only_sound=True)
                if len(i) != 1:
                        print(i);print(res);return
                total.append(res) # [[],...]
        if action >= 0: fil = open(fil, 'w')
        for i in range(len(vowels)):
                v = vowels[i]
                t = total[i]
                v = "-".join(v)
                fil.write(v+"\n--------------------------------------------------------------------------------\n")
                count = 1
                text = ''
                for st in t:
                        if count == 7:
                                count = 1
                                text += st+'\n'
                        else:
                                text += st+"   "
                                count += 1
                fil.write(text+"\n\n")

timeit(call)
