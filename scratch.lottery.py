import random
lottery = [random.randint(1,48)]

#print('Initial number: ',lottery[0])
#print('Lenth of list: ',len(lottery))

while len(lottery) < 6:
    newNum = random.randint(1,48)
    if lottery.count(newNum) == 0:
        lottery.append(newNum)

lottery.sort()
print('Chosen numbers: ',lottery)
#print('List length: ',len(lottery))
#print('First position: ',lottery[0])
