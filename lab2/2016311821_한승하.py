# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J0JscwNO_gAN6U1CwK5nz7PkYhXST6rQ
"""

import json

import nltk
from nltk.tokenize import word_tokenize


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
d = {}

with open('./bbc_articles.json') as json_file:
    data = json.load(json_file)
    json_string = data["business"]
    json_tech = data["tech"]
    json_politics = data["politics"]
f = open("2016311821_한승하.txt",'w')
idx = 1;
for words in json_string:
  tokens = word_tokenize(words)
  tagged_tokens = nltk.pos_tag(tokens)
  extract_tokens = list()
  for token, pos in tagged_tokens:
    if pos in ['VB','VBD','VBG','VBN','VBP','VBZ','NN','NNS','NNP','NNPS']:
      extract_tokens.append("%s/%s" % (token,pos))
  for words in extract_tokens:
    if d.get(words):
      d[words] = d[words] + 1
    else:
      d[words] = 1
  f.write("(business%d)\n" % (idx))
  sorted_dict = sorted(d.items())
  for words in sorted_dict:    
    f.write("%s\tTF:%d\n" % (words[0],words[1]))
  idx = idx + 1
  d.clear()
  sorted_dict.clear()
  extract_tokens.clear()
  f.write("\n")

idx = 1;
for words in json_tech:
  tokens = word_tokenize(words)
  tagged_tokens = nltk.pos_tag(tokens)
  extract_tokens = list()
  for token, pos in tagged_tokens:
    if pos in ['VB','VBD','VBG','VBN','VBP','VBZ','NN','NNS','NNP','NNPS']:
      extract_tokens.append("%s/%s" % (token,pos))
  for words in extract_tokens:
    if d.get(words):
      d[words] = d[words] + 1
    else:
      d[words] = 1
  f.write("(tech%d)\n" % (idx))
  sorted_dict = sorted(d.items())
  for words in sorted_dict:    
    f.write("%s\tTF:%d\n" % (words[0],words[1]))
  idx = idx + 1
  d.clear()
  sorted_dict.clear()
  extract_tokens.clear()
  f.write("\n")

idx = 1;
for words in json_politics:
  tokens = word_tokenize(words)
  tagged_tokens = nltk.pos_tag(tokens)
  extract_tokens = list()
  for token, pos in tagged_tokens:
    if pos in ['VB','VBD','VBG','VBN','VBP','VBZ','NN','NNS','NNP','NNPS']:
      extract_tokens.append("%s/%s" % (token,pos))
  for words in extract_tokens:
    if d.get(words):
      d[words] = d[words] + 1
    else:
      d[words] = 1
  f.write("(politics%d)\n" % (idx))
  sorted_dict = sorted(d.items())
  for words in sorted_dict:    
    f.write("%s\tTF:%d\n" % (words[0],words[1]))
  idx = idx + 1
  d.clear()
  sorted_dict.clear()
  extract_tokens.clear()
  f.write("\n")