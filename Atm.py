# Entry=input("Enter your Atm card: yes/no? ")
# Language=input("Enter your language? 1.English/2.Hindi: ")
# Pin_id=input("Enter Your Pin: ")
# Type_of_account=input("Current/Saving: ")
# Amount=int(input("Enter your amount: "))
# Account_formate=input("1.Balance Enquary/2.change the password/3.cash withdrawl/4.Money transfer? ")
# if Entry=="Yes":
#     print("Welcome to SBI bank")
#     if Language==1:
#         if Pin_id=="7778":
#             print("change password")
#             if Account_formate==2:
                
        


# if selection=="view balance":
#     amount1=int(input("enter amount: "))
#     print("Your current balance:",amount1)
# elif selection=="Withdrawl":
#     amount2=float(input("enter withrawl amount: "))
#     total_amount=_amount-amount2
#     print("your ")
#     print("you amount:",total_amount)
#     if amount2>_amount:
#         print("you amount is greater than curren amount")
# elif selection=="Deposite":
#     _amount=float(input("enter deposite amount:"))
#     _Doposite=input("Is this correct amount:yes/no?"+str(amount)+" n ")
#     if _Doposite=="yes":
#         print("you amount deposite in:",_amount+amount1)
# elif selection=="change password":

#     print("Transaction number: ", random.randint(10000, 1000000))




import random module: 
import random 
print("Winning Rules of the stone paper scissor game as follows: \n"
								+"stone vs paper->paper wins \n"
								+ "stonevs scissor->stone wins \n"
								+"paper vs scissor->scissor wins \n") 

while True: 
	print("Enter choice \n 1. stone \n 2. paper \n 3. scissor \n") 
	choice = int(input("User turn: ")) 
	while choice > 3 or choice < 1: 
		choice = int(input("enter valid input: ")) 
	if choice == 1: 
		choice_name = 'stone'
	elif choice == 2: 
		choice_name = 'paper'
	else: 
		choice_name = 'scissor'
	print("user choice is: " + choice_name) 
	print("\nNow its computer turn.......") 
	comp_choice = random.randint(1, 3) 
	while comp_choice == choice: 
		comp_choice = random.randint(1, 3)  
	if comp_choice == 1: 
		comp_choice_name = 'stone'
	elif comp_choice == 2: 
		comp_choice_name = 'paper'
	else: 
		comp_choice_name = 'scissor'
	print("Computer choice is: " + comp_choice_name) 
	print(choice_name + " V/s " + comp_choice_name) 
	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )): 
		print("paper wins => ", end = "") 
		result = "paper"
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)): 
		print("stone wins =>", end = "") 
		result = "stone"
	else:  
		print("scissor wins =>", end = "") 
		result = "scissor" 
	if result == choice_name: 
		print("<== User wins ==>") 
	else: 
		print("<== Computer wins ==>") 
	print("Do you want to play again? (Y/N)") 
	ans = input()  
	if ans == 'n' or ans == 'N': 
		break
print("\nThanks for playing") 
input("Enter your Account Number")
print ("Current Account Balance: 25000")

# CHOICE = int(input ("Press 1 to make a Deposit or 2 to make a Withdrawal."))

# if CHOICE == 1:
#     DEPOSIT = int(input("Press 1 to deposit to checking, 2 for savings"))
#     if DEPOSIT == 1:
#     	print("Please insert check or money now")
#     elif DEPOSIT == 2:
#     	print("Please insert check or money now")
 
# elif CHOICE == 2:
#     WITHDRAWAL = int(input("press 1 to draw funds from checking, press 2 for savings."))
#     if WITHDRAWAL == 1:
#     	amount=int(input("How much would you like to withdraw today?"))
#     	print("Please remove your cash from the slot below")
#     elif WITHDRAWAL == 2:
#     	amount=int(input("How much would you like to withdraw today?"))
#     	print("Please remove your cash from the slot below")

# end_of_program = input("Thank you for your business, press enter to conclude this transaction.")


# Input = ['Geeeks, Forgeeks', '65.7492, 62.5405', 
#          'Geeks, 123', '555.7492, 152.5406'] 
           
# temp = [] 
  
# # Getting elem in list of list format 
# for elem in Input: 
#     temp2 = elem.split(', ') 
#     temp.append((temp2)) 
  
# List initialization 
# Output = []  
  
# Using Iteration to convert  
# element into list of list 
# for elem in temp: 
#     temp3 = []# Entry=input("Enter your Atm card: yes/no? ")
# Language=input("Enter your language? 1.English/2.Hindi: ")
# Pin_id=input("Enter Your Pin: ")
# Type_of_account=input("Current/Saving: ")
# Amount=int(input("Enter your amount: "))
# Account_formate=input("1.Balance Enquary/2.change the password/3.cash withdrawl/4.Money transfer? ")
# if Entry=="Yes":
#     print("Welcome to SBI bank")
#     if Language==1:
#         if Pin_id=="7778":
#             print("change password")
#             if Account_formate==2:
                
        


