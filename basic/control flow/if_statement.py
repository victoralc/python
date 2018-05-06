bank_balance = 8

if bank_balance < 10:
  print("Bankrupt")

n = 3
if n % 2 == 0:
  print("Number " + str(n) + " is even.")
else:
  print("Number " + str(n) + " is odd.")

season = ""
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')

#Third Example - try changing the value of age
age = 28

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines set the bus fares
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the ticket price logic
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)

points = 174  # use this input when submitting your answer
prize = ""
if points <= 50:
    prize = "wooden rabbit"
    result = "Congratulations! You won a {}!".format(prize)
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    prize = "wafer-thin mint"
    result = "Congratulations! You won a {}!".format(prize)
else:
    prize = "penguin"
    result = "Congratulations! You won a {}!".format(prize)

print(result)
  
