from pycricbuzz import Cricbuzz

c = Cricbuzz()

matches = c.matches()
a = []
for match in matches:
    print(match)