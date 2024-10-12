from collections import deque
def asteroid_collision(asteroids: list[int]) -> list[int]:

    stack = deque()
    # collision only happens if current asteroid is negative and top of stack is negative
    for asteroid in asteroids:
        if asteroid > 0 or (asteroid < 0 and  (len(stack) == 0 or stack[-1] < 0)):
            stack.append(asteroid)
        else:
            while stack and stack[-1] > 0 and asteroid < 0:
                colide = asteroid + stack[-1]
                if colide < 0:
                    stack.pop()
                elif colide > 0:
                    asteroid = 0
                    break
                else:
                    stack.pop()
                    asteroid = 0
                    break
            if asteroid < 0:
                stack.append(asteroid)
    return list(stack)

asteroids = [
    [5, 10, -5], 
    [8,-8], 
    [10,2,-5], 
    [-2,-1,1,2], 
    [-2,-2,1,-2], 
    [-2,-1,1,-2],
    [-2,-2,1,-1],
    [1,-2,-2,-2]
    ]
# print(asteroid_collision(asteroids[5]))
for i in asteroids:
    print(asteroid_collision(i))