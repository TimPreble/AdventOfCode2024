"""
    File: solution.py
    Desc: Day 2 solution(s)
 """
# pylint: disable=line-too-long
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))


def part1(input1: list, input2: list):
    """Part 1 solution"""


if __name__ == "__main__":
    try:
        # with open("src/Day1/input.txt", encoding="utf-8") as f:
        with open(script_dir + "/input.txt", encoding="utf-8") as f:
            lines = f.read().splitlines()  # Split the input into individual Lines.

    except Exception as err:
        errorMessage = f"Exiting program because of caught exception, Error: {err}"
        print(errorMessage)

    # finally:
