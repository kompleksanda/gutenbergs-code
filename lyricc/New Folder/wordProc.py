totalWords = []
with open(r"C:\Users\USER\Documents\mobygutenberg\words.txt") as worda:
    worda_content = worda.readlines()
for line in worda_content:
    lineSplit = line.rstrip("\n").split(",")
    for word in lineSplit:
        word = word.strip()
        if ((word in totalWords) or (word.lower() in totalWords) or (word.upper() in totalWords) or (word.capitalize() in totalWords)): pass
        else: totalWords.append(word)
totalWords = list(set(totalWords))
l = len(totalWords)
import repos, os
repos.activate("alt")
outdir = r"C:\Users\USER\Desktop\moby\rim\alt\nnnn3"
for word in totalWords:
    print ("remains", l-1, word)
    l -= 1
    if os.access(outdir+"\\"+word+".txt", os.F_OK): continue
    result = repos.get_alt_of_word(word, -1, request=False)
    if result == []: continue
    with open(outdir+"\\"+word+".txt", "w") as worda:
        for resi in result:
            count = 0
            for resi2 in resi:
                if count == 5:
                    worda.write(resi2+"\n")
                    count = 0
                else:
                    worda.write(resi2+",   ")
                    count += 1
            worda.write("\n\n---------------------------------------------------------\n")
