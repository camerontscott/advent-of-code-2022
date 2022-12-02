#!/usr/bin/env python3

def prepare_input():
# open text file in read mode
    text_file = open("/Users/cameronscott/Dev/advent-of-code-2022/day2/input.txt", "r")

    data = text_file.read()

    #close file
    text_file.close()
    lines = data.split('\n')

    return lines

def calculate_score(input):
    score = 0
    for line in input:
        if (line[2] == 'X'):
            score = score + 1
            if(line[0] == 'A'):
                score = score + 3
            if(line[0] == 'C'):
                score = score + 6
        if (line[2] == 'Y'):
            score = score + 2
            if(line[0] == 'A'):
                score = score + 6
            if(line[0] == 'B'):
                score = score + 3
        if (line[2] == 'Z'):
            score = score + 3
            if(line[0] == 'B'):
                score = score + 6
            if(line[0] == 'C'):
                score = score + 3
    print(score)


calculate_score(prepare_input())