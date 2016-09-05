# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:11:06 2015

@author: suppu
"""
from nltk.corpus import indian
'''
Let us generate a file having sentences in indian languages. The file is generated from the indian languages scorpus available
'''
print "Number of charachetrs is:"
for f in indian.fileids():
    print f
    print len(indian.raw(f))
print "No of words in each language are:"
for f in indian.fileids():
    print f
    print len(indian.words(f))
print "Number of sentences in each language:"
for f in indian.fileids():
    print f
    print len(indian.sents(f))
'''POS for hindi
'''
hindi_sent=indian.sents("hindi.pos")
hsent=file("hws.txt",'w')
for i in hindi_sent:
    hsent.write(" ".join(i))
hpos=indian.tagged_sents("hindi.pos")
hpossent=open("hpossent.txt",'w')
hpossent.seek(0)
for i in hpos:
    for j in i:
        hpossent.write(j[0]+" "+j[1]+"\n")
'''
POS for bangla
'''
bang_sent=indian.sents("bangla.pos")
bsent=file("bws.txt",'w')
for i in bang_sent:
    bsent.write(" ".join(i))
bpos=indian.tagged_sents("bangla.pos")
bpossent=open("bpossent.txt",'w')
bpossent.seek(0)
for i in bpos:
    for j in i:
        bpossent.write(j[0]+" "+j[1]+"\n")
'''
POS fr marathi
'''        
mar_sent=indian.sents("marathi.pos")
msent=file("mws.txt",'w')
for i in mar_sent:
    msent.write(" ".join(i))
mpos=indian.tagged_sents("marathi.pos")
mpossent=open("mpossent.txt",'w')
mpossent.seek(0)
for i in mpos:
    for j in i:
        mpossent.write(j[0]+" "+j[1]+"\n")
#POS for telgu
tel_sent=indian.sents("telugu.pos")
tsent=file("tws.txt",'w')
for i in tel_sent:
    tsent.write(" ".join(i))
tpos=indian.tagged_sents("telugu.pos")
tpossent=open("tpossent.txt",'w')
tpossent.seek(0)
for i in tpos:
    for j in i:
        tpossent.write(j[0]+" "+j[1]+"\n")

'''
OUPUT

Number of charachetrs is:
bangla.pos
121075
hindi.pos
103087
marathi.pos
229853
telugu.pos
138273
No of words in each language are:
bangla.pos
10281
hindi.pos
9408
marathi.pos
19066
telugu.pos
9999
Number of sentences in each language:
bangla.pos
899
hindi.pos
540
marathi.pos
1197
telugu.pos
994
'''