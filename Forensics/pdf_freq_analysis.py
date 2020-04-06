"""
================================================
	Y    U    B    I    T    S   E    C
================================================
Created by echel0n_1881
@ 14 Kas 2017

This will parse the text file and prints the words
and their counts.
================================================
	Y    U    B    I    T    S   E    C
================================================
"""

import re
import string
frequency = {}
document_text = open('1.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency = sorted(frequency.items(), key=lambda x: x[1])
frequency_list = frequency.keys()
for words in frequency_list:
    print words, frequency[words]
