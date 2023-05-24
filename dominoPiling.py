input = input()
nums = []
for i in input.split():
    nums.append(int(i))
if nums[0] %2 == 0:
        print(int((nums[1])*(nums[0] /2)))
else:
    if nums[1] %2 == 0:
        print(int((nums[1])*((nums[0] -1) /2) +(nums[1]/2)))
    else:
        print(int((nums[1])*((nums[0] -1) /2) + ((nums[1] -1) /2)))

    
       
