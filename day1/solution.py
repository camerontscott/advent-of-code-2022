#!/usr/bin/env python3
"""
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.

"""
def prepare_input():
# open text file in read mode
    text_file = open("/Users/cameronscott/Dev/advent-of-code-2022/day1/input.txt", "r")

    #read whole file to a string
    data = text_file.read()

    #close file
    text_file.close()

    each_elf_calories = data.split("\n\n")
    return each_elf_calories




def find_nax_sum():
    top_three_sum = 0
    maximums = []
    max = 0
    for calorie_counts in prepare_input():
        sum = 0
        for calorie_count in calorie_counts.split("\n"):
            sum = sum + int(calorie_count)  
            if sum > max:
                max = sum
                maximums.append(max)
    top_three_sum = top_three_sum + maximums[-3]
    top_three_sum = top_three_sum + maximums[-2]
    top_three_sum = top_three_sum + maximums[-1]
    print(top_three_sum)

find_nax_sum()
