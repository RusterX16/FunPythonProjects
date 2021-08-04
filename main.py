# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from string import ascii_letters
from random import randint


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def rock_paper_scissors():
    arr = ["Rock", "Paper", "Scissors"]
    player = input("Rock, Paper or Scissors ?\n")
    won = False

    while not arr.__contains__(player):
        player = input("Incorrect answer ! So, Rock, Paper or Scissors ?\n")

    n = arr.index(player)
    ia = randint(0, len(arr) - 1)
    print("\nYou » " + player + "\nIA » " + arr[ia])

    if player == arr[ia]:
        print("Draw !")
        return

    if n == ia + 1:
        won = True
    else:
        if n == 0 and ia == len(arr) - 1:
            won = True

    if won:
        print("Well done ! You won")
    else:
        print("Shame on you ! You lost")


def guess_the_number(length):
    n = randint(0, length)
    found = False
    count = 0

    guess = input("Guess the number !\n")

    while not found:
        if int(guess) == n:
            found = True
        else:
            if int(guess) > n:
                guess = input("Less\n")
            else:
                guess = input("More\n")
        count += 1
    print("Well done ! The number to guess was " + str(n) + "\nYou succeed with " + str(count) + " attempts")


def hangman():
    finished = False
    count = 0
    letters = list(ascii_letters)

    f = open("dictionnary")
    content = f.read().splitlines()
    n = randint(0, len(content) - 1)
    word = content[n]
    hidden_word = word

    print(word)

    while not finished:
        for i in letters:
            hidden_word = hidden_word.replace(i, "_")

        attempt = input("Tell a letter : \n")

        while not letters.__contains__(attempt):
            attempt = input("I said a letter come on :\n")

        for i in range(len(word)):
            print(attempt + " / " + word.__getitem__(i))
            if attempt == word.__getitem__(i):
                print("yes")
        print(hidden_word)

        if not hidden_word.__contains__("_"):
            finished = True

    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # rock_paper_scissors()
    # guess_the_number(100)
    hangman()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
