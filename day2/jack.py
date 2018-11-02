import random


sentence = "All work and no play makes Jack a dull boy"

letters = list("abcdefghijklmnopqrstuvwxyz ;,-.:")

p = 0.01
s = 0.001


for i in range(200):
	for j in range(len(sentence)):
		r = random.random()
		if r < p:
			print(random.choice(letters), end='')
		else:
			print(sentence[j], end='')
	p *= 1.01
	s += 0.005
	r = random.random()
	if r > s:
		print("")

