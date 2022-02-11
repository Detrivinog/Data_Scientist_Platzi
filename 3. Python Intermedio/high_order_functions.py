from functools import reduce

def run():
    palindrome = lambda string: string.lower() == string[::-1].lower()
    print(palindrome('Ana'))

    my_list = range(1, 11)
    odd = list(filter(lambda x: x%2 != 0, my_list))

    print(odd)

if __name__ == '__main__':
    run()