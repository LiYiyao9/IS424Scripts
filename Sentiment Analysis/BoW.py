from nltk.corpus import stopwords
import nltk
from collections import Counter
import numpy as np
import re
import csv
import unidecode

dic = []
songName = []
file_csv = csv.reader(
    open(r'user_song_data_ver1 - user_song_data_ver1.csv', 'r', encoding='utf-8'))
next(file_csv)

for row in file_csv:
    dic.append(row[10])
    songName.append(row[1])

#dic.remove(dic[0])

data = []
with open('Cleaned_Sentiment_List.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    data.append(row)

data.remove(data[0])

stop_words = set(stopwords.words('english'))

bad_chars = ['...','.','..',','] 
def word_extraction(sentence):
    ignore = stop_words
    words = re.sub("[^\w]", " ",  sentence).split()
    cleaned_text = [w.lower() for w in words if w not in ignore]
    return cleaned_text


def bigram(sentence):
    bigrams = []
    cleaned_bigram =[]
    for i in bad_chars : 
      sentence1 = sentence.replace(i, '') 

    for l in zip(sentence1.split()[:-1], sentence1.split()[1:]):
      bigrams.append(l)

    for j in bigrams:
      if j[0] not in stop_words and j[1] not in stop_words:
        cleaned_bigram.append(j)

    return cleaned_bigram


a = 0
finalResult = []
     
# Assigning Score Based on sentiments

# TFIDF, LDA, ngram, dont remove stop words if analyzing by sentence, topic modelling, clustering for survey results see maybe depress people tends to listen to happy song etc


for i in dic:
  words = []
  dicWords = []
  result = word_extraction(i) 
  #result contains all lyrics separated into 1 word each in an array
  #store everything into dicword to use for final word count 
  dicWords.extend(result)
  for j in result:
    if not j in words:
        words.append(j)

  list = {}
  counter = 0
  for l in data:
      sentimentScore = 0
      if l[2] in words:
          sentimentScore = float(l[0]) - float(l[1])
          if l[2] in list:
              list[l[2]] = list[l[2]] + sentimentScore
          else:
              list[l[2]] = sentimentScore
      

  negativeCount = 0
  positiveCount = 0
  noTagCount = 0      
  counts = Counter(dicWords)  
  for m in counts:
    if m in list:
      if list.get(m) > 0:
            positiveCount = positiveCount + 1
      elif list.get(m) < 0:
        negativeCount = negativeCount + 1
      else:
        noTagCount = noTagCount + 1

  totalCount = positiveCount + negativeCount + noTagCount

  positivePercentage = positiveCount/totalCount * 100
  negativePercentage = negativeCount/totalCount * 100
  neturalPercentage = noTagCount/totalCount * 100

  # finalList = []
  # finalList.append(positivePercentage)
  # finalList.append(negativePercentage)
  # finalList.append(neturalPercentage)
  
  #if max(finalList) == positivePercentage:
    #finalResult.append("Positive," + songName[a])
  #elif max(finalList) == negativePercentage:
    #finalResult.append("Negative," + songName[a])
  #elif max(finalList) == neturalPercentage:
    #finalResult.append("Neutral," + songName[a])
  #else: 
    #finalResult.append("Unknown," + songName[a])

  #########################################################
  #bigram codes below
  biwords = []
  bidicWords = []
  biresult = bigram(i) 
  #result contains all lyrics separated into 1 word each in an array
  #store everything into dicword to use for final word count 
  bidicWords.extend(biresult)
  for j in biresult:
    if not j in biwords:
        biwords.append(j)

  bilist = {}
  bicounter = 0
  for l in data:
      sentimentScore = 0
      for j in biwords:
        if l[2] in j:
            sentimentScore = float(l[0]) - float(l[1])
            if l[2] in bilist:
                bilist[l[2]] = bilist[l[2]] + sentimentScore
            else:
                bilist[l[2]] = sentimentScore
      

  binegativeCount = 0
  bipositiveCount = 0
  binoTagCount = 0      
  bicounts = Counter(bidicWords)  
  overall_Score = 0
  for m in bicounts:    
    if m[0] in bilist and m[1] in bilist:          
        overall_Score = bilist.get(m[0]) + bilist.get(m[1])
        if overall_Score > 0:
          bipositiveCount = bipositiveCount + 1
        elif overall_Score < 0:
          binegativeCount = binegativeCount + 1
        else:
          binoTagCount = binoTagCount + 1

  bitotalCount = bipositiveCount + binegativeCount + binoTagCount

  if bitotalCount != 0:
    bipositivePercentage = bipositiveCount/bitotalCount * 100
    binegativePercentage = binegativeCount/bitotalCount * 100
    bineturalPercentage = binoTagCount/bitotalCount * 100

    
  finalScore = (positivePercentage * 0.4) + (bipositivePercentage * 0.6)

  # bifinalList = []
  # bifinalList.append(bipositivePercentage)
  # bifinalList.append(binegativePercentage)
  # bifinalList.append(bineturalPercentage)
  
  if finalScore > 0.6:
    finalResult.append("Positive," + songName[a])
  elif finalScore <0.4:
    finalResult.append("Negative," + songName[a])
  elif finalScore <0.6 and finalScore >0.4:
    finalResult.append("Neutral," + songName[a])
  else: 
    finalResult.append("Unknown," + songName[a])
  
  a= a+1

  

#export to result.csv
with open('result.csv', 'w') as f:
  for item in finalResult:
    f.write("%s\n" % item)