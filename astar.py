import sys; args = sys.argv[1:]
# f = open(args[0], "r").read().splitlines()
f = open("Eckel55G.txt", "r").read().splitlines()
#Nihal Shah, Student, pd. 6
import time 
x = time.perf_counter()


def manhattantable():
    d = {}
    for ind,val in enumerate(goal):
        larr = []
        for i in range(16):

            originalrow = ind//length
            currentrow = i//length
            originalcol = ind%width
            currentcol = i%width

            rowdiff = abs(originalrow-currentrow)
            columndiff = abs(originalcol-currentcol)
            larr.append(rowdiff + columndiff)
        d[val] = larr
    return d
    


#isSolvable: Checks if a puzzle is solvable; takes a start and goal puzzle, returns a boolean.
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

#Function to get the Manhattan Count of between two puzzles, returns an integer of the total Manhattan Count
def countManhattan(start, goal):
    md=0
    for i, vall in enumerate(start):
        if vall != goal[i] and vall!="_":
            finalind = goal.find(vall)

            originalrow = finalind//length
            currentrow = i//length
            originalcol = finalind%width
            currentcol = i%width

            rowdiff = abs(originalrow-currentrow)
            columndiff = abs(originalcol-currentcol)
            md += rowdiff + columndiff
    return md



#Function to find the neighbors of a given puzzle, returns a list of tuples with the neighbors 
def find_neighbors(s, d):
    location = s.index("_")
    neighbors = []
    if location+width<len(s):
        k = [*s]
        k[location], k[location+width] = k[location+width], k[location]
        md = d[k[location]][location]-d[k[location]][location+width]
        neighbors.append((0,"".join(k),s, "D",0,md))
    if (location)%width!=width-1:
        k = [*s]
        k[location], k[location+1] = k[location+1], k[location]
        # print(d[k[location]][location+1])
        md = d[k[location]][location]-d[k[location]][location+1]
        neighbors.append((0,"".join(k), s, "R",0, md))
    if location-width>=0:
        k = [*s]
        k[location], k[location-width] = k[location-width], k[location]
        md = d[k[location]][location]-d[k[location]][location-width]
        neighbors.append((0,"".join(k),s, "U",0, md))
    if location%width!=0:
        k = [*s]
        k[location], k[location-1] = k[location-1], k[location]
        md = d[k[location]][location]-d[k[location]][location-1]
        neighbors.append((0,"".join(k),s,"L",0,md))
    return neighbors

#Function implements the AStar algorithm, finding the shortest path between two nodes using estimates.

def AStar(start, goal, d):
    if start==goal:
        return "G"
    if not isSolvable(start, goal):
        return "X"
    
    
    level = 0
    #Openset: a list of tuples for each node with the following data - ("f" estimate, Puzzle string, Puzzle parent string, level)
    openset = [[] for i in range(60)]
    count = countManhattan(start, goal)
    openset[count].append((None, start, None, None, level))
    ptr = 0
    # (None, start, None, None, level)
    closedset = {}
    minvar = 0
    # for pzl in openset[count]:
    while openset:
        #Finds the minimum node in the list, then calls sort if the first node is not the minimum node.
        # mv = min(openset)
        # if mv<openset[0]:
        #     openset.sort()
        # openset.sort()
        if(ptr<len(openset[count])):
            pzl = openset[count][ptr]
        else:
            count+=2
            ptr = 0
            pzl = openset[count][ptr]
        if pzl[1] in closedset:
            ptr+=1
            continue
        else:
            closedset[pzl[1]] = pzl 
            # print(pzl[1] in closedset)
        l = pzl[4]
        for tup in find_neighbors(pzl[1], d):
            estimate, string, parent, movement, lev, mdchange = tup
            if string == goal:
                closedset[string] = (estimate, string, parent, movement, lev)
                return closedset, (estimate, string, parent, movement, lev)
            if string in closedset:
                continue
            t = mdchange
            # print(f"Manhattan: {countManhattan(string, goal)}")
            # print(f"Table: {t}")
            # if(pzl[0]):
            #     f = pzl[0] +1 + t
            # else:
            f= count +1 +t
            openset[f].append((f, string, parent, movement, l+1))
        ptr+=1
        # if(ptr==len(openset[count])):
        #     count = count+2
#Assembles the path given a dictionary and the goal node
def assemblepath(pathdict, goalnode):
    m = goalnode
    path = ""
    while m[2]!=None:
        path = m[3]+path
        m = pathdict[m[2]]
    return path

#Function that calculates the length and width of a given puzzle
def calculatelength(puzzle):
    global length
    length = int(len(puzzle)**0.5)
    if len(puzzle)%length!=0:
        length-=1
    global width
    width = len(puzzle)//length
    return length, width

#Function that solves all the puzzles in an array, with the goal as the first puzzle.
def solvePuzzles(arr):
    global goal
    goal = arr[0]
    
    # goal = "ABCDEFGHIJKLMNO_"
    global length, width
    length,width = calculatelength(goal)
    mdict = manhattantable()
    tt = 0
    for i in range(len(arr)):
        start = arr[i]
        t = time.process_time()
        path = AStar(start, goal, mdict)
        if len(path)>1:
            path = assemblepath(path[0],path[1])
        t = time.process_time()-t
        tt+=t
        if(tt>=60):
            break
        print("{}: {} solved in {:.2f} secs => path {}".format(i+1, start, round(t, 2), path))
    print("Process Complete")
solvePuzzles(f)

#Nihal Shah, period 6, 2023 