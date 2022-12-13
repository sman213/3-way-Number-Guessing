import random

"""def guess_random_number(tries, start, stop):
    number = random.randint(start, stop)
    while tries > 0:
      print("number of tries left:", tries)
      guess = input("guess a number:")
      if int(guess) == number:
        print("congrats! you guessed the number!")
        return
      if int(guess) < number:
        print("guess higher!")
        tries = tries - 1
        continue
      elif int(guess) > number:
        print("guess lower!")
        tries = tries - 1
        continue
    if tries == 0:
      print("you have failed to guess the number:", number)


guess_random_number(5, 0, 10)"""

'''def guess_random_num_linear(tries, start, stop):
    for x in range(random.randint(start, stop)):
      number = random.randint(start, stop)
      print("the number for the program to guess is:", number)
      print("the number of tries left is:", tries)
      print("the program is guessing...", x)
      if x == number:
          print("program has guessed the correct answer!")
          return
      elif x < number:
          print("Number of tries left: ", tries)
          tries = tries - 1
          if tries == 0:
            print("The program failed to guess the correct number")
            break
      elif x > number:
          print("Number of tries: ", tries)
          tries = tries - 1
          if tries == 0:
            print("The program failed to guess the correct number")
            break

guess_random_num_linear(5, 0, 100)'''

def guess_random_num_binary(tries, start, stop):
    number = random.randint(start, stop)
    print("Random numnber to find:", number)
    lower_bound = start
    upper_bound = stop
    while lower_bound <= upper_bound:
      pivot = (lower_bound + upper_bound) // 2
      pivot_value = random.randint(start, stop)

      if pivot_value == number:
        print("found it!", number)
        return pivot
      if pivot_value > number:
        upper_bound = pivot - 1
        print("guessing lower!")
        tries = tries - 1
        if tries == 0:
          print("No more guesses left")
          break
      else:
        print("guessing higher!")
        lower_bound = pivot + 1
        tries = tries - 1
        if tries == 0:
          print("No more guesses left")
          break
    return -1

guess_random_num_binary(5, 0, 100)




