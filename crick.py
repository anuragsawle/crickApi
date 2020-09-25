from pycricbuzz import Cricbuzz

c= Cricbuzz()

matches = c.matches()

for match in matches:

    if(match['mchstate']!='nextlive'):
        print(c.livescore(match['id']))