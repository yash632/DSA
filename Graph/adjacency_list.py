v = 6
e = 7

edges = [(0,1), (0,3), (0,4), (1,2), (1,5), (2,4), (3,4)]

adm = [[]*v for _ in range(v)]

for edge in edges:
    adm[edge[0]].append(edge[1])
    adm[edge[1]].append(edge[0])
    
for i in adm:
    print(i)