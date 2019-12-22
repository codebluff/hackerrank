#!/bin/python3

import math
import os
import random
import re
import sys


"""Note: If you are copy pasting this code into your editor, then please copy only the gradingStudents() definition, 
Otherwise it will create problem while printing messages """


def gradingStudents(grades):
    for i in range(0, len(grades), 1):
        if grades[i] < 38:
            continue
        elif grades[i] % 5 >= 3:
            add = 5 - (grades[i] % 5)
            grades[i] += add
            continue
    return grades


grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)

print(result)