import math

print('enter opposite angle:')
opp = int(input())

print('enter adjacent angle:')
adj = int(input())

hyp = round(math.sqrt(((opp * opp) + (adj * adj))),4)

print('The hypotenuse length is ' + str(hyp) + '.')



