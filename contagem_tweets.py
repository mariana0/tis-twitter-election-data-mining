import json

users=['jairbolsonaro','cirogomes','haddad_fernando','marinasilva','geraldoalckmin']
timelines=['user_timeline_07-9','user_timeline_08-9','user_timeline_09-9','user_timeline_10-9',
           'user_timeline_11-9','user_timeline_12-9','user_timeline_13-9','user_timeline_14-9',
           'user_timeline_15-9','user_timeline_16-9','user_timeline_17-9','user_timeline_18-9',
           'user_timeline_19-9','user_timeline_20-9','user_timeline_21-9','user_timeline_22-9',
           'user_timeline_23-9','user_timeline_24-9','user_timeline_25-9','user_timeline_26-9',
           'user_timeline_27-9','user_timeline_28-9','user_timeline_29-9','user_timeline_30-9',
           'user_timeline_01-10', 'user_timeline_02-10','user_timeline_03-10','user_timeline_04-10',
           'user_timeline_05-10','user_timeline_06-10','user_timeline_07-10','user_timeline_08-10',
           'user_timeline_09-10','user_timeline_10-10','user_timeline_11-10','user_timeline_12-10',
           'user_timeline_13-10','user_timeline_14-10','user_timeline_15-10','user_timeline_16-10',
           'user_timeline_17-10','user_timeline_18-10','user_timeline_19-10','user_timeline_20-10',
           'user_timeline_21-10','user_timeline_22-10','user_timeline_23-10','user_timeline_24-10',
            'user_timeline_25-10','user_timeline_26-10','user_timeline_27-10','user_timeline_28-10',
           'user_timeline_29-10']

matriz_num_fav=[]
vetor=[]
nftweet=0

print("Número por dia")
for u in users:    
    for t in timelines:
        filename="timeline/{}".format(u)
        filename+="/{}".format(t)
        filename+=(".jsonl") 
        data=json.loads(open(filename).read())
        tweets=data['tweets']  
        for i in range (len(tweets)):
            tweet=tweets[i]
            soma=tweet['retweet_count']
            nftweet+=soma
        #print (nftweet)
        vetor.append(nftweet)
        nftweet=0

    print (vetor)
    vetor=[]
            
            
        








        
        
        
        
    
    




