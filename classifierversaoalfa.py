#%% 
import numpy as np
import pandas as pd
import re
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import matplotlib.pyplot as plt

from sklearn import metrics
import unicodedata

dataset = pd.read_csv('tweets_database.csv',encoding='cp1252')
colunas = ["texto","classificacao"]
lista = ["usuario","id","texto","classificacao","categoria"]

df = pd.read_csv('tweets_database.csv', sep = ',', names = lista, usecols=colunas, encoding="utf-8")
df = df.drop(0)

textoEntradas = df.texto
labels = df.classificacao

stopwords = ["de","a","o","que","e","do",
"da","em","um","para","é","com","não","uma"
,"os","no","se","na","por","mais","as","dos"
,"como","mas","foi","ao","ele","das","tem","à"
,"seu","sua","ou","ser","quando","muito","há"
,"nos","já","está","eu","também","só","pelo"
,"pela","até","isso","ela","entre","era","depois"
,"sem","mesmo","aos","ter","seus","quem","nas"
,"me","esse","eles","estão","você","tinha","foram"
,"essa","num","nem","suas","meu","às","minha","têm"
,"numa","pelos","elas","havia","seja","qual","será"
,"nós","tenho","lhe","deles","essas","esses","pelas"
,"este","fosse","dele","tu","te","vocês","vos","lhes"
,"meus","minhas","teu","tua","teus","tuas","nosso"
,"nossa","nossos","nossas","dela","delas","esta"
,"estes","estas","aquele","aquela","aqueles","aquelas"
,"isto","aquilo","estou","está","estamos","estão"
,"estive","esteve","estivemos","estiveram","estava","estávamos"
,"estavam","estivera","estivéramos","esteja","estejamos"
,"estejam","estivesse","estivéssemos","estivessem","estiver"
,"estivermos","estiverem","hei","há","havemos","hão","houve",
"houvemos","houveram","houvera","houvéramos","haja","hajamos",
"hajam","houvesse","houvéssemos","houvessem","houver","houvermos",
"houverem","houverei","houverá","houveremos","houverão","houveria",
"houveríamos","houveriam","sou","somos","são","era","éramos","eram",
"fui","foi","fomos","foram","fora","fôramos","seja","sejamos","sejam",
"fosse","fôssemos","fossem","for","formos","forem","serei","será",
"seremos","serão","seria","seríamos","seriam","tenho","tem","temos","tém",
"tinha","tínhamos","tinham","tive","teve","tivemos","tiveram","tivera",
"tivéramos","tenha","tenhamos","tenham","tivesse","tivéssemos"
,"tivessem","tiver","tivermos","tiverem","terei","terá","teremos"
,"terão","teria","teríamos","teriam"]

def remover_acentuacao(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def preprocessamento_texto(text):    
    for palavra in stopwords:
        text = text.replace(" " + palavra + " ", " ")
    text = remover_acentuacao(text)
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','', text)
    text = re.sub('@[^\s]+','', text)    
    text = text.lower()
    text = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text)
    text = re.sub(' +',' ', text)
    return text.strip()

entradas = [preprocessamento_texto(t) for t in textoEntradas]

text_clf = Pipeline([('vect', CountVectorizer()),                    
                     ('clf', MultinomialNB())])

tuned_parameters = {
    'vect__ngram_range': [(1, 1), (1, 2), (2, 2)],
    'clf__alpha': [1, 1e-1, 1e-2]
}

score = 'accuracy'

for()

x_train, x_test, y_train, y_test = train_test_split(entradas, labels, test_size=0.33, random_state=42)


clf = GridSearchCV(text_clf, tuned_parameters, cv=5, scoring=score)
np.errstate(divide='ignore')
clf.fit(x_train, y_train)


for mean, std, params in zip(clf.cv_results_['mean_test_score'], 
                             clf.cv_results_['std_test_score'], 
                             clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r" % (mean, std * 2, params))

print()
print()
print("Parametros Globais com os melhores resultados:")
print()
print(clf.best_params_)
print()

print("Resultados:")
print(classification_report(y_test, clf.predict(x_test), digits=4))
print()
y_pred = clf.best_estimator_.predict(x_train)
print()

#%%
