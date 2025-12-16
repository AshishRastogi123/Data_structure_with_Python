"""
Find union of two sorted array
a=[1,1,1,2,3,3,4,5]
b=[1,2,2,3,6,7]
output: [1,2,3,4,5,6,7]
"""
class Solution:
    def Union_sorted_optimal(self, a,b):
        c=[]
        for i in range(len(a)):
            if a[i] not in c:
                c.append(a[i])
        for j in range(len(b)):
            if b[j] not in c:
                c.append(b[j])
        return c.sort()
    def Union_sorted_2(self,a ,b):
        result=[]
        n=len(a)
        m=len(b)
        i=0
        j=0
        while i<n or j<m:
            if i<n and j<m:
                if a[i]>b[j]:
                    result.append(b[j])
                    j+=1
                elif a[i]==b[j]:
                    if a[i] not in result:
                        result.append(a[i])
                    else:
                        i+=1
                        j+=1
                else:
                        result.append(b[j])
                        i+=1
            else:
                if i<n:
                    if a[i] not in result:
                        result.append(a[i])
                        i+=1
                    else:
                        i+=1
                else:
                    if b[j] not in result:
                        result.append(b[j])
                        j+=1
                    else:
                        j+=1
        print(result)

    def findUnion(self, a, b):
        i, j = 0, 0
        n, m = len(a), len(b)
        ans = []

        while i < n and j < m:
            if a[i] == b[j]:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i += 1
            else:
                if not ans or ans[-1] != b[j]:
                    ans.append(b[j])
                j += 1

        # Remaining elements
        while i < n:
            if not ans or ans[-1] != a[i]:
                ans.append(a[i])
            i += 1

        while j < m:
            if not ans or ans[-1] != b[j]:
                ans.append(b[j])
            j += 1

        return ans

            

s=Solution()
a = [1, 2, 3, 4, 5]
b = [1, 1, 2, 3, 4]
# print(s.Union_sorted_2(a,b))
print(s.findUnion(a,b))