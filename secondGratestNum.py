def second_gratest_number(nums):
    # Check if list has less than two numbers
    if len(nums) >= 2:
        # Set these variables to low numbers 
        largest = (-9999999999) # Nota de Gemini, para la otra usa float('-inf') por si meten un numero mas pequeño
        second_largest = (-9999999999)
        # check for greatet number and puts it on a list
        for num in nums: 
            if num > largest:
                # Move current largest down a place 
                second_largest = largest

                # Update with new largest
                largest = num

            elif num > second_largest and num != largest:
                # Update second largest number and ignore if its the same number as largest
                second_largest = num

        result = (second_largest)
        print (f"Here is the second greatest number: {result}")
    else:
        print ("Please enter more than 2 numbers")
        return None



# Test Code, it asks the user for input separated by spaces then it splits the string into a list of strings
user_input = input("Please enter your numbers separated by spaces: ")
a = user_input.split()
# convert the string into numbers
user_list_numbers = []
for i in a:
    user_list_numbers.append(int(i))

second_gratest_number(user_list_numbers)




