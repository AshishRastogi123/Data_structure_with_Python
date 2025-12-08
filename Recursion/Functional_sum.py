"""
sum_of_n numbers from 1 to n
"""
def sum_of_n(i,n,sum=0):
    if i>n:
        print(sum)
        return
    sum=sum+i
    sum_of_n(i+1,n,sum)
sum_of_n(1,10)