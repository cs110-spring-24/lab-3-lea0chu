#1. Write a program that prints out the numbers 1 to 1000. (+5 points)
#2. Write a program that prints out the odd numbers between 1 and 1000. (+5 points)
#3. Write a program that prints out the numbers between 0 and 1000 that are divisible by 3. (+10 points)
#4. Write a program that prints out the numbers between 1 and 1000 that are divisible by 3 or 5. (+10 points)
#5. Write a program that asks the user to enter a number and prints out all the numbers between 1 and that number that are divisible by 11 or 13. The number entered should be greater than 200. (+10 points) Extra credit if the programs asks again if the number is less than 200. (+5 points)
#6. Write a program that prints out each letter of a string line by line (+5 points)
#7. Write a program that asks the user to enter a string and outputs every second letter. The string must be more than 10 letters long. (+10 points)
#8. Write a program that rolls 1000 dice and prints out the number of times each number was rolled. (+15 points)
#9. Write a program that checks if a given number is a prime number. A prime number is a number that is only divisible by 1 and itself. The user enters a number and the programs prints out whether the number is a prime number or not. (+15 points)
#10. Write a program that prints out the prime numbers less than 1000. (+20 points)
while True:
  print("Options: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
  run = input("Enter the problem you want to run: ")
  run = int(run)
  game=run
  if run == 1:
      for i in range(1000):
          print(i)
  elif run == 2:
      for i in range(1000):
          if i % 2 != 0:
              print(i, end=" ")
  elif run == 3:
      for i in range(0,1000):
          if i % 3 == 0:
              print(i)
  elif run == 4:
      for i in range(1,1000):
          if (i % 3 == 0 or i % 5 == 0):
              print(i)
  elif run == 5:
      num = int(input("Enter a number greater than 200: "))
      while num < 200:
          num = int(input("Too low"))
  
      for i in range(1, num):
          if (i % 11 == 0 or i % 13 == 0):
              print(i)
          # else:
              # print(input("Enter a number greater than 200."))
  elif run == 6:
      string = "I hate python"
      for loc in range(len(string)):
          print(string[loc])
  elif run == 7:
      user = input("Enter a ten character string. ")
      for l in range(0, len(user), 2):
          print(user[l])
  elif run == 8:
    import random
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    for rolls in range(1000):
        dice = random.randint(1,6)
        if dice == 1:
            ones += 1
        elif dice == 2:
            twos += 1
        elif dice == 3:
            threes +=1
        elif dice == 4:
            fours += 1
        elif dice == 5:
            fives +=1
        else:
            sixes +=1
    print(f"You rolled {ones} 1s, {twos} 2s, {threes} 3s, {fours} 4s, {fives} 5s, and {sixes} 6s.")
  elif run == 9:
      num2 = int(input("Enter a number: "))
      if num2 > 1:
        for i in range(2, int(num2/2)+1):
            if (num2 % i) == 0:
                print(num2, "is not a prime number")
                break
            else:
                print(num2, "is a prime number")
                break
  elif run == 10:
      for num in range(2,1000):
        for i in range(2, num):
            if num % i == 0:
                break
            else:
              print({num}, 'is a prime number')
  restart = input("Run again? ")
  if "Yes" in restart:
    continue
  else:
    print("Goodbye.")
    break