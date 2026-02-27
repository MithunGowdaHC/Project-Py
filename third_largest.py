def third_largest(nuums):
    first = float('-inf')
    second = float('-inf')
    third = float('-inf')
    for n in nums:
        if n > first:
            third = second
            second = first
            first = n

        elif n > second & n != first:
            third = second 
            second = n
        
        elif n > third & n != second:
            third = n
    return third

nums = [10,20,30,40,50]
result = third_largest(nums)
print(result)



