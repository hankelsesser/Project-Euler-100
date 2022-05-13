def check_grid(grid):
    #row
    target = grid[0][0]+grid[0][1]+grid[0][2]+grid[0][3]
    for row in range(1,len(grid)):
        sum = 0
        for num in grid[row]:
            sum += num
        if sum != target: return False
    
    #colomn
    for c in range(4):
        sum = 0
        for r in range(4):
            sum += grid[r][c]
        if sum != target: return False
    
    #diags
    sum = 0
    for i in range(4):
        sum += grid[i][i]
    if sum != target: return False
    
    sum = 0
    for i in range(4):
        sum += grid[i][3-i]
    if sum != target: return False
        
    return True

def show(n, grid):
    print("-----"+str(n)+"-----")
    for row in grid: print(row)
    print("")

def blank_grid():
    grid = []
    for i in range(4): grid.append(["X", "X", "X", "X"])
    return grid


#domain = [0, 8]
valid_grids= []

def main(domain):
    num = 0
    for a in range(domain[0],domain[1]+1):
        for b in range(domain[0],domain[1]+1):
            for c in range(domain[0],domain[1]+1):
                for d in range(domain[0],domain[1]+1):
                    target = a+b+c+d
                    #print(target)
                    #print(str(100*(((a* (domain[1]+1)**3)+ (b* (domain[1]+1)**2)+ (c* (domain[1]+1))+d)/((domain[1]+1)**4))), "valid_grids:", str(len(valid_grids)))
                    for e in range(domain[0],domain[1]+1):
                        for f in range(domain[0],domain[1]+1):
                            for g in range(domain[0],domain[1]+1):
                                for h in range(domain[0],domain[1]+1):
                                    if e+f+g+h == target:
                                        for i in range(domain[0],domain[1]+1):
                                            for j in range(domain[0],domain[1]+1):
                                                for k in range(domain[0],domain[1]+1):
                                                    for l in range(domain[0],domain[1]+1):
                                                        if i+j+k+l == target: 
                                                            for m in range(domain[0],domain[1]+1):
                                                                if d+g+j+m == target and a+e+i+m == target:
                                                                    for n in range(domain[0],domain[1]+1):
                                                                        if b+f+j+n == target: 
                                                                            for o in range(domain[0],domain[1]+1):
                                                                                if c+g+k+o == target:
                                                                                    for p in range(domain[0],domain[1]+1):
                                                                                        if m+n+o+p == target and a+f+k+p == target and d+h+l+p == target: 
                                                                                            valid_grids.append([
                                                                                                [a, b, c, d],
                                                                                                [e, f, g, h],
                                                                                                [i, j, k, l],
                                                                                                [m, n, o, p]
                                                                                            ])
                                                                                            num += 1
    return num

main([0, 2])
print(len(valid_grids))
for i in [207, 414]:
    show(i, valid_grids[i-1])


