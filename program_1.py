import random

def randDice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice_sum = die1 + die2
    return dice_sum

def main():
    total_sum = 0
    for _ in range(100):
        total_sum += randDice()
    average = total_sum / 100
    print(f"Average of 100 dice rolls: {average:.2f}")

if __name__ == "__main__":
    main()
