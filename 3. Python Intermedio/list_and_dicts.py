from os import sep


def run():
    my_list = [1, 2, 3, True, 1.2]
    my_dict = {"firstname": "David", "lastname": "Triviño"}

    super_list = [
        {"firstname": "David", "lastname": "Triviño"},
        {"firstname": "Esteban", "lastname": "Gonzalez"},
        {"firstname": "Julio", "lastname": "Cortazar"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1, -12, 5, 0],
        "floating_nums": [1.2, -3.6, 0.65]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


    print("-"*40)
    
    for values in super_list:
        for key, value in values.items():
            print(value, end=" ")
        print("", sep="\n")



if __name__ == '__main__':
    run()