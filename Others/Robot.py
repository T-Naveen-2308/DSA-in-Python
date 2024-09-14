l1 = [[-1,0], [0,-1], [1,0], [0,1]]

class Robot:
    def __init__(self, x, y, d):
        self.flag = 'True'
        self.x = x
        self.y = y
        self.d = d
    def update(self, c):
        if c=='F':
            self.x += l1[self.d][0]
            self.y += l1[self.d][1]
        elif c=='L':
            self.d = (self.d+1)%4
        else:
            self.d = (self.d-1)%4
        self.check()
    def check(self):
        if l[self.x][self.y]=='X' or self.x==-1 or self.y==-1 or self.x==r or self.y == c:
            self.flag = False

r, c = map(int, input().split())
l = [input() for i in range(r)]
p, q = map(int, input().split())
m = int(input())
d = [Robot(p,q,i) for i in range(4)]  
for i in range(m):
    k = input()
    for j in d:
        j.update(k)
d[1], d[2] = d[2], d[1]
for i in d:
    if i.flag:
        print(i.x, i.y)