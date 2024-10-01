import repos
repos.activate('pos')
word = ["laugh"]
for wor in word:
    i = repos.perm(wor)
    print(wor,"=",i,"=",repos.pos_file_fd_content_lists_word[i])
