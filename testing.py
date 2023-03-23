class A:
    s = 15

    def __init__(self):
        self.x = 10
        self.n1 = self.s
        self.n2 = self.s

    def add_num(self):
        res = self.n1 + self.n2
        print('sum:', res)


t = A()
print('x:', t.x)
t.x = 100

t.add_num()
# t.n1 += 2
# t.n2 += 5
t.s += 1
print('x:', t.x)
print('s:', t.s)
t.add_num()

t2 = A()
print(t2.s)