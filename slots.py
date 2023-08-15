#Not complete
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbolCount = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8,
}


def getSlotSpins(rows, cols, symbols):
    allSymbols = []

    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    columns = [[], [], []]
    for _ in range(cols):
        column = []
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|")
            else:
                print(column[row])



def deposit():
    while True:
        amount = input("Please enter an amount: £")        
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a value greater than 0")
        else:
            print("Please enter a number")

    return amount


def getNumberOfLines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")        
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid Number of lines")
        else:
            print("Please enter a number")

    return lines

def getBet():
    while True:
        bet = input("Please enter a bet: £")        
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be in between £{MIN_BET} - £{MAX_BET}")
        else:
            print("Please enter a number")

    return bet


def main():
    balance = deposit()
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines
        if totalBet > balance:
            print(f"You don't have enough funds for this bet. Your total balance is £{balance}.")
        else:
            break

    print(f"You are betting £{bet} on {lines} lines. Total bet is £{totalBet}.")

    slots = getSlotSpins(ROWS, COLS, symbolCount)
    printSlotMachine(slots)




main()