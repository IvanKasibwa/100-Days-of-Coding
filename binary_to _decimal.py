def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        last_digit = binary % 10
        decimal += last_digit * (2 ** power)
        power += 1
        binary //= 10
    return decimal

binary_input = 889
decimal_output = binary_to_decimal(binary_input)
print("Decimal equivalent:", decimal_output)
