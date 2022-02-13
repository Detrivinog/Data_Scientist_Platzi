from functools import reduce

def run():
    palindrome = lambda string: string.lower() == string[::-1].lower()
    print(palindrome('Ana'))

    my_list = range(1, 11)
    odd = list(filter(lambda x: x%2 != 0, my_list))

    squares = list(map(lambda x: x**2, my_list))

    sum_all = reduce(lambda a, b: a + b, my_list)

    print(odd)
    print(squares)
    print(sum_all)


if __name__ == '__main__':
    run()