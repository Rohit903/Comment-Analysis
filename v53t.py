#!/usr/bin/python3

import sys
import operator
import json
import os
import pandas as pd
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud import WatsonException
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features,SentimentOptions
#input csv file
data_Read1 = pd.read_csv(sys.argv[1])
data_Read = data_Read1[0:22222]
store=len(data_Read)
print(store)
natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='e337d8da-1054-47c5-a2bb-bd4166497a20',
  password='6Qrk7RUGiJrU',
  version='2017-02-27')


j=0
k=0
val=0
lab=""

for i in data_Read['Review Text']:
    #used by me for reference to print the sentence 
    #print(j) #count
    #print("------------------------------------------------------------------")
    #print(i) //sentence
    #print() //space
    #handling watson exception of two few words for sentiment analysis
    try:
        response = natural_language_understanding.analyze(
        text=i,
        features=Features(
        sentiment=SentimentOptions(
        )))
        sent=list(response.values())
        #print(sent)
       # handling Exceptions for the reviews for which sentiment could not be generated
        try:
            dictval=dict(sent[1])
            tpct=list(dictval.values())
            val=tpct[0]
            m= list(val.values())
            sentimentvalue=m[0]
            label=m[1]
            #printing the values on the screen used by me for reference
           #print(m[0])
            #print(m[1])
        
        except IndexError:
           pass
            

    

    #writing to the columns polarity and label sentiment and label and finally to csv file 
        data_Read.loc[j,'Polarity'] = sentimentvalue
        data_Read.loc[j,'Label'] = label
        data_Read.to_csv("50rtest1.csv")
        j=j+1

    except WatsonException:
        data_Read.loc[j,'Polarity']="NULL"
        data_Read.loc[j,'Label']="NULL"
        j=j+1

#Separating the reviews into positive and negative reviews and writing to the files
test=pd.read_csv("50rtest1.csv")
pos = test[test["Label"]=="positive"]
posper=(len(pos)/store)*100
print(posper)
neg = test[test["Label"]=="negative"]
negper=(len(neg)/store)*100
print(negper)
pos.to_csv("testpos1.csv")
neg.to_csv("testneg1.csv")
readt=pd.read_csv(sys.argv[1])
onlyrevn1=readt["Review Text"]
fabric1=onlyrevn1[onlyrevn1.str.contains("fabric" or "Fabric" or "quality")]
design1=onlyrevn1[onlyrevn1.str.contains("design" or "Design")]
stitching1=onlyrevn1[onlyrevn1.str.contains("stitching" or "Stitching")]
cost1=onlyrevn1[onlyrevn1.str.contains("price" or "cost")]
fit1=onlyrevn1[onlyrevn1.str.contains("fit" or "tight")]
count=[[],[]]
length=[[],[]]
y=0
for i in ["testpos1.csv","testneg1.csv"]:
    
    pdi = pd.read_csv(i)
    length[y]=len(pdi)
    _100k=pdi.loc[:]
    #print(_100k.columns)
    onlyrev = _100k["Review Text"]
    onlyrevn = onlyrev.dropna()
    fabric=onlyrevn[onlyrevn.str.contains("fabric" or "Fabric" or "quality")]
    filename="fabric" + str(i[4:7])+".csv"

    fabric.to_csv(filename)
    design=onlyrevn[onlyrevn.str.contains("design" or "Design")]
    filename1="design" + i[4:7]+".csv"
    #desper=(len(design)/store)/100
    #print(desper)
    design.to_csv(filename1)
    stitching=onlyrevn[onlyrevn.str.contains("stitching" or "Stitching")]
    filename2="stitching" + i[4:7]+".csv"
    #stitchper=(len(stitching)/store)/100
    #print(stitchper)
    stitching.to_csv(filename2)
    cost=onlyrevn[onlyrevn.str.contains("price" or "cost")]
    #print(cost.count)
   # costper=(len(cost)/store)/100
   # print(costper)
    filename3="cost" + i[4:7]+".csv"
    cost.to_csv(filename3)
    fit=onlyrevn[onlyrevn.str.contains("fit" or "tight")]
    #fitper=(len(fit)/store)*100
    #print(fitper)
    filename4="fit" + i[4:7]+".csv"
    fit.to_csv(filename4)

    fablen=len(fabric)
    dlen=len(design)
    stlen=len(stitching)
    clen= len(cost)
    filen= len(fit)
    flen=len(_100k)
    #print("fabric={}design={}stitching={}cost={}fitness={}".format(fablen,dlen,stlen,clen,filen))
    if(flen==0):
        fper=0.0
        sper=0.0
        dper=0.0
        cper=0.0
        fiper=0.0
    else:    
        fper = (fablen/flen)*100
        dper = (dlen/flen)*100
        sper = (stlen/flen)*100
        cper = (clen/flen)*100
        fiper = (filen/flen)*100
    count[y]= [fper,dper,sper,cper,fiper]
    y=y+1
  #  print(i.upper())    
    #print(fper)
    #print(dper)
    #print(sper)
    #print(cper)
    #print(fiper)
 #   print()
