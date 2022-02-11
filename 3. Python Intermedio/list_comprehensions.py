def run():
    squares = [i for i in range(1, 10000) if i % 36 == 0]
    print(squares)

    print("-"*40)

    cubes = {i: i**3 for i in range(1, 100) if i % 3 == 0}
    print(cubes)

if __name__ == '__main__':
    run()