# List comprehension
number = [1, 2, 3]
new_number = [n + 1 for n in number]
name = 'shahjade'
new_list = [l for l in name]
range_list = [r * 2 for r in range(1, 5)]
names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]

# Dictionary comprehension
import random

names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
student_score = {name: random.randint(1, 100) for name in names}
passed_student = {key: value for key, value in student_score.items() if value > 60}
