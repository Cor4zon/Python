import pandas as pd
import numpy as np
import re, datetime  # for task 5, 6

df = pd.read_csv('data.csv')


# task 1
# Сколько четных чисел в этом столбце?
def is_even(number):
    return not (number % 2)


# first column parsing
nums = np.array([int(df.num1[i]) for i in range(1, 1001)])

even_counter = 0
for num in nums:
    if is_even(num):
        even_counter += 1

print(even_counter)  # 507


# task 2
# Сколько простых чисел в этом столбце?
nums2 = np.array([int(df.num2[i]) for i in range(1, 1001)])


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    if not (number % 2) or not (number % 3):
        return False

    i = 5
    while i * i <= number:
        if not (number % i) or not (number % (i + 2)):
            return False
        i += 6
    return True


prime_counter = 0
for num in nums2:
    if is_prime(num):
        prime_counter += 1


print(prime_counter)  # 168


# task 3
# Сколько чисел, меньших 0.5 в этом столбце?
def is_greater(number, compare_number):
    if number > compare_number:
        return True
    return False


# deleting spaces and changing comma by dot
nums3 = np.array([float(df.num3[i].replace(' ', '').replace(',', '.')) for i in range(1, 1001)])

counter = 0
for num in nums3:
    if is_greater(num, 0.5):
        counter += 1

print(counter)  # 515


# task 4
# Сколько вторников в этом столбце?
dates1 = np.array([df.date1[i] for i in range(1, 1001)])

tuesday_counter = 0

for date in dates1:
    if 'Tue' in date:
        tuesday_counter += 1

print(tuesday_counter)      # 156


# task 5
# Сколько вторников в этом столбце?
TUESDAY = 1
tuesdayCounter = 0

for i in range(1, 1001):
    match = re.search('\d{4}-\d{2}-\d{2}', df.date2[i])
    date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
    if date.weekday() == TUESDAY:
        tuesdayCounter += 1

print(tuesdayCounter)       # 138


# task 6
# Сколько последних вторников месяца в этом столбце?
last_tuesday_counter = 0


for i in range(1, 1001):
    match = re.search('\d{2}-\d{2}-\d{4}', df.date3[i])
    date = datetime.datetime.strptime(match.group(), '%m-%d-%Y').date()
    if date.weekday() == TUESDAY:
        try:
            datetime.date(year=date.year, month=date.month, day=date.day + 7)
        except ValueError:
            last_tuesday_counter += 1


print(last_tuesday_counter)     # 43