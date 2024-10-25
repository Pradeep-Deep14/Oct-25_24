m=[
    [1,2,3,4],
    [5,6,7,8],
]
t=[]
for i in range(4):
    t.append([row[i]for row in m])

print(t)