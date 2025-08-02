nums=[1,2,4,5,6]
n=len(nums)+1
expected_sum=n*(n+1)//2
actual_sum=sum(nums)
result=expected_sum-actual_sum
print(result)