
import random


nums = []
for i in range(20):
    nums.append(random.randint(0, 5))

print (nums)

sums = []

for i in range(len(nums)-4):
    val = sum(nums[i:i+5])
    sums.append(val)
    
print(sums)
print (max(sums))
