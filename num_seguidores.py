import json

users=['jairbolsonaro','cirogomes','haddad_fernando','marinasilva','geraldoalckmin']
profiles=['user_profile_07-9','user_profile_08-9','user_profile_09-9','user_profile_10-9',
       'user_profile_11-9','user_profile_12-9','user_profile_13-9','user_profile_14-9',
       'user_profile_15-9','user_profile_16-9','user_profile_17-9','user_profile_18-9',
       'user_profile_19-9','user_profile_20-9','user_profile_21-9','user_profile_22-9',
          'user_profile_23-9','user_profile_24-9','user_profile_25-9','user_profile_26-9',
          'user_profile_27-9','user_profile_28-9','user_profile_29-9','user_profile_30-9',
          'user_profile_1-10','user_profile_2-10','user_profile_3-10','user_profile_4-10',
          'user_profile_5-10','user_profile_6-10','user_profile_7-10','user_profile_8-10',
          'user_profile_9-10','user_profile_10-10','user_profile_11-10','user_profile_12-10',
          'user_profile_13-10','user_profile_14-10','user_profile_15-10','user_profile_16-10',
          'user_profile_17-10','user_profile_18-10','user_profile_19-10','user_profile_20-10',
          'user_profile_21-10','user_profile_22-10','user_profile_23-10','user_profile_24-10',
          'user_profile_25-10','user_profile_26-10','user_profile_27-10','user_profile_28-10']

#Primeira parte: coleta nº de seguidores nos Json e coloca em uma matriz

matriz_num_seg=[]
vetor=[]

#print("Número de seguidores/dia")
for u in users:
    print (u)
    for p in profiles:
        filename="perfil/{}".format(u)
        filename+="/{}".format(p)
        filename+=(".json") 
        #print (open(filename).read())
        data=json.loads(open(filename).read())
        seguidores=data['followers_count']
        vetor.append(seguidores)
        print (seguidores)
    matriz_num_seg.append(vetor)
    vetor=[]

linhas1=len(matriz_num_seg)
colunas1=len(matriz_num_seg[0])


#Segunda parte: calcula seguidores ganhos por dia e coloca na matriz

matriz_seg_ganhos=[]
vetor=[]

print ("")
print("Número de seguidores ganhos/dia")
for i in range (linhas1):
    for j in range(colunas1-1):
        vetor.append(matriz_num_seg[i][j+1]-matriz_num_seg[i][j])
    matriz_seg_ganhos.append(vetor)
    print (vetor)
    vetor=[]







        
        
        
        
    
    




