def add_function(a, b):
    c = a + b
    return c

def show_func(numb):
    print(numb) 


if __name__ == "__main__":
    show_func(add_function(5, 7))