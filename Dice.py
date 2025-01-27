from Die import rollFairDie, rollUnFairDie

def rollDice(N=1):
    """
    Simulates rolling N fair dice simultaneously.
    :param N: Number of dice to roll.
    :return: Total score from rolling N dice.
    """
    total_score = 0
    for _ in range(N):
        total_score += rollFairDie()
    return total_score

def rollUnFairDice(N=1):
    """
    Simulates rolling N unfair dice simultaneously.
    :param N: Number of dice to roll.
    :return: Total score from rolling N unfair dice.
    """
    total_score = 0
    for _ in range(N):
        total_score += rollUnFairDie()
    return total_score

# endregion