# -*- coding: utf-8 -*-
"""2016311821_한승하_TFIDF_raw.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dGomJX85spp6NeJj7L-MiObU4Fjohe6e
"""

import nltk
import json
import math

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

fd = open("2016311821_한승하_TFIDF_raw.txt","w")

bow = dict()
TF = dict()
IDF = dict()


from nltk.tokenize import word_tokenize
with open('./bbc_articles.json') as json_file:
    data = json.load(json_file)
    json_business = data["business"]
    json_tech = data["tech"]
    json_politics = data["politics"]
json_list = list()
for items in json_business:
  json_list.append(items)
for items in json_tech:
  json_list.append(items)
for items in json_politics:
  json_list.append(items)

new_word = list()

for sentence in json_list:
  temp_list = list()
  pos_token = nltk.pos_tag(word_tokenize(sentence.lower()))
  for words in pos_token:
    if words[1] in ['VB','VBD','VBG','VBN','VBP','VBZ','NN','NNS','NNP','NNPS']:
      re_word = "/".join(words)
      temp_list.append(re_word)
      new_word.append(re_word)
  temp_list = list(set(temp_list))
  temp_list.sort()
  for tf_word in temp_list:
    if tf_word in TF:
     TF[tf_word] = TF[tf_word] + 1
    else:
     TF[tf_word] = 1
  del(temp_list)

new_word = list(set(new_word))
new_word.sort()
i = 0
for words in new_word:
    bow[words] = i

    i = i+1

for keys in TF:
  IDF[keys] = math.log(300) - math.log(TF[keys])


i = 0
for items in json_business:
  add_num = 0
  tf_idfs = list()
  artic = dict()
  i = i+1
  print_string = "(business,%d)"%i
  print(print_string,file = fd)
  pos_token = nltk.pos_tag(word_tokenize(items.lower()))
  for words in pos_token:
    if words[1] in ['VB','VBD','VBG','VBN','VBP','VBZ','NN','NNS','NNP','NNPS']:
      renew_word = "/".join(words)
      if renew_word in artic:
        artic[renew_word] = artic[renew_word] + 1
      else:
        artic[renew_word] = 1
  for items in bow:
      if items in artic:
        tf_idfs.append(artic[items] * IDF[items])
      else:
        tf_idfs.append(0)
  for numbers in tf_idfs:
      add_num = add_num + math.pow(numbers,2)
  N2 = math.sqrt(add_num)
  for numbers in tf_idfs:
    print_string = "%.4f"%(numbers/N2)
    print(print_string,end="\t",file = fd)

  del(artic)
  del(tf_idfs)
  fd.write("\n\n")

i = 0
for items in json_tech:
  add_num = 0
  tf_idfs = list()
  artic = dict()
  i = i+1
  print_string = "(tech,%d)"%i
  print(print_string,file = fd)
  pos_token = nltk.pos_tag(word_tokenize(items.lower()))
  for words in pos_token:
    if words[1] in ['VB','VBD','VBG','VBN','VBP','VBZ','NN','NNS','NNP','NNPS']:
      renew_word = "/".join(words)
      if renew_word in artic:
        artic[renew_word] = artic[renew_word] + 1
      else:
        artic[renew_word] = 1
  for items in bow:
      if items in artic:
        tf_idfs.append(artic[items] * IDF[items])
      else:
        tf_idfs.append(0)
  for numbers in tf_idfs:
      add_num = add_num + math.pow(numbers,2)
  N2 = math.sqrt(add_num)
  for numbers in tf_idfs:
    print_string = "%.4f"%(numbers/N2)
    print(print_string,end="\t",file = fd)

  del(artic)
  del(tf_idfs)
  fd.write("\n\n")

i = 0
for items in json_politics:
  add_num = 0
  tf_idfs = list()
  artic = dict()
  i = i+1
  print_string = "(politics,%d)"%i
  print(print_string,file = fd)
  pos_token = nltk.pos_tag(word_tokenize(items.lower()))
  for words in pos_token:
    if words[1] in ['VB','VBD','VBG','VBN','VBP','VBZ','NN','NNS','NNP','NNPS']:
      renew_word = "/".join(words)
      if renew_word in artic:
        artic[renew_word] = artic[renew_word] + 1
      else:
        artic[renew_word] = 1
  for items in bow:
      if items in artic:
        tf_idfs.append(artic[items] * IDF[items])
      else:
        tf_idfs.append(0)
  for numbers in tf_idfs:
      add_num = add_num + math.pow(numbers,2)
  N2 = math.sqrt(add_num)
  for numbers in tf_idfs:
    print_string = "%.4f"%(numbers/N2)
    print(print_string,end="\t",file = fd)

  del(artic)
  del(tf_idfs)
  fd.write("\n\n")

