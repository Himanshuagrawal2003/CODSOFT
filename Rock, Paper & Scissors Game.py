import random
User_Score = 0
Computer_Score = 0
choices = ['Rock', 'Paper', 'Scissors']
while True:
    computer = random.choice(choices)
    user = input("Rock, Paper & Scissors Choose one of them: ").capitalize()
    if user not in choices:
        print("You entered something wrong!")
    else:
        print(f"Computer chose {computer}\n You chose {user}")
        if computer == user:
            print("It's a tie!")
        elif computer == "Rock":
            if user == "Paper":
                print("You win!")
                User_Score += 1
            else:
                print("You lost!")
                Computer_Score += 1
        elif computer == "Paper":
            if user == "Scissors":
                print("You win!")
                User_Score += 1
            else:
                print("You lost!")
                Computer_Score += 1
        elif computer == "Scissors":
            if user == "Rock":
                print("You win!")
                User_Score += 1
            else:
                print("You lost!")
                Computer_Score += 1
        print(f"Score - You: {User_Score}, Computer: {Computer_Score}\n")