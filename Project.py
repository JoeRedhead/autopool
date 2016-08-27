import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from bs4 import BeautifulSoup as BS

f = open('Kickstart 10 entrants.txt', 'r+')

line = [line.lower() for line in f]                #all names in the api call must be lower case
line = [w.replace(' ', '-') for w in line]        #replaces blank spaces with - to put names into the correct format for api calls
player = [line.strip() for line in line]         #removes new lines

f.close()

L = len(player)

for x in range(0, L):
    r = requests.get('http://smashranking.eu/api/smashers/%s/' % player[x])

    if r.status_code == 404:
        print "Responses has status 404, printing player tag:", player[x]
        output_file = open("404 output.txt", "a")
        output_file.write('%s \n' % player[x])
        output_file.close()
        trueskill_file = open("trueskill.txt", "a")
        trueskill_file.write('%s is a new player/retagged player \n' % player[x])
        trueskill_file.close()
    else:
#        print "Response was successful, printing player info:"
        metric = r.json()

        mu = metric["mu"]
        sigma = metric["sigma"]
        country = metric["country"]
        region = metric["region"]
        city = metric["city"]
        
        trueskill_file = open("trueskill.txt", "a")
        trueskill_file.write('%s            ' % player[x])
        trueskill_file.write('%f            ' % mu)
        trueskill_file.write('%f            ' % sigma)
        trueskill_file.write('%s            ' % country)
        trueskill_file.write('%s            ' % region)
        trueskill_file.write('%s            \n' % city)     
        trueskill_file.close()
#        print player[x],mu,sigma,country,region,city
