def sum2(x, y):
    return x + y

def pos_or_neg(x):
    x = float(x)
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'


def check_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def check_quantity(n):
    return len(str(n))


def sum_list(num):
    return sum(num)



