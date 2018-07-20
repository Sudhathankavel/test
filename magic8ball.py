import random
"""def getAnswer(answerNumber):
	if answerNumber==1:
		return 'It is certain'
	elif answerNumber==2:
		return 'It is decidedly so'
	elif answerNumber==3:
		return 'Yes'
	elif answerNumber==4:
		return 'Reply hazy try again'
	elif answerNumber==5:
		return 'Ask again later'
	elif answerNumber==6:
		return 'concentrate and ask again'
		

#r=random.randint(1,6)
#print(r)
#fortune=getAnswer(r)
#print(fortune)

print(getAnswer(random.randint(1,6)))"""

messages=['It is certain','It is decidedly so','Reply hazy try again','Ask again later','concentrate and ask again']

print(messages[random.randint(0,len(messages)-1)])
		
