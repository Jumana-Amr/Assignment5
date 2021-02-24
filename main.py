from os import system, name


def func1(): 
    d = input("Enter diameter:")
    d = float(d)
    a = 1 / 4 * 3.14 * d * d
    c = 3.14 * d
    print("Area =", a)
    print("Circumference =", c)
    func1()


E = input("Press Y  to enter another diameter?:")
E = str(E)
while E == "Y":
    _ = system("clear")
    func1()
    E=input("Press Y  to enter another diameter?:")
    E=str(E)
