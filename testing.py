import time

start_time = time.time()

nums = [0,1,0,3,0,12]
print(nums)
# position = []
# count = 0 
# for i in range(len(nums)):
#     if nums[i] == 0: 
#         count = count + 1
#         position.append(i)
#     else: continue

# for i in range(count):
#     nums.remove(0)
#     nums.append(0)


for i in range(len(nums)):
    nums.remove(0)
    nums.append(0)
print(time.time() - start_time)

print(nums)
    #aniss has big pp
