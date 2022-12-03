#!/usr/bin/env python3
def prepare_input():
# open text file in read mode
    text_file = open("/Users/cameronscott/Dev/advent-of-code-2022/day3/input.txt", "r")

    data = text_file.read()

    #close file
    text_file.close()
    lines = data.split('\n')

    return lines

def map_priority(character):
    if character.islower():
        return ord(character) - 96
    else:
        return ord(character) - 38

def solve_p1(lines):
    sum = 0
    for line in lines:
        my_set = set(line[:len(line)//2])
        second_half = line[len(line)//2:]
        common_item = list(my_set.intersection(second_half))[0]
        sum = sum + map_priority(common_item)
    print(sum)


def solve_p2(lines):
    sum = 0
    for i in range(0, len(lines)-2, 3):
        s1 = set(lines[i])
        s2 = set(lines[i+1])
        s3 = set(lines[i+2])
      
        set1 = s1.intersection(s2)
        common_between_three = list(set1.intersection(s3))[0]
        sum = sum + map_priority(common_between_three)
    print(sum)

solve_p1(prepare_input())
solve_p2(prepare_input())
