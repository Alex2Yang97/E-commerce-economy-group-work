# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:08:11 2019

@author: yzr
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from collections import Counter
import jieba
import re
import matplotlib.pyplot as plt
from pylab import mpl


data = pd.read_excel('文献概略.xlsx')

title = data['Title'].values.tolist()
summary = data['Summary'].values.tolist()
author = data['Author'].values.tolist()
source = data['Source'].values.tolist()
year = data['Year'].values.tolist()
kword = data['Keyword'].values.tolist()
organ = data['Organ'].values.tolist()


# 分割机构
organ_dis = []
for i in range(len(organ)):
    if i in [94,256,272,273]: continue   
    a = organ[i].split(';')
    del a[-1]
    organ_dis.append(a)


# 统计机构，uni中的每一个键表示 大机构，值表示 子机构
uni_dis = []
for line in organ_dis:
    for uni in line:
        a = re.split(r'([\u4e00-\u9fa5]{2,10}?(?:大学|学院))',uni)
        while '' in a: a.remove('')
        while ' ' in a: a.remove(' ')
        uni_dis.append(a)

uni = [u[0] for u in uni_dis]
uni = list(set(uni))
uni_dict = dict()

for u in uni:
    uni_dict[u] = []
    for i in range(len(uni_dis)):
        if u == uni_dis[i][0]:
            uni_dict[u].append(uni_dis[i][1:])


# 统计 大机构 发表文章的次数
organ_cishu = []

for key in uni_dict:
    while [] in uni_dict[key]: uni_dict[key].remove([])
    if len(uni_dict[key]) == 0:
        cishu = 1
    else:
        cishu = len(uni_dict[key])
    organ_cishu.append((key,cishu))


# 先对大机构发表文章的次数进行排序
def takeSecond(elem):
    return elem[1]

organ_cishu.sort(reverse = True,key=takeSecond)


# 画图
mpl.rcParams['font.sans-serif']=['FangSong']
mpl.rcParams['axes.unicode_minus']=False

# 排名前100的大机构
label = list(map(lambda x: x[0], organ_cishu[:100]))
value = list(map(lambda y: y[1], organ_cishu[:100]))

plt.xticks(fontsize=3)
plt.xticks(rotation=90)
plt.bar(range(len(value)), value, tick_label=label)
plt.savefig('Organ_cishu1.png', dpi=400, bbox_inches='tight')
plt.show()

# 排名101到最后的
label1 = list(map(lambda x: x[0], organ_cishu[101:]))
value1 = list(map(lambda y: y[1], organ_cishu[101:]))

plt.xticks(fontsize=2)
plt.xticks(rotation=90)
plt.bar(range(len(value1)), value1, tick_label=label1)
plt.savefig('Organ_cishu2.png', dpi=400, bbox_inches='tight')
plt.show()


## 分割年份
#year_seg = []
#for i in [' 2019',' 2018',' 2017',' 2016',' 2015',' 2014']:
#    year_seg.append(year.index(i))
#
#
## 分割关键词
#kword_dis = [[] for i in range(6)]
#for i in range(len(kword)):
#    if i in [94,256,272,273]: continue
#    a = kword[i].split(';')
#    del a[-1]
#    if i in year_seg:
#        t = year_seg.index(i)
#    kword_dis[t].append(a)
#
#k = [[] for i in range(6)]    
#for i in range(len(k)):
#    kd = kword_dis[i]
#    for n in kd:
#        k[i] = k[i]+n


## 统计词频
#def cipin(data):
#    word_cipin = []
#    cnt=Counter()
#    for line in data:
#        line_cut = line.split()
#        for word in line_cut:
#            cnt[word] += 1
#    for t in cnt.most_common():
#        word_cipin.append(list(t))
#    return word_cipin,cnt.most_common()
#
#kword_cipin = [[] for i in range(6)]
#cnt = [[] for i in range(6)]
#for i in range(6):
#    kword_cipin[i],cnt[i] = cipin(k[i])
#
#
## 绘图
#def kword_plot(cn):
#    for i in range(len(cn)):
#        cnt_k = cn[i]
#        
#        mpl.rcParams['font.sans-serif']=['FangSong']
#        mpl.rcParams['axes.unicode_minus']=False
#        
#        if len(cnt_k) > 100: 
#            k=100
#            b=3
#        else:
#            k = len(cnt_k)
#            b=7
#        label = list(map(lambda x: x[0], cnt_k[:k]))
#        value = list(map(lambda y: y[1], cnt_k[:k]))
#        
#        plt.xticks(fontsize=b)
#        plt.xticks(rotation=90)
#        plt.bar(range(len(value)), value, tick_label=label)
#        plt.savefig('keyword_cipin%d.png'%i, dpi=400, bbox_inches='tight')
#        plt.show()

#kword_plot(cnt)
#
## 2018至2014年，重复出现的关键词
#intersection = []
#for term in list(set(k[1])):
#    i = 2
#    print(term)
#    while i<=5:
#        if term in k[i]:
#            i = i + 1
#        else:
#            i = 10
#    print(i)
#    if i != 10:
#        intersection.append(term)
#
#
## 分割摘要
#kword_dis = [[] for i in range(6)]
#for i in range(len(kword)):
#    if i in [94,256,272,273]: continue
#    if i in year_seg:
#        t = year_seg.index(i)
#    kword_dis[t].append(a)

## 分词
#sum_cut = []
#for line in comment_user:
#    line_cut = jieba.cut(line)
#    result = '|'.join(line_cut)
#    user_cut.append(result)
#
## 去除停用词
#with open(r'D:\科研\knowledge graph\实验\NMF\NMF1.0\stop_words.txt') as f:
#    stopwords = f.read().split('|')
#    user_cut_new = []
#for line in user_cut:
#    line = line.split()
#    outStr = ''
#    for word in line:
#        if word not in stopwords:
#            outStr += word
#            outStr += '|'
#    user_cut_new.append(outStr)


    
#with open('cipin_all.txt','w') as f1:
#    for i in comment_cipin:
#        f1.write(i[0])
#        f1.write('\t')
#        f1.write(str(i[1]))
#        f1.write('\n')


#==============================================================================测试
#words = 'study in 山海大学'
#regex_str = ".*?([\u4E00-\u9FA5]+大学)"
#match_obj = re.match(regex_str, words)
#if match_obj:
#    print(match_obj.group(1))


#ur'([\u4e00-\u9fa5]{2,5}?(?:省|自治区|市))([\u4e00-\u9fa5]{2,7}?(?:市|区|县|州)){0,1}([\u4e00-\u9fa5]{2,7}?(?:市|区|县)){0,1}'
#data_list = ['北京市', '陕西省西安市雁塔区', '西班牙', '北京市海淀区', '黑龙江省佳木斯市汤原县', '内蒙古自治区赤峰市',
#'贵州省黔南州贵定县', '新疆维吾尔自治区伊犁州奎屯市']

