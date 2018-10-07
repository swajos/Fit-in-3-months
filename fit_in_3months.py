# dictionary of food items

fooditems = {
	"banana": 105,
	"milk": 122,
	"bread": 66,
	"rice": 205,
	"apple": 72,
	"black coffee": 2,
	"chicken breast": 142,
	"egg": 102,
	"granola bar": 193,
	"ice cream": 145,
	"oatmeal": 147,
	"orange juice": 112,
	"pizza": 298,
	"potato chips": 155,
	"red wine": 123,
	"spaghetti": 221,
	"white wine": 121

}


def startplan():
	print ("What would you like to do?")
	print("1 - Create my weight loss plan")
	print("2 - Calculate today's calorie intake")
	print("3 - Too intimidating. Exit!")
	x = input (">")
	return int(x)


def weightlossplan():
	weight = input("What is your current weight in kgs : ")
	height = input("What is your height in centimeters : ")
	age = input ("What is your age in years : ")
	gender = input("Are you male or female? (M/F) :")
	print("How frequently do you exercise?")
	print("1 - never")
	print("2 - occasionally or once a week")
	print("3 - 2-3 times a week ")
	print("4 - more than 4 times per week")
	exercise = input (">")

	#Ideal body weight based on Devine formula
	#BMR using Mifflin - St Jeor Formula

	if gender == "M" or 'm':
		idealWeight = 50 + 2.3*(int(height) - 152.4)*0.3937
		BMR = 10*int(weight) + 6.25*int(height) - 5*int(age) + 5
		BMRex = BMR* (1.2 + (int(exercise)-1)*0.7/3)
		
	elif gender == "W" or 'w':
		idealWeight = 45.5 + 2.3*(int(height) - 152.4)*0.3937
		BMR = 10*int(weight) + 6.25*int(height) - 5*int(age) - 161
		BMRex = BMR* (1.2 + (int(exercise)-1)*0.7/3)
		
	else:
		print("Please provide valid inputs!")

	print(f"Your ideal weight is {round(idealWeight)} kgs.")
	
	diff = int(weight) - idealWeight
	
	if diff > 6:
		print("******************")
		print("In 3 months, you may not reach your ideal weight. But you'll be close!")
		print(f"Recommended daily calorie intake is {round(BMRex - 500)} calories per day. Good luck!")
		print(f"If you stick to the diet you will lose about 6 kgs, and your body weight will be {int(weight)-6} kgs.") 
		print("******************")	
	elif diff < 0:
		print("******************")
		print(f"You need to gain weight. Your weight is {round(idealWeight - int(weight))} kgs less than ideal.")	
		print("******************")
	elif diff == 0:
		print("******************")
		print("Wow! Your body weight is perfect. Keep it there!")	
		print("******************")
	elif diff < 6:
		daily = ((diff/12)/0.5)*500
		print("******************")
		print(f"You need to lose {diff} ks in 3 months. You can do it!")
		print(f"Recommended daily calorie intake is {round(BMRex - daily)} calories per day. Good luck!")
		print("******************")		


def calorieintake():
	print("What did you eat today? Enter one item per line. Type enter when done")

	x = input(">")
	foodstoday = []
	caloriestoday = 0

	while x != "":
		foodstoday.append(x)
		if x in fooditems:
			caloriestoday += fooditems[x]
		else:
			print(f" {x} does not exist in our list. ")
			add = input("Would you like to add? (Y/N): ")
			if add == "Y" or 'y':
				calofx = addfoods(x)
				caloriestoday += calofx
			else: 
				fooditems[x] = 150
				caloriestoday += calofx
				continue	
		x = input(">")
		if x == "":
			break	
	print (f"Your calorie intake for today is {caloriestoday} calories.")		
		

def addfoods(x):
	calofx = input(f"Enter calories of {x}: ")
	fooditems[x] = int(calofx)
	return int(calofx)


x = startplan()	

while x != 3:
	if x == 1:
		weightlossplan()
		x = startplan()
	elif x == 2:
		calorieintake()
		x = startplan()
	else:
		print ("Provide a valid input")
		x = startplan()


	