new = "C:\\Users\\pc\\Desktop\\myphone\\Download\\cmudict-master\\cmudict-master\\cmudict.dict"
old = r"C:\Users\pc\Documents\download\gutenberg\pronunciation\files\cmudict.txt"
out = r"C:\Users\pc\Desktop\moby\cmudict.txt"

old = open(old, encoding='iso8859-1')
new= open(new, encoding='iso8859-1')
out= open(out, 'w')

old_lines = old.readlines()
new_lines = new.readlines()
new_dict = {}
old_dict = {}
for i in new_lines:
	i = i.strip('\n').split(' ', 1)
	new_dict[i[0].strip().upper()] = i[1].strip()
for i in old_lines:
	i = i.strip('\n').split(' ', 1)
	i[0] = i[0].strip()
	old_dict[i[0]] = i[1].strip()
ov = old_dict.values()
for key in new_dict.keys():
    if key not in old_dict and new_dict[key] not in ov:
            old_dict.update({key:new_dict[key]})
    #elif key in old_dict and new_dict[key] not in ov:
    #       old_dict.update({key+'((':new_dict[key]})
for k,v in old_dict.items():
        out.write(k+' '+v+'\n')
old.close()
new.close()
out.close()
