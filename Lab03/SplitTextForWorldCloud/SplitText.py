# coding:utf-8

import codecs
from collections import Counter
import jieba


TEXT_PATH = './doc/CallOfCthulhu.txt'

with codecs.open(TEXT_PATH, 'r', 'UTF-8') as f:
    text = f.read()
jieba_word = jieba.cut(text, cut_all=False)  
data = []
for word in jieba_word:
    data.append(word)

dataDict = Counter(data)
with open('./doc/词频统计.csv', 'w', encoding='UTF-8') as fw:
    for k, v in dataDict.items():
        if (v >= 0):
            fw.write("%s,%d\n" % (k, v))
        else:
            fw.write("%s,%d\n" % ("null", 0))
print("Finish")