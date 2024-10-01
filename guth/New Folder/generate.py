import json, random
ddir = r"C:\Users\pc\Desktop\moby\Part Of Speech"
#ddir = r"/sdcard/moby/POS"
variables = ["nouns", "plurals", "noun_phrases", "verbs_part", "verbs_trans", "verbs_intrans", "adjectives", "adverbs", "conjunctions", "prepositions", "interjections", "pronouns", "def_articles", "indef_articles", "nominatives"]
for i in variables:
    with open(ddir+"\\"+i+".txt") as j: exec(i+" = json.load(j)")
word = input("Enter letters: ")

rules = {1:["N"],\
        2:["NV", "AN", "DN", "NN", "AN"],\
        3:["NVN", "VCV", "NAN", "DNV", "BNN", "NNN", "ANN","AAN"],\
        4:["DNAN", "DNBV", "VNVN", "BNNN", "NNBN", "NVNB", "NNDN"],\
        5:["DVDNV", "DNNNN", "NNBNN", "NNVNB" ,"NNNDN", "DNNVN"],\
        6:["DVDNBV", "DNNBNN", "NVVBDN", "NNAPDN", "ABBNVAN"],\
        7:["DNNNVDN", "NNBABVN", "ABBNVAN", "NNNBVAN","NVNANPN"],\
        8:["NNVBNPDN", "DNNVNPDN", "NNNPBNVP"],\
        9:["NNDNNDNNN", "DNCDNNBDB", "DNNNNNVBV"],\
        10:["NNNNNVBNCV", "NVNVVNNDAN", "CNVPNDNVNN"]}
#rules = {3:["AAN"]}

def get(letters, rule):
    string = ""
    for i in range(len(rule)):
        let = letters[i]
        ru = rule[i]
        if ru == "N":
            res = [a for a in nouns+plurals+noun_phrases+pronouns if a[0].lower() == let]
            if not res: res = ["___"]
            string += random.choice(res)+" "
        elif ru == "V":
            #res = [a for a in verbs_part+verbs_trans+verbs_intrans if a[0].lower() == let]
            res = [a for a in verbs_part if a[0].lower() == let]
            if not res: res = ["___"]
            string += random.choice(res)+" "
        elif  ru == "A":
            res = [a for a in adjectives if a[0].lower() == let]
            if not res: res = ["___"]
            string += random.choice(res)+" "
        elif  ru == "C":
            res = [a for a in conjunctions if a[0].lower() == let]
            if not res: res = ["___"]
            string += random.choice(res)+" "
        elif ru == "D":
            res = [a for a in def_articles if a[0].lower() == let]
            if not res: res = ["___"]
            string += random.choice(res)+" "
        elif ru == "B":
            res = [a for a in adverbs if a[0].lower() == let]
            if not res: res = ["___"]
            string += random.choice(res)+" "
        elif ru == "P":
            res = [a for a in prepositions if a[0].lower() == let]
            if not res: res = ["___"]
            string += random.choice(res)+" "
        else: print("'",ru,"' is undefined")
    return string

rule = rules[len(word)]
for i in range(50):
    rul = random.choice(rule)
    print(get(word, rul))

