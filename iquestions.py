# # Interview Questinos: and if else and nested if else :

# # question 1:

# # user1 =int(input("enter the lenght"))
# # user2 =int(input("enter the breadth"))
# # if user1 == user2:
# # 	print("it is square")
# # else:
# # 	print("it is not square")

# # question 2:

# # a=int(input("enter the first no:"))
# # b=int(input("enter the second no:"))
# # if a>b:
# # 	print(" a greater than b")
# # elif b>a:
# # 	print(" b sgreater than a")
# # else:
# # 	print("both are equal")

# # question 3:

# # quantity=int(input("enter the quantity"))
# # if quantity>1000:
# #    print("cost is",(quantity*10/100))
# # else:
# #    print("cost is",quantity)

# # question 4:

# # salary=int(input("enter the salary"))
# # year_service=int(input("enter year of servive"))
# # if year_service>5:
# # 	print("bonus is",.05*salary)
# # else:
# #     print("no bonus")

# # question 5:
# # user=int(input("enter the marks:"))
# # if user < 25:
# #   print("F")
# # elif user >=25 and user <=45:
# #  	print("E")
# # elif user >=45 and user <=50:
# #  	print("D")
# # elif user >=50 and user <=60:
# #  	print("C")
# # elif user >=60 and user <=80:
# #  	print("B")
# # elif user >=80 and user >80:
# #  	print("A")

# # question 6:

# # user1=int(input("enter the age"))
# # user2=int(input("enter the age"))
# # user3=int(input("enter the age"))
# # if user1<user2 and user2<user3:
# # 	print("user1 is youngest")
# # elif user2<user1 and user2<user3:
# # 	print("user2 is youngest")
# # elif user1>user3 and user2>user3:
# # 	print("user3 is youngest")
# # if user1<user2 and user2<user3:
# # 	print("user3 is oldest")
# # elif user2<user1 and user3<user1:
# # 	print("user1 is oldest")
# # elif user3>user1 and user2>user3:
# # 	print("user2 is oldest")

# # question 6:

# # user1=int(input("enter the first age"))
# # user2=int(input("enter the second age"))
# # user3=int(input("enter the third age")) 
# # if user1>=user2 and user1 >=user3:
# # 	print("oldest is user1")
# # elif user2>=user1 and user2>=user3:
# # 	print("oldest is user2")
# # elif user3>=user1 and user3>=user2:
# # 	print("oldest is user3")
# # else:
# # 	print("all is similar")

# # question 7:
# # user=int(input("enter the no"))
# # if user < 0:
# # 	print(user*(-1))
# # else:
# # 	print(user)

# # question 8:

# # classes=int(input("no of class held"))
# # classes_attend=int(input("no of class attended"))
# # attendance=(classes_attend/classes)*100
# # if attendance>75:
# #    print("you are allowed to sit in exam")
# # else:
# #    print("you are not allowed to sit in exam")

# # question 8,9:
# # classes=int(input("no of class held"))
# # classes_attend=int(input("no of class attended"))
# # attendance=(classes_attend/classes)*100
# # medical_cause=(input("enter y for yes and n for no")) 
# # if attendance>75 and  medical_cause=="y":
# #    print("you are allowed to sit in exam")
# # else:
# #    print("you are not allowed to sit in exam")

# # question 9
# # classes_attend=int(input("no of class attended:"))
# # medical_cause=(input("enter y for yes / n for no:"))
# # if classes_attend>75 and  medical_cause=="y":
# #    print("you are allowed")
# # else:
# # 	print("not allowed")


# # medical_cause=(input("enter y for yes / n for no:"))
# # if medical_cause=="y":
# #    print("you are allowed")
# # else:
# # 	print("not allowed")


# # question 7:

# # num=int(input("ENTER ANY NO:"))
# # if num%2!=0:
# #     print("weird")
# # else:
# # 	if num <=5:
# # 		print("not weird")
# # 	elif num>6:
# # 		if num <=20:
# # 			print("weird")
# # 	elif num >20:
# # 		print("not weird")

# # question 8
 
# # alien = input("Enter any alien colour:")
# # if alien == "green":
# # 	print("YOU WIN 5 POINTS")
# # else:
# # 	print("YOU WIN 10 POINTS")


# # alien_colour=input("enter a colour")
# # if alien_colour=="green":
# # 	print("earn 5 points")
# # else:
# # 	print("earn 10 points")


