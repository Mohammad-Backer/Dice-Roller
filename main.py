import random as rand

if __name__ == "__main__":
    
    while True:

        print("The dice is rolled!")

        print(rand.randint(1,6))

        user_decision = input("Do you want to Roll the dice again? ")

        if user_decision.lower() == "yes":
            continue

        else:
            break
