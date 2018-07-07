# -*- coding: UTF-8 -*-


from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from keras.layers import Input, Dense
from keras.models import Model
from keras.callbacks import TensorBoard


file = 'texto/movies_modificadoID_1M.csv'
content = []
cont = 0
for line in open(file).readlines():
 if len(line) > 3:
    line = (line.split('::'))
    print (line[0],line[2])
    content.insert(int(line[0]), line[2].strip() + ' ' + line[3].strip())

print ('Quantidade de Filmes: ',len(content))

################Construir a Bag Of Words##################
vectorizer = TfidfVectorizer(min_df=1)
dtm = vectorizer.fit_transform(content)
dtm = dtm.toarray()  # convert to a regular array
norms = np.sqrt(np.sum(dtm * dtm, axis=1, keepdims=True))

###################Calculo da Similaridade entre os vídeos#######################
from sklearn.metrics.pairwise import cosine_similarity
similarities = cosine_similarity(dtm[:], dtm)

#########################Criando o arquivo side information###########################
linha = len(similarities)
coluna = len(similarities[0])
nome = 'texto/bagOfWords1M.tsv'
f = open(nome, "w")

for i in range(linha):
    for j in range(coluna):
        if str(similarities[i, j]).startswith('nan'):
            # print idVideo[dic_videos[i+1]] ,  + idVideo[dic_videos[j+1]] , '0'
            f.write(str(i+1) + ' ' + str(j + 1) + ' ' + 'NAN' + '\n')
        else:
            f.write(str(i + 1) + ' ' + str(j + 1) + ' ' + str(similarities[i, j]) + '\n')


print('Acabou')
