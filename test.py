# n, m, x, y
m = 10
n = 10
matrix = [[0]*(m+1) for _ in range(n+1)]
res = False
# a<=b
def end(a, b):
    if a == 1 or b == 1 or (matrix[a-1][b] == 1 and matrix[a][b-1] == 1):
        return True
    return False

def dfs(a, b):
    global res
    if end(a, b):
        if a == 1 or b == 1:
            res = True
            return
        else:
            return

    if b < a:
        dfs(b, a)

    if a == 2:
        if matrix[a-1][b] == 0:
            matrix[a-1][b] = 1
            if not end(a, b):
                dfs(a, b-1)
                matrix[a-1][b] = 0
            else:
                return
        else:
            matrix[a][b-1] = 1
            if not end(a, b):
                dfs(a, b-1)
                matrix[a-1][b] = 0
            else:
                return
    
    if matrix[a-1][b-1] == 0:
        matrix[a-1][b-1] = 1
        if not end(a, b):
            dfs(a-1, b)
            matrix[a-1][b-1] = 0
        else:
            return



dfs(4-1,5)
if res:
    print 'YES'
else:
    print 'NO' 
