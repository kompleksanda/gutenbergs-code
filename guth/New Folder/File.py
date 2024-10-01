import pronouncing
import random

def ms(num=2, text = 'april is the cruelest month breeding lilacs out of the dead'):
	out = list()
	for word in text.split():
		phones = pronouncing.phones_for_word(word)
		if phones == []:
			out.append(word)
			continue
		first2 = phones[0].split()[:num]
		out.append(random.choice(pronouncing.search("^" + " ".join(first2))))

	print(' '.join(out))

def st(text = 'april is the cruelest month breeding lilacs out of the dead'):
	out = list()
	for word in text.split():
  		pronunciations = pronouncing.phones_for_word(word)
  		pat = pronouncing.stresses(pronunciations[0])
  		replacement = random.choice(pronouncing.search_stresses("^"+pat+"$"))
  		out.append(replacement)
	print(' '.join(out))

def rh(text = 'april is the cruelest month breeding lilacs out of the dead'):
 out = list()
 for word in text.split():
   rhymes = pronouncing.rhymes(word)
   if len(rhymes) > 0:
     out.append(random.choice(rhymes))
   else:
     out.append(word)
 print (' '.join(out))

t='I love life'
for i in range(5):
	rh(t)
	#ms(4,t)
