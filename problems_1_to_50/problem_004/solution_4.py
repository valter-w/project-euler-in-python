def largest_palindrome_product(digits):
    if type(digits) is not int:
        raise TypeError("argument 'digits' must be of type 'int'")
    if digits < 1:
        raise ValueError("argument 'digits' bust be > 0")
    
    largest_product = None
    min_factor = 10 ** (digits - 1)
    max_factor = (10 ** digits) - 1
    
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            product = i * j
            if not largest_product or product > largest_product:
                product_digits = str(product)
                if product_digits == product_digits[::-1]:
                    largest_product = product

    return largest_product

# Get largest product using only 3-digit factors
print(largest_palindrome_product(3))