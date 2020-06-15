#reference <python crash course> p169 10-1
import os

file_name = 'learning_python.txt'

with open(file_name) as file_object:
    content = file_object.read()

print('First:')
print(content)

print('Second')
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

print('Third')
with open(file_name) as file_object:
    lines = file_object.readlines()
    print(lines)





