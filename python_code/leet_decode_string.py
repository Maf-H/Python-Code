from collections import deque
def decode_string(s) -> str:
    stack = deque()
    s = []
    for v in s:
        if v != ']':
            stack.append(v)
        else:
            sub_string = []
            while stack[-1] != '[':
                sub_string.append(stack.pop()) # append sub_string to stack,
            stack.pop()  # remove '['
            sub_string.reverse() # reverse sub_string to correct order

            multiplier = ''
            while stack and str(stack[-1]).isdigit():
                multiplier += stack.pop()

            multiplier = multiplier[::-1]
            
            stack.extend(int(multiplier) * sub_string) # extend to stack
            
    return ''.join(stack)

s = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef", "2[abc3[cd]ef]"]
# for i in s:
print(decode_string("100[leetcode]"))


