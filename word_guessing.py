import random as r
words = ["apple", "banana", "cherry", "grape", "mango"]
word = r.choice(words)
print("The words are : apple, banana,cherry, grape, mango.")
print("Guess the word! You have 2 tries.")
print("_ " * len(word))
for a in range(2):
    print("Try", a + 1)
    guess = input("Your guess: ")
    if guess == word:
        print("Correct! You win!")
        break
    else:
        print("Wrong guess.\n")
else:
    print("Out of tries. The word was:", word)
