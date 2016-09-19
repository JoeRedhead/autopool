import requests
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#from bs4 import BeautifulSoup as BS

f = open('Kickstart 10 entrants.txt', 'r+')

line = [line.lower() for line in f]                #all names in the api call must be lower case
line = [w.replace(' ', '-') for w in line]        #replaces blank spaces with - to put names into the correct format for api calls
player = [line.strip() for line in line]         #removes new lines

f.close()

L = len(player)

columns = ['Skill', 'Country', 'Region', 'City', 'Pool']
df = pd.DataFrame(index=player, columns=columns)

for x in range(0, L):
    r = requests.get('http://smashranking.eu/api/smashers/%s/' % player[x])

    if r.status_code == 404:
#        print "Responses has status 404, printing player tag:", player[x]
#        output_file = open("404 output.txt", "a")
#        output_file.write('%s \n' % player[x])
#        output_file.close()
#        trueskill_file = open("trueskill.txt", "a")
#        trueskill_file.write('%s is a new player/retagged player \n' % player[x])
#        trueskill_file.close()
        df.loc[player[x]] = pd.Series({'Skill' :0, 'Country' :0, 'Region' :0, 'City' :0})
        
    else:
#        print "Response was successful, printing player info:"
        metric = r.json()
        
        listplayer = player[x]
        mu = metric["mu"]
        sigma = metric["sigma"]
        country = metric["country"]
        region = metric["region"]
        city = metric["city"]
        skill = mu - (1.5 * sigma)

        
        df.loc[player[x]] = pd.Series({'Skill' :skill, 'Country' :country, 'Region' :region, 'City' :city})
        
#        trueskill_file = open("trueskill.txt", "a")
#        trueskill_file.write('%s            ' % player[x])
#        trueskill_file.write('%f            ' % mu)
#        trueskill_file.write('%f            ' % sigma)
#        trueskill_file.write('%s            ' % country)
#        trueskill_file.write('%s            ' % region)
#        trueskill_file.write('%s            \n' % city)     
#        trueskill_file.close()
#        print player[x],mu,sigma,country,region,city

order = df.sort_values(['Skill'], ascending = [False])
#print order

pool = int(input("Enter number of pools: "))
what = float(L) / float(pool)
N = np.ceil(what)

#print L
#print N

#print order.iloc[1].name


lists = [[] for _ in range(pool)]

def poolassign(PlayerTotal, PoolSize, Dataframe):               #def poolassign(int, int, dataframe)
    z = 0
    for y in range (0,PlayerTotal):
        if (np.floor(float(y)/float(PoolSize))%2 == 0): 
            lists[z].append(Dataframe.iloc[y].name)
#            Dataframe.iloc[y].Pool
            z = z + 1 
        else:
            z = z - 1
            lists[z].append(Dataframe.iloc[y].name)
    return
    
poolassign(L, pool, order)

#lists[1].append('Professor Pro')
#lists[1].append('Steve') 
print lists

#Pools = np.zeros(pool, N)
#Pools[1][1] = 'Professor Pro'
#print Pools
