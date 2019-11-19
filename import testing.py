# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:08:55 2019

@author: 可欣
"""

from stanfordcorenlp import StanfordCoreNLP
nlp=StanfordCoreNLP(r'D:\学习那些事\研一\学习日常\NLP\stanfordnlp',lang='zh')
fin=open('news.txt','r',encoding='utf8')
fner=open('ner.txt','w',encoding='utf8')
ftag=open('pos_tag.txt','w',encoding='utf8')
 
for line in fin:
    line=line.strip()
    if len(line)<1:
        continue
    
    fner.write(" ".join([each[0]+"/"+each[1] for each in nlp.ner(line) if len(each)==2 ])+"\n")
    ftag.write(" ".join([each[0]+"/"+each[1] for each in nlp.pos_tag(line) if len(each)==2 ]) +"\n")
fner.close()
ftag.close()