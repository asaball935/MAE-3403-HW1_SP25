# region imports
import random as rnd
import math
# endregion

# region functions
def calculate_mean(data):
    """
    Calculates the mean of a dataset.

    :param data: A list of numeric values.
    :return: The mean of the dataset.
    """
    return sum(data) / len(data)


def calculate_stdev(data, mean):
    """
    Calculates the standard deviation of a dataset.

    :param data: A list of numeric values.
    :param mean: The mean of the dataset.
    :return: The standard deviation of the dataset.
    """
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)


def count_within_bins(data, mean, stdev):
    """
    Counts the percentage of data points within 1, 2, and 3 standard deviations of the mean.

    :param data: A list of numeric values.
    :param mean: The mean of the dataset.
    :param stdev: The standard deviation of the dataset.
    :return: Percentages within ±1, ±2, and ±3 standard deviations.
    """
    bin1 = sum(1 for x in data if mean - stdev <= x <= mean + stdev)
    bin2 = sum(1 for x in data if mean - 2 * stdev <= x <= mean + 2 * stdev)
    bin3 = sum(1 for x in data if mean - 3 * stdev <= x <= mean + 3 * stdev)

    bin1_percentage = (bin1 / len(data)) * 100
    bin2_percentage = (bin2 / len(data)) * 100
    bin3_percentage = (bin3 / len(data)) * 100

    return bin1_percentage, bin2_percentage, bin3_percentage


def generate_normal_data(mean, stdev, size):
    """
    Generates a list of normally distributed data.

    :param mean: The desired mean of the normal distribution.
    :param stdev: The desired standard deviation of the normal distribution.
    :param size: The number of data points to generate.
    :return: A list of normally distributed data points.
    """
    return [rnd.normalvariate(mean, stdev) for _ in range(size)]
# endregion


def main():
    """
    Generates a normally distributed dataset, calculates its mean and standard deviation,
    and verifies the data distribution by checking the percentage of values within 1, 2, and 3 standard deviations.

    :return: None
    """
    N = 1000  # Size of the dataset
    mean = 50  # Desired mean
    stdev = 10  # Desired standard deviation

    # Generate the data
    data = generate_normal_data(mean, stdev, N)

    # Calculate sample mean and standard deviation
    sample_mean = calculate_mean(data)
    sample_stdev = calculate_stdev(data, sample_mean)

    # Count percentages within standard deviation bins
    bin1_percentage, bin2_percentage, bin3_percentage = count_within_bins(data, sample_mean, sample_stdev)

    # Print results
    print(f"Sample Mean: {sample_mean:.2f}")
    print(f"Sample Standard Deviation: {sample_stdev:.2f}")
    print(f"{bin1_percentage:.1f}% of data within ±1 StDev of mean.")
    print(f"{bin2_percentage:.1f}% of data within ±2 StDev of mean.")
    print(f"{bin3_percentage:.1f}% of data within ±3 StDev of mean.")


if __name__ == "__main__":
    main()
