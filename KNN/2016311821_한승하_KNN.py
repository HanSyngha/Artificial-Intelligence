# -*- coding: utf-8 -*-
"""2016311821_한승하_KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LOQldhTkYhGgN_lAiQ8rhE0pzDk_AxOo
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import nltk
import json
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#output file
fd = open('./2016311821_한승하_KNN.txt','w') 

#opening files
with open("./bbc_articles_train.json",'r') as train_file:
  train_data = json.load(train_file)
  train_business = train_data['business']
  train_tech = train_data['tech']
  train_politics = train_data['politics']

with open("./bbc_articles_test.json",'r') as test_file:
  test_data = json.load(test_file)
  test_business = test_data['business']
  test_tech = test_data['tech']
  test_politics = test_data['politics']

#Make it to one list
train_corpus = list()
test_corpus = list()
for sentence in train_business:
  train_corpus.append(sentence)
for sentence in train_tech:
  train_corpus.append(sentence)
for sentence in train_politics:
  train_corpus.append(sentence)

for sentence in test_business:
  test_corpus.append(sentence)
for sentence in test_tech:
  test_corpus.append(sentence)
for sentence in test_politics:
  test_corpus.append(sentence)

#Get POS result
POS_tags = ['NN','NNS','NNP','NNPS','VB','VBD','VBG','VBN','VBP','VBZ']
POS_corpus_train = list()
for sentence in train_corpus:
  pos_token = nltk.pos_tag(word_tokenize(sentence))
  POS_corpus_train.append(''.join(t[0] for t in pos_token if t[1] in POS_tags))

#GET TF_IDF
tfidfvect = TfidfVectorizer()
tfidfvect.fit_transform(POS_corpus_train)
train_tf_idf = tfidfvect.transform(POS_corpus_train).toarray().tolist()

#make label
train_labels = list()
for i in range (0,80):
    train_labels.append('business')
for i in range (80,160):
    train_labels.append('tech')
for i in range (160,240):
    train_labels.append('politics')
test_labels = list()
for i in range (0,20):
    test_labels.append('business')
for i in range (20,40):
    test_labels.append('tech')
for i in range (40,60):
    test_labels.append('politics')

#Test TF_IDF
POS_corpus_test = list()
for sentence in test_corpus:
  pos_token = nltk.pos_tag(word_tokenize(sentence))
  POS_corpus_test.append(''.join(t[0] for t in pos_token if t[1] in POS_tags))
test_tf_idf = tfidfvect.transform(POS_corpus_test).toarray().tolist()

#KNN
classifier = KNeighborsClassifier(n_neighbors=1, weights='distance',metric="euclidean")
classifier.fit(train_tf_idf,train_labels)
prediction = classifier.predict(test_tf_idf)



#confusion matrix
print('Confusion matrix',file=fd)
conf = confusion_matrix(test_labels, prediction)
for tup in conf:
  for num in tup:
    print(num,end="\t",file=fd)
  print("\n",file=fd)

# Accuracy
acc = "Accuracy : %.4f"%(accuracy_score(test_labels, prediction) * 100)
print(acc+"%",end="\n\n",file=fd)

# Precision
prec1 = "Macro averaging precision : %.4f"%(precision_score(test_labels, prediction, average='macro') * 100)
print(prec1+"%",file=fd)
prec2 = "Micro averaging precision : %.4f"%(precision_score(test_labels, prediction, average='micro') * 100)
print(prec2+"%",end="\n\n",file=fd)

# Recall
recal1 = "Macro averaging recall : %.4f"%(recall_score(test_labels, prediction, average='macro') * 100)
print(recal1 + "%",file=fd)
recal2 = "Micro averaging recall : %.4f"%(recall_score(test_labels, prediction, average='micro') * 100)
print(recal2 + "%",end="\n\n",file=fd)

# F1-score
F11 = "Macro averaging f1-score : %.4f"%(f1_score(test_labels, prediction, average='macro') * 100)
print(F11+"%",file=fd)
F12 = "Micro averaging f1-score : %.4f"%(f1_score(test_labels, prediction, average='micro') * 100)
print(F12+"%",file=fd)

fd.close()

