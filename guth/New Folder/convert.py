import repos
def getpron(word):
        repos.activate("pron")
        word = word.strip().lower()
        res = ""
        for w in word.split():
                if w in repos.pron_cmd_fd_content_word:
                        id = repos.pron_cmd_fd_content_word.index(w)
                        pr = "".join(repos.pron_cmd_fd_content_pron[id]).replace("0","").replace("1","").replace("2","")
                        res += pr+" "
                else:
                        res += w+" "
        res = res.lower().capitalize()
        return res
def reversee(word):
    import random
    def scat(w):
        w = list(w)
        r = ''
        while w:
            p = random.choice(range(len(w)))
            r += w[p]
            del(w[p])
        return r

    word = word.strip().lower()
    ret = ''
    for w in word.split():
        if len(w) == 1: ret += w+" "
        else:
            if w[-1] in ',.?!':
                ret += w[0]+scat(w[1:-1])+w[-1]+" "
            else:
                ret += w[0]+scat(w[1:])+" "
    return ret.capitalize()
def space(word):
    import random
    word = word.strip()
    r = ''
    for w in word.split():
        c = random.choice(range(3,6))
        s = " "*c
        r += s.join(list(w))+" "*3
    return r
def sylabu(word):
    repos.activate('syl')
    r = ''
    word = word.strip().lower()
    for w in word.split():
        if w in repos.hype_file_fd_content_word:
            r += " ".join(repos.hype_file_fd_content_s[repos.hype_file_fd_content_word.index(w)])+" "
        else: r += w+" "
    return r
if __name__ == '__main__':
    import sys
    tot = ' '.join(sys.argv[1:])
    #out = getpron(tot)
    out = reversee(tot)
    #out = space(tot)
    #out = sylabu(tot)
    print(out)
