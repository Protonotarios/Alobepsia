# -*- coding: utf-8 -*-
"""
Alobepsia 
for Python 3.x
by Ioannis Protonotarios
"""

# Add your lexicon files to the list
lexica = ['el_GR.dic']
results_file = 'results.txt'

def capitalized(word):
    return word.upper().translate(str.maketrans('¶ΆΈΉΊΪΌΎΫΏ', 'ΑΑΕΗΙΙΟΥΥΩ'))
    
def atbash(word):
    alphabet = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
    letters = list(alphabet)
    alobepsia = dict(zip(letters, reversed(letters)))
    return ''.join([alobepsia[char] for char in list(capitalized(word)) if char in letters])

open(results_file, 'w').close()
for lexicon in lexica:
    with open(lexicon) as f:
        words = f.read().splitlines()
    for word in words:
        if capitalized(word) == atbash(word[::-1]):
            print(word)
            with open(results_file, 'a') as results:
                results.write(word+'\n')
