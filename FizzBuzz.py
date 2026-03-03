def fizzBuzz(n):
    # Write your code here
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0: 
            print ("FizzBuzz")   
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print (i)

user_number = int(input("Please Enter Your Number: "))
fizzBuzz(user_number)

