import random

KREWES = {
    'orpheus': ['Emily','Kevin','Vishwaa','Eric','Jay'],
    'rex': ['William','Joseph','Calvin','Ethan','Moody'],
    'endymion': ['Grace','Nahi','Derek','Jun Tao','Connor']
}

def rando(tn):
    print(random.choice(KREWES[tn]))

tn = input("Enter team name: ") 
if tn in KREWES:
  rando(tn)
else: 
    print("Team not there") 
