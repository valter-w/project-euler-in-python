first_100 = list(range(101))
first_100_squared = [x**2 for x in first_100]

sum_of_squares = sum(first_100_squared)
square_of_sum = sum(first_100)**2

diff = square_of_sum - sum_of_squares

print(f"{square_of_sum} - {sum_of_squares} = {diff}")