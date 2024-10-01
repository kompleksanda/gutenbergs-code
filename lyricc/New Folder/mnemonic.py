import repos
word = input("enter word: ")
use_pron = False
if use_pron:
    repos.activate('pron')
    words = repos.pron_cmd_fd_content_word
    length = repos.pron_cmd_fd_content_len
else:
    repos.activate('pos')
    words = repos.pos_file_fd_content_lists_word
    length = repos.pos_file_fd_content_len
for i in range(length):
    c_word = words[i]
    if all(w in c_word or w.swapcase() in c_word for w in word):
        if len(c_word) <= 3 + len(word) and (c_word[0] in word or c_word[0].swapcase() in word):
            #if True:
            try:
                print(c_word)
            except UnicodeError:
                print(i)
