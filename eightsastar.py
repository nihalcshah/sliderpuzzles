import sys; args = sys.argv[1:]
# f = open(args[0], "r").read().splitlines()
f = open("Eckel55G.txt", "r").read().splitlines()
# f = ["MDAHEOGNCFBJKLI_","MDAHOCN_EIGBKFLJ"]
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



#Method to find the neighbors of a given puzzle, returns a list with the neighbors
# def find_neighbors(s):
    location = s.index("_")
    neighbors = []
    if location+width<len(s):
        k = [*s]
        k[location], k[location+width] = k[location+width], k[location]
        neighbors.append((0,"".join(k),s, "D"))
    if (location)%width!=width-1:
        k = [*s]
        k[location], k[location+1] = k[location+1], k[location]
        neighbors.append((0,"".join(k), s, "R"))
    if location-width>=0:
        k = [*s]
        k[location], k[location-width] = k[location-width], k[location]
        neighbors.append((0,"".join(k),s, "U"))
    if location%width!=0:
        k = [*s]
        k[location], k[location-1] = k[location-1], k[location]
        neighbors.append((0,"".join(k),s,"L"))
    return neighbors


# def find_neighbors(s):
#     location = s.index("_")
#     neighbors = []
#     if (location)%width!=width-1:
#         k = [*s]
#         k[location], k[location+1] = k[location+1], k[location]
#         neighbors.append(("".join(k), "R"))
#     if location-width>=0:
#         k = [*s]
#         k[location], k[location-width] = k[location-width], k[location]
#         neighbors.append(("".join(k), "U"))
#     if location%width!=0:
#         k = [*s]
#         k[location], k[location-1] = k[location-1], k[location]
#         neighbors.append(("".join(k),"L"))
#     if location+width<len(s):
#         k = [*s]
#         k[location], k[location+width] = k[location+width], k[location]
#         neighbors.append(("".join(k), "D"))
#     return neighbors

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
            if not i[0] in visited:
                if i[0] == goal:
                    visited[i[0]] = (p,i[1])
                    m = i
                    path = ""
                    while m!=None:
                        path = m[1]+path
                        m = visited[m[0]]
                    return path[:-1]
                else:
                    # parseme.append(i[0])
                    inserted = False
                    index = 0
                    if index<len(parseme) and len(parseme)>0:
                        while not inserted and index<len(parseme):
                            update = countManhattan(i[0], goal)
                            node = countManhattan(parseme[index], goal)
                            if update<node:
                                parseme.insert(index, i[0])
                                inserted= True
                            index+=1
                    else:
                        parseme.append(i[0])
                    visited[i[0]] = (p,i[1])
    return "X"

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

def AStar(start, goal):
    if start==goal:
        return "G"
    if not isSolvable(start, goal):
        return "X"
    
    openset = [(None, start, None, None)]
    level = 1
    closedset = {}
    while openset:
        openset.sort()
        pzl = openset.pop(0)
        if pzl[1] in closedset:
            continue
        else:
            closedset[pzl[1]] = pzl 
        for i in find_neighbors(pzl[1]):
            if i[1] == goal:
                closedset[i[1]] = i
                m = i
                path = ""
                while m[2]!=None:
                    path = m[3]+path
                    m = closedset[m[2]]
                return path
            if i[1] in closedset:
                continue
            t = countManhattan(i[1], goal)
            f = level +1 + t
            openset.append((f, i[1], i[2], i[3])) 
        level +=1
        



def calculatelength(puzzle):
    global length
    length = int(len(puzzle)**0.5)
    if len(puzzle)%length!=0:
        length-=1
    global width
    width = len(puzzle)//length
    return length, width

def solvePuzzles(arr):
    global goal
    goal = arr[0]
    # goal = "ABCDEFGHIJKLMNO_"
    global length, width
    length,width = calculatelength(goal)
    for i in range(len(arr)):
        start = arr[i]
        t = time.process_time()
        k = bfs(start, goal)
        t = time.process_time()-t
        print("{}: {} solved in {} secs => path {}".format(i+1, start, t, k))
    print("Process Complete")
solvePuzzles(f)

#Nihal Shah, period 6, 2023 