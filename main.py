def binary_sum(num1, num2):
    if num1 < num2:
        while num1 < num2:
            num1 += 1
    elif num1 > num2:
        while num1 > num2:
            num2 += 1
    else:
        return num1, num2
    return num1, num2


if __name__ == "__main__":
    print(binary_sum(2, 30))
    


