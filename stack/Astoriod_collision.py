"""
735. Asteroid Collision
Link : https://leetcode.com/problems/asteroid-collision/description/

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
"""
class Astroid:
    def astro_collision(self,asteroids):
        stack=[]
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            
            else:
                while len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                    stack.pop()
                if len(stack)!=0 and stack[-1]==abs(asteroids[i]):
                    stack.pop()

                elif len(stack)==0 or stack[-1]<0:
                    stack.append(asteroids[i])
        return stack

            

            


s=Astroid()
l=[5,10,-5]
p=s.astro_collision(l)
print(p)