# if selection=="view balance":
#     amount1=int(input("enter amount: "))
#     print("Your current balance:",amount1)
# elif selection=="Withdrawl":
#     amount2=float(input("enter withrawl amount: "))
#     total_amount=_amount-amount2
#     print("your ")
#     print("you amount:",total_amount)
#     if amount2>_amount:
#         print("you amount is greater than curren amount")
# elif selection=="Deposite":
#     _amount=float(input("enter deposite amount:"))
#     _Doposite=input("Is this correct amount:yes/no?"+str(amount)+" n ")
#     if _Doposite=="yes":
#         print("you amount deposite in:",_amount+amount1)
# elif selection=="change password":

#     print("Transaction number: ", random.randint(10000, 1000000))




# # import random module 
# import random 
# print("Winning Rules of the stone paper scissor game as follows: \n"
# 								+"stone vs paper->paper wins \n"
# 								+ "stonevs scissor->stone wins \n"
# 								+"paper vs scissor->scissor wins \n") 

# while True: 
# 	print("Enter choice \n 1. stone \n 2. paper \n 3. scissor \n") 
# 	choice = int(input("User turn: ")) 
# 	while choice > 3 or choice < 1: 
# 		choice = int(input("enter valid input: ")) 
# 	if choice == 1: 
# 		choice_name = 'stone'
# 	elif choice == 2: 
# 		choice_name = 'paper'
# 	else: 
# 		choice_name = 'scissor'
# 	print("user choice is: " + choice_name) 
# 	print("\nNow its computer turn.......") 
# 	comp_choice = random.randint(1, 3) 
# 	while comp_choice == choice: 
# 		comp_choice = random.randint(1, 3)  
# 	if comp_choice == 1: 
# 		comp_choice_name = 'stone'
# 	elif comp_choice == 2: 
# 		comp_choice_name = 'paper'
# 	else: 
# 		comp_choice_name = 'scissor'
# 	print("Computer choice is: " + comp_choice_name) 
# 	print(choice_name + " V/s " + comp_choice_name) 
# 	if((choice == 1 and comp_choice == 2) or
# 	(choice == 2 and comp_choice ==1 )): 
# 		print("paper wins => ", end = "") 
# 		result = "paper"
# 	elif((choice == 1 and comp_choice == 3) or
# 		(choice == 3 and comp_choice == 1)): 
# 		print("stone wins =>", end = "") 
# 		result = "stone"
# 	else:  
# 		print("scissor wins =>", end = "") 
# 		result = "scissor" 
# 	if result == choice_name: 
# 		print("<== User wins ==>") 
# 	else: 
# 		print("<== Computer wins ==>") 
# 	print("Do you want to play again? (Y/N)") 
# 	ans = input()  
# 	if ans == 'n' or ans == 'N': 
# 		break
# print("\nThanks for playing") 
# input("Enter your Account Number")
# print ("Current Account Balance: 25000")

# CHOICE = int(input ("Press 1 to make a Deposit or 2 to make a Withdrawal."))

# if CHOICE == 1:
#     DEPOSIT = int(input("Press 1 to deposit to checking, 2 for savings"))
#     if DEPOSIT == 1:
#     	print("Please insert check or money now")
#     elif DEPOSIT == 2:
#     	print("Please insert check or money now")
 
# elif CHOICE == 2:
#     WITHDRAWAL = int(input("press 1 to draw funds from checking, press 2 for savings."))
#     if WITHDRAWAL == 1:
#     	amount=int(input("How much would you like to withdraw today?"))
#     	print("Please remove your cash from the slot below")
#     elif WITHDRAWAL == 2:
#     	amount=int(input("How much would you like to withdraw today?"))
#     	print("Please remove your cash from the slot below")

# end_of_program = input("Thank you for your business, press enter to conclude this transaction.")


# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
#         27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
#         51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,
#         75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
# i=0
# new_list=[]
# while i<len(list):
#   new_list.append(list[i:i+10])
#   i+=10 
# print(new_list)
          
 
  
# ATM Processes
# while True:
 
#        # Reading id from user
#        id = int(input("\nEnter account pin: "))
 
#        # Loop till id is valid
#        while id < 1000 or id > 9999:
#            id = int(input("\nInvalid Id.. Re-enter: "))
 
#        # Iterating over account session
#        while True:
 
#            # Printing menu
#            print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")
 
#            # Reading selection
#            selection = int(input("\nEnter your selection: "))
 
#            # Getting account object
#             for acc in accounts:
#                # Comparing account id
#            	if acc.getId() == id:
#                    accountObj = acc
#                    break
 
#            # View Balance
#            if selection == 1:
#                # Printing balance
#                print(accountObj.getBalance())
 
#            # Withdraw
#            elif selection == 2:
#                # Reading amount
#                amt = float(input("\nEnter amount to withdraw: "))
#                ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
 
