


# for x in range(1, 10 + 1):
#     print(x, end=' ')

def print_x_rev(x):
    if x == 0:
        return
    print_x_rev(x - 1)
    print(x, end=' ')

def print_x_asc(x):
    if x == 11:
        return
    print_x_asc(x + 1)
    print(x, end=' ')

print_x_rev(10)
print()
# # ...
# print_x(9)
#print_x(10)

print_x_asc(1)

def add_recur(x, y):
    # return x + y
    if y == 0:
        result = x
        return result
    result = add_recur(x + 1, y - 1)
    return result

def add_recur_1(x, y):
    # return x + y
    if y == 0:
        return x
    result = 1 + add_recur_1(x, y - 1)
    return result

print()
print(add_recur(4, 3))

print(add_recur_1(4, 3))

def sum_digits(x):
    if x < 10:
        print (f"{x} = ", end = '')
        return x
    ahadot = x % 10
    print (f"{ahadot} + ", end = '')
    bli_ahadot = x // 10
    return ahadot +  sum_digits(bli_ahadot)

print(sum_digits(473820))

def check_if_is_in(c: str, line: str):
    if len(line) == 0:
        return False
    if line[0] == c:
        return True
    return check_if_is_in(c, line[1:])

# "a" "dbsdbfa"
print('btbccca', check_if_is_in("a", "btbccca"))
print('babc', check_if_is_in("a", "babc"))
print('dfjh', check_if_is_in("a", "dfjh"))
print('adfjhfgvajh', check_if_is_in("a", "adfjhfgvajh"))
print('sdfjhfgvjh11', check_if_is_in("a", "sdfjhfgvjh11"))

