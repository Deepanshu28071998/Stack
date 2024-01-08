def prec(c):
    if c=='^':
        return 3
    elif c== '/' or c=='*':
        return 2
    elif c=='+' or c=='-':
        return 1
    else:
        return -1
def ass(c):
    if c=='^':
        return 'R'
    return 'L'
def infix_to_postfix(s):
    result=[]
    stack = []
    for i in range(len(s)):
        c=s[i]
        # If the scanned character is an operand (number), add it to output.
        if ('a'<=c<='z') or ('A'<=c<='Z') or ('0'<=c<='9'):
            result.append(c)
        elif c=='(':
            stack.append(c)
        elif c==')':
            while stack and stack[-1]!= result.append(stack.pop())
            stack.pop
        else:
            while stack and (prec(s[i])<prec(stack[-1]) or prec(s[i]==prec(stack[-1]) and ass(s[i])=='L')):
                result.append(stack.pop())
            stack.append(c)
while stack:
    result.append(stack.pop())
    print(''.join(result))
#DRIVER CODE
exp=(A+B)+(C-D)/G
#function call
infix_to_postfix(exp)