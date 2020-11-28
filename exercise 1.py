def greetings(name, x = 1):
    for i in range(x):
        print(f'Hello, {name}!')


def main():
    name = input("What's your name? : ")
    greetings(name)


if __name__ == '__main__':
    main()
