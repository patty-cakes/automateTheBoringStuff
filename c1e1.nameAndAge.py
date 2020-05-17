# this program says hello and ask for your name
print ('What is your name?')
myName = input() #input always records a string
print ('It is good to meet you ' + myName + '.')
print ('Your name contains ' + str(len(myName)) + ' characters.') #takes ibnt length of name and converts to string for print
myNameLen = str(len(myName)) #stores charcater length of name as a string
print()
print ('What is your age?')
myAge = input() #stores age as a string
print ('In 1 year, you will be ' + str(int(myAge) + 1) + '.') # converts age to int (for addition), then back to string (for print)
# print (myNameLen + ' ' + myName)

