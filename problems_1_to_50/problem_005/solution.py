def smallest_number(max_denom):
    i = 1
    while True:
        for factor in range(1, max_denom + 1):
            if i % factor != 0: break
        else:
            return i
        i += 1

print(smallest_number(20))