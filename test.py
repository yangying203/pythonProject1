name = 'yy'


def fun1(fun):
    print(name)

    def fun2():
        fun()
        name = 'ii'
        print(name)
        print('fun2')
    return fun2


@fun1
def decorete():
    print('hhhh')
decorete()

