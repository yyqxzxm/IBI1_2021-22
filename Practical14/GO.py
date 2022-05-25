import xml.dom.minidom
from xml.dom.minidom import parse
import matplotlib.pyplot as plt
from numpy import*
name='go_obo.xml'
DOMTree = xml.dom.minidom.parse(name)
obo = DOMTree.documentElement
terms = obo.getElementsByTagName('term')
hh =[]
hh_tran=[]
def yy(did,score_set):
    if did in tree_dic:
        child_direct=tree_dic[did]
        if len(child_direct) > 0:
            for j in child_direct:
                score_set.add(j)
                yy(j,score_set)
    else:
        score_set.add(did)
z = 0
x = 0

go_id = []
k_id =[]
go_chl = {}
tree_dic={}
child_num={}
for term in terms:
    z += 1
    x = len(term.getElementsByTagName('is_a'))
    id_go = term.getElementsByTagName('id')[0]
    id_mark=id_go.childNodes[0].data
    if x>0:
        for i in range(x):
            is_a = term.getElementsByTagName('is_a')[i]
            is_a_go = is_a.childNodes[0].data
            if is_a_go not in hh:
                hh.append(is_a_go)
                tree_dic[is_a_go]=[id_mark]
            else:
                tree_dic[is_a_go].append(id_mark)
print(z)
for term in terms:
    id_mark = term.getElementsByTagName('id')[0].childNodes[0].data
    x=len(term.getElementsByTagName('is_a'))
    if x > 0:
        for i in range(x):
            is_a = term.getElementsByTagName('is_a')[i].childNodes[0].data
            child_num[is_a]=0
for index in tree_dic:
    score_set = set()
    yy(index,score_set)
    for i in score_set:
        child_num[index] += 1

for i in child_num.values():
    k_id.append(i)
for i in hh:
    go_id.append(i)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.boxplot(k_id,vert=True,whis=1.5,patch_artist=True,notch=False)
plt.title('Distribution of child nodes across terms in Gene Ontology')
plt.xlabel("all terms in Gene Ontology")
plt.ylabel('Child Nodes Number')
plt.show()

dic={}
dic_number={}
translation=[]
average_list=[]
translation_number=[]
for term in terms:
    ids=term.getElementsByTagName('id')[0].childNodes[0].data
    direct_parents_id=[]
    for is_a in term.getElementsByTagName('is_a'):
        direct_parents_id.append(is_a.childNodes[0].data)
    dic[ids]= direct_parents_id
    dic_number[ids]=0
    if term.getElementsByTagName("defstr")[0].childNodes[0].data.find("translation"or"Translation")!=-1:
        translation.append(True)
    else:
        translation.append(False)

def yy(direct_id,parent):
    pa_direct=dic[direct_id]
    if len(pa_direct):
        for j in pa_direct:
            parent.add(j)
            yy(j,parent)


for key in dic.keys():
    parent=set()
    yy(key,parent)

    for i in parent:
        dic_number[i]+=1


for index,(a,b)in enumerate(dic_number.items()):
    average_list.append(b)
    if translation[index]:
        translation_number.append(b)
        
plt.boxplot(translation_number,vert=True,whis=1.5,patch_artist=True,notch=False)
plt.title('Distribution of child nodes across terms associated with translation')
plt.xlabel('terms related to translation')
plt.ylabel('Child Nodes Number')
plt.show()


ave=12.08177017321504
ave_transition=mean(translation_number)
if ave>ave_transition:
    print("The translation terms contain, on average, a smaller number of child nodes than the overall Gene Ontology.")
else:
    print("The translation terms contain, on average, a greater number of child nodes than the overall Gene Ontology.")




