import random

messages = ['It is certain.',
            'It is decidely so.',
            'Yes!',
            'Reply hazy.',
            'try again.',
            'Ask again later.',
            'Concentrate and ask again.',
            'My reply is no.',
            'Outlook not so good.',
            'Very doubtful.']

#print('Virtual 8 ball is ready. Ask any question...')
#input()

print(messages[random.randint(0, len(messages) - 1)])
