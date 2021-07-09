# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    rock_paper_scissors()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
