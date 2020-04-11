# -*- coding: utf-8 -*-

import jieba
import jieba.analyse




lines=[]
fenci=[]
for d in open("C:\Users\92084\Desktop\jbtest.txt"):
    lines.append(d)
    fenci.append('/'.join(jieba.cut(d)))

for f in fenci:
    print f

for line in lines:
    print line
    a=jieba.analyse.textrank(line)
    print a
    for v in a:
        print v
    print '\n'


