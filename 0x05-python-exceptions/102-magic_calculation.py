def magic_calculation(a, b):
    result = 0
    for x in range(1, 3):
        try:
            if (x > a):
                raise Exception('Too far')
            else:
                result += (a ** b) / x
        except Exception:
            result = (b + a)
            break
    return result
