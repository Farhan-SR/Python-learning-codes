import random
for x in range(1,6):
    gussing_number = int(input("Enter your guess between 1 to 5 : "))
    random_number = random.randint(1,5)

    if gussing_number == random_number :
        print("YOU HAVE WON.....")
    else:
      print("you have lost.. you can try up to 5 times ")

      print("random number was ",random_number)