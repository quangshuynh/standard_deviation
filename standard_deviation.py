"""
Standard Deviation Reaction Times
03/16/2024
author: Quang Huynh
"""

def main():
    print("Example: 0.410, 1.108, 2.224, 0.341, 0.441, 0.325, 0.842, 1.074, 3.475, 0.958")
    input_string = input("Enter reaction times separated by commas: \n> ")
    reaction_times = input_string.split(",")
    print("reaction times list: " + str(reaction_times) + "\n")

    # convert each item to float type
    for i in range(len(reaction_times)):
        # convert each item to float type
        reaction_times[i] = float(reaction_times[i])

    sum_of_reaction_times = 0
    for i in reaction_times:
        sum_of_reaction_times += i

    mean = sum_of_reaction_times / len(reaction_times)
    standard_deviation = float(input("Input standard deviation: \n> "))

    # Calculating the range
    highest_value = max(reaction_times)
    lowest_value = min(reaction_times)
    range_of_data = highest_value - lowest_value

    # Calculating how many values are within one standard deviation of the mean
    values_within_std_dev = sum(1 for time in reaction_times if (mean - standard_deviation) < time < (mean + standard_deviation))

    print("mean: " + str(mean))
    print("highest value: " + str(highest_value))
    print("lowest value " + str(lowest_value))
    print("range: " + str(range_of_data))
    print("standard deviation: " + str(standard_deviation))
    print("values within standard deviation: " + str(values_within_std_dev))


if __name__ == "__main__":
    main()
