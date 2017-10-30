#Challenge 1 (Exchange Rate Calculation)

x_rate = 0.65,total_dollars = 200,fee = 2,(total_dollars - fee) * x_rate,total_pounds = (total_dollars - fee) * x_rate

#Challenge 2 (Exchange Rate Calculation 2)
total_dollars = (total_pounds / x_rate) - fee,import math ,math.ceil(total_dollars)

#Challenge 3 (String Concatenation)
greeting.py
greeting = "G'day" + " " + "mate"
print(greeting)


#Challenge 4 (Getting Started with Python Strings)
#comedian.py
name = "Jim Gaffigan"
description = "stand-up comedian"
year = 2001

sentence = name + ' is a ' + description + ' since ' + str(year)
print(sentence)

#Challenge 5 (String Formatting)
#movies.py
movie1 = "\n\tBrave Heart"
movie2 = "\n\tAnenger's"

print('My Favorite Movies:', movie1, movie2)

#Challenge 6 (Pythonese)
#pythonese.py
word = 'Python'
first = word[0]
rest = word[1:]
result = rest + '-' + first + 'y'
print(result)



#Challenge 7 (Comparison Operators)
#comparison.py
answer = 10 > 4
print(answer)

#Challenge 8 (If Else)
#rain_slang.py
rain_speed = 6

if rain_speed < 5:
    print("Just a Scotch mist")
else:
    print("It's a real Cow-quaker out there")


#Challenge 9 (Rock-Paper-Python)
#rock_paper_python.py
computer_choice = 'rock'
user_choice = input("Enter rock, paper, or python:\n")
if computer_choice == user_choice:
    print('TIE')
else:
    print('You lose :( Computer wins :D')

#Challenge 10 (Improving Rock-Paper-Python)
#rock_paper_python.py
computer_choice = 'rock'
user_choice = input("Enter rock, paper, or python:\n")

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'python':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
elif user_choice == 'python' and computer_choice == 'paper':
    print('WIN')
else:
    print('You lose :( Computer wins :D')
