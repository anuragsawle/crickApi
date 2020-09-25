from pycricbuzz import Cricbuzz

c= Cricbuzz()

matches = c.matches()

for match in matches:

    print(match)