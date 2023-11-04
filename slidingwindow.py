a=[1,2,3,4,5,6,7,8]
n=len(a)
k=4
window_sum=sum(a[0:4])
max_sum=window_sum
for i in range(n-k):
    window_sum=max_sum-a[i]+a[i+k]
    max_sum=max(window_sum,max_sum)
print(max_sum)
