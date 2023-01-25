import random

user = 0
computer = 0

choices = ["rock", "paper", "scissors"]

while True:
    x = input("Choose: Rock / Paper / Scissors? <Type exit to exit the game> ").lower()
    if x == "exit":
        break    
    if x not in choices:
        continue
    
    random_num = random.randint(0,2)
    computer_pick = choices[random_num]
    print("Computer: ", computer_pick + ".")
    # rock : 0, paper : 1, scissors :2
    if x == "rock" and computer_pick == "scissors":
        print("Congratulations, you won!")
        user += 1
        continue

    if x == "rock" and computer_pick == "paper":
        print("Sorry, Computer wins!")
        computer += 1
        continue

    if x == "rock" and computer_pick == "rock":
        print("It's a tie!")
        continue

    if x == "scissors" and computer_pick == "rock":
        print("Sorry, Computer wins!")
        computer +=1
        continue

    if x == "scissors" and computer_pick == "paper":
        print("Congratulations, you won!")
        user +=1
        continue

    if x == "scissors" and computer_pick == "scissors":
        print("It's a tie!")
        continue

    if x == "paper" and computer_pick == "rock":
        print("Congratulations, you won!")
        user +=1
        continue

    if x == "paper" and computer_pick == "scissors":
        print("Sorry, Computer wins!")
        computer +=1
        continue

    if x == "paper" and computer_pick == "paper":
        print("It's a tie!")
        continue

print("Your Score: " , user, "." )
print("Computer Score: " , user, "." )
print("Thank you for playing!")