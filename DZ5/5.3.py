from collections import defaultdict
n = 3
l_to_e = defaultdict(list)
for i in range(n):
    e_word, l_words = input().split(' - ')
    l_trans = l_words.split(', ')
    for l_word in l_trans:
        l_to_e[l_word].append(e_word)

print(len(l_to_e))
for l_word, e_trans in sorted(l_to_e.items()):
    print(l_word + ' - ' + ', '.join(e_trans))

