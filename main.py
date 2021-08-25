import random as r

correct = r.randint(1,100)
guessed_numbers = []

def my_function():
  comp_guess = r.randint(1,100)
  if comp_guess in guessed_numbers:
    my_function()
  elif comp_guess not in guessed_numbers:
    guessed_numbers.append(comp_guess)
    if guessed_numbers[-1] == correct:
      print("the correct number was " + str(correct) + ". the computer won in " + str(len(guessed_numbers)) + " guesses.")
      print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
      print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
      print(guessed_numbers)
      print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
      print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
      guessed_numbers.sort()
      print(guessed_numbers)
    else:
      my_function()

my_function()