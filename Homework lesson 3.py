def max_prime_nuber():
    n = int(input("введите икс: "))
    ans = n
    answer = n
    l = 2
    while l <= n**0.5 and ans != 1:
        if ans % l == 0:
            ans = ans/l
            print(f'{l=}')
            answer = l
        else:
            l += 1
    print(f"ваш ответ = {int(answer)}")

max_prime_nuber()