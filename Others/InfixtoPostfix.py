i = input('\nEnter the infix expression:\n')
s = ['(']
p = []
d = {'(':1,')':1,'+':2,'-':2,'/':3,'%':3,'//':3,'*':3, '**':4, '^':4}
x = 0
while x<len(i):
    j = i[x]
    if j.isalnum():
        p.append(j)
    elif j=='(':
        s.append('(')
    elif j==')':
        for k in range(len(s)-1,-1,-1):
            if s[k]=='(':
                break
            p.append(s.pop())
    else:
        if j==i[x+1]:
            j = 2*j
            x += 1
        while d[s[-1]]>=d[j]:
            p.append(s.pop())
        s.append(j)
    x += 1
for j in range(len(s)-1, 0, -1):
    p.append(s.pop())
p = ''.join(p)
print(f'\nThe postfix expression is:\n{p}')