"""print(count[0][0])
print(count[1][0])
print(count[0][1])
print(count[1][1])
print(count[0][2])
print(count[1][2])
print(count[0][3])
print(count[1][3])
print(count[0][4])
print(count[1][4])
"""
fabper=(len(fabric1)/store)/100
print(fabper)
desper=(len(design1)/store)/100
print(desper)
stitchper=(len(stitching1)/store)/100
print(stitchper)
costper=(len(cost1)/store)/100
print(costper)
fitper=(len(fit1)/store)/100
print(fitper)
#print()
hh=""	
o=0
flag=0
flag1=5
#count1=[[],[],[],[],[]]
nm=["NaN","Review Text","Polarity","Label"]
#print(filename)
for i,z in zip(["fabricneg.csv","designneg.csv","stitchingneg.csv","costneg.csv","fitneg.csv","fabricpos.csv","designpos.csv","stitchingpos.csv","costpos.csv","fitpos.csv"], ["fabric","design","stitching","cost","fit","fabric","design","stitching","cost","fit"]):
    if(flag==0):
        flag=1
        print(length[1])
    if(o==flag1):
        flag1=1
        print(length[0])
    o=o+1    
    data_Read1 = pd.read_csv(i,names=nm,header=None)
    data_Read=data_Read1[0:len(data_Read1)+1]
    natural_language_understanding = NaturalLanguageUnderstandingV1(
    username='e337d8da-1054-47c5-a2bb-bd4166497a20',
    password='6Qrk7RUGiJrU',
    version='2017-02-27')

    hh=i
    j=0
    k=0
    val=0
    lab=i[:-4]
    fil=lab +"11"+".csv"
   # print("i value")
   # print(i)
   # print("pirniting j value")
    #print(z)
    #data_Read=data_Read.iloc[:,[1]]
   # print("hellowowrld")
    #print(data_Read["Review Text"])
   # data_Read=list(data_Read)

    for i in data_Read["Review Text"]:
        #used by me for reference to print the sentence 
        #print(j) //count
        #print("------------------------------------------------------------------")
        #print(i) #sentence
        #print() //space
        #handling watson exception of two few words for sentiment analysis
        try:
            response = natural_language_understanding.analyze(
            text=i,
            features=Features(
            sentiment=SentimentOptions(targets=[z]
            )))
            #print(response.values)
            sent=list(response.values())
           # print(sent)
       # handling Exceptions for the reviews for which sentiment could not be generated
            try:
                dictval=dict(sent[1])
                tpct=list(dictval.values())
                val=tpct[0]
                #print(val)
                uu=dict(val[0])
                m= list(uu.values())
                sentimentvalue=m[1]
                label=m[2]
                #print(sentimentvalue)
               # print(label)
                #printing the values on the screen used by me for reference
                # print(m[0])
                # print(m[1])
        
            except IndexError:
                 pass
            

    

    #writing to the columns polarity and label sentiment and label and finally to csv file 
            data_Read.loc[j,'Polarity'] = sentimentvalue
            data_Read.loc[j,'Label'] = label
            data_Read.to_csv(fil)
            j=j+1

        except WatsonException:
            data_Read.loc[j,'Polarity']="null"
            data_Read.loc[j,'Label']="\"null\""
            data_Read.to_csv(fil)
            j=j+1
    

    if(data_Read.empty):
        data_Read.to_csv(fil)
   # print(len(data_Read))
#Separating the reviews into positive and negative reviews and writing to the files
    #os.system("cat commonfile.csv")
    test=pd.read_csv(fil)
    neut = test[(test["Label"])=="null"]
    pos = test[(test["Label"])=="positive"]
    neg = test[test["Label"]=="negative"]
    filea=lab+"pos1.csv"
    pos.to_csv(filea)
    fileb=lab+"neg1.csv"
    neg.to_csv(fileb)
    tlen=len(data_Read)
    poslen=len(pos)
    neglen=len(neg)
    if(tlen == 0):
        percpos=0.0
        negper=0.0
    else:
        percpos =(poslen/tlen)*100 
        negper =(neglen/tlen)*100
    #print(hh.upper())    
    print(percpos)
    print(negper)
    #print(tlen)
    #print(poslen)
    #print(neglen)
   # print()

