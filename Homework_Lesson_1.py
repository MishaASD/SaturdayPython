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


def wild_dog_runs():
    """
    Собака бегает туда-сюда вдоль забора длиной d со скоростью v.
    Как только  собака добегает до угла она разворачивается и бежит назад.
    Куда будет направлена морда через s секунд
    (0 - в сторону угла, откуда собака начинала свой бег, 1 - в противоположную сторону).
    """
    print("Бешеной собаке 3 километра не круг")
    d = int(input("Расстояние от угла до угла: "))
    v = int(input("Скорость собаки: "))
    s = int(input("Сколько секунд собака бежит: "))
    answer = int((s // ( d / v) + 1) % 2)
    print(f'Dog is facing to the side No. {answer}')


def bit_xray():
    """
    Необходимо выделить из числа x  n последовательных бит, начиная с бита под номером m
    :return:
    """
    x = int(input("Исходное число Х в двоичной системе: "), 2)
    m = int(input("Начальный бит выделения справа: "))
    n = int(input("Количество выделяемых битов справа: "))
    answer = (x>>(m-1))%(2**n)
    print(f'The result is: {bin(answer)}')


def switch_on_the_lights():
    """
    У вас есть бинарная последовательность из 16 бит,
    каждый из бит - управляет своим выключателем.
    ваша задача включить свет в лампах с М по N (справа),
    оставив состояние остальных ламп неизменным.
    :return:
    """
    m = int(input("Начальная лампа (бит) справа: "))
    n = int(input("Конечная лампа (бит) справа: "))
    x = int(input("Исходное состояние: "), 2)
    mask = ((1<<(n-m+1))-1)<<(m-1)
    answer = x|mask
    print(f'Mask is {bin(mask)}')
    print(f'Lamps are switched as follows: {bin(answer)}')


def switch_off_the_lights():
    """
    У вас есть бинарная последовательность из 16 бит,
    каждый из бит - управляет своим выключателем.
    ваша задача выключить свет в лампах с М по N (справа),
    оставив состояние остальных ламп неизменным
    :return:
    """
    m = int(input("Начальная лампа (бит) справа: "))
    n = int(input("Конечная лампа (бит) справа: "))
    x = int(input("Исходное состояние: "), 2)
    mask = 65535^(((1<<(n-m+1))-1)<<(m-1))
    answer = x & mask
    print(f'Mask is {bin(mask)}')
    print(f'Lamps are switched as follows: {bin(answer)}')
