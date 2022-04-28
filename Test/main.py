def binary_sum(num1, num2):
    if num1 < num2:
        while num1 < num2:
            num1 += 1
    elif num1 > num2:
        while num1 > num2:
            num2 += 1
    else:
        return num1, num2
    print(num1, num2)

def main():
    binary_sum(2, 6)

if __name__ == "__main__":
    main()
    


