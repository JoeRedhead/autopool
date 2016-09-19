import requests
import sys
import numpy as np

name = raw_input("Enter tournament name: ")

r = requests.get('https://api.smash.gg/tournament/%s' % name)

if r.status_code == 404:
    print "Response has status 404, check tournament name."
    sys.exit(0)
else:
    print "Valid tournament name entered."
    metric = r.json()
    number = metric["result"]       #This is the Tournament ID
    tournamentid = metric["entities"]["tournament"]["registrationOptions"]      #This is the event ids
        
#print number 

for key in tournamentid.keys():
    if tournamentid[key]["name"] == 'Melee Singles':
        tournamentnumber = float(key)
#    else:
#        print "No Melee Singles"

print tournamentnumber

s = requests.get('https://api.smash.gg/tournament/%s/attendees?filter={"eventIds"%%3A%f}&page=%f' % (name, tournamentnumber, 1))
pagecheckcount = s.json()   #gets object to check entrant number
totalcount = pagecheckcount["total_count"]    #gets entrant number 

pagecount = int(np.ceil(float(totalcount)/float(25))) #calculates number of pages to check

for x in range(0, pagecount):
    t = requests.get('https://api.smash.gg/tournament/%s/attendees?filter={"eventIds"%%3A%f}&page=%f' % (name, tournamentnumber, x))
    name = t.json()
    playername = name["items"]["entities"]["attendee"]
    for y in range(0, 25):
        output_file = open("entrants.txt", "a")
        playeroutput = playername[y]["player"]["gamerTag"]
        output_file.write('%s \n' % playeroutput)
        output_file.close()


    

#https://api.smash.gg/tournament/smashbox/attendees?filter={"eventIds"%3A13570}&page=1
#multiple pages with 25 players per page, event id 13570 for smashbox, need to get that from the json request first
