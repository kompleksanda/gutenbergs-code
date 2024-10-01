totalWords = []
import repos, os, json
with open(r"C:\Users\USER\Desktop\moby\jsson.txt") as op:
    totalWords = json.load(op)
repos.activate("alt")
outdir = r"C:\Users\USER\Desktop\moby\rim\alt\nnnn"
outdir2 = r"C:\Users\USER\Desktop\moby\rim\alt\nnnn2"
outdir3 = r"C:\Users\USER\Desktop\moby\rim\alt\nnnn3"
l = len(totalWords)
for word in totalWords:
    print ("remains", l-1)
    l -= 1
    #if (os.access(outdir+"\\"+word+".txt", os.F_OK)) or (os.access(outdir2+"\\"+word+".txt", os.F_OK)):
    #    continue
    result = repos.get_alt_of_word(word, -1, request=False)
    if result == []:
        continue
    with open(outdir3+"\\"+word+".txt", "w") as worda:
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
