col=4
row=4
start=col-2

arr=[]
k=0
for i in range(1,2):
    for j in range(start,col-1):
        arr[k]=[i,j]
        k=k+1
for i in range(i+1,row-1):
    start=start-1
    for j in range(col-1,start-1,-1):
        arr[k]=[i,j]
        k=k+1
    for k in range(i,0,-1):
        for l in range(start,start+1):
            arr[k]=[i,j]
            k=k+1
    for s in range(start-1,start):
        for k in range(start-1,col-1):
            arr[k]=[i,j]
            k=k+1