# # question 9:

# # varx = int(input("enter 1st no"))
# # vary = int(input("enter 2nd no"))
# # if varx%vary==0:
# # 	print("it is divisible")
# # else:
# # 	print("it is not divisible")

# # question 10:

# person_age = int(input("enter the age:"))
# if person_age < 2:
# 	prnt("person is a baby")
# elif person_age < 4:
# 	if person_age >2:
# elif person_age >= 65:		
# 	print("person is an elder: ")

# question 11:   

# day = input("which is day today? (monday/tuesday) > ")
# time = input("meal time? (breakfast/lunch/dinner) > ")
# if day == "monday":
#  if time == "breakfast":
# 		print("person is a toddler")
# elif person_age < 13:
# 	if person_age > 4:
# 	 	print("person is a kid")
# elif person_age < 20:
# 	if person_age > 13:
# 		print("person is a teenager")
# elif person_age < 65:
# 	if person_age > 20:
# 		print("person is a adult")
# elif person_age >= 65:		
# 	print("person is an elder: ")

# question 11:   

# day = input("which is day today? (monday/tuesday) > ")
# time = input("meal time? (breakfast/lunch/dinner) > ")
# if day == "monday":
#  if time == "breakfast":
#  	print("poori sabji")
# if day == "monday":
#  if time == "lunch":
#  	print("sambhar rice")
# if day == "monday":
#  if time == "dinner":
#  	print("chiken rice")
# else: 	
# 	if day == "tuesday":
# 	 if time == "breakfast":
# 	 	print("poha")
# 	if day == "tuesday":
# 	 if time == "lunch":
# 	 	print("rajma rice")
# 	if day == "tuesday":
# 		print("<class 'str'>")
# 	elif isin
# 	 if time == "dinner":
# 	 	print("roti sabji")
		 	 	
# n1=max(input("enter any no"))
# n2=max(input("enter any no"))
# n3=max(input("enter erson is a adult")
	  
# n1=max(input("enter any no"))
# n2=max(input("enter any no"))
# n3=max(input("enter any no"))
# print("n3 is max no")

# question 12:

# NESTED IF ELSE QUESTIONS :
# QUESTION 1:

# num = -99
# if num > 0:
#     print("Positive Number")
# else:
#     print("Negative Number")
#     #nested if
#     if -99<=num:
#         print("Two digit Negative Number")

#   QUESTION 2:

# x = int(input("Enter your age: "))

# if x > 21:
#     if x > 100:
#         print("You are too old, go away!")
#     else:
#         print("Welcome, you are of the right age!")
# else:
#     print("You are too young, go away!") 

# QUESTION 3:

# year = int(input("Please Enter the Year Number:"))
# if (year%100 == 0):
#     if (year%400 == 0):
#         print("%d is a Leap Year" %year)
#     else:
#         print("%d is Not the Leap Year" %year)
# elif (year%4 == 0):
#     print("%d is a Leap Year" %year)
# else:
#     print("%d is Not the Leap Year" %year)


#     # 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, and 2048.

# QUESTION  loop 4:

# i = 1
# while i<=100:
#     if i%2==0:
#         print(-i)
#     else:
#         print(+i)
#     i=i+1        

# QUESTION loop 5:

# count = 156
# while count <=165:
#     print(count)
#     count=count+1 

# QUESTION  loop 6:

# user= int(input("ENTER ANY NO:"))
# num=0
# sum=0
# while num<user:
#     user1=int(input("ENTER ANY NO:"))
#     sum=sum+user
#     num=num+1
# print(sum)

# question 13:

# year = int(input("enter the year:"))
# if year/100==0:
# 	print("it is a century")
# elif year%100+1:
# 	print("return century")	
# else:
# 	print("it is not a century")

	


# question 14:

# user = int(input("enter any num: "))
# if user<0:
# 	print(user*(-1))
# else:
# 	print(user)	


# question 15:	

# count=1
# while count<=100:
# 	if count%3==0 and count%7==0:
# 		print("chocolate")
# 	elif count%3==0:
# 		print("choco")
# 	elif count%7==0:
# 		print("late")		
# 	else:		
# 		print(count)
# 	count=count+1


# count=1
# while count<=100:
# 	if count%3==0: 
# 		if count%7==0:
# 			print("chocolate")
# 	elif count%3==0:
# 		print("choco")
# 	elif count%7==0:
# 		print("late")		
# 	else:		
# 		print(count)
# count=count+1

			
# # question 19

