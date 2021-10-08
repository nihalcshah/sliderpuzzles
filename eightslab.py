import sys; args = sys.argv[1:]
# f = open(args[0], "r").read().splitlines()
f = open("Eckel55G.txt", "r").read().splitlines()
#Nihal Shah, Student, pd. 6
import time
x = time.perf_counter()


def isSolvable(s,g):
    global length
    global width

    st = s
    go = g
    space_ind = s.find("_")
    if space_ind!=len(s)-1:
        s = s[:space_ind]+s[space_ind+1:]
    else:
        s= s[:space_ind]
    space_ind = g.find("_")
    if space_ind!=len(g)-1:
        g = g[:space_ind]+g[space_ind+1:]
    else:
        g= g[:space_ind]
    invcount = 0
    for ind, val in enumerate(s):
        pos = g.find(val)
        for i in range(ind,len(s)):
            if pos>g.find(s[i]):
                invcount+=1
    if width%2==0:
        a = ((st.find("_")//width)+1)
        b = ((go.find("_")//width)+1)
        invcount += abs(a-b)
    # print(invcount
    if invcount%2==0:
        return True
    return False

def countManhattan(start, goal):
    md=0
    for ind, vall in enumerate(start):
        if vall != goal[ind] and vall!="_":
            finalind = goal.find(vall)
            widthdiff = abs((finalind%width)-(ind%width))
            lendiff = abs((finalind//length)-(ind//length))
            md += lendiff + widthdiff
    return md


# def getrow(ind):
#     row = ind//width
#     column = ind-(width*row)
#     return (row, column)

#Method to find the neighbors of a given puzzle, returns a list with the neighbors
def find_neighbors(s):
    location = s.index("_")
    neighbors = []
    if (location)%width!=width-1:
        k = [*s]
        k[location], k[location+1] = k[location+1], k[location]
        neighbors.append(("".join(k), "R"))
    if location-width>=0:
        k = [*s]
        k[location], k[location-width] = k[location-width], k[location]
        neighbors.append(("".join(k), "U"))
    if location%width!=0:
        k = [*s]
        k[location], k[location-1] = k[location-1], k[location]
        neighbors.append(("".join(k),"L"))
    if location+width<len(s):
        k = [*s]
        k[location], k[location+width] = k[location+width], k[location]
        neighbors.append(("".join(k), "D"))
    return neighbors

#Method to search through a given start and goal to find a path between them.
def bfs(start, goal):
    parseme = [start]
    visited = {start:None}
    if start==goal:
        return "G"
    if not isSolvable(start, goal):
        return "X"
    while parseme:
        p = parseme.pop(0)
        for i in find_neighbors(p):
            # if time.process_time()-start_time>60:
            #     return 0
            if not i[0] in visited:
                # print(i[0])
                if i[0] == goal:
                    visited[i[0]] = (p,i[1])
                    # r=[goal]
                    # i = goal
                    m = i
                    path = ""
                    while m!=None:
                        path = m[1]+path
                        m = visited[m[0]]
                    return path[:-1]
                else:
                    parseme.append(i[0])
                    # inserted = False
                    # index = 0
                    # if index<len(parseme) and len(parseme)>0:
                    #     while not inserted and index<len(parseme):
                    #         update = countManhattan(i[0], goal)
                    #         node = countManhattan(parseme[index], goal)
                    #         if update<node:
                    #             parseme.insert(index, i[0])
                    #             inserted= True
                    #         index+=1
                    # else:
                    #     parseme.append(i[0])
                    visited[i[0]] = (p,i[1])
    return "X"

# def sort(arr):
#     # arr = sorted(arr)
#     for k in range(len(arr)):
#         mdarr = [countManhattan(i, arr[0]) for i in arr[k:]]
#         manhattanind = mdarr.index(min(mdarr))+k
#         arr[k], arr[manhattanind] = arr[manhattanind], arr[k]
#     return arr
def solvePuzzles(arr):
    totaltime = time.process_time()
    start, goal = arr[0], arr[0]
    global length
    length = int(len(start)**0.5)
    if len(start)%length!=0:
        length-=1
    global width
    width = len(start)//length  
    # print(countManhattan(start, goal))
    # arr = sort(arr)
    for i in range(len(arr)):
        start, goal = arr[i], arr[0]
        length = int(len(start)**0.5)
        if len(start)%length!=0:
            length-=1
        width = len(start)//length    
        # if time.process_time-totaltime>120:
        #     break
        t = time.process_time()
        # print(start)
        # if isSolvable(start, goal):
        #     k = bfs(start, goal)
        # else: 
        #     k = "X"
        k = bfs(start, goal)
        t = time.process_time()-t
        print("{}: {} solved in {} secs => path {}".format(i+1, start, t, k))

        # if k == 0:
        #     break
        
        # if inversioncount(start, goal):
        #     print("Is Solvable")r
        # print(f"Manhattan Distance: {countManhattan(start, goal)}")
        # count+=1
    print("Process Complete")
solvePuzzles(f)
#Start, Goal Generation
# m = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# if len(args)<2:
#     goal =  m[0:len(args[0])-1] + "_"
# else:
#     goal = args[-1]
# start = args[0]
# #Length, Width Definition
# length = int(len(start)**0.5)
# if len(start)%length!=0:
#     length-=1
# width = len(start)//length        

# v= bfs(start, goal)


# #Printing
# if len(v)==1:
#     banded_print(v)
#     print("Steps: 0")
# elif v==start:
#     banded_print([v])
#     print("Steps: -1")
# else:
#     banded_print(v)
#     print("Steps: "+str(len(v)-2))
# y = time.perf_counter()
# print("Time: {:.2f}s".format(ro.und(y-x, 2)))

#Nihal Shah, period 6, 2023 