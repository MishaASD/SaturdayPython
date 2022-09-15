def find_digit():
    """
    Используя только математические операции, выделить из числа X N-ую цифру справа.
    :return: Искомая цифра
    """



def exclude_digit():
    x = int(input("Input X: "))
    n = int(input("Input N: "))
    answer = x//10**n*10**(n-1)+x%10**(n-1)
    print(f'Your new number is {answer}')

exclude_digit()