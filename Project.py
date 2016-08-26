import requests
import ast
import numpy as np
#from bs4 import BeautifulSoup as BS

f = open('Kickstart 10 entrants.txt', 'r+')

line = [line.lower() for line in f]                #all names in the api call must be lower case
line = [w.replace(' ', '-') for w in line]        #replaces blank spaces with - to put names into the correct format for api calls
player = [line.rstrip('\n') for line in line]    #removes new lines

f.close()

#print player[3]

L = len(player)

for x in range(0, 60):
    r = requests.get('http://smashranking.eu/api/smashers/%s/' % player[x])

    if r.status_code == 404:
        print "Responses has status 404, printing player tag:", player[x]
    else:
        print "Response was successful, printing player info:"
        metric = r.json()               #getting player info, this is a string also

        mu = metric["mu"]
        sigma = metric["sigma"]
        country = metric["country"]
        region = metric["region"]
        city = metric["city"]
        print player[x],mu,sigma,country,region,city



#    print metric[pos1+5:pos1end]               #+5 to return only math value
#    print metric[pos2+8:pos2end]              #+8 to get all sigma 
#    print metric[pos3+10:pos3end]            #+10 to return country in quotes
#    print metric[pos4+9:pos4end]            #+9 to return region in quotes
#    print metric[pos5+7:pos5end]           #+7to return city in quotes
