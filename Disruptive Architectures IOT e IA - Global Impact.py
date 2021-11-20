#!/usr/bin/env python
# coding: utf-8

# In[45]:



#LEITURA DO DATASET
tomates = []
with open ("C:/Users/caiqu/Desktop/dataset_tomate.data", "r") as dataset:
    for linha in dataset.readlines ():
        
        x = linha.replace('\n', '').replace ('O', '0').split(',')
        
         #Aqui será necesssario converter os 22 objetos de String para float através do metodo "float (x[y])" quando tento
        #transformar o seguinte erro é apresentado: ValueError: could not convert string to float
        lista = [
            float (x[1]), float (x[2]), float(x[3])
          
        ]
            
        amostras.append(lista)
        
        #print ('\n')
        #print (amostras)
        
        #iMPRIMINDO DADOS DO DATASET INTEIRO
       
    def info_dataset (tomates, info=True): 
            output1, output2 = 0,0
            
            for tomate in tomates: 
                if tomate [-1] == 1: 
                    output1 +=1 #Tomate resiste ao fungo phytophthora
                    
                else: 
                    output2: += 1 #Tomate não resiste ao fungo phytophthora
                            
                    if info == True 
                            print ('Total de tomates na plantação', len (tomates))
                            print ('Total de tomates resistentes ao fungo phytophthora', output1)
                            print ('Total de tomates não resistentes ao fungo phytophthora', output2)
                            
                            return [len (tomates), output1, output2]
                        
                        #SEPARANDO O DATASET EM TREINAMENTO E TESTES
                        
                    porcentagem = 0.7 #Porcentagem para TREINAMENTO
                        
                    _, output1, output2 = info_dataset(tomates, info=False) 
                        
                    treinamento = []
                    teste = []
                        
                    max_output1 = int ( porcentagem * output1 )
                    max_output2 = int ( porcentagem * output2 )
                        
                    total_outpu1 = 0
                    total_outpu2 = 0
                        
            for tomate in tomates: 
                if (total_output1 + total_output2) < (max_output1 + max_output2):
                                #Ainda é possível a inserção de números no treinamento da KNN
                                
                                treinamento.append (tomate)
                                
                if tomate [-1] == 1 and total_output1 < max_output1:
                                    total_output1 += 1
                                    
                else: 
                    total output2 += 1
                                        
                #Limite de amostras (treinamentos) excedido, consequentemente as amostras que sobrar será adicionada nos testes
                else: 
                    teste.appened (tomate)

                def knn(treinamento, nova_amostra, k):

                    distancias ={}
                    tamanho_treino = len(treinamento)

                    for i in range(tamanho_treino):
                        d = distancia_euclidiana(treinamento[i], nova_amostra)
                        distancias[i] = d
                    k_vizinhos = sorted(distancias, key=distancias.get) [:k]
                    qtd_output1 = 0
                    qtd_output2 = 0
                    for indice in k_vizinhos:
                        if treinamento[indice] [-1] == 1:
                            qtd_output1 += 1
                        else: 
                            qtd_output2 += 1

                    if qtd_output1 > qtd_output2:
                        return 1
                    else:
                        return 0

        
        


# In[ ]:





# In[ ]:




