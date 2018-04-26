def func(curso, *args, **kwargs):
    print(curso)
    for arg in args:
        print(arg)
    if kwargs is not None:
        for key,value in kwargs.items():
            print("{0}: {1}".format(key,value))


func("Engenharia de Computação", "Igor", "Bragaia", 20, nome="Professor Yano", idade=50)
