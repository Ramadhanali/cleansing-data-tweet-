import pandas as pd
import re
import nltk 
from nltk.corpus import stopwords

listStopword =  set(stopwords.words('indonesian'))

data_slang = pd.read_csv (r"D:\data analys\chalenge\archive\new_kamusalay.csv",encoding = 'latin = 1', names=['kata_slang','kata_baku'])

def cleansing (t):
  x1 = re.sub ('RT',' ',t)
  x2 = re.sub ('USER',' ',x1)
  x3 = re.sub ('http/s+',' ', x2)
  x4 = re.sub ('[^a-zA-Z0-9]+',' ',x3)
  x5 = re.sub ('x[a-z0-9]{2}', ' ',x4)
  x6 = x5.lower()
  return x6

def replace (x):
    sent = []
    for i in x.split():
        if i in data_slang.kata_slang.values:
            sent.append(data_slang[data_slang['kata_slang'] == i]['kata_baku'].iloc [0])
        else:
            sent.append(i)
        sent.append(' ')
    text= ''.join(sent)
    return text

def remove(y) :
    sent=[]
    for t in y.split():
        if t not in listStopword:
            sent.append(t)
        sent.append(' ')
    text= ''.join(sent)
    text= re.sub('  +', ' ',text)
    return text

def challenge (x) : 
    text = cleansing (x)
    text = replace (text)
    text = remove (text)
    return text 