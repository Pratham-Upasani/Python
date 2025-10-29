list=[]
N=int(input())
for i in range(N):
    list2 = []
    size=2
    for j in range(size):
        value = eval(input())
        list2.append(value)
    list.append(list2)
print(list)

""" 
Nested List Comprehension Version
N=int(input())
size=2
list = [[eval(input()) for j in range(size)]for i in range(N)]
print(list)

"""