# word = input("Input a word to reverse: ")

# for char in range(len(word) - 1, -1, -1):
#   print(word[char], end="")
# print("\n")

# word=input("enter reverse name: ")
# for char in range(len(word) -1,-1,-1):
# 	print(word[char],end="")
# print("\n")count=1
# while count<=100:
# 	if count%3==0: 
# 		if count%7==0:
# 			print("chocolate")
# 	elif count%3==0:
# 		print("choco")
# 	elif count%7==0:
# 		print("late")		
# 	else:		
# 		print(count)
# count=count+1

# question 18:

# amount = 2400
# transaction_type = "L"
# if transaction_type == "L":
#     if amount <= 25000:
#         discount = amount*.0
#         print ("Net Amount:", discount)
#     if amount <=57000:
#         discount = amount*.5
#         print ("Net Amount:", discount)
# else:
#     if amount <=100000:
#         discount = amount*.075
#         print ("Net Amount:", discount)
#     if amount >= 100000:
#         discount = amount*.10
#         print ("Net Amount:", discount)


# i = 1
# while i<=100:
#     if i%2==0:
#         print(-i)
#     else:
#         print(+i)
#     i=i+1        


# year=int(input("enter any year: "))
# if year%400==0:
# 	print("the year is centuary")
# elif year%4==0:
# 	print("the year is leap")
# else:
# 	print("no leap year")


# Python program to illustrate 
# functions 
# def hello(): 
# 	print("hello") 
# 	print("hello again") 
# 	print("hello sandhya")
# hello() 
  



# name = input("Enter your name: ")  
# print("hello", name) 

# Python program to illustrate 
# function with main 
# def getfloat(): 
# 	result = float(input("Enter float: ")) 
# 	return result 
# def Main(): 
# 	print("Started") 
# 	output = getfloat()	 
# 	print(output) 
# if __name__=="__main__": 
# 	Main() 


# def main():
# 	a=int(input("enter any number:"))
# 	if a%2==0:
# 		print("it is divisible by 2")
# 	else:
# 		print("it is not divisible by 2")
# if __name__ == '__main__':
	

# def checking(data):
# 	if isinstance(data,str):
# 		print("<class 'str'>")
# 	elif isinstance(data,int):
# 		print("<class 'int'>")
# 	elif isinstance(data,float):
# 		print("<class 'float'>")
# 	elif isinstance(data,complex):
# 		print("<class 'complex'>")
# checking(5j)


# a=int(input("enter first num:"))
# b=int(input("enter second num:"))
# if a>b:
# 	print("num 1st is maximum num")
# elif b>a:
# 	print("num 2nd is maximum num")
# else:
# 	print("both num are equal")

# user1=int(input("enter 1st num"))
# user2=int(input("enter 2nd num"))
# user3=int(input("enter 3rd num"))
# if user1>user2 and user2>user3:
# 	print("1st num is maximum")
# elif user2>user1 and user1>user3:
#     print("2nd num is maximum")
# elif user3>user1 and user3>user2:
# 	print("3rd num is maximum")
# else:
# 	print("all num is equal")

# num=int(input("enter any no:"))
# if num<0:
# 	print("negative number")
# elif num>0: 	
#     print("Positive number")
# elif num==0:
# 	print("Number is zero")    	


# num=int(input("enter any no:"))
# if num<0:
# 	print("negative")
# elif num>0:
# 	print("Positive")
# else:
# 	print("zero")	

# num=int(input("enter any num:"))
# if num%5==0:
#     print("it is divisible")
# elif num%11==0:   
#     print("it is divisible")
# else:
# 	print("it is not divisible") 

# num=int(input("ENTER ANY NO:"))
# if num%2==0:
#     print("even")
# else:
# 	print("odd")

# year=int(input("enter the yaer:"))
# if year%4==0 and year%100!=0:
#  	print("it is a leap year")
# elif year%100==0:
#  	print("it is not leap year")
# elif year%400==0:
#  	print("it is a leap year")
# else:
#  	print("is not leap year")


# week=int(input("enter the week num"))
# day=input("enter the day")

# if week == 

# count=12
# sum=0
# while count <= 421:
# 	print(count)
# 	sum = sum + count
# 	count = count + 1
# print("The total is ",sum)

