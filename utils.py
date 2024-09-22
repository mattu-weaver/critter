import random

def get_rnd_norm(mean, std_dev):
    """
    Generate a random value from a normal distribution within the specified range.
    mean: float - the mean of the distribution
    std_dev: float - the standard deviation of the distribution
    """
    return random.gauss(mean, std_dev)


def get_rnd_norm_range(mean, std_dev):
    """
    Generate a random value from a normal distribution within the specified range.
    mean: float - the mean of the distribution
    std_dev: float - the standard deviation of the distribution
    """
    val1 = random.gauss(mean, std_dev)
    val2 = random.gauss(mean, std_dev)
    return min(val1, val2), max(val1, val2)