import math

def pythagorean_triplet_by_sum(target_sum):
    max_a = round((target_sum-3) / 3) # if a = b - 1 and c = b - 1
    max_b = round((target_sum-2) / 2) # if a = 1 and b = c - 1
    max_c = target_sum - 3 # if a = 1 and b = 2

    for a in range(1, max_a + 1):
        for b in range(a + 1, max_b + 1):
            for c in range(b + 1, max_c + 1):
                # if a**2 + b**2 == c**2 and sum == product:
                if a**2 + b**2 == c**2 and sum([a, b, c]) == target_sum:
                    return (a, b, c)


triplet = pythagorean_triplet_by_sum(1000)
print(f"{triplet[0]}² + {triplet[1]}² = {triplet[2]}²")
print(f"{triplet[0]} + {triplet[1]} + {triplet[2]} = 10000")

product = math.prod(triplet)
print(f"{triplet[0]} * {triplet[1]} * {triplet[2]} = {product}")
print(f"({product} is the answer.)")