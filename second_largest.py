def second_larget(nums):
    largest = float('-inf')
    second = float('-inf')
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n > second and n != largest:
            second = n
    
    return second

nums = [10, 20, 30, 40,6,2,200,40]

result = second_larget(nums)

print(result)
