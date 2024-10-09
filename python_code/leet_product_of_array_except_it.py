from time import perf_counter
def productExceptSelf(nums: list[int]) -> list[int]:
    length = len(nums)
    prefix = [1] * length
    suffix = [1] * length

    for i in range(1, length):
        prefix[i] = prefix[i - 1] * nums[i - 1]
        suffix[-i - 1] = suffix[-i] * nums[-i]
        print(prefix, suffix)

    
    for i in range(length):
        nums[i] =  prefix[i] * suffix[i]
            
    return nums

def product_except_itself(nums: list[int]) -> list[int]:
    ans, pre, post = [1]*len(nums), 1, 1
    for i in range(len(nums)):
        ans[i] *= pre
        ans[-1-i] *= post
        pre, post = pre*nums[i], post*nums[-1-i]
    return ans
num = [[1,2,3,4], [1,2,3,4,5,7,9,55,3,12,3]]
t2 = perf_counter()
print(productExceptSelf(num[0]))
print(perf_counter() - t2)

t1 = perf_counter()
print(product_except_itself(num[0]))
print(perf_counter() - t1)


