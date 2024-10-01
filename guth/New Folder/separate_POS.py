import repos
import json, os
#word = input("Enter word: ")
repos.include_pos = True
repos.activate('pron')
words = repos.pron_cmd_fd_content_word
length = repos.pron_cmd_fd_content_len
part_os = repos.pron_cmd_fd_content_pos
nouns, plurals, noun_phrases, verbs_part, verbs_trans, verbs_intrans, adjectives, adverbs, conjunctions, prepositions, interjections, pronouns, def_articles, indef_articles, nominatives = [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

total = ["nouns", "plurals", "noun_phrases", "verbs_part", "verbs_trans", "verbs_intrans", "adjectives", "adverbs", "conjunctions", "prepositions", "interjections", "pronouns", "def_articles", "indef_articles", "nominatives"]

for i in range(length):
    w = words[i]
    p = part_os[i]
    if p == "*": continue
    for each in p:
        if each == "N": nouns.append(w)
        elif each == "p": plurals.append(w)
        elif each == "h": noun_phrases.append(w)
        elif each == "V": verbs_part.append(w)
        elif each == "t": verbs_trans.append(w)
        elif each == "i": verbs_intrans.append(w)
        elif each == "A": adjectives.append(w)
        elif each == "v": adverbs.append(w)
        elif each == "C": conjunctions.append(w)
        elif each == "P": prepositions.append(w)
        elif each == "!": interjections.append(w)
        elif each == "r": pronouns.append(w)
        elif each == "D": def_articles.append(w)
        elif each == "I": indef_articles.append(w)
        elif each == "o": nominatives.append(w)
out_dir = r"C:\Users\pc\Desktop\moby\Part Of Speech"
if not os.access(out_dir, os.F_OK):
    os.mkdir(out_dir)
for each in total:
    ddir = out_dir+"\\"+each+".txt"
    with open(ddir, "w") as fp:
        json.dump(eval(each), fp)
print("done")
