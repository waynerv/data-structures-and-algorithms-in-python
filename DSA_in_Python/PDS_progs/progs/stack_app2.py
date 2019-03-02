""" 栈的应用2，迷宫求解，基于队列的迷宫求解 """

from stack_list import *
from queue_list import *

maze1 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,0,1],
    [1,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1],
    [1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1],
    [1,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,0,1],
    [1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1],
    [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1],
    [1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

maze2 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,1,0,0,0,1,0,0,0,1],
    [1,0,1,0,0,0,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,1,1,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,0,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,0,0,1,1,1,0,1,0,1,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,0,0,1],
    [1,0,1,0,1,0,1,0,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0

############################################
########## A recursive maze path finder ####


def maze_solver_rec(maze, start, end):
    """ A maze solver using a recursive procedure to find the path.
    """
    def find_path(maze, pos, end):
        mark(maze, pos)
        if pos == end:
            print(pos, end=' ')
            return True
        for i in range(4):
            nextp = pos[0]+dirs[i][0], pos[1]+dirs[i][1]
            if passable(maze, nextp):
                if find_path(maze, nextp, end):
                    print(pos, end=' ')
                    return True
        return False

    print("If find, print the path from end to start:")
    if find_path(maze, start, end):
        print("\n")
    else:
        print("No path exists.")
# end maze_solver_rec


##################################################
####### A non-recursive maze path finder #########
####### which use a stack as temporary storage ####

def print_path(end, last, st):
    print(end, last, sep=" ", end=' ')
    while not st.is_empty():
        print(st.pop()[0], end=' ')
    print('\n')


def print_path_rev(end, last, st):  # print the path from start to end
    path = [end, last]
    while not st.is_empty():
        path.append(st.pop())
    path.reverse()
    for pos in path:
        print(pos, end=" ")
    print('\n')


def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)                 
    st.push((start, 0))          # start position into stack
    while not st.is_empty():     # have possibility to try
        pos, nxt = st.pop()      # get last branch position
        for i in range(nxt, 4):  # try to find non-exploring direction(s)
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])  # next point
            if nextp == end:     # find end, great! :-)
                print_path(end, pos, st)
                return
            if passable(maze, nextp):  # new position is passable
                st.push((pos, i+1))    # original position in stack
                mark(maze, nextp)
                st.push((nextp, 0))    # new position into stack
                break
    print("No path.")  # :-(


####### Search a maze using a queue ##############
####### No path record ###########################


def maze_solver_queue(maze, start, end):
    if start == end:
        print("Path finds.")
        return
    qu = SQueue()
    mark(maze, start)                
    qu.enqueue(start)         # start position into queue
    while not qu.is_empty():  # have possibility to try
        pos = qu.dequeue()    # take next try position
        for i in range(4):    # check each direction
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])  # next position
            if passable(maze, nextp):      # find new position
                if nextp == end:           # end position, :-)
                    print("Path finds.")   # where is the path??
                    return
                mark(maze, nextp)
                qu.enqueue(nextp)          # new position into queue
    print("No path.")  # :-(


####### Search a maze using a queue ###############
####### recording the path precedent relation #####


def build_path(start, pos, end, precedent):
    path = [end]
    while pos != start:
        path.append(pos)
        pos = precedent[pos]
    path.append(start)
    path.reverse()
    return path    


def maze_solver_queue1(maze, start, end):
    if start == end:
        return [start]
    qu = SQueue()
    precedent = dict()
    mark(maze, start)                
    qu.enqueue(start)         # start position into queue
    while not qu.is_empty():  # have possibility to try
        pos = qu.dequeue()    # take next try position
        for i in range(4):    # check each direction
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])  # next position
            if passable(maze, nextp):      # find new position
                if nextp == end:           # end position, :-)
                    return build_path(start, pos, end, precedent)
                mark(maze, nextp)
                precedent[nextp] = pos     # set precedent of nextp
                qu.enqueue(nextp)          # new position into queue
    print("No path.")  # :-(


#### Another implementation using a stack.
#### A pos and a stack hold the information used in searching.
#### It seems that this implementation is not really better,
#### not clearer, nor shorter, nor conceptually better.


def print_path1(end, st):
    print(end, end=' ')
    while not st.is_empty():
        print(st.pop()[0], end=' ')
    print('\n')


def maze_solver1(maze, start, end):
    st = SStack()
    pos, nxt = start, 0
    while True:
        if pos == end:
            print_path1(pos, st)
            return
        mark(maze, pos)
        for i in range(nxt, 4):  # 依次检查潜在探索方向
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])  # 算出下一点
            if passable(maze, nextp):      # 遇到未探查点
                st.push((pos, i+1))        # 原位置进栈
                pos, nxt = nextp, 0
                break
        else:
            if st.is_empty():
                break
            pos, nxt = st.pop()
    print("No path found.")  # 找不到路径
# end of maze_solver


if __name__ == "__main__":
    pass
#    maze_solver_rec(maze1, (1,1), (18,18))
#    maze_solver1(maze1, (1,1), (18,18))

#    maze_solver_queue(maze1, (1,1), (18,18))
#    print(maze_solver_queue1(maze1, (1,1), (18,18)))
