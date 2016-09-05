# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:39:14 2015

@author: suppu
"""

import nltk
import nltk.data
from nltk.corpus import indian
word_to_be_tagged = u"पूर्ण प्रतिबंध हटाओ : इराक"

hindi_sents=indian.sents("hindi.pos")
train_data = indian.tagged_sents('hindi.pos')[:300] 
test_data = indian.tagged_sents('hindi.pos')[301:]

from nltk.tag import tnt
tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data)
tnt_pos_tagger.evaluate(test_data)

tagged=(tnt_pos_tagger.tag(nltk.word_tokenize(word_to_be_tagged)))
out=open("ooutput.txt",'w')
for i in tagged:
    out.write(i[0])
    out.write(" "+i[1]+"\n")
    
'''
OUTPUT ooutput.txt file:
पूर्ण JJ
प्रतिबंध NN
हटाओ VFM
: SYM
इराक NNP
'''