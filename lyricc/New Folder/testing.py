import repos
repos.activate("pos")

word = "looking booking keeping shaking dodging loving lurking shocking talking bullying docking".split()
#word=["foxes"]
for wor in word:
    print(wor,"===",repos.get_word_pos(wor))

