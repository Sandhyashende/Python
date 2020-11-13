
# debugging questions:
# question 1:

# number1 = 234
# 	print numer1

# ansswer 1:

# number1 = 234
# print(number1)

# question 2:

# number1 = 234
# number2 = "1"
# print number1 + number2

# ansswer 2:

# number1 = 234
# number2 = "1"
# number2 = int(number2)
# print (number1 + number2)

# question 3:

# year = 2016
# name = "NavGurukul"
# print name + ', ' +   + "mein start hua tha!"

# ansswer 3:

# year = 2016
# name = "NavGurukul"
# year = str(year)
# print (name + ', ' +  year + " " + "mein start hua tha!")

# question 4:

# price_milk = raw_input("1L milk ka price daalo?")
# print "10L milk " + price_milk*10 + " rupees ka aata hai."

# ansswer 4:

# price_milk = int(input("1L milk ka price daalo?"))
# print ("10L milk " , price_milk*10 , " rupees ka aata hai")

# question 5:

# number = raw_input("please enter a decimal number")
# print "your number divided by 2 is equal to = " + number/2

# ansswer 5:

# number = float(input("please enter a decimal number"))
# print ("your number divided by 2 is equal to = " , number/2)

# question 6

# Tumhare paas 5 mangoes hai
# mangoes = 5
#  Kisi ne humhe 5 aur mangoes de diye
# manGoes = mangoes + 5
# Ab tumne unn mangoes ko 5 logo mei baant diya
# print mangoes / 5
# Par isse toh 1 mango hi mila. Par milne 2 chahiye the. Code ko sahi karo jisse ki sabko sahi mangoes mile.

# ansswer 6:

# mangoes = 5
# manGoes = mangoes + 5
# print(manGoes/5) 

# output:  2.0

# question 7:

# Aapke paas ek variable mein `raw_input` se gaadi ki speed ka ek integer hai
# speed = int( raw_input("Gaadi ki speed daalo > ") )

# Ab aapne speed check kar ke kuch print karna hai:
# Agar 60 se kam hai toh print karna: "Speed kam hai"
# Agar 30 se kam hai toh print karna: "Speed bahot kam hai"
# Agar 100 se zyada hai toh print karo: "Bahot zyada hai"
# if speed < 60:
#     print "Speed kam hai"
# elif speed < 30:
#     print "Speed bahot kam hai"
# elif speed > 100:
#     print "Speed bahot fast hai"

# Isme ek baar speed 20 daal ke dekho aur dekho ki "Speed bahot kam" hai ki
# output aati hai ya nahi. Agar nahi aati toh isko theek karo aur yeh socho
# ki kya problemn hai.


# ansswer 7:

# speed = int(input("Gaadi ki speed daalo > "))
# if speed < 30:
#     print ("Speed bohot kam hai")
# elif speed < 60:
#     print ("Speed kam hai")
# elif speed >100:
#     print ("Speed bahot fast hai")

   

# question 8:

# `raw_input` ka use kar ke user se din aur abhi ka samay (lunch, dinner) input
# leke uss samay ka menu print karvana hai. Abhi hum sirf monday aur tuesday ke
# liye likh rahe hain
# Monday aur Tuesday dono time daal roti banegi, bas Tuesday raat ko Pav Bhaji banegi
# Neeche waale program mein jab tuesday daalte ho toh pav bhaji print nahi hota.
# Isko sahi karo.
# day = raw_input("Aaj ka din kya hai? (monday/tuesday) > ")
# time =raw_ input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
# if day == "monday" or day == "tuesday":
#     print "Daal-Roti banegi aaj"
# elif day == "tuesday" and time == "dinner":
#     print "Pav-Bhaji banegi aaj toh :)"w


# answer 8: 

# day = input("Aaj ka din kya hai? (monday/tuesday) > ")
# time = input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
# if day == "monday" or day == "tuesday":
#    print ("Daal-Roti banegi aaj")
# if day == "tuesday" and time == "dinner":
#     print ("Pav-Bhaji banegi aaj toh:")

# just practice:    	
    	
# varx = 300-123
# a = int(input("Enter the no:"))
# if varx == a:
# 	print("barabar hai")
# else:
# 	print("barabar nhi hai")

    	


 

















