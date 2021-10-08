import sys; args = sys.argv[1:]
import time
#Nihal Shah, Student, pd. 6
x = time.perf_counter()




#Banded Array Printing: 
#Takes an array of strings and prints them as 2D Matrices, line by line
def banded_print(arr):
    if len(arr)>1:
        arr= arr[:-1]
    r = round(len(arr)/7)
    if r>0:
        x = 0
        xmax = 7
        for i in range(r):
            for l in range(length):
                s = ""
                for k in arr[x:xmax]:
                    s+=k[width*l: (width*l)+width] + " "
                print(s)
            x=xmax
            if(xmax+7>len(arr) and len(arr)>xmax):
                xmax = len(arr)
                for l in range(length):
                    s = ""
                    for k in arr[x:xmax]:
                        s+=k[width*l: (width*l)+width] + " "
                    print(s)
            else: xmax+=7
    else:
        #Case for arrays with a length of less than 7
        for i in range(length):
          s = ""
          for k in arr:
            s+=k[width*i: (width*i)+width] + " "
          print(s)
#Method to find the neighbors of a given puzzle, returns a list with the neighbors
def find_neighbors(s):
    location = s.index("_")
    neighbors = []
    if (location)%width!=width-1:
        k = [*s]
        k[location], k[location+1] = k[location+1], k[location]
        neighbors.append("".join(k))
    if location-width>=0:
        k = [*s]
        k[location], k[location-width] = k[location-width], k[location]
        neighbors.append("".join(k))
    if location%width!=0:
        k = [*s]
        k[location], k[location-1] = k[location-1], k[location]
        neighbors.append("".join(k))
    if location+width<len(s):
        k = [*s]
        k[location], k[location+width] = k[location+width], k[location]
        neighbors.append("".join(k))
    return neighbors

#Method to search through a given start and goal to find a path between them.
def bfs(start, goal):
    parseme = [start]
    visited = {start:None}
    if start==goal:
        return [start]
    while parseme:
        p = parseme.pop(0)
        for i in find_neighbors(p):
            if not i in visited:
                if i == goal:
                    visited[i] = p
                    r=[goal]
                    i = goal
                    while i!=None:
                        r.insert(0,i)
                        i = visited[i]
                    return r
                else:
                    parseme.append(i)
                    visited[i] = p
    return start


#Start, Goal Generation
m = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if len(args)<2:
    goal =  m[0:len(args[0])-1] + "_"
else:
    goal = args[-1]
start = args[0]
#Length, Width Definition
length = int(len(start)**0.5)
if len(start)%length!=0:
    length-=1
width = len(start)//length        

v= bfs(start, goal)


#Printing
if len(v)==1:
    banded_print(v)
    print("Steps: 0")
elif v==start:
    banded_print([v])
    print("Steps: -1")
else:
    banded_print(v)
    print("Steps: "+str(len(v)-2))
y = time.perf_counter()
print("Time: {:.2f}s".format(round(y-x, 2)))


