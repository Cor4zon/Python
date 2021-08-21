# 51 ? impossible -> -1
# 3 ? impossible -> -1
# 50 -> 2
# 45 -> 1
# 5 -> 1

def number_len(number):
    length = 0
    while number > 0:
        number //= 10
        length += 1
    return length


def is_special_number(number):
    special_symbols = '45'
    for i in str(number):
        if i not in special_symbols:
            return False
    return True


def get_max_special_number_less_than_x(x):
    max_special_num = 0
    # x = reversed(str(x))
    while x > 0:
        cur_digit = x % 10
        if cur_digit >= 5:
            max_special_num = (max_special_num * 10) + 5
        elif cur_digit == 4:
            max_special_num = (max_special_num * 10) + 4
        else:
            max_special_num *= 10

        x //= 10

    return max_special_num


def get_min_number_of_special_terms(number):
    terms_count = 0
    while number > 0:
        number -= get_max_special_number_less_than_x(number)
        terms_count += 1

    if number == 0:
        return terms_count
    return -1



def solve(T, samples):
    result = []
    for i in range(T):
        result.append(get_min_number_of_special_terms(samples[i]))

    return result


T = int(input())
samples = []
for _ in range(T):
    samples.append(int(input()))

out_ = solve(T, samples)
print ('\n'.join(map(str, out_)))




