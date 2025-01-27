# HW1SP25_Prob1.py
from Die import rollFairDie as rfd, rollUnFairDie as rufd

def main():
    # Initialize counters for each face (1 through 6)
    counts = [0] * 6

    # Simulate rolling the die 1000 times
    for _ in range(1000):
        roll = rfd()  # Call the rollFairDie function
        counts[roll - 1] += 1  # Increment the count for the rolled number

    # Print the probabilities
    print("After rolling the die 1000 times:")
    for i in range(6):
        print(f"Probability of rolling a {i+1}: {counts[i] / 1000:.4f}")

def main2():
    # Initialize counters for each face (1 through 6)
    counts = [0] * 6

    # Simulate rolling the die 10,000 times
    for _ in range(10000):
        roll = rfd()  # Call the rollFairDie function
        counts[roll - 1] += 1  # Increment the count for the rolled number

    # Print the probabilities
    print("After rolling the die 10000 times:")
    for i in range(6):
        print(f"Probability of rolling a {i+1}: {counts[i] / 10000:.4f}")

def main3():
    # Initialize counters for each face (1 through 6)
    counts = [0] * 6

    # Simulate rolling the unfair die 10,000 times
    for _ in range(10000):
        roll = rufd()  # Call the rollUnFairDie function
        counts[roll - 1] += 1  # Increment the count for the rolled number

    # Print the probabilities
    print("After rolling the unfair die 10000 times:")
    for i in range(6):
        print(f"Probability of rolling a {i+1}: {counts[i] / 10000:.4f}")

if __name__ == "__main__":
    main()
    print()  # Add a line break between results
    main2()
    print()  # Add a line break between results
    main3()
