#Есть площадка шириной w и длиной h. напишите программу, которая определяет можно
#ли замостить эту площадку квадратными плитками со стороной a.

def fill_the_tiles():
    '''
Есть площадка шириной w и длиной h. напишите программу, которая определяет можно
ли замостить эту площадку квадратными плитками со стороной a.
даны три отрезка a, b, c. Определите могут ли эти отрезки быть сторонами одного
треугольника.Напишите программу, которая определяет, можно ли поместить один прямоугольник со
сторонами a, b в другой c, d
    '''
    w = int(input("Input side W: "))
    h = int(input("Input side H: "))
    a = int(input("Input side of tile (A): "))
    if w%a==0 and h%a ==0:
        print(f"You can fill the rectangular {w} by {h} with square tiles of {a}")
    else:
        print(f"You can NOT fill the rectangular {w} by {h} with square tiles of {a}")


def check_triangle_sides():
    a = int(input("Input side A: "))
    b = int(input("Input side B: "))
    c = int(input("Input side C: "))
    if  a < b+c and b<c+a and c<a+b:
        print(f"You can make a regular triangle where {a=}, {b=}, {c=}")
    else :
        print(f"You can NOT make a regular triangle where A={a} B = {b} C = {c}...bla-bla-bla....")

check_triangle_sides()
