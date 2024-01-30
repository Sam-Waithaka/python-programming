def d():
    animal = 'elephant'
    def e():
        nonlocal animal
        animal = 'girraffe'
        print('INSIDE NESTED FUNCTION e '+ animal)
    print('before calling function '+ animal)
    e()
    print('after calling function e ' + animal)

animal = 'camel'
d()
print(f"The final value of the variable animal is {animal}")