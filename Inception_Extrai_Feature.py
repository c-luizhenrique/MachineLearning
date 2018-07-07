###Este trabalho extrai features de imagens a partir de um modelo treinado


import os
import re
import tensorflow as tf
import timeit
import os.path

def extrai_feature(image_data):

     with tf.Session() as sess:
        image_data = tf.gfile.FastGFile(img, 'rb').read()
        next_to_last_tensor = sess.graph.get_tensor_by_name('pool_3/_reshape:0')
        feature = sess.run(next_to_last_tensor, {'DecodeJpeg/contents:0': image_data})  # Extrair Feature
        # 1.16785 0.370534 0.236206
        feature = feature[0]
        # print len(feature)
        vet_aux = ''
        print (feature)


inicio = timeit.default_timer()
diretorio = 'imagem/'

# image_data = tf.gfile.FastGFile(imagem, 'rb').read()

###Define o nome do modelo
modelo= "modelo/imageNet.pb"
img = 'imagem/imagem_teste.jpg'


# Carregar o Modelo Treinado
with tf.gfile.FastGFile(modelo, 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())

    _ = tf.import_graph_def(graph_def, name='')


###Extrair Features de todos os diretorios

extrai_feature(img)

fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))

























