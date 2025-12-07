
def power(x,n,y=1):
            if n==0:
               print(y)
               return 1
            y=y*x
            power(x,n-1,y)
power(2,10)