def moveZeroes(nums):
    print (f"Your List Is: {nums}")
    
    # Count how many 0s are in original list
    zero_count = nums.count(0)

    # Create a list of non-zero numbers?

    non_zero = []
    for n in nums:
        if n != 0:
            non_zero.append(n) 
    
    # To the list of non zero numbers add 0s x the number of 0s in original list
    nums = non_zero + [0] * zero_count
    print (f"Your Final List Is: {nums}")


# Test Code
user_list = [0, 1, 0, 3, 12]
moveZeroes(user_list)




