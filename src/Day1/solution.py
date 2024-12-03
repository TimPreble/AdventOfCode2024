"""
    File: solution.py
    Desc: Day 1 solution(s)
 """

import os
from collections import Counter

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))


def part1(input1: list, input2: list):
    """Part 1 solution"""
    result = 0
    for x, y in zip(sorted(input1), sorted(input2)):  # Sort and pair each row
        result += abs(
            x - y
        )  # Find the difference between each pair & sum with previous row's results

    print(result)  # Show the final Sum


def part2(input1: list, input2: list):
    """Part 2 solution"""
    c = Counter(input2)
    result = 0

    for i in input1:
        result += i * c.get(i, 0)

    print(result)


if __name__ == "__main__":
    try:
        with open(script_dir + "/input.txt", encoding="utf-8") as f:
            lines = f.read().splitlines()  # Split the input into individual Lines.

        input1 = []
        input2 = []

        for line in lines:
            (
                x,
                y,
            ) = (
                line.split()
            )  # Split each line into 2 values.  Default seperator is whitespace
            input1.append(int(x))  # Append each list value into their own lists
            input2.append(int(y))

        part1(input1, input2)
        part2(input1, input2)
    except Exception as err:
        errorMessage = f"Exiting program because of caught exception, Error: {err}"
        print(errorMessage)

    # finally:
