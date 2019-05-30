#!/usr/bin/python
"""mapper_co.py"""

import sys
import re
import string

# input comes from STDIN (standard input)
for text in sys.stdin:
    paras = text.split("\n")
    for line in paras:
        line = line.strip().lower()
        line = re.sub(r'[^\w\s]','',line)
        stopwords = ['some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be','above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'until', 'below', 'are', 'we', 'these', 'your',
'most', 'itself', 'other', 'off', 'is', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves','then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which','those', 'i', 'after', 'few', 'whom', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than', 'rt', 'wa', 'ha', 'said','would', 'one','game','player','season','year','time','team','first','de','la','yearly','mr','kraft', 'salary', 'en', 'y', 'que','unnamed']
        # spliting the line to words
        words = line.split()
        cleaned_data = [word for word in words if word not in stopwords]

        # to increase the counts
        for a in list(range(0,len(cleaned_data)-1)):
            for b in list(range(a,len(cleaned_data)-1)) :
                if cleaned_data[a] != cleaned_data[b]:
		    print '%s\t%s' % (str(cleaned_data[a]+','+cleaned_data[b]), 1)
