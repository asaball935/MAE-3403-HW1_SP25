import random
from Dice import rollDice, rollUnFairDice


def calculate_probabilities(roll_function, N, num_trials=1000):
    """
    Rolls the dice multiple times and calculates the probabilities of each possible score.
    :param roll_function: The function to use for rolling dice (either fair or unfair).
    :param N: Number of dice.
    :param num_trials: Number of trials to run.
    :return: A dictionary with scores as keys and their probabilities as values.
    """
    # The possible score range for N dice
    min_score = N
    max_score = 6 * N

    # Initialize a dictionary to hold the frequency of each score
    score_counts = {score: 0 for score in range(min_score, max_score + 1)}

    # Roll the dice num_trials times
    for _ in range(num_trials):
        score = roll_function(N)
        score_counts[score] += 1

    # Calculate probabilities
    probabilities = {score: count / num_trials for score, count in score_counts.items()}

    return probabilities


def main():
    N = int(input("Enter the number of dice to roll for fair dice: "))
    probabilities = calculate_probabilities(rollDice, N)
    print(f"Probabilities for rolling {N} fair dice:")
    for score in sorted(probabilities.keys()):
        print(f"Probability of rolling a {score}: {probabilities[score]:.3f}")


def main2():
    N = 5  # We are rolling 5 unfair dice
    num_trials = 1000
    probabilities = calculate_probabilities(rollUnFairDice, N, num_trials)
    print(f"Probabilities for rolling {N} unfair dice:")
    for score in sorted(probabilities.keys()):
        print(f"Probability of rolling a {score}: {probabilities[score]:.3f}")


if __name__ == "__main__":
    main()  # or main2() for unfair dice
