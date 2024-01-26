
def fizz():
    if (x % 3 == 0 and x % 5 == 0):
        return 'FizzBuzz'
    elif (x % 3 == 0):
        return 'Fizz'
    elif (x % 5 == 0):
        return 'Buzz'
    else:
        return x

if __name__ == "__main__":
    for x in range(21):
        print(fizz())