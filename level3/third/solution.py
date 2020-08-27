def shortest_path(sx, sy, map, width, height):
    board = [[None for i in range(width)] for i in range(height)]
    board[sx][sy] = 1

    arr = [(sx, sy)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
          nx, ny = x + i[0], y + i[1]
          if 0 <= nx < height and 0 <= ny < width:
            if board[nx][ny] is None:
                board[nx][ny] = board[x][y] + 1
                if map[nx][ny] == 1 :
                  continue
                arr.append((nx, ny))

    return board

def solution(map):
    height= len(map)
    width = len(map[0])
    tb = shortest_path(0, 0, map, width, height)
    bt = shortest_path(height-1, width-1, map, width, height)
    board = []

    ans = 2 ** 32-1
    for i in range(height):
        for j in range(width):
            if tb[i][j] and bt[i][j]:
                ans = min(tb[i][j] + bt[i][j] - 1, ans)
    return ans

assert solution([[0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0]]) == 21

assert solution([[0, 1, 1, 0],
                 [0, 0, 0, 1],
                 [1, 1, 0, 0],
                 [1, 1, 1, 0]]) == 7

assert solution([[0,1,0,0,0],
                 [0,0,0,1,0],
                 [1,1,1,1,0]]) == 7

assert solution([[0,1,1,1],
                 [0,1,0,0],
                 [1,0,1,0],
                 [1,1,0,0]]) == 7

assert solution([[0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1],
                 [0, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0]]) == 11
