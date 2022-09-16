def find_digit():
    """
    Используя только математические операции, выделить из числа X N-ую цифру справа.
    """
    print("Выделить N-ую цифру справа")
    x = int(input("Input X: "))
    n = int(input("Input N: "))
    answer = x // 10 ** (n-1) % 10
    print(f'Your N number is {answer}')



def exclude_digit():
    """
    Убрать в числе Х N-ую цифру справа
    """
    print("Убрать из числа N-ую цифру справа")
    x = int(input("Input X: "))
    n = int(input("Input N: "))
    answer = x//10**n*10**(n-1)+x%10**(n-1)
    print(f'Your new number is {answer}')

def help_the_rooster_hours():
    """
    Сколько часов осталось до восхода?
    """
    print("Сколько часов осталось до восхода?")
    n = int(input("Текущий час: "))
    r = int(input("Час восхода: "))
    answer = (r + 24 - n)%24
    print(f'Your new number is {answer}')


def help_the_rooster_minutes():
    """
    Сколько минут осталось до восхода?
    """
    print("Сколько минут осталось до восхода?")
    n = int(input("Текущий час: "))
    nm = int(input("Текущие минуты: "))
    r = int(input("Час восхода: "))
    rm = int(input("Минуты восхода: "))
    answer = (r*60 + rm + 1440 - n*60 - nm)%1440
    print(f'Your new number is {answer}')


def help_cheburashka_with_cakes():
    """
    Какое нужно минимальное количество тортов, если каждый торт режется на М частей,
    а к Чебурашке пришли N друзей?
    """
    print("Чебурашка и торты")
    n = int(input("Сколько друзей пришло к Чебурашке? "))
    m = int(input("Сколько кусочков в каждом торте? "))
    answer = (n-1)//m+1
    print(f'Cheburashka will need {answer} cakes')

help_cheburashka_with_cakes()
