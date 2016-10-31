def fizz_buzz(i):
    if i % 15 == 0:  # Test for FizzBuzz
        return "FizzBuzz"
    elif i % 3 == 0:  # Test for Fizz
        return "Fizz"
    elif i % 5 == 0:  # Test for Buzz
        return "Buzz"
    else:  # Condition if not Fizz,Buzz or FizzBuzz
        return i
