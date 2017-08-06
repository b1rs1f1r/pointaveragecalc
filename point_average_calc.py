numbers=0
points=[]

lesson=int(input("How many lessons do you have?: "))

for x in range(lesson):
	info=int(input("{}. point: ".format(x+1)))
	numbers+=info
	points+=[info]

print("Entered points: ", *points)
print("Point average: ", numbers/lesson)