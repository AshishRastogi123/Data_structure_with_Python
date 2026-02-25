"""
N meetings in one 

Input: start[] = [1, 3, 0, 5, 8, 5], end[] =  [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2), (3, 4), (5,7) and (8,9)
"""
class Solution:
    def N_meetings(self,start,end):
         meetings = sorted(zip(start, end), key=lambda x: x[1])
         #[(1, 2), (3, 4), (0, 6), (5, 7)]
         count = 0
         temp = float('-inf')
         for s, e in meetings:
            if s > temp:
                count += 1
                temp = e

         return count
    
    def another(self,start,end):
        meet=[Meeting(start[i],end[i],i+1) for i in range(len(start))]
        meet.sort(key=lambda x: (x.end,x.start))
        count=1
        result=[meet[0].position]
        last=meet[0].end
        for i in range(len(meet)):
            if meet[i].start>last:
                count+=1
                result.append(meet[i].position)
                last=meet[i].end
        return count,result
    
#another solution
class Meeting:
    def __init__(self,start,end,position):
        self.start=start
        self.end=end
        self.position=position

        

s=Solution()
start= [1, 3, 0, 5, 8, 5]
end =  [2, 4, 6, 7, 9, 9]
print(s.another(start,end))