# age=int(input("enter any age: "))
# if age<2:
# 	print("person is baby")
# elif age<4:
# 	print("person is toddler")
# elif age<13:
# 	print("person is kid")
# elif age<20:
# 	print("person is teenager")
# elif age<65:
# 	print("person is adult")
# elif age<70:
# 	print("person is older")

# marks=int(input("enter any marks:"))
# if marks<100:
# 	if marks>90:
# 		print("grade a")
# if marks<89:
# 	if marks>80:
# 		print("grade b")
# if marks<79:
# 	if marks>70:
# 		print("grade c")
# if marks<69:
# 	if marks>60:
# 		print("grade d")
# 	else:
# 		print("grade e")

# Character = input("Please Enter Character :")
# if Character >= 'a' and Character <= 'z' or Character >= 'A' and Character <= 'Z': 
#     print("The Given Character ", Character, "is an Alphabet") 
# else:
#     print("The Given Character ", Character, "is Not an Alphabet ")

# Character = input("The Enter Character :")
# if Character >= 'A' and Character <= 'Z':
#     print("it is capital Alphabet") 
# elif Character >= 'a' and Character <= 'z':
#     print("it is small Alphabet") 
# else:
#     print("it is Not a Alphabet ")


# Character = input("Enter The Character :")
# if Character >= 'a' and Character <= 'z':
#     print("it is small Alphabet")
# elif Character >= 'A' and Character <= 'Z': 
# 	print("it is a capital Alphabet")     
# elif Character >= '0' and Character <= '9':
#     print("it is a Digit")    
# else:
#     print("It is special Character")


# Character = input("Enter the character: ")
# if Character=='A'or Character=='a':
#     print("It is a Vowel")
# elif Character=='E' or Character=='e':
# 	print("It is a Vowel") 
# elif Character=='I'or Character=='i':
# 	print("It  is  a Vowel")
# elif Character=='O' or Character=='o':
# 	print("It is a Vowel")
# elif Character=='U' or Character=='u':
# 	print("It is a Vowel")  
# else:
#     print("Character is a Consonant")

 
# Character = input(" Enter The Character:")
# if Character >='A'and Character <='Z':
#     print("It is Uppercase Alphabet") 
# elif Character >= 'a' and Character <= 'z':
#     print("It is Lowercase Alphabet")
# else:
#     print("It is Not Lowercase or Uppercase")

 
# weekday = int(input("Enter The weekday and number Number of day:"))

# if weekday == 1 :
#     print("Monday");

# elif weekday == 2 :
#     print("Tuesday")

# elif(weekday == 3) :
#     print("Wednesday")

# elif(weekday == 4) :
#     print("Thursday")

# elif(weekday == 5) :
#     print("Friday")

# elif(weekday == 6) :
#     print("Saturday")

# elif (weekday == 7) :
#     print("Sunday")

# else :
#     print("Please enter weekday number between 1-7.")


# month_name = input("Input the name of Month: ")
# if month_name == "February":
# 	print("No. of days: 28/29 days")
# elif month_name in ("April", "June", "September", "November"):
# 	print("No. of days: 30 days")
# elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
# 	print("No. of days: 31 day")
# else:
# 	print("Wrong month name")


# amount=int(input("enter the amount:"))
# if amount%500==0:
# 	notes=amount//500
# 	print("No of notes:",notes)
# else:
# 	print("only 500 notes is available")

# angle1=int(input("enter  the 1st angle:"))
# angle2=int(input("enter the 2nd angle:"))
# angle3=int(input("enter the 3rd angle:"))
# if angle1+angle2+angle3==180:
# 	print("it is a valid triangle")
# else:
# 	print("it is not valid triangle")

# angle1=int(input("enter  the 1st angle side:"))
# angle2=int(input("enter the 2nd angle  side:"))
# angle3=int(input("enter the 3rd angle side:"))
# if angle1 + angle2 > angle3 and angle1 + angle3 > angle2 and angle2 + angle3 > angle1:
# 	print("it is a valid triangle")
# else:
# 	print("it is not valid triangle")

# angle1=int(input("enter  the 1st angle side:"))
# angle2=int(input("enter the 2nd angle  side:"))
# angle3=int(input("enter the 3rd angle side:"))
# if angle1==angle2==angle3:
# 	print("it is a equilateral triangle")
# else:
# 	print("it is not equilateral triangle")






























































	

	    	












  
