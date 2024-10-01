import json, random
ddir = r"C:\Users\pc\Desktop\moby\Part Of Speech"
variables = ["nouns", "plurals", "noun_phrases", "verbs_part", "verbs_trans", "verbs_intrans", "adjectives", "adverbs", "conjunctions", "prepositions", "interjections", "pronouns", "def_articles", "indef_articles", "nominatives"]
for i in variables:
    with open(ddir+"\\"+i+".txt") as j: exec(i+" = json.load(j)")
word = input("Enter letters: ")
for m in range(30):
    string = ""
    for i in range(len(word)):
        w = word[i]
        if  i % 2 == 0:
            res = [a for a in nouns+plurals+noun_phrases+pronouns if a[0].lower() == w]
            string += random.choice(res)+" "
        else:
            res = [a for a in verbs_part+verbs_trans+verbs_intrans if a[0].lower() == w]
            string += random.choice(res)+" "
    print(string)
