#using enumerate

for key , value in enumerate(['apple','banna','mango','orange']):
    print(key,value)

#using zip
question = ['name','fathername','surname']
answer = ['pradip','appasaheb','kolage']

for question , answer in zip(question ,answer):
    print(f'what is your {question} ? --> {answer}')