#                if ver_withdraw == "Yes":
#                    print("Verify withdraw")
#                else:
#                    break
 
#                if amt < accountObj.getBalance():
#                   # Calling withdraw method
#                   accountObj.withdraw(amt)
#                   # Printing updated balance
#                   print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
#                else:
#                     print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " n")
#                     print("\nPlease make a deposit.")
 
#            # Deposit
#            elif selection == 3:
#                # Reading amount
#                amt = float(input("\nEnter amount to deposit: "))
#                ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")
 
#                if ver_deposit == "Yes":
#                   # Calling deposit method
#                   accountObj.deposit(amt)
#                   # Printing updated balance
#                   print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
#                else:
#                    break
 
#            elif selection == 4:
#                print("nTransaction is now complete.")
#                print("Transaction number: ", random.randint(10000, 1000000))
#                print("Current Interest Rate: ", accountObj.annualInterestRate)
#                print("Monthly Interest Rate: ", accountObj.annualInterestRate / 12)
#                print("Thanks for choosing us as your bank")
#                exit()
 
#            # Any other choice
#            else:
#                print("nThat's an invalid choice.")
 
# # Main function
# main()



candidate_name=input("enter candidate name for post:")
post_name=input("enter post name:")
day_election=input("enter day for election:")
election_form=input("enter election form:")
election_choice=input("offline or online:")
selection=input("yes or no")
if post_name=="GenSec,Disco":
	if day_election=="monday":
		print("election today will happen")
	elif election_form=="GenSec,Disco" and election_choice=="online":
		print("i will share election_form and election will happen online:")
	elif election_choice=="offline":
		print("election will happen offline:")
	elif selection=="yes":
		work_GenSec=input("enter GenSec work:")
		work_Disco=input("enter disco work:")
		print("you are selected for this post:")
	else:
		print("you are not selected for this post:")
if post_name=="T&P":
	if day_election=="tuesday":
		print("election today will happen")
	elif election_form=="T&P" and election_choice=="online":
		print("i will share election_form and election will happen online:")
	elif election_choice=="offline":
		print("election will happen offline:")
	elif selection=="yes":
		print("you are selected for this post:")
		work_TP=input("enter T&P work:")

	else:
		print("you are not selected for this post:")
if post_name=="food_cordinator":
	if day_election=="wednesday":
		print("election today will happen")
	elif election_form=="food_cordinator" and election_choice=="online":
		print("i will share election_form and election will happen online:")
	elif election_choice=="offline":
		print("election will happen offline:")
	elif selection=="yes":
		work_food_cordinator=input("enter food_cordinator work:")
		print("you are selected for this post:")
	else:
		print("you are not selected for this post:")
if post_name=="FM":
	if day_election=="thursday":
		print("election today will happen")
	elif election_form=="FM" and election_choice=="online":
		print("i will share election_form and election will happen online:")
	elif election_choice=="offline":
		print("election will happen offline:")
	elif selection=="yes":
		work_FM=input("enter FM work:")
		print("you are selected for this post:")
	else:
		print("you are not selected for this post:")
if post_name=="IT":
	if day_election=="friday":
		print("election today will happen")
	elif election_form=="IT" and election_choice=="online":
		print("i will share election_form and election will happen online:")
	elif election_choice=="offline":
		print("election will happen offline:")
	elif selection=="yes":
		work_IT=input("enter IT work:")
		print("you are selected for this post:")
	else:
		print("you are not selected for this post:")
if post_name=="health_cordinator,outreach":
	if day_election=="saturday":
		print("election today will happen")
	elif election_form=="health cordinator,outreach" and election_choice=="online":
		print("i will share election_form and election will happen online:")
	elif election_choice=="offline":
		print("election will happen offline:")
	elif selection=="yes":
		work_health_cordinator=input("enter health_cordinator work:")
		work_outreach=input("enter outreach work")
		print("you are selected for this post:")
	else:
		print("you are not selected for this post:")
post_name1="GenSec"
post_name2="Disco"
post_name3="T&P"
post_name4="FM"
post_name5="food_cordinator"
post_name6="IT"
post_name7="health_cordinator"
post_name8="outreach"
print("candidate_name",candidate_name,"post name",post_name1,"work of GenSec:",work_GenSec)
print("candidate_name",candidate_name,"post name",post_name2,"work of Disco:",work_Disco)
print("candidate_name",candidate_name,"post name",post_name3,"work of T&P:",work_TP)
Print("candidate_name",candidate_name,"post name",post_name4,"work of FM:",work_FM)
Print("candidate_name",candidate_name,"post name",post_name5,"work of food_cordinator:",work_food_cordinator)
Print("candidate_name",candidate_name,"post name",post_name6,"work of IT:",work_IT)
Print("candidate_name",candidate_name,"post name",post_name7,"work of health_cordinator:",work_health_cordinator)
Print("candidate_name",candidate_name,"post name",post_name8,"work of outreach:",work_outreach)
























