def fill_the_tiles():
    w = int(input("Input side W: "))
    h = int(input("Input side H: "))
    a = int(input("Input side of tile (A): "))
    if w%a==0 and h%a ==0:
        print(f"You can fill the rectangular {w} by {h} with square tiles of {a}")
    else:
        print(f"You can NOT fill the rectangular {w} by {h} with square tiles of {a}")


