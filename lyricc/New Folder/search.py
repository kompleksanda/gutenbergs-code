import repos
word = input("enter word: ").upper()
repos.activate('pos')
words = repos.pos_file_fd_content_lists_word
length = repos.pos_file_fd_content_len
for i in words:
    ip = i.upper()
    if word in ip:
        try:print(i)
        except UnicodeEncodeError: print("---------")
